"""
Test scaffolding for OpenAI <-> Kintu converters.

This file contains test cases for converting between Kintu Messages and OpenAI types.
We're using real examples from type_inspector.py as test cases.
"""

import base64
import json
from pathlib import Path
from typing import Any
from PIL import Image

from kintu.types.message import Message
from kintu.types.role import Role
from kintu.types.content import (
    TextContent,
    ImageContent,
    DocumentContent,
    ThinkingContent,
    ToolCallContent,
    ToolResultContent,
    OpenAIWebSearchCalled,
    OpenAICodeInterpreterToolResult,
    OpenAICodeInterpreterOutputElement,
)
from kintu.types.llmsdks.openai_types import (
    RawOpenAIResponseOutputMessageParam,
    RawOpenAIEasyInputMessageParam,
    RawOpenAIResponseInputTextParam,
    RawOpenAIResponseInputImageParam,
    RawOpenAIResponseInputFileParam,
    RawOpenAIResponseReasoningItemParam,
    RawOpenAIResponseFunctionToolCallParam,
    RawOpenAIFunctionCallOutput,
    RawOpenAIResponseFunctionWebSearchParam,
    RawOpenAIResponseCodeInterpreterToolCallParam,
    RawOpenAIResponseOutputMessage,
    RawOpenAIResponseOutputText,
    RawOpenAIResponseReasoningItem,
    RawOpenAIResponseFunctionToolCall,
    RawOpenAIResponseCodeInterpreterToolCall,
    RawOpenAIResponseFunctionWebSearch,
)
from kintu.utilities import image_to_base64_png


# Test data setup
def get_test_image() -> tuple[Image.Image, str]:
    """Load test image and return PIL Image and base64 string."""
    image_path = Path(__file__).parent.parent.parent.parent / "data" / "test_image_3.png"
    image = Image.open(image_path)
    b64_image = image_to_base64_png(image)
    return image, b64_image


def get_test_pdf() -> tuple[bytes, str]:
    """Load test PDF and return bytes and base64 string."""
    pdf_path = Path(__file__).parent.parent.parent.parent / "data" / "berkshire_hathaway_letter.pdf"
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    b64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    return pdf_bytes, b64_pdf


class KintuToOpenAIConverter:
    """Converts Kintu Messages to OpenAI types."""
    
    def convert_message(self, message: Message) -> Any:
        """Convert a single Kintu Message to OpenAI type."""
        content = message.content
        
        # Handle user messages
        if message.role == Role.USER:
            if isinstance(content, TextContent):
                return RawOpenAIEasyInputMessageParam(
                    role="user",
                    content=[RawOpenAIResponseInputTextParam(
                        text=content.text,
                        type="input_text"
                    )]
                )
            elif isinstance(content, ImageContent):
                b64_image = image_to_base64_png(content.image)
                return RawOpenAIEasyInputMessageParam(
                    role="user",
                    content=[RawOpenAIResponseInputImageParam(
                        detail="low",
                        type="input_image",
                        image_url=f"data:image/png;base64,{b64_image}"
                    )]
                )
            elif isinstance(content, DocumentContent):
                b64_doc = base64.b64encode(content.document).decode("utf-8")
                filename = content._openai_filename or "document.pdf"
                return RawOpenAIEasyInputMessageParam(
                    role="user",
                    content=[RawOpenAIResponseInputFileParam(
                        type="input_file",
                        file_data=f"data:application/pdf;base64,{b64_doc}",
                        filename=filename
                    )]
                )
        
        # Handle assistant messages
        elif message.role == Role.ASSISTANT:
            if isinstance(content, TextContent):
                # For now, return the essential structure
                # In real implementation, would need to handle id, status, etc.
                return RawOpenAIResponseOutputMessageParam(
                    role="assistant",
                    content=[{
                        "type": "output_text",
                        "text": content.text
                    }]
                )
            elif isinstance(content, ThinkingContent):
                return RawOpenAIResponseReasoningItemParam(
                    type="reasoning",
                    content=content.thinking if not content.encrypted_data else None,
                    encrypted_content=content.encrypted_data
                )
            elif isinstance(content, ToolCallContent):
                return RawOpenAIResponseFunctionToolCallParam(
                    type="function_call",
                    name=content.tool_name,
                    arguments=json.dumps(content.input),
                    call_id=content.tool_id,
                    id=content.openai_id or ""
                )
            elif isinstance(content, OpenAIWebSearchCalled):
                action = {"type": content.action_type}
                if content.search_query:
                    action["query"] = content.search_query
                elif content.open_page_url:
                    action["url"] = content.open_page_url
                elif content.find_url:
                    action["url"] = content.find_url
                    action["pattern"] = content.find_pattern
                    
                return RawOpenAIResponseFunctionWebSearchParam(
                    type="web_search_call",
                    id=content.id,
                    action=action
                )
            elif isinstance(content, OpenAICodeInterpreterToolResult):
                return RawOpenAIResponseCodeInterpreterToolCallParam(
                    type="code_interpreter_call",
                    id=content.id,
                    code=content.code,
                    container_id=content.container_id,
                    outputs=content.outputs
                )
        
        # Handle tool messages
        elif message.role == Role.TOOL:
            if isinstance(content, ToolResultContent):
                # Combine all text results
                output_text = ""
                for result in content.results:
                    if isinstance(result, TextContent):
                        output_text += result.text
                
                return RawOpenAIFunctionCallOutput(
                    call_id=content.tool_id,
                    output=output_text,
                    type="function_call_output"
                )
        
        raise NotImplementedError(f"Conversion not implemented for {type(content)} with role {message.role}")
    
    def convert_messages(self, messages: list[Message]) -> list[Any]:
        """Convert a list of Kintu Messages to OpenAI types."""
        return [self.convert_message(msg) for msg in messages]


