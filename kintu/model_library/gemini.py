from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

# Model specifications database
GEMINI_MODEL_LIBRARY: dict[str, ModelSpec] = {
    # Gemini Models
    Model.gemini_2_5_pro: ModelSpec(
        model_id=Model.gemini_2_5_pro,
        llmsdk=LLMSDK.GEMINI,
        provider=Provider.GEMINI,
        llmsdk_model_id="gemini-2.5-pro",
        provider_model_id="gemini-2.5-pro",
        model_label="Gemini 2.5 Pro",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # Gemini 2.0+ supports thinking
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=1.25, output=10.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=2_000_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-17",
    ),
    Model.gemini_2_5_flash: ModelSpec(
        model_id=Model.gemini_2_5_flash,
        llmsdk=LLMSDK.GEMINI,
        provider=Provider.GEMINI,
        llmsdk_model_id="gemini-2.5-flash",
        provider_model_id="gemini-2.5-flash",
        model_label="Gemini 2.5 Flash",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # Gemini 2.0+ supports thinking
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.3, output=2.5, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=1_000_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.gemini_2_5_flash_lite: ModelSpec(
        model_id=Model.gemini_2_5_flash_lite,
        llmsdk=LLMSDK.GEMINI,
        provider=Provider.GEMINI,
        llmsdk_model_id="gemini-2.5-flash-lite",
        provider_model_id="gemini-2.5-flash-lite",
        model_label="Gemini 2.5 Flash Lite Preview",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # Gemini 2.0+ supports thinking
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.1, output=0.4, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=1_000_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="PLACEHOLDER",
    ),
    Model.gemma_3n_e2b_it: ModelSpec(  # DONE, NOT TESTED
        model_id=Model.gemma_3n_e2b_it,
        llmsdk=LLMSDK.GEMINI,
        provider=Provider.GEMINI,
        llmsdk_model_id="gemma-3n-e2b-it",
        provider_model_id="gemma-3n-e2b-it",
        model_label="Gemma 3n 2B",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(  # These are seemingly free?
            input_nocache=0.0, output=0.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_000,
        max_output_tokens=32_000,
        temperature_range=(0.0, 1.0),  # Gemma is 0.0 to 1.0 based on AI Studio UI
        release_date="2025-06-25",
    ),
    Model.gemma_3n_e4b_it: ModelSpec(  # DONE, NOT TESTED
        model_id=Model.gemma_3n_e4b_it,
        llmsdk=LLMSDK.GEMINI,
        provider=Provider.GEMINI,
        llmsdk_model_id="gemma-3n-e4b-it",
        provider_model_id="gemma-3n-e4b-it",
        model_label="Gemma 3n 4B",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=False,
            web_search=False,
            code_execution=False,
        ),
        pricing=ModelPricing(  # These are seemingly free?
            input_nocache=0.0, output=0.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=32_000,
        max_output_tokens=32_000,
        temperature_range=(0.0, 1.0),  # Gemma is 0.0 to 1.0 based on AI Studio UI
        release_date="2025-06-25",
    ),
}
