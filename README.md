# SandLogic Lexicon

Welcome to the SandLogic Lexicon, your premier destination for optimized Large Language Models (LLMs) ready for immediate deployment across a variety of hardware platforms. Our repository is designed to bridge the gap between cutting-edge AI research and practical, real-world applications.

## Overview

The SandLogic Lexicon houses a comprehensive collection of pre-trained and fine-tuned LLMs, meticulously optimized for superior performance and efficiency. Our models are engineered to run seamlessly on both GPU and CPU architectures, democratizing access to advanced natural language processing capabilities. Our aim is to facilitate the spread and usage of Large Language Models (LLM) among a wider audience of developers, researchers, and enthusiasts. 
## Key Features

### 1. Optimized Performance

All models in our Lexicon  undergo rigorous optimization processes to ensure peak performance across diverse hardware configurations. Whether you're running on high-end GPUs or commodity CPUs, our models deliver exceptional results without compromising on efficiency.

### 2. Advanced Quantization Techniques

We employ state-of-the-art quantization methods to reduce the model size and increase inference speed without significant loss in accuracy. Our offerings include:

- Legacy quantization techniques (e.g., Q5_K_M, Q4_K_M)
- Cutting-edge imatrix quants (e.g., IQ4_XS)

These quantization approaches allow for deploying powerful models on resource-constrained devices, enabling edge AI applications.

### 3. Benchmark-Validated Performance

Each model in our Lexicon  is rigorously evaluated on standard industry benchmarks, including:

- HellaSwag: A challenging commonsense reasoning task that tests a model's ability to complete scenarios with plausible endings.

-  MMLU (Massive Multitask Language Understanding): A comprehensive benchmark covering 57 subjects across STEM, humanities, and social sciences to evaluate a model's multitask capabilities.

-  CodeXGLUE Code2Text: Assesses a model's ability to generate natural language descriptions from source code snippets.

-  Winogrande: A large-scale dataset for testing commonsense reasoning, based on the Winograd Schema Challenge.

-  MedMCQA: A multiple-choice question answering dataset designed to evaluate medical knowledge and reasoning.

-  MMLU Clinical Knowledge: A subset of MMLU focusing specifically on clinical knowledge, testing a model's understanding of medical concepts and practices.

These benchmarks provide a comprehensive evaluation of our models' performance across various domains, including general knowledge, reasoning, coding, and specialized medical understanding.



## Documentation

For in-depth information on our quantization techniques and methodologies, please refer to our [Quantization Guide](Docs/Quantization/quantization.md).

To learn more about our benchmark evaluation processes and results, check out our [Benchmark Documentation](Docs/BenchmarkEvaluation/benchmark.md).

To know about the models considered for quantization you can click on the below link -
1. [Meta-Llama-3-8B-Instruct](Models/Meta-Llama-3-8B-Instruct/Llama3.md)
2. [Phi-3-mini-4k-instruct](Models/Phi-3.1-mini-4k-instruct/Phi3.1.md)
3. [Gemma-2-9b-it](Models/Gemma-2-9b-it/Gemma.md)
4. [Nxcode-CQ-7B-orpo](Models/Nxcode-CQ-7B-orpo/Nxcode.md)
5. [Llama3-Med42-8B](Models/Llama3-Med42-8B/Llama3Med42.md)
6. [Llama3-Hindi-8B](Models/LLama3-Gaja-Hindi-8B/GajaHindi.md)

## Models 


This document provides a comparison of various quantized models, detailing their bit configurations, original sizes, and quantized sizes.

