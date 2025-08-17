from pydantic import BaseModel, Field

from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.provider import Provider


class ModelFeatures(BaseModel):
    vision: bool
    thinking: bool
    tools: bool
    web_search: bool
    code_execution: bool


class ModelPricing(BaseModel):
    output: float = Field(description="Cost per million output tokens")
    input_nocache: float = Field(description="Cost per million input tokens that are neither written to cache or read from cache")
    input_cache_read: float = Field(description="Cost per million cached input tokens")
    input_cache_write: float = Field(description="Cost to write million tokens to cache")


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
    temperature_range: tuple[float, float]

    release_date: str = Field(description="Model release date")
