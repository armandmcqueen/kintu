from kintu.model_library.anthropic import ANTHROPIC_MODEL_LIBRARY
from kintu.model_library.gemini import GEMINI_MODEL_LIBRARY
from kintu.model_library.groq import GROQ_MODEL_LIBRARY
from kintu.model_library.openai import OPENAI_MODEL_LIBRARY
from kintu.model_library.together import TOGETHER_MODEL_LIBRARY
from kintu.types.model import Model
from kintu.types.model_spec import ModelSpec

# Model specifications database
MODEL_LIBRARY: dict[str, ModelSpec] = {}
MODEL_LIBRARY.update(ANTHROPIC_MODEL_LIBRARY)
MODEL_LIBRARY.update(OPENAI_MODEL_LIBRARY)
MODEL_LIBRARY.update(GEMINI_MODEL_LIBRARY)
MODEL_LIBRARY.update(GROQ_MODEL_LIBRARY)
MODEL_LIBRARY.update(TOGETHER_MODEL_LIBRARY)


def get_spec(model: Model) -> ModelSpec:
    if model not in MODEL_LIBRARY:
        raise KeyError(f"No specification found for model: {model}")

    return MODEL_LIBRARY[model]
