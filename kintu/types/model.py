import enum


class Model(str, enum.Enum):
    """Enum for all available models."""

    # Anthropic models
    claude_4_1_opus_20250805 = "claude-opus-4-1-20250805"
    claude_4_opus_20250514 = "claude-opus-4-20250514"
    claude_4_sonnet_20250514 = "claude-sonnet-4-20250514"
    claude_3_7_sonnet_20250219 = "claude-3-7-sonnet-20250219"
    claude_3_5_haiku_20241022 = "claude-3-5-haiku-20241022"

    # Gemini models
    gemini_2_5_pro = "gemini-2.5-pro"
    gemini_2_5_flash = "gemini-2.5-flash"
    gemini_2_5_flash_lite = "gemini-2.5-flash-lite"
    gemma_3n_e2b_it = "gemma-3n-e2b-it"
    gemma_3n_e4b_it = "gemma-3n-e4b-it"

    # OpenAI models
    gpt_5 = "gpt-5"
    gpt_5_mini = "gpt-5-mini"
    gpt_5_nano = "gpt-5-nano"
    gpt_4_1 = "gpt-4.1"
    gpt_4_1_mini = "gpt-4.1-mini"
    gpt_4_1_nano = "gpt-4.1-nano"
    o4_mini = "o4-mini"
    o3_pro = "o3-pro"
    o3 = "o3"

    # LiteLLM models
    # Via TogetherAI
    llama_4_scout_17b_together = "together_ai/meta-llama/Llama-4-Scout-17B-16E-Instruct"
    llama_4_maverick_17b_together = "together_ai/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"
    llama_3_2_11b_vision_together = "together_ai/meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo"
    qwen3_235b_thinking_together = "together_ai/Qwen/Qwen3-235B-A22B-Thinking-2507"
    qwen3_235b_instruct_together = "together_ai/Qwen/Qwen3-235B-A22B-Instruct-2507-tput"
    qwq_32b_together = "together_ai/Qwen/QwQ-32B"
    glm_4_5_air_together = "together_ai/zai-org/GLM-4.5-Air-FP8"
    openai_gpt_oss_20b_together = "together_ai/openai/gpt-oss-20b"
    openai_gpt_oss_120b_together = "together_ai/openai/gpt-oss-120b"
    kimi_k2_instruct_together = "together_ai/moonshotai/Kimi-K2-Instruct"
    gemma_3n_e4b_it_together = "together_ai/google/gemma-3n-E4B-it"
    deepseek_r1_0528_tput_together = "together_ai/deepseek-ai/DeepSeek-R1-0528-tput"


    # Via Groq
    llama_3_1_8b_groq = "groq/llama-3.1-8b-instant"
    llama_3_3_70b_groq = "groq/llama-3.3-70b-versatile"
    llama_guard_4_12b_groq = "groq/meta-llama/llama-guard-4-12b"
    deepseek_r1_distill_llama_3_3_70b_groq = "groq/deepseek-r1-distill-llama-70b"
    llama4_maverick_groq = "groq/meta-llama/llama-4-maverick-17b-128e-instruct"
    llama4_scout_groq = "groq/meta-llama/llama-4-scout-17b-16e-instruct"
    llama_prompt_guard_2_22m_groq = "groq/meta-llama/llama-prompt-guard-2-22m"
    llama_prompt_guard_2_86m_groq = "groq/meta-llama/llama-prompt-guard-2-86m"
    kimi_k2_instruct = "groq/moonshotai/kimi-k2-instruct"
    openai_gpt_oss_120b_groq = "groq/openai/gpt-oss-120b"
    openai_gpt_oss_20b_groq = "groq/openai/gpt-oss-20b"
    qwen3_32b_groq = "groq/qwen/qwen3-32b"

