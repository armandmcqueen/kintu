import enum


class LLMSDK(str, enum.Enum):
    # The LLM SDK is the library that we use to call the model. The SDK may support
    # multiple providers.
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GEMINI = "gemini"
    LITELLM = "litellm"
