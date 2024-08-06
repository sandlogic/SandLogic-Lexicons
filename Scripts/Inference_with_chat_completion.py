from llama_cpp import Llama

llm = Llama(
      model_path="./models/7B/llama-model.gguf",
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # n_ctx=2048, # Uncomment to increase the context window
    verbose=False
)
output = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "Your a AI assistant who answers all the general knowledge question."},
          {
              "role": "user",
              "content": "What is the largest moon in our solar system, and which planet does it orbit?"
          }
      ]
)
print(output["choices"][0]['message']['content'])

