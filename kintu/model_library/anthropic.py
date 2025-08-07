from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.model_spec import ModelFeatures, ModelPricing, ModelSpec
from kintu.types.provider import Provider

# Model specifications database
ANTHROPIC_MODEL_LIBRARY: dict[str, ModelSpec] = {
    # Anthropic Models
    Model.claude_4_opus_20250514: ModelSpec(
        model_id=Model.claude_4_opus_20250514,
        llmsdk=LLMSDK.ANTHROPIC,
        provider=Provider.ANTHROPIC,
        llmsdk_model_id="claude-opus-4-20250514",
        provider_model_id="claude-opus-4-20250514",
        model_label="Claude 4.0 Opus (2025-05-14)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=15.0, output=75.0, input_cache_read=1.5, input_cache_write=18.75
        ),
        context_window=200_000,
        max_output_tokens=4_096,
        temperature_range=(0.0, 1.0),
        release_date="2025-05-14",
    ),
    Model.claude_4_sonnet_20250514: ModelSpec(
        model_id=Model.claude_4_sonnet_20250514,
        llmsdk=LLMSDK.ANTHROPIC,
        provider=Provider.ANTHROPIC,
        llmsdk_model_id="claude-sonnet-4-20250514",
        provider_model_id="claude-sonnet-4-20250514",
        model_label="Claude 4.0 Sonnet (2025-05-14)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=3.0, output=15.0, input_cache_read=0.3, input_cache_write=3.75
        ),
        context_window=200_000,
        max_output_tokens=4_096,
        temperature_range=(0.0, 1.0),
        release_date="2025-05-14",
    ),
    Model.claude_3_7_sonnet_20250219: ModelSpec(
        model_id=Model.claude_3_7_sonnet_20250219,
        llmsdk=LLMSDK.ANTHROPIC,
        provider=Provider.ANTHROPIC,
        llmsdk_model_id="claude-3-7-sonnet-20250219",
        provider_model_id="claude-3-7-sonnet-20250219",
        model_label="Claude 3.7 Sonnet (2025-02-19)",
        features=ModelFeatures(
            vision=True,
            thinking=True,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=3.0, output=15.0, input_cache_read=0.3, input_cache_write=3.75
        ),
        context_window=200_000,
        max_output_tokens=4_096,
        temperature_range=(0.0, 1.0),
        release_date="2025-02-19",
    ),
    Model.claude_3_5_sonnet_20241022: ModelSpec(
        model_id=Model.claude_3_5_sonnet_20241022,
        llmsdk=LLMSDK.ANTHROPIC,
        provider=Provider.ANTHROPIC,
        llmsdk_model_id="claude-3-5-sonnet-20241022",
        provider_model_id="claude-3-5-sonnet-20241022",
        model_label="Claude 3.5 Sonnet (2024-10-22)",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=3.0, output=15.0, input_cache_read=0.3, input_cache_write=3.75
        ),
        context_window=200_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 1.0),
        release_date="2024-10-22",
    ),
    Model.claude_3_5_haiku_20241022: ModelSpec(
        model_id=Model.claude_3_5_haiku_20241022,
        llmsdk=LLMSDK.ANTHROPIC,
        provider=Provider.ANTHROPIC,
        llmsdk_model_id="claude-3-5-haiku-20241022",
        provider_model_id="claude-3-5-haiku-20241022",
        model_label="Claude 3.5 Haiku",
        features=ModelFeatures(
            vision=True,
            thinking=False,
            tools=True,
            web_search=True,
            code_execution=True,
        ),
        pricing=ModelPricing(
            input_nocache=0.8, output=4.0, input_cache_read=0.08, input_cache_write=1.0
        ),
        context_window=200_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 1.0),
        release_date="2024-10-22",
    ),
}
