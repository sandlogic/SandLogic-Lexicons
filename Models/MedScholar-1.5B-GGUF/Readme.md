# Quantized MedScholar-1.5B

[![license](https://www.apache.org/licenses/LICENSE-2.0)]

This repository provides **quantized GGUF** versions of the `yasserrmd/MedScholar-1.5B`. These 4-bit and 5-bit quantized variants retain the original model’s strengths in multimodal medical reasoning, while reducing memory and compute requirements—ideal for efficient inference on resource-constrained devices.

---
## Model Overview

- **Original Model**: yasserrmd/MedScholar-1.5B
- **Quantized Versions**: 
  - Q4_K_M (4-bit quantization)
  - Q5_K_M (5-bit quantization)
- **Architecture**: Decoder-only transformer
- **Base Model**: Qwen2.5-1.5B-Instruct-unsloth-bnb-4bit
- **Training Framework**: Unsloth + QLoRA
- **Dataset**: MIRIAD-4.4M (1M samples) [ODC-By 1.0]
- **License**: Apache-2.0 (inherits from base model); dataset is ODC-By 1.0
- **Language**: English

---

## Quantization Details

### Q4_K_M (4-bit)
- Approx. ~68% size reduction
- Lower memory footprint (~940 MB)
- Best suited for deployment on edge devices or low-resource GPUs
- Slight performance degradation in complex reasoning scenarios  

### Q5_K_M (5-bit)
- Approx. ~64% size reduction
- Higher fidelity (~1.04 GB)
- Better performance retention, recommended when quality is a priority 

---

## Quick Start

```bash
./llama-cli -hf SandLogicTechnologies/MedScholar-1.5B-GGUF -p "What are the symptoms of diabetes"

```
---

## Note 

⚠️ This model is for research, educational, and exploration purposes only. It is not a medical device and must not be used to provide clinical advice, diagnosis, or treatment.

---

## Acknowledgments

- These quantized models are based on the original work by the [https://huggingface.co/yasserrmd/MedScholar-1.5B].
- MIRIAD Dataset by Zheng et al. (2025) – [https://huggingface.co/datasets/miriad/miriad-4.4M].
- Qwen2.5 by Alibaba - [https://huggingface.co/Qwen].
- Training infrastructure: [https://github.com/unslothai/unsloth].

---

## Contact
For any inquiries or support, please contact us at support@sandlogic.com or visit our [Website](https://www.sandlogic.com/).
