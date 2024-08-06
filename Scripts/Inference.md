## Inference Guide

This guide explains how to install and use the llama-cpp-python package for inference with our quantized models.

## Installation

### Requirements:
- Python 3.8+
- C compiler
  - Linux: gcc or clang
  - Windows: Visual Studio or MinGW
  - MacOS: Xcode

To install the package, run:

```bash
pip install llama-cpp-python 
```
This command will build llama.cpp from source and install it alongside the Python package. If the installation fails, add --verbose to the pip install command to see the full cmake build log.
Please refer to the llama-cpp-python [documentation](https://llama-cpp-python.readthedocs.io/en/latest/).

### Basic Text Completion
Here's an example demonstrating how to use the high-level API for basic text completion:

```bash
from llama_cpp import Llama

llm = Llama(
    model_path="./models/7B/llama-model.gguf",
    verbose=False,
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # n_ctx=2048, # Uncomment to increase the context window
)

output = llm(
    "Q: Name the planets in the solar system? A: ", # Prompt
    max_tokens=32, # Generate up to 32 tokens
    stop=["Q:", "\n"], # Stop generating just before a new question
    echo=False # Don't echo the prompt in the output
)

print(output["choices"][0]["text"])
```


### Pulling Models from Hugging Face Hub

You can download `Llama` models in `gguf` format directly from Hugging Face using the `from_pretrained` method. This feature requires the `huggingface-hub` package.

To install it, run: `pip install huggingface-hub`

```bash
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="SandLogic/Meta-Llama-3-8B-Instruct-GGUF",
    filename="*q5_KM.gguf",
    verbose=False
)
```
By default, from_pretrained will download the model to the Hugging Face cache directory. You can manage installed model files using the huggingface-cli tool.

### Chat Completion
The high-level API also provides a simple interface for chat completion:

```bash
from llama_cpp import Llama

llm = Llama(
    model_path="./models/7B/llama-model.gguf",
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # n_ctx=2048, # Uncomment to increase the context window
    verbose=False
)

output = llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "You're an AI assistant who answers general knowledge questions."},
        {
            "role": "user",
            "content": "What is the largest moon in our solar system, and which planet does it orbit?"
        }
    ]
)

print(output["choices"][0]['message']['content'])
```
### Additional Notes

1. The `llama-cpp-python` package provides Python bindings for the `llama.cpp` library, allowing for efficient inference of LLM models.

2. GPU acceleration can significantly improve inference speed. To use it, uncomment the `n_gpu_layers=-1` line in the Llama initialization or set `n_gpu_layers=n` where n is the number of layers you want to offload to GPU.
3. The context window size (`n_ctx`) determines how much text the model can process at once. Increasing it allows for longer inputs but may require more memory.
4. The create_chat_completion method is particularly useful for chatbot-like applications, allowing for multi-turn conversations.

### Performance Considerations

- Inference speed and memory usage will vary depending on the model size and quantization level.
- For optimal performance, consider using GPU acceleration when available.
- Adjust the `max_tokens` parameter based on your needs to balance between response length and inference time.