| Models                   | Download Links    | Bits          | Original size | Quantized size |
|--------------------------|----------|---------------|---------------|----------------|
| Meta-Llama-3-8B-Instruct | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/ESpFRPYv0gtOgf0Racp_9OABpYXSyIhgbzdESgqc7THCvg?e=18J8y7)       | 5 bit         | 16 GB         | 5.73 GB        |
| Meta-Llama-3-8B-Instruct | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EfuowO5pD_1CrS8GIIxPl3sBJ-UaBn-JEWBMtJuhzlIcKw?e=gGqjlz) | Imatrix 4 bit | 16 GB         | 4.45 GB        |
| Meta-Llama-3-8B-Instruct | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EfIt1HwWyRlGhPwX8UGQJJUBuVB69A-UAaDo84gRPqlbBw?e=G9Eexx)       | 4 bit         | 16 GB         | 4.92 GB        |
| Phi-3-mini-4k-instruct   | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EeqcdqjF041KoimJACBA1mUBZaZlk1G-PmRwVxKInhJ8Xw?e=KUWAL5)       | 5 bit         | 8 GB          | 2.82 GB        |
| Phi-3-mini-4k-instruct   | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EUlhoZQwxtdAty7DCdZOjFgBZltj1xcoYe_1_5GsqBN50g?e=6yOVRD) | Imatrix 4 bit | 8 GB          | 2.06 GB        |
| Phi-3-mini-4k-instruct   | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EVpJTjph6FRFupV8ahyhWS8BWjFK87ufRFMteTRvUdHsrg?e=3ITIRn)       | 4 bit         | 8 GB          | 2.39 GB        |
| Gemma-2-9b-it            | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EWc0YMTTtYNGuNElvvShu0cBmeardml8yKkZ9L5ElPlA7A?e=wJdQoJ)       | 5 bit         | 19 GB         | 6.65 GB        |
| Gemma-2-9b-it            | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EevURY_Vz25DqdbTFJJpvfcBmEo35Ez7t4Lm1XLGUj1Q_g?e=0qKWiU) | Imatrix 4 bit | 19 GB         | 5.76 GB        |
| Gemma-2-9b-it            | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EQeFSWyfTiBHjansoeYQzxUBQbIH5SEYpNJJHWb8vztIkw?e=6FbSwc)       | 4 bit         | 19 GB         | 5.18 GB        |
| Nxcode-CQ-7B-orpo        | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EUOJzCo1h7RJg4IGszZJOKABL7fHOasUf3nfuHof28rNRg?e=iaOMoQ)  | 5 bit         | 14.5 GB       | 5.43 GB        |
| Nxcode-CQ-7B-orpo        | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EXVWLAH1o-RGlJYEQkhEqj0B6Xp47IRGNvX43xR5AY1L-g?e=S12pMM)  | 4 bit         | 14.5 GB       | 4.74 GB        |
| Llama3-Med42-8B          | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/Ea7NUHUk-89CjGwgSMgTzKQBxP6azT-ruMi_srVURJbgRg?e=u0Evnn)  | 5 bit         | 16.07 GB      | 5.34 GB        |
| Llama3-Med42-8B          | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EcxEdHD_yR1EtqZc_4vq1LQBdhpSUXWSqTqGdlEyONtGcA?e=K1Zrel)  | 4 bit         | 16.07 GB      | 4.58 GB        |
| Llama3-Hindi-8B          | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EUMb2HjZoHlGqnExXhwB0noB-ckpZXRk8Y2piV7ROxKzVg?e=X1i7Zv)  | 5 bit         | 16.07 GB      | 5.34 GB        |
| Llama3-Hindi-8B          | [Click here](https://sandlogic0-my.sharepoint.com/:u:/g/personal/rakshit_aralimatti_sandlogic_com/EYmOS-jf5U5AkqDqguD3DpMBD0Xc2iAFkR1hnB2kTDcplg?e=2lu6SP)  | 4 bit         | 16.07 GB      | 4.58 GB        |



## Inference

Our Model Zoo supports efficient inference using the `llama-cpp-python` package. This allows you to run our quantized models on both CPU and GPU with minimal setup.

For detailed instructions on installation, usage examples, and advanced configurations, please refer to our [Inference Guide](Scripts/Inference.md).
## License

This repository and all its contents are licensed under the [MIT License](https://opensource.org/licenses/MIT). By using the SandLogic Lexicon, you agree to the terms and conditions of this license. 
 
``` 
MIT License 
 
Copyright (c) 2024 SandLogic 
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
``` 
 

## Contact

For any inquiries or support, please contact us at support@sandlogic.com or visit our (https://www.sandlogic.com/contact-us/). 
## Acknowledgments

We would like to express our gratitude to the following projects and organizations for their invaluable contributions to the field of AI and for making their work available to the community:

1. [llama.cpp](https://github.com/ggerganov/llama.cpp) - For providing an efficient C/C++ implementation of LLM inference, which we use for model conversion and quantization.

2. [Hugging Face](https://huggingface.co/) - The Hugging Face Hub is a valuable resource for sharing and accessing state-of-the-art machine learning models, reflecting their commitment to open-source development and democratizing AI. Their tools and libraries greatly simplify working with large language models.
3. [Meta AI](https://ai.meta.com/) - For developing and releasing the Llama 3 model, pushing the boundaries of large language models.

4. [Google AI](https://ai.google/) - For creating the Gemma 2 model and contributing to the advancement of open-source AI.

5. [Microsoft Research](https://www.microsoft.com/en-us/research/) - For their work on the Phi-3 model, furthering the capabilities of smaller, more efficient language models.

6. [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) - For providing Python bindings to llama.cpp, enabling easy integration and inference in Python environments.

7. [NTQAI](https://ntq.com.vn/): For developing the Nxcode-CQ-7B-orpo model, advancing AI-assisted coding capabilities.

8. [M42 Health AI Team](https://m42.ae/): For creating the Llama3-Med42-8B model, expanding access to medical knowledge through AI.

9. [Cognitive-Lab](https://www.cognitivelab.in/): For producing the LLama3-Gaja-Hindi-8B-v0.1 model, pushing the boundaries of bilingual English/Hindi AI technologies.

These projects have been instrumental in our work, and we are thankful for their contributions to the open-source AI community.
