## Llama-3.2-1B-Instruct-Medical

### Model Information
The Meta Llama 3.2 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction-tuned generative models in 1B and 3B sizes (text in/text out). The Llama 3.2 instruction-tuned text only models are optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. They outperform many of the available open source and closed chat models on common industry benchmarks.

**Model Developer**: Meta

**Model Architecture**: Llama 3.2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety.

## Original Model Information

- **Base Model**: [Meta Llama 3.2 1B Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
- **Developer**: Meta (base model)
- **Model Type**: Multilingual large language model (LLM)
- **Architecture**: Auto-regressive language model with optimized transformer architecture
- **Parameters**: 1 billion
- **Training Approach**: Supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF)

## Fine-tuning Details

- **Dataset**: [bigbio/med_qa](https://huggingface.co/datasets/bigbio/med_qa)
- **Languages**: English, simplified Chinese, and traditional Chinese
- **Dataset Size**: 
  - English: 12,723 questions
  - Simplified Chinese: 34,251 questions
  - Traditional Chinese: 14,123 questions
- **Data Type**: Free-form multiple-choice OpenQA for medical problems, collected from professional medical board exams

## Model Capabilities

This model is optimized for medical-related dialogue and tasks, including:

- Answering medical questions
- Summarizing medical information
- Assisting with medical problem-solving

## Intended Use in Medical Domain

1. **Medical Education**: Assisting medical students in exam preparation and learning
2. **Clinical Decision Support**: Providing quick references for healthcare professionals
3. **Patient Education**: Explaining medical concepts in simple terms for patients
4. **Medical Literature Review**: Summarizing and extracting key information from medical texts
5. **Differential Diagnosis**: Assisting in generating potential diagnoses based on symptoms
6. **Medical Coding**: Aiding in the accurate coding of medical procedures and diagnoses
7. **Drug Information**: Providing information on medications, their uses, and potential interactions
8. **Medical Translation**: Assisting with medical translations across supported languages
