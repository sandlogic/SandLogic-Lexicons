## Med42-v2: A Suite of Clinically-aligned Large Language Models

### Overview

Med42-v2 is a suite of open-access clinical large language models (LLMs) instruct and preference-tuned by M42 to expand access to medical knowledge. Built on LLaMA-3 architecture, these models come in 8B and 70B parameter versions, designed to provide high-quality answers to medical questions.

### Key Performance Metrics

- Med42-v2-70B outperforms GPT-4.0 in most MCQA tasks.
- Med42-v2-70B achieves a MedQA zero-shot performance of 79.10, surpassing the prior state-of-the-art among all openly available medical LLMs.
- Med42-v2-70B leads the Clinical Elo Rating Leaderboard.

### Clinical Elo Rating Leaderboard

| Model | Elo Score |
|-------|-----------|
| **Med42-v2-70B** | 1764 |
| Llama3-70B-Instruct | 1643 |
| GPT4-o | 1426 |
| Llama3-8B-Instruct | 1352 |
| Mixtral-8x7b-Instruct | 970 |
| **Med42-v2-8B** | 924 |
| OpenBioLLM-70B | 657 |
| JSL-MedLlama-3-8B-v2.0 | 447 |

### Limitations & Safe Use

- The Med42-v2 suite is not yet ready for real clinical use. Extensive human evaluation is ongoing to ensure safety.
- There is potential for generating incorrect or harmful information.
- Risk of perpetuating biases present in the training data.

**Important:** Use these models responsibly. Do not rely on them for medical usage without rigorous safety testing.

### Model Details

*Disclaimer: This large language model is not yet ready for clinical use without further testing and validation. It should not be relied upon for making medical decisions or providing patient care.*

- **Model Developers:** M42 Health AI Team
- **Base Model:** Llama3 - 8B & 70B Instruct
- **Training Data:** Instruction-tuned using a dataset of ~1B tokens compiled from various open-access and high-quality sources, including medical flashcards, exam questions, and open-domain dialogues.
- **Context Length:** 8k tokens
- **Input/Output:** Text-only data for both input and output
- **Status:** Static model trained on an offline dataset. Future versions will be released as performance is enhanced.


### Intended Use

The Med42-v2 suite is being made available for further testing and assessment as AI assistants to enhance clinical decision-making and access to LLMs for healthcare use. Potential use cases include:

1. Medical question answering
2. Patient record summarization
3. Aiding medical diagnosis
4. General health Q&A

### Evaluation Results of Quantized Model 

 |                Tasks                 | Metric   | Value |  Stderr |
|--------------------------------------|-----------|------:|--------:|
 |medmcqa                               |acc        |  0.56 |0.0709|
 |                                      | acc_norm   |  0.56 |0.0709|
 |clinical_knowledge                    | acc        |  0.68 |0.0666|
