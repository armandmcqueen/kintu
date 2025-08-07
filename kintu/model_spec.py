from typing import Optional

from pydantic import BaseModel, Field

from kintu.llmsdk import LLMSDK
from kintu.model import Model
from kintu.provider import Provider


class ModelFeatures(BaseModel):
    vision: bool
    thinking: bool
    tools: bool


class ModelPricing(BaseModel):
    input: float = Field(description="Cost per million input tokens")
    output: float = Field(description="Cost per million output tokens")

    cache_read: Optional[float] = Field(
        default=None, description="Cost per million cached input tokens"
    )
    cache_write: Optional[float] = Field(
        default=None, description="Cost to write million tokens to cache"
    )


class ModelSpec(BaseModel):
    model_id: Model  # Unique identifier for the model, unique within kintu
    provider: Provider
    llmsdk: LLMSDK

    llmsdk_model_id: str = Field(description="The ID used by the LLM SDK")
    provider_model_id: str = Field(description="The ID used by the provider's API")
    model_label: str = Field(description="Human-readable name")

    features: ModelFeatures
    pricing: ModelPricing

    context_window: int
    max_output_tokens: int
    temperature_range: tuple[float, float] = (0.0, 1.0)

    release_date: Optional[str] = Field(default=None, description="Model release date")


# Model specifications database
MODEL_SPECS: dict[str, ModelSpec] = {
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
        ),
        pricing=ModelPricing(input=15.0, output=75.0, cache_read=1.5, cache_write=18.75),
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
        ),
        pricing=ModelPricing(input=3.0, output=15.0, cache_read=0.3, cache_write=3.75),
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
        ),
        pricing=ModelPricing(input=3.0, output=15.0, cache_read=0.3, cache_write=3.75),
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
        ),
        pricing=ModelPricing(input=3.0, output=15.0, cache_read=0.3, cache_write=3.75),
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
        ),
        pricing=ModelPricing(input=0.8, output=4.0, cache_read=0.08, cache_write=1.0),
        context_window=200_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 1.0),
        release_date="2024-10-22",
    ),
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
        ),
        pricing=ModelPricing(input=2.0, output=8.0),
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
        ),
        pricing=ModelPricing(input=0.4, output=1.6),
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
        ),
        pricing=ModelPricing(input=0.1, output=0.4),
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
        ),
        pricing=ModelPricing(input=1.1, output=4.4),
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
        ),
        pricing=ModelPricing(input=2.0, output=8.0),
        context_window=128_000,
        max_output_tokens=64_000,
        temperature_range=(0.0, 2.0),
        release_date="2025-04-16",
    ),
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
        ),
        pricing=ModelPricing(input=1.25, output=10.0),
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
        ),
        pricing=ModelPricing(input=0.3, output=2.5),
        context_window=1_000_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="2025-01-01",
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
        ),
        pricing=ModelPricing(input=0.1, output=0.4),
        context_window=1_000_000,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
        release_date="2025-06-17",
    ),
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
        ),
        pricing=ModelPricing(input=0.18, output=0.18),
        context_window=16_384,
        max_output_tokens=4_096,
        temperature_range=(0.0, 2.0),
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
        ),
        pricing=ModelPricing(input=0.18, output=0.18),
        context_window=128_000,
        max_output_tokens=4_096,
        temperature_range=(0.0, 2.0),
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
        ),
        pricing=ModelPricing(input=12.0, output=12.0),
        context_window=32_768,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
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
        ),
        pricing=ModelPricing(input=0.3, output=0.3),
        context_window=32_768,
        max_output_tokens=32_768,
        temperature_range=(0.0, 2.0),
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
        ),
        pricing=ModelPricing(input=0.0, output=0.0),
        context_window=0,
        max_output_tokens=0,
        temperature_range=(0.0, 2.0),
    ),
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
        ),
        pricing=ModelPricing(input=0.15, output=0.15),
        context_window=32_768,
        max_output_tokens=8_192,
        temperature_range=(0.0, 2.0),
    ),
}


def get_spec(model: Model) -> ModelSpec:
    if model not in MODEL_SPECS:
        raise KeyError(f"No specification found for model: {model}")

    return MODEL_SPECS[model]