class OpenAIToKintuConverter:
    """Converts OpenAI types to Kintu Messages."""
    
    def convert_item(self, item: Any) -> Message:
        """Convert a single OpenAI item to Kintu Message."""
        
        # TypedDicts may come as dicts or as TypedDict instances
        # Check by attributes rather than type
        
        # Handle RawOpenAIEasyInputMessageParam (check for role and content attributes)
        if isinstance(item, dict) and 'role' in item and 'content' in item:
            role = Role.USER if item['role'] == "user" else Role.ASSISTANT
            
            # Handle different content types
            if item['content'] and len(item['content']) > 0:
                first_content = item['content'][0]
                
                # Check content type by 'type' field
                if first_content.get('type') == 'input_text':
                    return Message(
                        role=role,
                        content=TextContent(text=first_content['text'])
                    )
                elif first_content.get('type') == 'input_image':
                    # Extract base64 from data URL
                    if first_content['image_url'].startswith("data:image"):
                        b64_data = first_content['image_url'].split(",")[1]
                        image_bytes = base64.b64decode(b64_data)
                        image = Image.open(io.BytesIO(image_bytes))
                        return Message(
                            role=role,
                            content=ImageContent(image=image)
                        )
                elif first_content.get('type') == 'input_file':
                    # Extract base64 from data URL
                    if first_content['file_data'].startswith("data:"):
                        b64_data = first_content['file_data'].split(",")[1]
                        doc_bytes = base64.b64decode(b64_data)
                        return Message(
                            role=role,
                            content=DocumentContent(
                                document=doc_bytes,
                                _openai_filename=first_content['filename']
                            )
                        )
        
        # Handle RawOpenAIResponseOutputMessage
        elif hasattr(item, 'type') and item.type == 'message' and hasattr(item, 'role'):
            if item.content and len(item.content) > 0:
                first_content = item.content[0]
                if hasattr(first_content, 'text'):
                    return Message(
                        role=Role.ASSISTANT,
                        content=TextContent(text=first_content.text)
                    )
        
        # Handle RawOpenAIResponseReasoningItem
        elif hasattr(item, 'type') and item.type == 'reasoning':
            # Extract thinking from summary if available
            thinking_text = ""
            if hasattr(item, 'summary') and item.summary and len(item.summary) > 0:
                summary_item = item.summary[0]
                if isinstance(summary_item, dict):
                    thinking_text = summary_item.get('text', str(summary_item))
                else:
                    thinking_text = summary_item.text if hasattr(summary_item, 'text') else str(summary_item)
            elif hasattr(item, 'content') and item.content:
                thinking_text = item.content
            
            return Message(
                role=Role.ASSISTANT,
                content=ThinkingContent(
                    thinking=thinking_text,
                    reasoning_id=item.id if hasattr(item, 'id') else None,
                    encrypted_data=item.encrypted_content if hasattr(item, 'encrypted_content') else None
                )
            )
        
        # Handle RawOpenAIResponseFunctionToolCall
        elif hasattr(item, 'type') and item.type == 'function_call' and hasattr(item, 'call_id'):
            input_dict = json.loads(item.arguments) if item.arguments else {}
            return Message(
                role=Role.ASSISTANT,
                content=ToolCallContent(
                    tool_id=item.call_id,
                    tool_name=item.name,
                    input=input_dict,
                    openai_id=item.id
                )
            )
        
        # Handle RawOpenAIFunctionCallOutput
        elif (hasattr(item, 'type') and hasattr(item, 'call_id') and 
              getattr(item, 'type', None) == 'function_call_output'):
            return Message(
                role=Role.TOOL,
                content=ToolResultContent(
                    tool_id=item.call_id if hasattr(item, 'call_id') else item['call_id'],
                    results=[TextContent(text=item.output if hasattr(item, 'output') else item['output'])],
                    is_error=False
                )
            )
        # Also handle as dict
        elif isinstance(item, dict) and item.get('type') == 'function_call_output':
            return Message(
                role=Role.TOOL,
                content=ToolResultContent(
                    tool_id=item['call_id'],
                    results=[TextContent(text=item['output'])],
                    is_error=False
                )
            )
        
        # Handle RawOpenAIResponseFunctionWebSearch
        elif (hasattr(item, 'type') and hasattr(item, 'id') and 
              getattr(item, 'type', None) == 'web_search_call'):
            action = item.action if isinstance(item.action, dict) else {"type": "search"}
            action_type = action.get("type", "search")
            
            return Message(
                role=Role.ASSISTANT,
                content=OpenAIWebSearchCalled(
                    id=item.id,
                    action_type=action_type,
                    search_query=action.get("query"),
                    open_page_url=action.get("url") if action_type == "open_page" else None,
                    find_url=action.get("url") if action_type == "find" else None,
                    find_pattern=action.get("pattern") if action_type == "find" else None
                )
            )
        # Also handle as dict  
        elif isinstance(item, dict) and item.get('type') == 'web_search_call':
            action = item.get('action', {"type": "search"})
            if not isinstance(action, dict):
                action = {"type": "search"}
            action_type = action.get("type", "search")
            
            return Message(
                role=Role.ASSISTANT,
                content=OpenAIWebSearchCalled(
                    id=item['id'],
                    action_type=action_type,
                    search_query=action.get("query"),
                    open_page_url=action.get("url") if action_type == "open_page" else None,
                    find_url=action.get("url") if action_type == "find" else None,
                    find_pattern=action.get("pattern") if action_type == "find" else None
                )
            )
        
        # Handle RawOpenAIResponseCodeInterpreterToolCall
        elif hasattr(item, 'type') and item.type == 'code_interpreter_call':
            return Message(
                role=Role.ASSISTANT,
                content=OpenAICodeInterpreterToolResult(
                    id=item.id,
                    code=item.code,
                    container_id=item.container_id,
                    outputs=item.outputs
                )
            )
        
        raise NotImplementedError(f"Conversion not implemented for {type(item)}")
    
    def convert_items(self, items: list[Any]) -> list[Message]:
        """Convert a list of OpenAI items to Kintu Messages."""
        return [self.convert_item(item) for item in items]


