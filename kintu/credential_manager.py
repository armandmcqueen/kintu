import os
from typing import Dict
from kintu.types.provider import Provider
from kintu.types.model import Model
from kintu.model_library.model_library import get_spec
from kintu.types.errors import MissingCredentialsError

# Environment variable names for each provider
ENV_VAR_MAPPING = {
    Provider.ANTHROPIC: "ANTHROPIC_API_KEY",
    Provider.OPENAI: "OPENAI_API_KEY",
    Provider.GEMINI: "GEMINI_API_KEY",
    Provider.GROQ: "GROQ_API_KEY",
    Provider.TOGETHER: "TOGETHER_API_KEY",
}

class CredentialManager:
    """Manages API credentials for all LLM providers."""
    def __init__(self, verbose: bool = False):
        """Initialize and load available credentials from environment."""
        self.verbose = verbose
        self._credentials: Dict[Provider, str] = {}
        self._load_credentials()

    def vlog(self, *args):
        if self.verbose:
            print(*args)

    def _load_credentials(self) -> None:
        """Load credentials from environment variables."""
        for provider, env_var in ENV_VAR_MAPPING.items():
            self.vlog(f"CredentialManager: Checking for {env_var}...")
            api_key = os.environ.get(env_var)
            if api_key:
                self.vlog(f"✓ Found {env_var}")
                self._credentials[provider] = api_key
            else:
                self.vlog(f"ⅹ Missing {env_var}")

    def get_api_key_for_model(self, model: Model) -> str:
        """
        Get API key for a model.

        Raises MissingCredentialsError if credentials are missing.
        """
        spec = get_spec(model)
        provider = spec.provider
        return self.get_api_key(provider)

    def get_api_key(self, provider: Provider) -> str:
        """
        Get API key for a provider if available.

        Raises MissingCredentialsError if credentials are missing.
        """
        if not self.has_api_key(provider):
            raise MissingCredentialsError(f"Missing credentials for {provider.value} provider.")
        return self._credentials.get(provider)


    def has_api_key(self, provider: Provider) -> bool:
        """Check if we have the API Key for a Provider."""
        return provider in self._credentials

    def has_api_key_for_model(self, model: Model) -> bool:
        """Check if we have the API Key for a Model."""
        spec = get_spec(model)
        return self.has_api_key(spec.provider)

    def ensure_has_api_keys(self, providers: list[Provider]) -> None:
        """
        Check if we have API Keys for all of a set of providers and raise exception if not.

        Intended to be used on startup to fail fast if credentials are missing.
        """
        has_keys = all(self.has_api_key(p) for p in providers)
        if not has_keys:
            raise MissingCredentialsError(f"Missing credentials for providers: {providers}")

    def ensure_has_api_keys_for_models(self, models: list[Model]) -> None:
        """
        Check if we have API Keys for all of a set of models and raise exception if not.

        Intended to be used on startup to fail fast if credentials are missing.
        """
        providers = [get_spec(m).provider for m in models]
        self.ensure_has_api_keys(providers)

