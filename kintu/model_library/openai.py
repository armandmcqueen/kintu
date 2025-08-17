from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

OPENAI_MODEL_LIBRARY: dict[str, ModelSpec] = {
    Model.gpt_5: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-5
        model_id=Model.gpt_5,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-5-2025-08-07",
        provider_model_id="gpt-5-2025-08-07",
        model_label="GPT 5 (2025-08-07)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=1.25, output=10.0, input_cache_read=0.125, input_cache_write=0.0
        ),
        context_window=400_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-07",
    ),
    Model.gpt_5_mini: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-5-mini
        model_id=Model.gpt_5_mini,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-5-mini-2025-08-07",
        provider_model_id="gpt-5-mini-2025-08-07",
        model_label="GPT 5 Mini (2025-08-07)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.25, output=2.0, input_cache_read=0.025, input_cache_write=0.0
        ),
        context_window=400_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-07",
    ),
    Model.gpt_5_nano: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-5-nano
        model_id=Model.gpt_5_nano,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-5-nano-2025-08-07",
        provider_model_id="gpt-5-nano-2025-08-07",
        model_label="GPT 5 Nano (2025-08-07)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=False,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.05, output=0.4, input_cache_read=0.005, input_cache_write=0.0
        ),
        context_window=400_000,
        max_output_tokens=128_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-08-07",
    ),
    Model.gpt_4_1: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-4.1
        model_id=Model.gpt_4_1,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1-2025-04-14",
        provider_model_id="gpt-4.1-2025-04-14",
        model_label="GPT 4.1 (2025-04-14)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=2.0, output=8.0, input_cache_read=0.5, input_cache_write=0.0
        ),
        context_window=1_047_576,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.gpt_4_1_mini: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-4.1-mini
        model_id=Model.gpt_4_1_mini,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1-mini-2025-04-14",
        provider_model_id="gpt-4.1-mini-2025-04-14",
        model_label="GPT 4.1 Mini (2025-04-14)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.4, output=1.6, input_cache_read=0.1, input_cache_write=0.0
        ),
        context_window=1_047_576,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.gpt_4_1_nano: ModelSpec(
        # https://platform.openai.com/docs/models/gpt-4.1-nano
        model_id=Model.gpt_4_1_nano,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="gpt-4.1-nano-2025-04-14",
        provider_model_id="gpt-4.1-nano-2025-04-14",
        model_label="GPT 4.1 Nano (2025-04-14)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.1, output=0.4, input_cache_read=0.025, input_cache_write=0.0
        ),
        context_window=1_047_576,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-14",
    ),
    Model.o4_mini: ModelSpec(
        # https://platform.openai.com/docs/models/o4-mini
        model_id=Model.o4_mini,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="o4-mini",
        provider_model_id="o4-mini",
        model_label="OpenAI o4-mini (2025-04-16)",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # o-series models have reasoning
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=1.1, output=4.4, input_cache_read=0.275, input_cache_write=0.0
        ),
        context_window=200_000,
        max_output_tokens=100_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-16",
    ),
    Model.o3_pro: ModelSpec(
        # https://platform.openai.com/docs/models/o3-pro
        # No streaming!
        model_id=Model.o3_pro,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="o3-pro",
        provider_model_id="o3-pro",
        model_label="OpenAI o3-pro (2025-06-10)",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # o-series models have reasoning
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=20.0, output=80.0, input_cache_read=0.0, input_cache_write=0.0
        ),
        context_window=200_000,
        max_output_tokens=100_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-06-10",
    ),
    Model.o3: ModelSpec(
        # https://platform.openai.com/docs/models/o3
        model_id=Model.o3,
        llmsdk=LLMSDK.OPENAI,
        provider=Provider.OPENAI,
        llmsdk_model_id="o3",
        provider_model_id="o3",
        model_label="OpenAI o3 (2025-04-16)",
        features=ModelFeatures(
            vision=True,
            thinking=True,  # o-series models have reasoning
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=2.0, output=8.0, input_cache_read=0.5, input_cache_write=0.0
        ),
        context_window=200_000,
        max_output_tokens=100_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-16",
    ),
}
