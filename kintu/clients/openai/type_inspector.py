import base64
import openai
from kintu.types.llmsdks.openai_types import (
    RawOpenAIEasyInputMessageParam,
    RawOpenAIResponseInputItemParam,
    RawOpenAIResponseInputTextParam,
    RawOpenAIResponseInputImageParam,
    RawOpenAIResponseInputFileParam,
    RawOpenAIFunctionCallOutput
)
from openai.types import Reasoning, ReasoningEffort
from kintu.utilities import image_to_base64_png
from pathlib import Path
import logging

# logging.getLogger('openai').setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)  # Also needed for handler

def get_client():
    return openai.OpenAI()

def get_image():
    from PIL import Image
    image_path = Path(__file__).parent.parent.parent.parent / "data" / "test_image_3.png"
    image = Image.open(image_path)
    return image_to_base64_png(image)

def get_pdf():
    pdf_path = Path(__file__).parent.parent.parent.parent / "data" / "berkshire_hathaway_letter.pdf"
    with open(pdf_path, "rb") as f:
        data = f.read()
    base64_string = base64.b64encode(data).decode("utf-8")
    return base64_string

def get_tools():
    tools = [
        {
            "type": "function",
            "name": "get_horoscope",
            "description": "Get today's horoscope for an astrological sign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sign": {
                        "type": "string",
                        "description": "An astrological sign like Taurus or Aquarius",
                    },
                },
                "required": ["sign"],
            },
        },
        {"type": "web_search_preview"},
        {
            "type": "code_interpreter",
            "container": {"type": "auto"}
        }
    ]
    return tools

def run_responses_api():
    client = get_client()
    b64_image = get_image()
    b64_pdf = get_pdf()
    pdf_data = f"data:application/pdf;base64,{b64_pdf}"
    image_data = f"data:image/png;base64,{b64_image}"
    # print(f"pdf_data length: {len(b64_pdf)}")
    # print(pdf_data[:100])
    # print(f"image_data length: {len(b64_image)}")
    # print(image_data[:100])
    text = "Hello. I am testing my SDK for calling the OpenAI Responses API. Please follow my instructions carefully to build a useful test case. First, here is an image and document input. Search for headlines from today, pick one and describe it to me, Calculate the 5th prime number using python via the code interpreter tool. Summarize the document in 3 sentences and describe the image in one sentence. Do all of this and then send back a single text response. Finally, after that is done and you have sent back the text response with the answers for everything else, get today's horoscope for Scorpio. You MUST output text and wait for the user to respond before querying for the horoscope information."

    # with open("/Users/armandmcqueen/code/kintu/kintu/clients/openai/berkshire_hathaway_letter.pdf", "rb") as f:
    #     data = f.read()
    #
    # base64_string = base64.b64encode(data).decode("utf-8")


    messages:  list[RawOpenAIResponseInputItemParam] = [
        RawOpenAIEasyInputMessageParam(role="user", content=[RawOpenAIResponseInputTextParam(text=text, type="input_text")]),
        RawOpenAIEasyInputMessageParam(role="user", content=[RawOpenAIResponseInputImageParam(detail="low", type="input_image", image_url=image_data)]),
        RawOpenAIEasyInputMessageParam(role="user", content=[RawOpenAIResponseInputFileParam(type="input_file", file_data=pdf_data, filename="../../../data/berkshire_hathaway_letter.pdf")]),
        # {
        #     "role": "user",
        #     "content": [
        #         {
        #             "type": "input_file",
        #             "filename": "draconomicon.pdf",
        #             "file_data": f"data:application/pdf;base64,{base64_string}",
        #         },
        #     ],
        # },
    ]
    response = client.responses.create(
        model="gpt-5-mini",
        input=messages,
        reasoning=Reasoning(
            effort="low",
            summary="auto"
        ),
        tools=get_tools()
    )

    message_type_list = [m.type for m in response.output]
    assert len(response.output) == 5, f"The first message didn't have 5 items {message_type_list}"
    assert response.output[0].type == "reasoning"
    assert response.output[1].type == "web_search_call"
    assert response.output[2].type == "reasoning"
    assert response.output[3].type == "code_interpreter_call"
    assert response.output[4].type == "message"
    assert response.output[4].role == "assistant"
    print("=" * 100)
    print(response)
    print()
    print()
    print("-" * 100)
    for item in response.output:
        print(item)
        print()
    print("=" * 100)

    new_messages = []
    new_messages.extend(messages)
    new_messages.extend(response.output)
    new_messages.extend([RawOpenAIEasyInputMessageParam(role="user", content=[RawOpenAIResponseInputTextParam(text="Okay, now get the horoscope for Scorpio.", type="input_text")])])
    response = client.responses.create(
        model="gpt-5-mini",
        input=new_messages,
        reasoning=Reasoning(
            effort="low",
            summary="auto"
        ),
        tools=get_tools()
    )

    message_type_list = [m.type for m in response.output]
    assert len(response.output) == 2, f"The second message didn't have 2 items {message_type_list}"
    assert response.output[0].type == "reasoning"
    assert response.output[1].type == "function_call"

    print("=" * 100)
    print(response)
    print()
    print()
    print("-" * 100)
    for item in response.output:
        print(item)
        print()
    print("=" * 100)
    assert len(response.output) == 2  # Reasoning
    assert response.output[0].type == "reasoning"
    assert response.output[1].type == "function_call"
    function_call_message_id = response.output[1].id
    function_call_id = response.output[1].call_id

    tool_call_response = RawOpenAIFunctionCallOutput(call_id=function_call_id, output='{"horoscope": "You will have a good day."}', type="function_call_output")
    final_messages = []
    final_messages.extend(new_messages)
    final_messages.extend(response.output)
    final_messages.append(tool_call_response)
    # print("final_messages: " + str(final_messages))
    response = client.responses.create(
        model="gpt-5-mini",
        input=final_messages,
        reasoning=Reasoning(
            effort="low",
            summary="auto"
        ),
        tools=get_tools()
    )
    message_type_list = [m.type for m in response.output]
    assert len(response.output) == 1, f"The final message didn't have 1 items {message_type_list}"
    assert response.output[0].type == "message"
    print("=" * 100)
    print(response)
    print()
    print()
    print("------------------")
    for item in response.output:
        print(item)
        print()
    print("=" * 100)


