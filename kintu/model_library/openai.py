from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

# Model specifications database
OPENAI_MODEL_LIBRARY: dict[str, ModelSpec] = {
    # OpenAI Models
    Model.gpt_4_1: ModelSpec(
        model_id=Model.gpt_4_1,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1",
        provider_model_id="gpt-4.1",
        model_label="GPT 4.1 (2025-04-14)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=2.0, output=8.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=16_384,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.gpt_4_1_mini: ModelSpec(
        model_id=Model.gpt_4_1_mini,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1-mini",
        provider_model_id="gpt-4.1-mini",
        model_label="GPT 4.1 Mini (2025-04-14)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.4, output=1.6, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=16_384,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.gpt_4_1_nano: ModelSpec(
        model_id=Model.gpt_4_1_nano,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1-nano",
        provider_model_id="gpt-4.1-nano",
        model_label="GPT 4.1 Nano (2025-04-14)",
        features=ModelFeatures(
            vision=False,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.1, output=0.4, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=1_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.o4_mini: ModelSpec(
        model_id=Model.o4_mini,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="o4-mini",
        provider_model_id="o4-mini",
        model_label="OpenAI o4-mini (2025-04-16)",
        features=ModelFeatures(
            vision=False,
            thinking=True,  # o-series models have reasoning
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=1.1, output=4.4, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=64_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-16",
    ),
    Model.o3: ModelSpec(
        model_id=Model.o3,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="o3",
        provider_model_id="o3",
        model_label="OpenAI o3 (2025-04-16)",
        features=ModelFeatures(
            vision=False,
            thinking=True,  # o-series models have reasoning
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=2.0, output=8.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=128_000,
        max_output_tokens=64_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-16",
    ),
}
