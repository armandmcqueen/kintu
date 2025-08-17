
# kintu types (content.py)
```python
ContentTypes = (
        TextContent
        | ImageContent
        | DocumentContent
        | ThinkingContent
        | ToolCallContent
        | ToolResultContent
        | AnthropicRedactedThinkingContent
        | AnthropicServerToolUse
        | AnthropicWebSearchToolResult
        | AnthropicCodeInterpreterToolResult
        | OpenAIWebSearchCalled
        | OpenAICodeInterpreterToolResult
        | GeminiServerToolUse
        | GeminiWebSearchResult
        | GeminiCodeExecutionResult
)
```


# openai items fed into the API
```python
ResponseInputItemParam: TypeAlias = Union[
    EasyInputMessageParam,
    Message,
    ResponseOutputMessageParam,
    ResponseFileSearchToolCallParam,
    ResponseComputerToolCallParam,
    ComputerCallOutput,
    ResponseFunctionWebSearchParam,
    ResponseFunctionToolCallParam,
    FunctionCallOutput,
    ResponseReasoningItemParam,
    ImageGenerationCall,
    ResponseCodeInterpreterToolCallParam,
    LocalShellCall,
    LocalShellCallOutput,
    McpListTools,
    McpApprovalRequest,
    McpApprovalResponse,
    McpCall,
    ResponseCustomToolCallOutputParam,
    ResponseCustomToolCallParam,
    ItemReference,
]
```

# API documentation: https://platform.openai.com/docs/api-reference/responses/create#responses_create-input


# Missing (not currently supported)
- OpenAI refusal response message
- FileSearch tool call
- Computer tool call
- Computer tool call result
- ImageGeneration call (result, content in base64)
- MCP
- Local shell call
- Local shell call result
- Custom tool call
- Custom tool call result

# Conversions
```
TextContent <-> RawOpenAIResponseOutputMessageParam (assistant)
TextContent <-> EasyInputMessageParam/ResponseInputTextParam (user)
ImageContent <-> EasyInputMessageParam/ResponseInputImageParam
DocumentContent <-> EasyInputMessageParam/ResponseInputFileParam
ThinkingContent <-> ResponseReasoningItemParam
ToolCallContent <-> ResponseFunctionToolCallParam
ToolResultContent <-> FunctionCallOutput
OpenAIWebSearchResult <-> ResponseFunctionWebSearchParam
OpenAICodeInterpreterToolResult <-> ResponseCodeInterpreterToolCallParam
```
