import enum


class Provider(str, enum.Enum):
    # Provider is the underlying hosting provider that runs the models. They may be called by
    # multiple LLM SDKs or an LLM SDK may call multiple providers.
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GEMINI = "gemini"
    GROQ = "groq"
    TOGETHER = "together"
