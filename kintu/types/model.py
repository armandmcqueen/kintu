import enum


class Model(str, enum.Enum):
    """Enum for all available models."""

    # Anthropic models
    claude_4_opus_20250514 = "claude-opus-4-20250514"
    claude_4_sonnet_20250514 = "claude-sonnet-4-20250514"
    claude_3_7_sonnet_20250219 = "claude-3-7-sonnet-20250219"
    claude_3_5_sonnet_20241022 = "claude-3-5-sonnet-20241022"
    claude_3_5_haiku_20241022 = "claude-3-5-haiku-20241022"

    # Gemini models
    gemini_2_5_pro = "gemini-2.5-pro"
    gemini_2_5_flash = "gemini-2.5-flash"
    gemini_2_5_flash_lite = "gemini-2.5-flash-lite"

    # OpenAI models
    gpt_4_1 = "gpt-4.1"
    gpt_4_1_mini = "gpt-4.1-mini"
    gpt_4_1_nano = "gpt-4.1-nano"
    o4_mini = "o4-mini"
    o3 = "o3"

    # LiteLLM models
    # Via TogetherAI
    llama_4_scout_17b = "together_ai/meta-llama/Llama-4-Scout-17B-16E-Instruct"
    llama_3_2_11b_vision = "together_ai/meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"
    qwen3_235b_thinking = "together_ai/Qwen/Qwen3-235B-A22B-Thinking-2507"
    qwq_32b = "together_ai/Qwen/QwQ-32B"
    glm_4_5_air = "together_ai/zai-org/GLM-4.5-Air-FP8"
    # Via Groq
    kimi_k2_instruct = "groq/moonshotai/kimi-k2-instruct"
    qwen3_32b = "groq/qwen/qwen3-32b"
    llama4_maverick_groq = "groq/meta-llama/llama-4-maverick-17b-128e-instruct"
