from typing import Protocol

from kintu.types.complete import CompleteInput, CompleteReply


# Core interface for a client
class LLMClient(Protocol):
    """Core interface that all providers implement."""

    async def complete(self, inp: CompleteInput) -> CompleteReply:
        """Asynchronous completion."""
        ...