# Import io for image conversion
import io


def get_example_messages() -> dict[str, Any]:
    """Get all example messages from type_inspector.py output."""
    image, b64_image = get_test_image()
    pdf_bytes, b64_pdf = get_test_pdf()
    
    # Initial user messages
    text_input = RawOpenAIEasyInputMessageParam(
        role="user",
        content=[RawOpenAIResponseInputTextParam(
            text="Hello. I am testing my SDK for calling the OpenAI Responses API. Please follow my instructions carefully to build a useful test case.",
            type="input_text"
        )]
    )
    
    image_input = RawOpenAIEasyInputMessageParam(
        role="user",
        content=[RawOpenAIResponseInputImageParam(
            detail="low",
            type="input_image",
            image_url=f"data:image/png;base64,{b64_image}"
        )]
    )
    
    file_input = RawOpenAIEasyInputMessageParam(
        role="user",
        content=[RawOpenAIResponseInputFileParam(
            type="input_file",
            file_data=f"data:application/pdf;base64,{b64_pdf}",
            filename="../../../data/berkshire_hathaway_letter.pdf"
        )]
    )
    
    # First response items (from type_inspector output)
    reasoning_1 = RawOpenAIResponseReasoningItem(
        id="rs_68a1984dd958819690f678ff6e89e9640ff7ccaf75048215",
        summary=[],
        type="reasoning",
        content=None,
        encrypted_content=None,
        status=None
    )
    
    web_search = RawOpenAIResponseFunctionWebSearch(
        id="ws_68a1985143a48196aa2be097e2e233db0ff7ccaf75048215",
        action={"query": "top headlines August 17 2025 news", "type": "search"},
        status="completed",
        type="web_search_call"
    )
    
    reasoning_2 = RawOpenAIResponseReasoningItem(
        id="rs_68a1985b27d08196a0c93a4523766c9d0ff7ccaf75048215",
        summary=[{"text": "**Deciding on a headline**\n\nI need to choose a headline from today's results and describe it.", "type": "summary_text"}],
        type="reasoning",
        content=None,
        encrypted_content=None,
        status=None
    )
    
    code_interpreter = RawOpenAIResponseCodeInterpreterToolCall(
        id="ci_68a1985d7f848196973f02b55ccc02070ff7ccaf75048215",
        code="# compute 5th prime\ndef is_prime(n):\n    if n<2: return False\n    i=2\n    while i*i<=n:\n        if n%i==0:\n            return False\n        i+=1\n    return True\n\nprimes=[]\nn=2\nwhile len(primes)<5:\n    if is_prime(n):\n        primes.append(n)\n    n+=1\nprimes, primes[-1]",
        container_id="cntr_68a19849bb3481939e316f73a5b193e6023d6726327df5f7",
        outputs=None,
        status="completed",
        type="code_interpreter_call"
    )
    
    output_message_1 = RawOpenAIResponseOutputMessage(
        id="msg_68a1985dbd048196a07583dd9342a10c0ff7ccaf75048215",
        content=[RawOpenAIResponseOutputText(
            annotations=[],
            text="Headline I picked: Prime Minister Narendra Modi inaugurated major highway projects. 5th prime number: 11. Document summary: Warren Buffett's 2024 letter reviews performance. Image: bright red neon numeral '3'.",
            type="output_text",
            logprobs=[]
        )],
        role="assistant",
        status="completed",
        type="message"
    )
    
    # Second user message
    user_followup = RawOpenAIEasyInputMessageParam(
        role="user",
        content=[RawOpenAIResponseInputTextParam(
            text="Okay, now get the horoscope for Scorpio.",
            type="input_text"
        )]
    )
    
    # Second response items
    reasoning_3 = RawOpenAIResponseReasoningItem(
        id="rs_68a1986434ac8196b733eb16f2a51be80ff7ccaf75048215",
        summary=[{"text": "**Fetching horoscope for Scorpio**\n\nI can use the function to get today's horoscope.", "type": "summary_text"}],
        type="reasoning",
        content=None,
        encrypted_content=None,
        status=None
    )
    
    function_call = RawOpenAIResponseFunctionToolCall(
        arguments='{"sign":"Scorpio"}',
        call_id="call_HxLthnPZegFu0AfBQRXYno8y",
        name="get_horoscope",
        type="function_call",
        id="fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215",
        status="completed"
    )
    
    # Tool result
    tool_result = RawOpenAIFunctionCallOutput(
        call_id="call_HxLthnPZegFu0AfBQRXYno8y",
        output='{"horoscope": "You will have a good day."}',
        type="function_call_output"
    )
    
    # Final response
    output_message_2 = RawOpenAIResponseOutputMessage(
        id="msg_68a1986c589081968db13a3b1094f3b20ff7ccaf75048215",
        content=[RawOpenAIResponseOutputText(
            annotations=[],
            text="You will have a good day.",
            type="output_text",
            logprobs=[]
        )],
        role="assistant",
        status="completed",
        type="message"
    )
    
    return {
        "user_inputs": [text_input, image_input, file_input, user_followup],
        "assistant_outputs": [
            reasoning_1, web_search, reasoning_2, code_interpreter,
            output_message_1, reasoning_3, function_call, output_message_2
        ],
        "tool_outputs": [tool_result],
        "all_messages": [
            text_input, image_input, file_input,
            reasoning_1, web_search, reasoning_2, code_interpreter, output_message_1,
            user_followup,
            reasoning_3, function_call,
            tool_result,
            output_message_2
        ],
        "test_data": {
            "image": image,
            "b64_image": b64_image,
            "pdf_bytes": pdf_bytes,
            "b64_pdf": b64_pdf
        }
    }


