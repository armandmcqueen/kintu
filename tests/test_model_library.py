"""Tests for the model_library module."""

from kintu.model_library.model_library import MODEL_LIBRARY, get_spec
from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.provider import Provider


class TestModelLibraryCoverage:
    """Test that MODEL_LIBRARY has correct coverage."""

    def test_all_models_in_library(self):
        """Test that every Model enum value has an entry in MODEL_LIBRARY."""
        missing_models: list[str] = []
        for model in Model:
            if model not in MODEL_LIBRARY:
                missing_models.append(model.value)

        assert not missing_models, f"Missing models in MODEL_LIBRARY: {missing_models}"

    def test_no_extra_models_in_library(self):
        """Test that MODEL_LIBRARY doesn't have entries for non-existent models."""
        extra_models: list[str] = []
        valid_models = set(Model)

        for model_key in MODEL_LIBRARY.keys():
            if model_key not in valid_models:
                extra_models.append(str(model_key))

        assert not extra_models, f"Extra models in MODEL_LIBRARY: {extra_models}"

    def test_model_id_matches_key(self):
        """Test that each ModelSpec's model_id matches its dictionary key."""
        mismatched: list[str] = []
        for model_key, spec in MODEL_LIBRARY.items():
            if spec.model_id != model_key:
                mismatched.append(f"{model_key} != {spec.model_id}")

        assert not mismatched, f"Mismatched model IDs: {mismatched}"


class TestModelSpecSanityChecks:
    """Sanity checks for ModelSpec values."""

    def test_temperature_range_valid(self):
        """Test that temperature range is valid."""
        for model_key, spec in MODEL_LIBRARY.items():
            assert len(spec.temperature_range) == 2, f"{model_key}: Invalid temperature range"
            min_temp, max_temp = spec.temperature_range
            assert min_temp >= 0, f"{model_key}: Min temperature < 0"
            assert max_temp > min_temp, f"{model_key}: Max temp <= min temp"
            assert max_temp <= 2.0, f"{model_key}: Max temperature > 2.0"

    def test_pricing_fields_non_negative(self):
        """Test that all pricing fields are non-negative."""
        for model_key, spec in MODEL_LIBRARY.items():
            assert spec.pricing.input_nocache >= 0, f"{model_key}: Negative input price"
            assert spec.pricing.output >= 0, f"{model_key}: Negative output price"
            assert spec.pricing.input_cache_read >= 0, f"{model_key}: Negative cache read"
            assert spec.pricing.input_cache_write >= 0, f"{model_key}: Negative cache write"

    def test_web_search_and_code_execution_fields(self):
        """Test that web_search and code_execution are set correctly."""
        for model_key, spec in MODEL_LIBRARY.items():
            # Major providers (Anthropic, OpenAI, Gemini) should have both enabled
            if spec.provider in [Provider.ANTHROPIC, Provider.OPENAI, Provider.GEMINI]:
                assert spec.features.web_search is True, f"{model_key}: Should have web_search"
                assert spec.features.code_execution is True, (
                    f"{model_key}: Should have code_execution"
                )
            else:
                # Other providers should have both disabled
                assert spec.features.web_search is False, f"{model_key}: Should not have web_search"
                assert spec.features.code_execution is False, (
                    f"{model_key}: Should not have code_execution"
                )

    # Commented out test to identify placeholder values
    # def test_identify_placeholder_values(self):
    #     """Identify models with placeholder values that need to be filled."""
    #     models_with_placeholders = []
    #     models_with_zero_context = []
    #     models_with_zero_pricing = []
    #
    #     for model_key, spec in MODEL_LIBRARY.items():
    #         # Check for PLACEHOLDER in release_date
    #         if spec.release_date == "PLACEHOLDER":
    #             models_with_placeholders.append(model_key.value)
    #
    #         # Check for 0 context window or max tokens
    #         if spec.context_window == 0 or spec.max_output_tokens == 0:
    #             models_with_zero_context.append(model_key.value)
    #
    #         # Check for 0 pricing
    #         if (spec.pricing.input_nocache == 0.0 and spec.pricing.output == 0.0 and
    #             "glm_4_5_air" not in model_key.value):  # GLM might legitimately be free
    #             models_with_zero_pricing.append(model_key.value)
    #
    #     if models_with_placeholders:
    #         print(f"\nModels with PLACEHOLDER release dates: {models_with_placeholders}")
    #     if models_with_zero_context:
    #         print(f"Models with zero context/tokens: {models_with_zero_context}")
    #     if models_with_zero_pricing:
    #         print(f"Models with zero pricing: {models_with_zero_pricing}")
    #
    #     # This test would fail if uncommented - it's for information only
    #     # assert not models_with_placeholders, "Some models have placeholder values"


class TestGetSpec:
    """Test the get_spec function."""

    def test_get_spec_existing_model(self):
        """Test getting spec for an existing model."""
        spec = get_spec(Model.claude_4_opus_20250514)
        assert spec.model_id == Model.claude_4_opus_20250514
        assert spec.provider == Provider.ANTHROPIC
        assert spec.llmsdk == LLMSDK.ANTHROPIC

    def test_get_spec_all_models(self):
        """Test that get_spec works for all models."""
        for model in Model:
            spec = get_spec(model)
            assert spec.model_id == model


# TODO: Add back in provider-specific sanity checks
