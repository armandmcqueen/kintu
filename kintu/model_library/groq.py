from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

GROQ_MODEL_LIBRARY: dict[str, ModelSpec] = {
    Model.llama_3_1_8b_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-3.1-8b-instant
        # 560 TPS
        model_id=Model.llama_3_1_8b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/llama-3.1-8b-instant",
        provider_model_id="llama-3.1-8b-instant",
        model_label="Llama 3.1 8B Instant (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.05, output=0.08, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=131_072,
        temperature_range=(0.0, 2.0),
        release_date="2024-07-23",
    ),
    Model.llama_3_3_70b_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-3.3-70b-versatile
        # 280 TPS
        model_id=Model.llama_3_3_70b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/llama-3.3-70b-versatile",
        provider_model_id="llama-3.3-70b-versatile",
        model_label="Llama 3.3 70B Versatile (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.59, output=0.79, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="2024-12-06",
    ),
    Model.llama_guard_4_12b_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-guard-4-12b
        # 1200 TPS
        model_id=Model.llama_guard_4_12b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-guard-4-12b",
        provider_model_id="meta-llama/llama-guard-4-12b",
        model_label="Llama Guard 4 12B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.20, output=0.20, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=1024,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.deepseek_r1_distill_llama_3_3_70b_groq: ModelSpec(
        # https://console.groq.com/docs/model/deepseek-r1-distill-llama-70b
        # 260 TPS
        # NOTE: Avoid adding a system prompt and include all instructions within the user prompt.
        model_id=Model.deepseek_r1_distill_llama_3_3_70b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/deepseek-r1-distill-llama-70b",
        provider_model_id="deepseek-r1-distill-llama-70b",
        model_label="DeepSeek R1 Distill Llama 70B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.75, output=0.99, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=131_072,
        temperature_range=(0.0, 2.0),  # Recommended 0.5-0.7, use 0.6
        release_date="2025-01-20",
    ),
    Model.llama4_maverick_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-4-maverick-17b-128e-instruct
        # 600 TPS
        # 5 input images
        model_id=Model.llama4_maverick_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-4-maverick-17b-128e-instruct",
        provider_model_id="meta-llama/llama-4-maverick-17b-128e-instruct",
        model_label="Llama 4 Maverick 17B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.20, output=0.60, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.llama4_scout_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-4-scout-17b-16e-instruct
        # 750 TPS
        # 5 input images
        model_id=Model.llama4_scout_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-4-scout-17b-16e-instruct",
        provider_model_id="meta-llama/llama-4-scout-17b-16e-instruct",
        model_label="Llama 4 Scout 17B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.11, output=0.34, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.llama_prompt_guard_2_22m_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-prompt-guard-2-22m
        model_id=Model.llama_prompt_guard_2_22m_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-prompt-guard-2-22m",
        provider_model_id="meta-llama/llama-prompt-guard-2-22m",
        model_label="Llama Prompt Guard 2 22M (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.03, output=0.03, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=512,
        max_output_tokens=512,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.llama_prompt_guard_2_86m_groq: ModelSpec(
        # https://console.groq.com/docs/model/llama-prompt-guard-2-86m
        model_id=Model.llama_prompt_guard_2_86m_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-prompt-guard-2-86m",
        provider_model_id="meta-llama/llama-prompt-guard-2-86m",
        model_label="Llama Prompt Guard 2 86M (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.04, output=0.04, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=512,
        max_output_tokens=512,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.kimi_k2_instruct: ModelSpec(
        # https://console.groq.com/docs/model/moonshotai/kimi-k2-instruct
        # 200 TPS
        model_id=Model.kimi_k2_instruct,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/moonshotai/kimi-k2-instruct",
        provider_model_id="moonshotai/kimi-k2-instruct",
        model_label="Kimi K2 Instruct (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=1.00, output=3.00, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=16_384,
        temperature_range=(0.0, 2.0),
        release_date="2025-07-12",
    ),
    Model.openai_gpt_oss_120b_groq: ModelSpec(
        # https://console.groq.com/docs/model/openai/gpt-oss-120b
        # 500 TPS
        model_id=Model.openai_gpt_oss_120b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/openai/gpt-oss-120b",
        provider_model_id="openai/gpt-oss-120b",
        model_label="OpenAI GPT OSS 120B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.15, output=0.75, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=65_536,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-05",
    ),
    Model.openai_gpt_oss_20b_groq: ModelSpec(
        # https://console.groq.com/docs/model/openai/gpt-oss-20b
        # 1000 TPS
        model_id=Model.openai_gpt_oss_20b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/openai/gpt-oss-20b",
        provider_model_id="openai/gpt-oss-20b",
        model_label="OpenAI GPT OSS 20B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.10, output=0.50, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=65_536,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-05",
    ),
    Model.qwen3_32b_groq: ModelSpec(
        # https://console.groq.com/docs/model/qwen/qwen3-32b
        # 400 TPS
        model_id=Model.qwen3_32b_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/qwen/qwen3-32b",
        provider_model_id="qwen/qwen3-32b",
        model_label="Qwen3 32B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.29, output=0.59, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=40_960,
        temperature_range=(0.0, 2.0),
        release_date="2025-05-14",
    ),
}