# Test cases based on real examples from type_inspector.py
class TestKintuToOpenAI:
    """Test converting Kintu Messages to OpenAI types."""
    
    def test_text_content_to_easy_input(self):
        """Test TextContent (user) -> RawOpenAIEasyInputMessageParam."""
        message = Message(
            role=Role.USER,
            content=TextContent(text="Hello. I am testing my SDK for calling the OpenAI Responses API.")
        )
        
        converter = KintuToOpenAIConverter()
        result = converter.convert_message(message)
        
        # Check it's a dict with the right structure (TypedDict)
        assert isinstance(result, dict)
        assert result['role'] == "user"
        assert len(result['content']) == 1
        assert result['content'][0]['text'] == "Hello. I am testing my SDK for calling the OpenAI Responses API."
        assert result['content'][0]['type'] == "input_text"
    
    def test_image_content_to_input(self):
        """Test ImageContent -> RawOpenAIResponseInputImageParam."""
        image, b64_image = get_test_image()
        
        message = Message(
            role=Role.USER,
            content=ImageContent(image=image)
        )
        
        converter = KintuToOpenAIConverter()
        result = converter.convert_message(message)
        
        assert isinstance(result, dict)
        assert result['role'] == "user"
        assert len(result['content']) == 1
        assert result['content'][0]['type'] == "input_image"
        assert result['content'][0]['detail'] == "low"
        assert result['content'][0]['image_url'].startswith("data:image/png;base64,")
    
    def test_document_content_to_input(self):
        """Test DocumentContent -> RawOpenAIResponseInputFileParam."""
        pdf_bytes, b64_pdf = get_test_pdf()
        
        message = Message(
            role=Role.USER,
            content=DocumentContent(
                document=pdf_bytes,
                _openai_filename="berkshire_hathaway_letter.pdf"
            )
        )
        
        converter = KintuToOpenAIConverter()
        result = converter.convert_message(message)
        
        assert isinstance(result, dict)
        assert result['role'] == "user"
        assert len(result['content']) == 1
        assert result['content'][0]['type'] == "input_file"
        assert result['content'][0]['filename'] == "berkshire_hathaway_letter.pdf"
        assert result['content'][0]['file_data'].startswith("data:application/pdf;base64,")
    
    def test_tool_call_content_to_function_call(self):
        """Test ToolCallContent -> RawOpenAIResponseFunctionToolCallParam."""
        message = Message(
            role=Role.ASSISTANT,
            content=ToolCallContent(
                tool_id="call_HxLthnPZegFu0AfBQRXYno8y",
                tool_name="get_horoscope",
                input={"sign": "Scorpio"},
                openai_id="fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215"
            )
        )
        
        converter = KintuToOpenAIConverter()
        result = converter.convert_message(message)
        
        assert result["type"] == "function_call"
        assert result["name"] == "get_horoscope"
        assert result["call_id"] == "call_HxLthnPZegFu0AfBQRXYno8y"
        assert json.loads(result["arguments"]) == {"sign": "Scorpio"}
    
    def test_tool_result_content_to_output(self):
        """Test ToolResultContent -> RawOpenAIFunctionCallOutput."""
        message = Message(
            role=Role.TOOL,
            content=ToolResultContent(
                tool_id="call_HxLthnPZegFu0AfBQRXYno8y",
                results=[TextContent(text='{"horoscope": "You will have a good day."}')],
                is_error=False
            )
        )
        
        converter = KintuToOpenAIConverter()
        result = converter.convert_message(message)
        
        assert isinstance(result, dict)
        assert result['call_id'] == "call_HxLthnPZegFu0AfBQRXYno8y"
        assert result['output'] == '{"horoscope": "You will have a good day."}'
        assert result['type'] == "function_call_output"


