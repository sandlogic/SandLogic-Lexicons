# SandLogic Model Zoo

Welcome to the SandLogic Model Zoo, your premier destination for optimized Large Language Models (LLMs) ready for immediate deployment across a variety of hardware platforms. Our repository is designed to bridge the gap between cutting-edge AI research and practical, real-world applications.

## Overview

The SandLogic Model Zoo houses a comprehensive collection of pre-trained and fine-tuned LLMs, each meticulously optimized for superior performance and efficiency. Our models are engineered to run seamlessly on both GPU and CPU architectures, democratizing access to advanced natural language processing capabilities. Our aim is to facilitate the spread and usage of Large Language Models (LLM) among a wider audience of developers, researchers, and enthusiasts.

## Key Features

### 1. Optimized Performance

All models in our zoo undergo rigorous optimization processes to ensure peak performance across diverse hardware configurations. Whether you're running on high-end GPUs or commodity CPUs, our models deliver exceptional results without compromising on efficiency.

### 2. Advanced Quantization Techniques

We employ state-of-the-art quantization methods to reduce the model size and increase inference speed without significant loss in accuracy. Our offerings include:

- Legacy quantization techniques (e.g., Q5_K_M, Q4_K_M)
- Cutting-edge imatrix quants (e.g., IQ4_XS)

These quantization approaches allow for deploying powerful models on resource-constrained devices, enabling edge AI applications.

### 3. Benchmark-Validated Performance

Each model in our zoo is rigorously evaluated on standard industry benchmarks, including:

- HellaSwag: Testing common sense reasoning
- MMLU (Massive Multitask Language Understanding): Assessing knowledge and reasoning across diverse domains
- Winogrande: Evaluating commonsense reasoning capabilities

We provide detailed performance metrics for each model, allowing you to make informed decisions based on your specific requirements.



## Documentation

For in-depth information on our quantization techniques and methodologies, please refer to our [Quantization Guide](Docs/Quantization/quantization.md).

To learn more about our benchmark evaluation processes and results, check out our [Benchmark Documentation](Docs/Benchmark Evaluation/benchmark.md).

To know about the models considered for quantization you can click on the below link -
1. [Meta-Llama-3-8B-Instruct](Models/Meta-Llama-3-8B-Instruct/Llama3.md)
2. [Phi-3-mini-4k-instruct](Models/Phi-3.1-mini-4k-instruct/Phi-3.1.md)
3. [Gemma-2-9b-it](Models/Gemma-2-9b-it/Gemma.md)

## Models 


This document provides a comparison of various quantized models, detailing their bit configurations, original sizes, and quantized sizes.

| Models                      | Download Links    | Bits           | Original size | Quantized size |
|-----------------------------|----------|----------------|---------------|----------------|
| Meta-Llama-3-8B-Instruct    | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/ESpFRPYv0gtOgf0Racp_9OABpYXSyIhgbzdESgqc7THCvg?e=18J8y7)       | 5 bit          | 16 GB         | 5.73 GB        |
| Meta-Llama-3-8B-Instruct    | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EfuowO5pD_1CrS8GIIxPl3sBJ-UaBn-JEWBMtJuhzlIcKw?e=gGqjlz) | Imatrix 4 bit  | 16 GB         | 4.45 GB        |
| Meta-Llama-3-8B-Instruct    | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EfIt1HwWyRlGhPwX8UGQJJUBuVB69A-UAaDo84gRPqlbBw?e=G9Eexx)       | 4 bit          | 16 GB         | 4.92 GB        |
| Phi-3-mini-4k-instruct      | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EeqcdqjF041KoimJACBA1mUBZaZlk1G-PmRwVxKInhJ8Xw?e=KUWAL5)       | 5 bit          | 8 GB          | 2.82 GB        |
| Phi-3-mini-4k-instruct      | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EUlhoZQwxtdAty7DCdZOjFgBZltj1xcoYe_1_5GsqBN50g?e=6yOVRD) | Imatrix 4 bit  | 8 GB          | 2.06 GB        |
| Phi-3-mini-4k-instruct      | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EVpJTjph6FRFupV8ahyhWS8BWjFK87ufRFMteTRvUdHsrg?e=3ITIRn)       | 4 bit          | 8 GB          | 2.39 GB        |
| Gemma-2-9b-it               | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EWc0YMTTtYNGuNElvvShu0cBmeardml8yKkZ9L5ElPlA7A?e=wJdQoJ)       | 5 bit          | 19 GB         | 6.65 GB        |
| Gemma-2-9b-it               | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EevURY_Vz25DqdbTFJJpvfcBmEo35Ez7t4Lm1XLGUj1Q_g?e=0qKWiU) | Imatrix 4 bit  | 19 GB         | 5.76 GB        |
| Gemma-2-9b-it               | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EQeFSWyfTiBHjansoeYQzxUBQbIH5SEYpNJJHWb8vztIkw?e=6FbSwc)       | 4 bit          | 19 GB         | 5.18 GB        |


## Inference

Our Model Zoo supports efficient inference using the `llama-cpp-python` package. This allows you to run our quantized models on both CPU and GPU with minimal setup.

For detailed instructions on installation, usage examples, and advanced configurations, please refer to our [Inference Guide](Scripts/Inference.md).
## License

[Add license information]

## Contact

[Add contact information or support channels]

## Acknowledgments

We would like to express our gratitude to the following projects and organizations for their invaluable contributions to the field of AI and for making their work available to the community:

1. [llama.cpp](https://github.com/ggerganov/llama.cpp) - For providing an efficient C/C++ implementation of LLM inference, which we use for model conversion and quantization.

2. [Hugging Face](https://huggingface.co/) - The Hugging Face Hub is a valuable resource for sharing and accessing state-of-the-art machine learning models, reflecting their commitment to open-source development and democratizing AI. Their tools and libraries greatly simplify working with large language models.
2. [Meta AI](https://ai.meta.com/) - For developing and releasing the Llama 3 model, pushing the boundaries of large language models.

3. [Google AI](https://ai.google/) - For creating the Gemma 2 model and contributing to the advancement of open-source AI.

4. [Microsoft Research](https://www.microsoft.com/en-us/research/) - For their work on the Phi-3 model, furthering the capabilities of smaller, more efficient language models.

5. [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - For providing Python bindings to llama.cpp, enabling easy integration and inference in Python environments.

These projects have been instrumental in our work, and we are thankful for their contributions to the open-source AI community.
