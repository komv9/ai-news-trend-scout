# agent/llm.py
import os

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

def run_llm(prompt: str) -> str:
    """
    Unified LLM interface.
    Supports: ollama | mock | cloud (future)
    """

    if LLM_PROVIDER == "ollama":
        import ollama
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"]

    elif LLM_PROVIDER == "mock":
        return (
            "Detected trends: AI agents, autonomous workflows.\n"
            "These topics appear frequently in recent articles, "
            "indicating sustained industry focus."
        )

    elif LLM_PROVIDER == "cloud":
        # Placeholder for Groq / HF / OpenAI
        return "Cloud LLM response placeholder"

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
