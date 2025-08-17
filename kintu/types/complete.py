from __future__ import annotations

from typing import Any, Protocol

from pydantic import BaseModel, ConfigDict

from kintu.types.message import Message
from kintu.types.model import Model
from kintu.types.provider import Provider
from kintu.types.provider_config import ProviderConfigs
from kintu.types.tool import Tool


class LLMUsage(BaseModel):
    # Unified token counting. These are non-overlapping fields. Total tokens is the sum
    # of all of them.
    input_uncached_tokens: int = 0
    input_cached_tokens: int = 0  # Read from cache
    input_cache_write_tokens: int = 0  # Written to cache
    completion_tokens: int = 0  # Output tokens (not including reasoning)
    reasoning_tokens: int = 0  # Thinking/reasoning tokens

    # Provider-specific usage data
    provider_usage: dict[str, Any] = {}


class RequestTiming(BaseModel):
    # All times in seconds
    ttft: float  # Time to first token. Maybe be a reasoning token.
    duration: float  # Total request duration


# Core API types
class CompleteInput(BaseModel):
    messages: list[Message]
    model: Model

    # Core parameters supported across all providers
    max_tokens: int | None = None  # Will use the max tokens for the model if not provided
    # Temperature is a value from 0 to 1. It will scale the actual temperature value to match the
    # model's temperature range
    temperature: float | None = None

    # Tools (if supported by provider)
    tools: list[Tool] | None = None  # Can be Tool or provider-specific tools

    # Provider-specific configs
    provider_configs: ProviderConfigs | None = None

    # Streaming
    stream: bool = False
    stream_callback: AsyncStreamCallback | None = None

    model_config = ConfigDict(arbitrary_types_allowed=True)


class CompleteReply(BaseModel):
    # Core response
    messages: list[Message]  # Assistant messages generated
    model: Model
    provider: Provider

    # Metadata
    usage: LLMUsage
    timing: RequestTiming

    # Raw provider data (always preserved)
    provider_response: Any | list[Any]  # Single response or list of stream chunks
    # TODO: Better typing

    model_config = ConfigDict(arbitrary_types_allowed=True)


# Streaming types
class StreamChunk(BaseModel):
    """
    A streaming chunk with provider data and timing.

    kintu does not interpret the provider data at all.
    """

    provider_data: Any
    timestamp: float
    chunk_index: int

    model_config = ConfigDict(arbitrary_types_allowed=True)


# Streaming callback
class AsyncStreamCallback(Protocol):
    async def __call__(self, chunk: StreamChunk) -> None: ...
