from typing import Optional

from pydantic import BaseModel, Field

from kintu.types.llmsdk import LLMSDK
from kintu.types.model import Model
from kintu.types.provider import Provider


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