"""
(kintu) ➜  kintu git:(converters) ✗ uv run kintu/clients/openai/type_inspector.py
====================================================================================================
Response(id='resp_68a198475f348196b217854eef254f0a0ff7ccaf75048215', created_at=1755420743.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-5-mini-2025-08-07', object='response', output=[ResponseReasoningItem(id='rs_68a1984dd958819690f678ff6e89e9640ff7ccaf75048215', summary=[], type='reasoning', content=None, encrypted_content=None, status=None), ResponseFunctionWebSearch(id='ws_68a1985143a48196aa2be097e2e233db0ff7ccaf75048215', action=ActionSearch(query='top headlines August 17 2025 news', type='search'), status='completed', type='web_search_call'), ResponseReasoningItem(id='rs_68a1985b27d08196a0c93a4523766c9d0ff7ccaf75048215', summary=[Summary(text='**Deciding on a headline**\n\nI have enough search results to pick a relevant headline from today, August 17, 2025. I\'m considering the US-EU trade framework, but that was actually from July. Instead, I’m leaning towards "Prime Minister Modi inaugurates highway projects." However, I remember the user is likely in the US, so I\'m also thinking about the Trump-Putin Alaska summit from August 15. Ultimately, I need to choose a headline from today\'s results and describe it. After that, I’ll compute the 5th prime number using Python and summarize the document in three sentences.', type='summary_text')], type='reasoning', content=None, encrypted_content=None, status=None), ResponseCodeInterpreterToolCall(id='ci_68a1985d7f848196973f02b55ccc02070ff7ccaf75048215', code='# compute 5th prime\ndef is_prime(n):\n    if n<2: return False\n    i=2\n    while i*i<=n:\n        if n%i==0:\n            return False\n        i+=1\n    return True\n\nprimes=[]\nn=2\nwhile len(primes)<5:\n    if is_prime(n):\n        primes.append(n)\n    n+=1\nprimes, primes[-1]', container_id='cntr_68a19849bb3481939e316f73a5b193e6023d6726327df5f7', outputs=None, status='completed', type='code_interpreter_call'), ResponseOutputMessage(id='msg_68a1985dbd048196a07583dd9342a10c0ff7ccaf75048215', content=[ResponseOutputText(annotations=[], text='Headline I picked (from today, August 17, 2025): Prime Minister Narendra Modi inaugurated major highway projects in the Delhi‑NCR region to improve connectivity (reports on Aug 17, 2025). Description: The announcement and ribbon‑cutting highlight completion and opening of key sections (including an airport‑to‑Noida connector), which officials say will significantly shorten travel times to/from Indira Gandhi International Airport and ease congestion across the Delhi‑NCR corridor; the event included statements about boosting regional economic activity and infrastructure investment.\n\n5th prime number (calculated with Python): 11.\n\nDocument summary (3 sentences):\n1. Warren Buffett’s 2024 annual letter to Berkshire Hathaway shareholders reviews mistakes and successes, emphasizes candid reporting, and repeats the company’s long-term preference for reinvesting earnings rather than paying dividends. \n2. The letter highlights 2024 operating results (noting strong investment income and insurance performance), discusses the centrality and risks of property‑casualty insurance, and describes strategic moves including increased utility ownership and expanded Japanese investments. \n3. Buffett stresses prudent capital allocation, the importance of capable managers (telling the story of Pete Liegl), Berkshire’s American focus tempered by select foreign holdings, and the company’s commitment to long‑term shareholder value and responsible stewardship.\n\nImage description (1 sentence):\nThe image shows a bright red neon numeral “3” glowing against a pitch‑black background. \n\nI’ve completed the search, the Python calculation, the document summary, and the image description. When you’re ready, reply and I will fetch today’s Scorpio horoscope for you.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[CodeInterpreter(container=CodeInterpreterContainerCodeInterpreterToolAuto(type='auto', file_ids=None), type='code_interpreter'), FunctionTool(name='get_horoscope', parameters={'type': 'object', 'properties': {'sign': {'type': 'string', 'description': 'An astrological sign like Taurus or Aquarius'}}, 'required': ['sign'], 'additionalProperties': False}, strict=True, type='function', description="Get today's horoscope for an astrological sign."), WebSearchTool(type='web_search_preview', search_context_size='medium', user_location=UserLocation(type='approximate', city=None, country='US', region=None, timezone=None))], top_p=1.0, background=False, max_output_tokens=None, max_tool_calls=None, previous_response_id=None, prompt=None, prompt_cache_key=None, reasoning=Reasoning(effort='low', generate_summary=None, summary='detailed'), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=53058, input_tokens_details=InputTokensDetails(cached_tokens=23296), output_tokens=651, output_tokens_details=OutputTokensDetails(reasoning_tokens=320), total_tokens=53709), user=None, store=True)


----------------------------------------------------------------------------------------------------
ResponseReasoningItem(id='rs_68a1984dd958819690f678ff6e89e9640ff7ccaf75048215', summary=[], type='reasoning', content=None, encrypted_content=None, status=None)

ResponseFunctionWebSearch(id='ws_68a1985143a48196aa2be097e2e233db0ff7ccaf75048215', action=ActionSearch(query='top headlines August 17 2025 news', type='search'), status='completed', type='web_search_call')

ResponseReasoningItem(id='rs_68a1985b27d08196a0c93a4523766c9d0ff7ccaf75048215', summary=[Summary(text='**Deciding on a headline**\n\nI have enough search results to pick a relevant headline from today, August 17, 2025. I\'m considering the US-EU trade framework, but that was actually from July. Instead, I’m leaning towards "Prime Minister Modi inaugurates highway projects." However, I remember the user is likely in the US, so I\'m also thinking about the Trump-Putin Alaska summit from August 15. Ultimately, I need to choose a headline from today\'s results and describe it. After that, I’ll compute the 5th prime number using Python and summarize the document in three sentences.', type='summary_text')], type='reasoning', content=None, encrypted_content=None, status=None)

ResponseCodeInterpreterToolCall(id='ci_68a1985d7f848196973f02b55ccc02070ff7ccaf75048215', code='# compute 5th prime\ndef is_prime(n):\n    if n<2: return False\n    i=2\n    while i*i<=n:\n        if n%i==0:\n            return False\n        i+=1\n    return True\n\nprimes=[]\nn=2\nwhile len(primes)<5:\n    if is_prime(n):\n        primes.append(n)\n    n+=1\nprimes, primes[-1]', container_id='cntr_68a19849bb3481939e316f73a5b193e6023d6726327df5f7', outputs=None, status='completed', type='code_interpreter_call')

ResponseOutputMessage(id='msg_68a1985dbd048196a07583dd9342a10c0ff7ccaf75048215', content=[ResponseOutputText(annotations=[], text='Headline I picked (from today, August 17, 2025): Prime Minister Narendra Modi inaugurated major highway projects in the Delhi‑NCR region to improve connectivity (reports on Aug 17, 2025). Description: The announcement and ribbon‑cutting highlight completion and opening of key sections (including an airport‑to‑Noida connector), which officials say will significantly shorten travel times to/from Indira Gandhi International Airport and ease congestion across the Delhi‑NCR corridor; the event included statements about boosting regional economic activity and infrastructure investment.\n\n5th prime number (calculated with Python): 11.\n\nDocument summary (3 sentences):\n1. Warren Buffett’s 2024 annual letter to Berkshire Hathaway shareholders reviews mistakes and successes, emphasizes candid reporting, and repeats the company’s long-term preference for reinvesting earnings rather than paying dividends. \n2. The letter highlights 2024 operating results (noting strong investment income and insurance performance), discusses the centrality and risks of property‑casualty insurance, and describes strategic moves including increased utility ownership and expanded Japanese investments. \n3. Buffett stresses prudent capital allocation, the importance of capable managers (telling the story of Pete Liegl), Berkshire’s American focus tempered by select foreign holdings, and the company’s commitment to long‑term shareholder value and responsible stewardship.\n\nImage description (1 sentence):\nThe image shows a bright red neon numeral “3” glowing against a pitch‑black background. \n\nI’ve completed the search, the Python calculation, the document summary, and the image description. When you’re ready, reply and I will fetch today’s Scorpio horoscope for you.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')

====================================================================================================
====================================================================================================
Response(id='resp_68a198612afc8196a20f42e920ec12cd0ff7ccaf75048215', created_at=1755420769.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-5-mini-2025-08-07', object='response', output=[ResponseReasoningItem(id='rs_68a1986434ac8196b733eb16f2a51be80ff7ccaf75048215', summary=[Summary(text='**Fetching horoscope for Scorpio**\n\nI see that I can use the function to get today\'s horoscope without needing a web search. This means I can just call functions.get_horoscope with "Scorpio" as the sign. Using multi_tool_use.parallel doesn\'t seem necessary here, so I\'ll keep it simple and stick to the provided tools. I\'m ready to get that horoscope for the user!', type='summary_text')], type='reasoning', content=None, encrypted_content=None, status=None), ResponseFunctionToolCall(arguments='{"sign":"Scorpio"}', call_id='call_HxLthnPZegFu0AfBQRXYno8y', name='get_horoscope', type='function_call', id='fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215', status='completed')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[CodeInterpreter(container=CodeInterpreterContainerCodeInterpreterToolAuto(type='auto', file_ids=None), type='code_interpreter'), FunctionTool(name='get_horoscope', parameters={'type': 'object', 'properties': {'sign': {'type': 'string', 'description': 'An astrological sign like Taurus or Aquarius'}}, 'required': ['sign'], 'additionalProperties': False}, strict=True, type='function', description="Get today's horoscope for an astrological sign."), WebSearchTool(type='web_search_preview', search_context_size='medium', user_location=UserLocation(type='approximate', city=None, country='US', region=None, timezone=None))], top_p=1.0, background=False, max_output_tokens=None, max_tool_calls=None, previous_response_id=None, prompt=None, prompt_cache_key=None, reasoning=Reasoning(effort='low', generate_summary=None, summary='detailed'), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=15420, input_tokens_details=InputTokensDetails(cached_tokens=14464), output_tokens=87, output_tokens_details=OutputTokensDetails(reasoning_tokens=64), total_tokens=15507), user=None, store=True)


----------------------------------------------------------------------------------------------------
ResponseReasoningItem(id='rs_68a1986434ac8196b733eb16f2a51be80ff7ccaf75048215', summary=[Summary(text='**Fetching horoscope for Scorpio**\n\nI see that I can use the function to get today\'s horoscope without needing a web search. This means I can just call functions.get_horoscope with "Scorpio" as the sign. Using multi_tool_use.parallel doesn\'t seem necessary here, so I\'ll keep it simple and stick to the provided tools. I\'m ready to get that horoscope for the user!', type='summary_text')], type='reasoning', content=None, encrypted_content=None, status=None)

ResponseFunctionToolCall(arguments='{"sign":"Scorpio"}', call_id='call_HxLthnPZegFu0AfBQRXYno8y', name='get_horoscope', type='function_call', id='fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215', status='completed')

====================================================================================================
====================================================================================================
Response(id='resp_68a19868750c8196accec503705d40f30ff7ccaf75048215', created_at=1755420776.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-5-mini-2025-08-07', object='response', output=[ResponseOutputMessage(id='msg_68a1986c589081968db13a3b1094f3b20ff7ccaf75048215', content=[ResponseOutputText(annotations=[], text='You will have a good day.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[CodeInterpreter(container=CodeInterpreterContainerCodeInterpreterToolAuto(type='auto', file_ids=None), type='code_interpreter'), FunctionTool(name='get_horoscope', parameters={'type': 'object', 'properties': {'sign': {'type': 'string', 'description': 'An astrological sign like Taurus or Aquarius'}}, 'required': ['sign'], 'additionalProperties': False}, strict=True, type='function', description="Get today's horoscope for an astrological sign."), WebSearchTool(type='web_search_preview', search_context_size='medium', user_location=UserLocation(type='approximate', city=None, country='US', region=None, timezone=None))], top_p=1.0, background=False, max_output_tokens=None, max_tool_calls=None, previous_response_id=None, prompt=None, prompt_cache_key=None, reasoning=Reasoning(effort='low', generate_summary=None, summary='detailed'), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=15533, input_tokens_details=InputTokensDetails(cached_tokens=15104), output_tokens=11, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=15544), user=None, store=True)


------------------
ResponseOutputMessage(id='msg_68a1986c589081968db13a3b1094f3b20ff7ccaf75048215', content=[ResponseOutputText(annotations=[], text='You will have a good day.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')

====================================================================================================

"""

if __name__ == '__main__':
    run_responses_api()

