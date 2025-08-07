from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

# Model specifications database
TOGETHER_MODEL_LIBRARY: dict[str, ModelSpec] = {
    # LiteLLM Models (via various providers)
    Model.llama_4_scout_17b: ModelSpec(
        model_id=Model.llama_4_scout_17b,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/meta-llama/Llama-4-Scout-17B-16E-Instruct",
        provider_model_id="meta-llama/Llama-4-Scout-17B-16E-Instruct",
        model_label="Llama 4 Scout 17B (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.18, output=0.18, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=16_384,
        max_output_tokens=4_096,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.llama_3_2_11b_vision: ModelSpec(
        model_id=Model.llama_3_2_11b_vision,
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
        max_output_tokens=4_096,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.qwen3_235b_thinking: ModelSpec(
        model_id=Model.qwen3_235b_thinking,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/Qwen/Qwen3-235B-A22B-Thinking-2507",
        provider_model_id="Qwen/Qwen3-235B-A22B-Thinking-2507",
        model_label="Qwen3 235B Thinking (Together AI)",
        features=ModelFeatures(
            vision=False,
            thinking=True,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=12.0, output=12.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_768,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.qwq_32b: ModelSpec(
        model_id=Model.qwq_32b,
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
            input_nocache=0.3, output=0.3, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_768,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.glm_4_5_air: ModelSpec(
        model_id=Model.glm_4_5_air,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.TOGETHER,
        llmsdk_model_id="together_ai/zai-org/GLM-4.5-Air-FP8",
        provider_model_id="zai-org/GLM-4.5-Air-FP8",
        model_label="GLM 4.5 Air (Together AI)",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # QwQ is a reasoning model
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.0, output=0.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=0,
        max_output_tokens=0,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
}
