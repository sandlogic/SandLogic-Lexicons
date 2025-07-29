# MedGemma-4B-IT (Quantized GGUF Versions)

[![license](https://img.shields.io/badge/license-Gemma-blue.svg)](https://developers.google.com/health-ai-developer-foundations/terms)

This repository provides **quantized GGUF** versions of the `google/medgemma-4b-it` model. These 4-bit and 5-bit quantized variants maintain the original model’s multimodal medical reasoning capabilities while being optimized for efficient inference on resource-constrained devices.

---

## Model Overview

- **Original Model**: [`google/medgemma-4b-it`](https://huggingface.co/google/medgemma-4b-it)
- **Quantized Model Hugging Face Link**: [`SandLogicTechnologies/MedGemma-4B-IT-GGUF`](https://huggingface.co/SandLogicTechnologies/MedGemma-4B-IT-GGUF).
- **Quantized Versions**:  
  - `Q4_K_M` – 4-bit quantization (~2.3 GB)
  - `Q5_K_M` – 5-bit quantization (~2.6 GB)  
- **Architecture**: Decoder-only Transformer (based on Gemma) + SigLIP Vision Encoder  
- **Base Model**: `google/gemma-3-4b-pt`  
- **Modalities**: Text + Image  
- **Language**: English (medical domain)  
- **License**: [Health AI Developer Foundations License](https://developers.google.com/health-ai-developer-foundations/terms)  
- **Developer**: Google  

---

## Key Features

- Multimodal: Understands **text + images** for clinical tasks  
- Expert-level reasoning on:  
  - Chest X-rays  
  - Dermatology images  
  - Fundus photos  
  - Histopathology slides  
- Fine-tuned on:  
  - Clinical QA datasets  
  - Biomedical literature  
  - Radiology reports  
- Use cases: Clinical VQA, medical assistants, and healthcare R&D  
- Optimized for **CPU**, **low-end GPU**, and **edge devices**  

---

## Quantization Details

### Q4_K_M (4-bit)
- ~75% size reduction  
- Smallest memory footprint (~2.3 GB)  
- Slight performance degradation in complex reasoning  

### Q5_K_M (5-bit)
- ~69% size reduction  
- Higher accuracy (~2.6 GB)  
- Recommended for balanced performance and efficiency  

---

## Quick Start

### Text-only (Llama.cpp)
```bash
./llama-cli -hf SandLogicTechnologies/MedGemma-4B-IT-GGUF -p "What are the symptoms of diabetes?"
```
### Text-only (Llama.cpp)
```bash
./llama-gemma3-cli -hf SandLogicTechnologies/MedGemma-4B-IT-GGUF \
  -p "Describe this image." \
  --image ~/Downloads/xray_image.png


