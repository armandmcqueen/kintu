
from openai.types.responses import (
    Response as RawOpenAIResponse,
    ResponseOutputItem as RawOpenAIResponseOutputItem,
    ResponseOutputMessage as RawOpenAIResponseOutputMessage,
    ResponseOutputText as RawOpenAIResponseOutputText,
    ResponseReasoningItem as RawOpenAIResponseReasoningItem,
    ResponseFunctionToolCall as RawOpenAIResponseFunctionToolCall,
    ResponseCodeInterpreterToolCall as RawOpenAIResponseCodeInterpreterToolCall,
    ResponseFileSearchToolCall as RawOpenAIResponseFileSearchToolCall,
    ResponseComputerToolCall as RawOpenAIResponseComputerToolCall,
    ResponseFunctionWebSearch as RawOpenAIResponseFunctionWebSearch,
    ResponseInputItemParam as RawOpenAIResponseInputItemParam,
    ResponseOutputMessageParam as RawOpenAIResponseOutputMessageParam,
    ResponseInputParam as RawOpenAIResponseInputParam,
    ResponseInputItemParam as RawOpenAIResponseInputItemParam, # All the stuff that can be sent in, which is a superset of the stuff that can be sent out
    EasyInputMessageParam as RawOpenAIEasyInputMessageParam,
    ResponseInputTextParam as RawOpenAIResponseInputTextParam,
    ResponseInputImageParam as RawOpenAIResponseInputImageParam,
    ResponseInputFileParam as RawOpenAIResponseInputFileParam,
    ResponseFunctionWebSearchParam as RawOpenAIResponseFunctionWebSearchParam,
    ResponseCodeInterpreterToolCallParam as RawOpenAIResponseCodeInterpreterToolCallParam,
    ResponseFileSearchToolCallParam as RawOpenAIResponseFileSearchToolCallParam,
    ResponseComputerToolCallParam as RawOpenAIResponseComputerToolCallParam,
    ResponseFunctionToolCallParam as RawOpenAIResponseFunctionToolCallParam,
    ResponseReasoningItemParam as RawOpenAIResponseReasoningItemParam,
    ResponseCustomToolCallOutputParam as RawOpenAIResponseCustomToolCallOutputParam,
    ResponseCustomToolCallParam as RawOpenAIResponseCustomToolCallParam,
    WebSearchTool as RawOpenAIWebSearchTool,
    ResponseInputFile as RawOpenAIResponseInputFile,
    ResponseInputText as RawOpenAIResponseInputText,
    ResponseInputImage as RawOpenAIResponseInputImage,
    ResponseOutputItem as RawOpenAIResponseOutputItem,
    ResponseStreamEvent as RawOpenAIResponseStreamEvent,

)

from openai.types.responses.response_input_item_param import FunctionCallOutput as RawOpenAIFunctionCallOutput

# ComputerCallOutput
# FunctionCallOutput
# ImageGenerationCall
# LocalShellCall
# LocalShellCallOutput
# McpListTools
# McpApprovalRequest
# McpApprovalResponse
# McpCall