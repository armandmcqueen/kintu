# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kintu is a generic multi-provider LLM SDK written in Python that provides a unified interface for working with different LLM providers (Anthropic, OpenAI, Gemini, Groq, Together). It allows users to switch between providers and models interchangeably while maintaining consistent API contracts.

Version: 0.0.2 (early development)

## Development Environment

This project uses `uv` as the Python package manager and `Flit` as the build backend. Python 3.10+ is required.

## Common Commands

### Development Setup
```bash
# Install dependencies
uv sync

# Install package in development mode
invoke dev
```

### Code Quality & Testing
```bash
# Run all checks (format, lint, typecheck, optionally tests)
invoke check --tests

# Run individual checks
invoke lint           # Run ruff linter
invoke format         # Format code with ruff
invoke format --check # Check formatting without changes
invoke typecheck      # Run pyright type checking
invoke test           # Run pytest tests
invoke test --verbose --coverage  # Run tests with coverage

# Quick format and fix imports
python -m ruff format .
python -m ruff check --fix . --select I
```

### Build and Deploy
```bash
# Clean build artifacts
invoke clean

# Build distribution packages
invoke build

# Check distribution packages
invoke check-dist

# Version management
invoke bump           # Bump patch version (e.g., 0.0.2 -> 0.0.3)
invoke bump --part=minor  # Bump minor version (e.g., 0.0.2 -> 0.1.0)
invoke bump --part=major  # Bump major version (e.g., 0.0.2 -> 1.0.0)

# Deploy to TestPyPI (for testing)
invoke test-deploy

# Deploy to PyPI (for production release)
invoke release

# Deploy with custom options
invoke deploy --repository=testpypi
```

## Project Structure

```
kintu/
├── __init__.py                    # Package metadata, version
├── main.py                        # Simple entry point (hello world)
├── credential_manager.py          # Manages API keys for all providers
├── utilities.py                   # Shared utility functions
├── types/                         # Core type definitions
│   ├── client.py                  # LLMClient protocol
│   ├── complete.py                # CompleteInput/Reply, streaming types
│   ├── content.py                 # Content types (text, image, etc.)
│   ├── errors.py                  # Custom exceptions
│   ├── llmsdk.py                  # SDK enum (which SDK to use)
│   ├── message.py                 # Message types
│   ├── model.py                   # Model enum (all supported models)
│   ├── model_spec.py              # Model specifications (context, pricing, features)
│   ├── provider.py                # Provider enum (Anthropic, OpenAI, etc.)
│   ├── provider_config.py         # Provider-specific configurations
│   ├── role.py                    # Role types (user, assistant, system)
│   ├── tool.py                    # Tool/function calling types
│   └── llmsdks/                   # SDK-specific type definitions
│       ├── openai_types.py        # OpenAI SDK types
│       └── gemini_types.py        # Gemini SDK types
├── model_library/                 # Model specifications database
│   ├── model_library.py           # Main registry and get_spec()
│   ├── anthropic.py               # Anthropic model specs
│   ├── openai.py                  # OpenAI model specs
│   ├── gemini.py                  # Gemini/Google model specs
│   ├── groq.py                    # Groq model specs
│   └── together.py                # Together AI model specs
└── clients/                       # Provider client implementations
    ├── anthropic/                 # Anthropic client (planned)
    ├── openai/                    # OpenAI client
    │   ├── converter_test.py      # Type converter testing
    │   └── type_inspector.py      # Type inspection utilities
    ├── gemini/                    # Gemini client (planned)
    └── litellm/                   # LiteLLM client (planned)
```

## Key Concepts

### Providers vs SDKs
- **Provider**: The underlying hosting provider (Anthropic, OpenAI, Gemini, Groq, Together)
- **SDK**: The client library used to communicate with providers (can be provider-specific or generic like LiteLLM)

### Core Types
- `Model`: Enum of all supported models across all providers
- `Provider`: Enum of hosting providers
- `LLMClient`: Protocol that all provider clients must implement
- `CompleteInput/CompleteReply`: Unified request/response types
- `ModelSpec`: Detailed specifications for each model (context window, pricing, features, etc.)

### Credential Management
The `CredentialManager` class handles API keys for all providers via environment variables:
- `ANTHROPIC_API_KEY`
- `OPENAI_API_KEY`
- `GEMINI_API_KEY`
- `GROQ_API_KEY`
- `TOGETHER_API_KEY`

## Current Status

The library is in active development (3rd/4th iteration). Core architecture is established:
- ✅ Type system and core interfaces defined
- ✅ Model library with comprehensive specs
- ✅ Credential management system
- ✅ Testing infrastructure
- 🚧 Provider client implementations in progress

## Dependencies

Core:
- `google-genai>=1.29.0` - Google Gemini SDK
- `openai>=1.99.9` - OpenAI SDK
- `pillow>=11.3.0` - Image processing
- `pydantic>=2.11.7` - Data validation and settings

Development:
- `flit>=3.9.0` - Build backend
- `invoke>=2.2.0` - Task runner
- `pytest>=8.3.4` - Testing framework
- `ruff>=0.8.0` - Linter and formatter
- `pyright>=1.1.0` - Type checker