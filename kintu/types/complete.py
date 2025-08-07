from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, Protocol
from kintu.types.provider import Provider
from kintu.types.model import Model
from kintu.types.message import Message
from kintu.types.provider_config import ProviderConfigs


class LLMUsage(BaseModel):
    # Unified token counting
    input_tokens: int = 0
    input_cached_tokens: int = 0  # Read from cache
    input_cache_write_tokens: int = 0  # Written to cache
    completion_tokens: int = 0  # Output tokens (not including reasoning)
    reasoning_tokens: int = 0  # Thinking/reasoning tokens

    # Provider-specific usage data
    provider_usage: dict[str, Any] = {}


class RequestTiming(BaseModel):
    # All times in seconds
    ttft: float  # Time to first token (any visible content)
    duration: float  # Total request duration

# Core API types
class CompleteInput(BaseModel):
    messages: list[Message]
    model: Model

    # Core parameters supported across all providers
    max_tokens: int = 4096
    temperature: float | None = None

    # Tools (if supported by provider)
    tools: list[Any] | None = None  # Can be Tool or provider-specific tools

    # Provider-specific configs
    provider_configs: ProviderConfigs | None = None

    # Streaming
    stream: bool = False
    stream_callback: Any | None = None  # Will be AsyncStreamCallback

    def validate(self) -> None:
        """Validate that messages are supported by this provider/model."""
        # Provider implementations will check message types, roles, etc.
        pass

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

    model_config = ConfigDict(arbitrary_types_allowed=True)

# Streaming types
class StreamChunk(BaseModel):
    """A streaming chunk with provider data and timing."""
    provider_data: Any
    timestamp: float
    chunk_index: int

    model_config = ConfigDict(arbitrary_types_allowed=True)

# Streaming callback
class AsyncStreamCallback(Protocol):
    async def __call__(self, chunk: StreamChunk) -> None: ...

# Core interface
class LLMClient(Protocol):
    """Core interface that all providers implement."""

    async def complete(self, input: CompleteInput) -> CompleteReply:
        """Asynchronous completion."""
        ...
