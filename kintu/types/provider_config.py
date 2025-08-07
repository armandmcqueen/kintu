from pydantic import BaseModel, Literal

# Provider configurations
class AnthropicConfig(BaseModel):
    # Anthropic-specific features
    disable_parallel_tool_use: bool = False
    container_id: str | None = None
    tool_choice: dict | None = None  # {"type": "auto|any|tool", "name": "tool_name"}
    stop_sequences: list[str] | None = None
    top_p: float | None = None
    top_k: int | None = None

    # Thinking configuration
    thinking: dict | None = None  # {"type": "enabled|disabled", "budget_tokens": int}

    # Beta features
    beta_headers: list[str] | None = None  # e.g., ["computer-use-2024-10-22"]

class OpenAIConfig(BaseModel):
    # OpenAI-specific features
    max_completion_tokens: int | None = None
    store: bool = False
    metadata: dict[str, str] | None = None
    prompt_cache_key: str | None = None
    parallel_tool_calls: bool = True
    tool_choice: str | dict | None = None  # "auto", "none", "required", or {"type": "function", "function": {"name": "..."}}
    top_p: float | None = None

    # Reasoning configuration
    reasoning_effort: Literal["low", "medium", "high"] | None = None

class GeminiConfig(BaseModel):
    top_p: float | None = None
    top_k: int | None = None
    stop_sequences: list[str] | None = None

    # Gemini-specific features
    response_mime_type: str | None = None
    response_schema: dict | None = None
    seed: int | None = None

    # Function calling config
    function_calling_config: RawGeminiFunctionCallingConfig | None = None  # {"mode": "AUTO|ANY|NONE", "allowed_function_names": [...]}

    # Thinking configuration
    thinking_config: RawGeminiThinkingConfig | None = None  # {"include_thoughts": bool, "thinking_budget": int}

class LiteLLMConfig(BaseModel):
    # LiteLLM-specific features
    top_p: float | None = None
    top_k: int | None = None
    stop: list[str] | None = None
    repetition_penalty: float | None = None
    presence_penalty: float | None = None
    frequency_penalty: float | None = None

    # Provider-specific overrides (e.g., for TogetherAI)
    custom_llm_provider: str | None = None  # e.g., "together_ai"
    api_base: str | None = None

class ProviderConfigs(BaseModel):
    anthropic: AnthropicConfig | None = None
    openai: OpenAIConfig | None = None
    gemini: GeminiConfig | None = None
    litellm: LiteLLMConfig | None = None