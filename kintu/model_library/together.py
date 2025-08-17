from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

TOGETHER_MODEL_LIBRARY: dict[str, ModelSpec] = {
    Model.llama_4_scout_17b_together: ModelSpec(
        model_id=Model.llama_4_scout_17b_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/meta-llama/Llama-4-Scout-17B-16E-Instruct",
        provider_model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
        model_label="Llama 4 Scout 17B (Together AI)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.18, output=0.59, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=1_048_576,
        max_output_tokens=1_048_576,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.llama_4_maverick_17b_together: ModelSpec(
        model_id=Model.llama_4_maverick_17b_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        provider_model_id="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        model_label="Llama 4 Maverick 17B (Together AI)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.27, output=0.85, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=1_048_576,
        max_output_tokens=1_048_576,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-05",
    ),
    Model.llama_3_2_11b_vision_together: ModelSpec(
        model_id=Model.llama_3_2_11b_vision_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        provider_model_id="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        model_label="Llama 3.2 11B Vision (Together AI)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.18, output=0.18, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2024-04-18",
    ),
    Model.qwen3_235b_thinking_together: ModelSpec(
        model_id=Model.qwen3_235b_thinking_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/Qwen/Qwen3-235B-A22B-Thinking-2507",
        provider_model_id="Qwen/Qwen3-235B-A22B-Thinking-2507",
        model_label="Qwen3 235B Thinking (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.65, output=3.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=262_000,
        max_output_tokens=262_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-07",
    ),
    Model.qwen3_235b_instruct_together: ModelSpec(
        model_id=Model.qwen3_235b_instruct_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
        provider_model_id="Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
        model_label="Qwen3 235B Instruct (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.2, output=0.6, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=262_000,
        max_output_tokens=262_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-07",
    ),
    Model.qwq_32b_together: ModelSpec(
        model_id=Model.qwq_32b_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/Qwen/QwQ-32B",
        provider_model_id="Qwen/QwQ-32B",
        model_label="QwQ 32B (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,  # QwQ is a reasoning model
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=1.20, output=1.20, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=131_072,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="2025-03-06",
    ),
    Model.glm_4_5_air_together: ModelSpec(
        model_id=Model.glm_4_5_air_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/zai-org/GLM-4.5-Air-FP8",
        provider_model_id="zai-org/GLM-4.5-Air-FP8",
        model_label="GLM 4.5 Air (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.2, output=1.1, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-11",
    ),
    Model.openai_gpt_oss_20b_together: ModelSpec(
        model_id=Model.openai_gpt_oss_20b_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/openai/gpt-oss-20b",
        provider_model_id="openai/gpt-oss-20b",
        model_label="OpenAI GPT OSS 20B (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.05, output=0.20, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-05",
    ),
    Model.openai_gpt_oss_120b_together: ModelSpec(
        model_id=Model.openai_gpt_oss_120b_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/openai/gpt-oss-120b",
        provider_model_id="openai/gpt-oss-120b",
        model_label="OpenAI GPT OSS 120B (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.15, output=0.60, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-05",
    ),
    #     kimi_k2_instruct_together = "together_ai/moonshotai/Kimi-K2-Instruct"
    #     gemma_3n_e4b_it_together = "together_ai/google/gemma-3n-E4B-it"
    #     deepseek_r1_0528_tput_together = "together_ai/deepseek-ai/DeepSeek-R1-0528-tput"
    Model.kimi_k2_instruct_together: ModelSpec(
        model_id=Model.kimi_k2_instruct_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/moonshotai/Kimi-K2-Instruct",
        provider_model_id="moonshotai/Kimi-K2-Instruct",
        model_label="Kimi K2 Instruct (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=1.0, output=3.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-07-12",
    ),
    Model.gemma_3n_e4b_it_together: ModelSpec(
        model_id=Model.gemma_3n_e4b_it_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/google/gemma-3n-E4B-it",
        provider_model_id="google/gemma-3n-E4B-it",
        model_label="Gemma 3n 4B (Together AI)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.02, output=0.04, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_000,
        max_output_tokens=32_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-06-25",
    ),
    Model.deepseek_r1_0528_tput_together: ModelSpec(
        model_id=Model.deepseek_r1_0528_tput_together,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/deepseek-ai/DeepSeek-R1-0528-tput",
        provider_model_id="deepseek-ai/DeepSeek-R1-0528-tput",
        model_label="DeepSeek R1 0528 Throughput (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.55, output=2.19, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-05-28",
    ),
}
