from __future__ import annotations

from typing import Any, Literal

from PIL import Image
from pydantic import BaseModel, ConfigDict


# Content is a general holder for entities that go into/out of the LLM. Usually you will send the
# LLM a series of Messages, each of which will be associated with a single specific Content type.
# There are some cases where a message may have multiple pieces of Content, specifically tool
# call results.
class Content(BaseModel):
    """Base class for all content types."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class TextContent(Content):
    text: str


class ImageContent(Content):
    image: Image.Image


class DocumentContent(Content):
    document: bytes
    _openai_filename: str | None = None


class ThinkingContent(Content):
    thinking: str
    reasoning_id: str | None = None
    # For multi-turn, we need to preserve encrypted thinking data
    encrypted_data: Any | None = None


class ToolCallContent(Content):
    tool_id: str
    tool_name: str
    input: dict[str, Any]

    openai_id: str | None = None


class ToolResultContent(Content):
    tool_id: str
    results: list[Content]  # Can contain TextContent, ImageContent, etc.
    is_error: bool = False


class AnthropicRedactedThinkingContent(Content):
    data: str

# Anthropic-specific content types
class AnthropicServerToolUse(Content):
    """Anthropic server-side tool use (web search, code execution, etc.)"""

    tool_id: str
    tool_name: str
    input: dict[str, Any] = {}


class AnthropicWebSearchIndividualResult(BaseModel):
    encrypted_content: str
    page_age: str | None = None
    title: str
    url: str


class AnthropicWebSearchToolResult(Content):
    """Anthropic web search tool result"""

    search_results: list[AnthropicWebSearchIndividualResult]
    tool_use_id: str
    error: str | None = None


class AnthropicCodeInterpreterToolResult(Content):
    """Anthropic code interpreter tool result"""

    tool_use_id: str
    return_code: int
    stdout: str
    stderr: str
    files: list[str]
    error_code: str | None = None


class OpenAIWebSearchCalled(Content):
    # This is a server-side message that says "We called the web search tool"
    # The output is never directly presented to the user, but there is text output from the API call that will leverage the
    # search results and will include annotations (which kintu doesn't currently support/reveal). In fact, this is an output
    # message that should probably be dropped before passing it back into the LLM.
    id: str
    action_type: Literal["search", "open_page", "find"]

    search_query: str | None = None
    open_page_url: str | None = None
    find_url: str | None = None
    find_pattern: str | None = None


class OpenAICodeInterpreterOutputElement(BaseModel):
    type: Literal["logs", "image"]
    content: str  # logs or image url

class OpenAICodeInterpreterToolResult(Content):
    """OpenAI code interpreter tool result"""
    id: str
    code: str | None = None
    container_id: str
    outputs: list[OpenAICodeInterpreterOutputElement] | None = None


# Gemini-specific content types
class GeminiServerToolUse(Content):
    """Gemini server-side tool use (web search, code execution, etc.)"""

    tool_id: str
    tool_name: str
    tool_type: str  # 'google_search', 'code_execution', etc.
    input: dict[str, Any] = {}


class GeminiWebSearchResult(Content):
    """Gemini web search result"""

    tool_use_id: str
    search_results: list[dict[str, Any]]  # List of search result dicts
    error: str | None = None


class GeminiCodeExecutionResult(Content):
    """Gemini code execution result"""

    tool_use_id: str
    outcome: str  # 'OUTCOME_OK' or error
    output: str | None = None
    error: str | None = None


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
