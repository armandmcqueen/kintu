class KintuError(Exception):
    """Base class for all Kintu errors."""

    pass


class MissingCredentialsError(KintuError):
    """Raised when credentials are missing."""

    pass


class InvalidLiteLLMModelError(KintuError):
    """Raised when a model is not a valid LiteLLM model."""

    pass
