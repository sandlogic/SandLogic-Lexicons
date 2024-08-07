## Gemma-2-9b - it

Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. They are text-to-text, decoder-only large language models, available in English, with open weights for both pre-trained variants and instruction-tuned variants. Gemma models are well-suited for a variety of text generation tasks, including question answering, summarization, and reasoning. Their relatively small size makes it possible to deploy them in environments with limited resources such as a laptop, desktop or your own cloud infrastructure, democratizing access to state of the art AI models and helping foster innovation for everyone. 

### Prompt format :  

`<start_of_turn>user

{prompt}<end_of_turn> 

<start_of_turn>model 

<end_of_turn> 

<start_of_turn>model `

Open Large Language Models (LLMs) have diverse applications across multiple sectors and fields. The following examples illustrate some potential uses, though this list is not exhaustive. These use-cases were likely considered by the model developers during the training and creation process.  



**Text Creation**: These models can produce various creative text formats, including poetry, scripts, programming code, advertising copy, and email drafts. 

**Interactive AI and Chatbots**: Enable conversational interfaces for customer support, digital assistants, or interactive programs. 

**Text Condensation**: Produce concise overviews of text collections, scholarly articles, or reports. 

 ### Benchmark results

| Model       | Quantization Type | Original Size | Quantized Size | Winogrande Score | HellaSwag Score |
|-------------|-------------------|---------------|----------------|------------------|-----------------|
| Gemma2-9B   | Q5_KM             | 19 GB         | 6.65 GB        | 75.29            | 78.75           |
| Gemma2-9B   | IQ4_XS            | 19 GB         | 5.76 GB        | 75.92            | 79.25           |
| Gemma2-9B   | Q4_KM             | 19 GB         | 5.18 GB        | 76.17            | 78.0            |
