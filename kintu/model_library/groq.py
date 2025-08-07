from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

# Model specifications database
GROQ_MODEL_LIBRARY: dict[str, ModelSpec] = {
    Model.kimi_k2_instruct: ModelSpec(
        model_id=Model.kimi_k2_instruct,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/moonshotai/kimi-k2-instruct",
        provider_model_id="moonshotai/kimi-k2-instruct",
        model_label="Kimi K2 Instruct (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(
            input_nocache=0.15, output=0.15, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_768,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    # Missing models with placeholder values
    Model.qwen3_32b: ModelSpec(
        model_id=Model.qwen3_32b,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/qwen/qwen3-32b",
        provider_model_id="qwen/qwen3-32b",
        model_label="Qwen3 32B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
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
    Model.llama4_maverick_groq: ModelSpec(
        model_id=Model.llama4_maverick_groq,
        llmsdk=LLMSDK.LITELLM,
        provider=Provider.GROQ,
        llmsdk_model_id="groq/meta-llama/llama-4-maverick-17b-128e-instruct",
        provider_model_id="meta-llama/llama-4-maverick-17b-128e-instruct",
        model_label="Llama 4 Maverick 17B (Groq via LiteLLM)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
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