class TestOpenAIToKintu:
    """Test converting OpenAI types to Kintu Messages."""
    
    def test_easy_input_text_to_message(self):
        """Test RawOpenAIEasyInputMessageParam (text) -> Message with TextContent."""
        openai_item = RawOpenAIEasyInputMessageParam(
            role="user",
            content=[RawOpenAIResponseInputTextParam(
                text="Okay, now get the horoscope for Scorpio.",
                type="input_text"
            )]
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.USER
        assert isinstance(result.content, TextContent)
        assert result.content.text == "Okay, now get the horoscope for Scorpio."
    
    def test_easy_input_image_to_message(self):
        """Test RawOpenAIEasyInputMessageParam (image) -> Message with ImageContent."""
        image, b64_image = get_test_image()
        
        openai_item = RawOpenAIEasyInputMessageParam(
            role="user",
            content=[RawOpenAIResponseInputImageParam(
                detail="low",
                type="input_image",
                image_url=f"data:image/png;base64,{b64_image}"
            )]
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.USER
        assert isinstance(result.content, ImageContent)
        assert result.content.image is not None
        assert isinstance(result.content.image, Image.Image)
    
    def test_easy_input_file_to_message(self):
        """Test RawOpenAIEasyInputMessageParam (file) -> Message with DocumentContent."""
        pdf_bytes, b64_pdf = get_test_pdf()
        
        openai_item = RawOpenAIEasyInputMessageParam(
            role="user",
            content=[RawOpenAIResponseInputFileParam(
                type="input_file",
                file_data=f"data:application/pdf;base64,{b64_pdf}",
                filename="berkshire_hathaway_letter.pdf"
            )]
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.USER
        assert isinstance(result.content, DocumentContent)
        assert result.content.document == pdf_bytes
        assert result.content._openai_filename == "berkshire_hathaway_letter.pdf"
    
    def test_output_message_to_text(self):
        """Test RawOpenAIResponseOutputMessage -> Message with TextContent."""
        openai_item = RawOpenAIResponseOutputMessage(
            id="msg_68a1986c589081968db13a3b1094f3b20ff7ccaf75048215",
            content=[RawOpenAIResponseOutputText(
                annotations=[],
                text="You will have a good day.",
                type="output_text",
                logprobs=[]
            )],
            role="assistant",
            status="completed",
            type="message"
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.ASSISTANT
        assert isinstance(result.content, TextContent)
        assert result.content.text == "You will have a good day."
    
    def test_function_call_to_tool_call(self):
        """Test RawOpenAIResponseFunctionToolCall -> Message with ToolCallContent."""
        openai_item = RawOpenAIResponseFunctionToolCall(
            arguments='{"sign":"Scorpio"}',
            call_id="call_HxLthnPZegFu0AfBQRXYno8y",
            name="get_horoscope",
            type="function_call",
            id="fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215",
            status="completed"
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.ASSISTANT
        assert isinstance(result.content, ToolCallContent)
        assert result.content.tool_id == "call_HxLthnPZegFu0AfBQRXYno8y"
        assert result.content.tool_name == "get_horoscope"
        assert result.content.input == {"sign": "Scorpio"}
        assert result.content.openai_id == "fc_68a19866343c81968e77963c6ddde4be0ff7ccaf75048215"
    
    def test_function_output_to_tool_result(self):
        """Test RawOpenAIFunctionCallOutput -> Message with ToolResultContent."""
        openai_item = RawOpenAIFunctionCallOutput(
            call_id="call_HxLthnPZegFu0AfBQRXYno8y",
            output='{"horoscope": "You will have a good day."}',
            type="function_call_output"
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.TOOL
        assert isinstance(result.content, ToolResultContent)
        assert result.content.tool_id == "call_HxLthnPZegFu0AfBQRXYno8y"
        assert len(result.content.results) == 1
        assert isinstance(result.content.results[0], TextContent)
        assert result.content.results[0].text == '{"horoscope": "You will have a good day."}'
    
    def test_web_search_to_content(self):
        """Test RawOpenAIResponseFunctionWebSearch -> Message with OpenAIWebSearchCalled."""
        openai_item = RawOpenAIResponseFunctionWebSearch(
            id="ws_68a1985143a48196aa2be097e2e233db0ff7ccaf75048215",
            action={"query": "top headlines August 17 2025 news", "type": "search"},
            status="completed",
            type="web_search_call"
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.ASSISTANT
        assert isinstance(result.content, OpenAIWebSearchCalled)
        assert result.content.id == "ws_68a1985143a48196aa2be097e2e233db0ff7ccaf75048215"
        assert result.content.action_type == "search"
        assert result.content.search_query == "top headlines August 17 2025 news"
    
    def test_code_interpreter_to_content(self):
        """Test RawOpenAIResponseCodeInterpreterToolCall -> Message with OpenAICodeInterpreterToolResult."""
        openai_item = RawOpenAIResponseCodeInterpreterToolCall(
            id="ci_68a1985d7f848196973f02b55ccc02070ff7ccaf75048215",
            code="def is_prime(n):\n    return n > 1",
            container_id="cntr_68a19849bb3481939e316f73a5b193e6023d6726327df5f7",
            outputs=None,
            status="completed",
            type="code_interpreter_call"
        )
        
        converter = OpenAIToKintuConverter()
        result = converter.convert_item(openai_item)
        
        assert result.role == Role.ASSISTANT
        assert isinstance(result.content, OpenAICodeInterpreterToolResult)
        assert result.content.id == "ci_68a1985d7f848196973f02b55ccc02070ff7ccaf75048215"
        assert result.content.code == "def is_prime(n):\n    return n > 1"
        assert result.content.container_id == "cntr_68a19849bb3481939e316f73a5b193e6023d6726327df5f7"


class TestRoundTrip:
    """Test round-trip conversions with all real messages."""
    
    def test_all_message_types_round_trip(self):
        """Test round-trip for all message types from real examples."""
        examples = get_example_messages()
        to_openai = KintuToOpenAIConverter()
        from_openai = OpenAIToKintuConverter()
        
        # Test each type of message that can be round-tripped
        testable_messages = [
            # User text input
            examples["user_inputs"][0],
            # User image input
            examples["user_inputs"][1],
            # User file input
            examples["user_inputs"][2],
            # User followup
            examples["user_inputs"][3],
            # Assistant text output
            examples["assistant_outputs"][4],  # output_message_1
            # Function call
            examples["assistant_outputs"][6],  # function_call
            # Tool result
            examples["tool_outputs"][0],
            # Final output
            examples["assistant_outputs"][7],  # output_message_2
        ]
        
        for original_openai in testable_messages:
            # Convert OpenAI -> Kintu
            kintu_msg = from_openai.convert_item(original_openai)
            
            # Convert Kintu -> OpenAI
            back_to_openai = to_openai.convert_message(kintu_msg)
            
            # Verify key properties match
            # Check if it's an input message (has 'role' and 'content')
            if hasattr(original_openai, 'role') and hasattr(original_openai, 'content'):
                assert back_to_openai['role'] == original_openai['role']
                assert len(back_to_openai['content']) == len(original_openai['content'])
                # Check content type matches
                assert back_to_openai['content'][0]['type'] == original_openai['content'][0]['type']
            
            # Check if it's a function call output
            elif hasattr(original_openai, 'call_id'):
                assert back_to_openai['call_id'] == original_openai['call_id']
                assert back_to_openai['output'] == original_openai['output']
            
            # Can't fully round-trip output messages due to missing fields like id, status
            # But we can verify the essential content is preserved
    
    def test_conversation_flow(self):
        """Test converting a full conversation flow."""
        examples = get_example_messages()
        from_openai = OpenAIToKintuConverter()
        
        # Convert the conversation to Kintu messages
        conversation_items = [
            examples["user_inputs"][0],  # Initial text
            examples["user_inputs"][1],  # Image
            examples["user_inputs"][2],  # PDF
            examples["assistant_outputs"][4],  # First response
            examples["user_inputs"][3],  # Followup
            examples["assistant_outputs"][6],  # Function call
            examples["tool_outputs"][0],  # Tool result
            examples["assistant_outputs"][7],  # Final response
        ]
        
        kintu_messages = []
        for item in conversation_items:
            try:
                msg = from_openai.convert_item(item)
                kintu_messages.append(msg)
            except NotImplementedError:
                continue
        
        # Verify we have a coherent conversation
        assert len(kintu_messages) >= 6
        
        # Check role alternation makes sense
        user_count = sum(1 for m in kintu_messages if m.role == Role.USER)
        assistant_count = sum(1 for m in kintu_messages if m.role == Role.ASSISTANT)
        tool_count = sum(1 for m in kintu_messages if m.role == Role.TOOL)
        
        assert user_count == 4  # 3 initial + 1 followup
        assert assistant_count >= 2
        assert tool_count == 1


def run_tests():
    """Run all tests manually."""
    print("Running KintuToOpenAI tests...")
    kintu_to_openai = TestKintuToOpenAI()
    
    try:
        kintu_to_openai.test_text_content_to_easy_input()
        print("✓ test_text_content_to_easy_input passed")
    except Exception as e:
        print(f"✗ test_text_content_to_easy_input failed: {e}")
    
    try:
        kintu_to_openai.test_image_content_to_input()
        print("✓ test_image_content_to_input passed")
    except Exception as e:
        print(f"✗ test_image_content_to_input failed: {e}")
    
    try:
        kintu_to_openai.test_document_content_to_input()
        print("✓ test_document_content_to_input passed")
    except Exception as e:
        print(f"✗ test_document_content_to_input failed: {e}")
    
    try:
        kintu_to_openai.test_tool_call_content_to_function_call()
        print("✓ test_tool_call_content_to_function_call passed")
    except Exception as e:
        print(f"✗ test_tool_call_content_to_function_call failed: {e}")
    
    try:
        kintu_to_openai.test_tool_result_content_to_output()
        print("✓ test_tool_result_content_to_output passed")
    except Exception as e:
        print(f"✗ test_tool_result_content_to_output failed: {e}")
    
    print("\nRunning OpenAIToKintu tests...")
    openai_to_kintu = TestOpenAIToKintu()
    
    try:
        openai_to_kintu.test_easy_input_text_to_message()
        print("✓ test_easy_input_text_to_message passed")
    except Exception as e:
        print(f"✗ test_easy_input_text_to_message failed: {e}")
    
    try:
        openai_to_kintu.test_easy_input_image_to_message()
        print("✓ test_easy_input_image_to_message passed")
    except Exception as e:
        print(f"✗ test_easy_input_image_to_message failed: {e}")
    
    try:
        openai_to_kintu.test_easy_input_file_to_message()
        print("✓ test_easy_input_file_to_message passed")
    except Exception as e:
        print(f"✗ test_easy_input_file_to_message failed: {e}")
    
    try:
        openai_to_kintu.test_output_message_to_text()
        print("✓ test_output_message_to_text passed")
    except Exception as e:
        print(f"✗ test_output_message_to_text failed: {e}")
    
    try:
        openai_to_kintu.test_function_call_to_tool_call()
        print("✓ test_function_call_to_tool_call passed")
    except Exception as e:
        print(f"✗ test_function_call_to_tool_call failed: {e}")
    
    try:
        openai_to_kintu.test_function_output_to_tool_result()
        print("✓ test_function_output_to_tool_result passed")
    except Exception as e:
        print(f"✗ test_function_output_to_tool_result failed: {e}")
    
    try:
        openai_to_kintu.test_web_search_to_content()
        print("✓ test_web_search_to_content passed")
    except Exception as e:
        print(f"✗ test_web_search_to_content failed: {e}")
    
    try:
        openai_to_kintu.test_code_interpreter_to_content()
        print("✓ test_code_interpreter_to_content passed")
    except Exception as e:
        print(f"✗ test_code_interpreter_to_content failed: {e}")
    
    print("\nRunning RoundTrip tests...")
    round_trip = TestRoundTrip()
    
    try:
        round_trip.test_all_message_types_round_trip()
        print("✓ test_all_message_types_round_trip passed")
    except Exception as e:
        print(f"✗ test_all_message_types_round_trip failed: {e}")
    
    try:
        round_trip.test_conversation_flow()
        print("✓ test_conversation_flow passed")
    except Exception as e:
        print(f"✗ test_conversation_flow failed: {e}")


if __name__ == "__main__":
    run_tests()