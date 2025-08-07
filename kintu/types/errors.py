

class MissingCredentialsError(Exception):
    """Raised when required credentials for a LiteLLM backend are missing."""
    pass

class InvalidLiteLLMModelError(Exception):
    """Raised when a model is not a valid LiteLLM model."""
    pass