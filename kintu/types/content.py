from __future__ import annotations

from typing import Any

from PIL import Image
from pydantic import BaseModel, ConfigDict


# Content types
class Content(BaseModel):
    """Base class for all content types."""

    model_config = ConfigDict(arbitrary_types_allowed=True)


class TextContent(Content):
    text: str


class ImageContent(Content):
    image: Image.Image


class DocumentContent(Content):
    document: bytes
    openai_filename: str | None = None


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


# OpenAI-specific content types
class OpenAIServerToolUse(Content):
    """OpenAI server-side tool use"""

    tool_id: str
    tool_name: str
    tool_type: str  # e.g., 'web_search_preview_2025_03_11', 'code_interpreter'
    input: dict[str, Any] = {}


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
    | OpenAIServerToolUse
    | GeminiServerToolUse
    | GeminiWebSearchResult
    | GeminiCodeExecutionResult
)
