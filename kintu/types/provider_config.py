import enum
from typing import Any

from pydantic import BaseModel


class AnthropicToolChoice(str, enum.Enum):
    AUTO = "auto"  # Pick whether to use a tool
    NONE = "none"  # No tools
    ANY = "any"  # One or more
    TOOL = "tool"  # For one specific tool


# Provider configurations
class AnthropicConfig(BaseModel):
    # Anthropic-specific features
    disable_parallel_tool_use: bool | None = None
    container_id: str | None = None
    stop_sequences: list[str] | None = None
    top_p: float | None = None
    top_k: int | None = None

    tool_choice: AnthropicToolChoice | None = None
    tool_choice_specific_name: str | None = (
        None  # If tool_choice is TOOL, you must provide the name of the tool
    )

    # Thinking configuration
    thinking_enabled: bool | None = None
    thinking_budget: int | None = None

    # Beta features
    additional_beta_headers: list[str] | None = None  # e.g., ["computer-use-2024-10-22"]


class OpenAIReasoningLevel(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class OpenAIToolChoice(str, enum.Enum):
    AUTO = "auto"  # Pick whether or not to use a tool
    NONE = "none"  # No tools
    REQUIRED = "required"  # One or more
    SPECIFIC = "specific"  # For one specific tool


class OpenAIConfig(BaseModel):
    # OpenAI-specific features
    max_completion_tokens: int | None = None
    store: bool | None = None
    metadata: dict[str, str] | None = None
    prompt_cache_key: str | None = None
    parallel_tool_calls: bool | None = None
    top_p: float | None = None

    tool_choice: OpenAIToolChoice | None = None
    tool_choice_specific_name: str | None = (
        None  # If tool_choice is SPECIFIC, you must provide the name of the tool
    )

    # Reasoning configuration
    reasoning_effort: OpenAIReasoningLevel | None = None


class GeminiToolChoice(str, enum.Enum):
    AUTO = "auto"  # Pick whether or not to use a tool
    NONE = "none"  # No tools
    ANY = "any"  # One or more


class GeminiConfig(BaseModel):
    top_p: float | None = None
    top_k: int | None = None
    stop_sequences: list[str] | None = None

    # Gemini-specific features
    response_mime_type: str | None = None
    response_schema: dict[str, Any] | None = None
    seed: int | None = None

    # Function calling config
    tool_choice: GeminiToolChoice | None = None
    tool_choice_allowed_tools: list[str] | None = None  # Restrict the set of allowed tools

    # Thinking configuration
    thinking_include_thoughts: bool | None = None
    thinking_budget: int | None = None


class LiteLLMConfig(BaseModel):
    # Placeholder for now
    pass


class ProviderConfigs(BaseModel):
    # This allows the user to specify settings. If a provider config field is set, that will
    # override any defaults determined by the provider OR by kintu.
    anthropic: AnthropicConfig | None = None
    openai: OpenAIConfig | None = None
    gemini: GeminiConfig | None = None
    litellm: LiteLLMConfig | None = None
