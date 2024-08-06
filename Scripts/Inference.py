from llama_cpp import Llama

llm = Llama(
      model_path="./models/7B/llama-model.gguf",
      verbose=False,
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: Name the planets in the solar system? A: ", # Prompt
      max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=False # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output["choices"][0]["text"])
