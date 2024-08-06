## Phi-3-mini-4k  

Phi-3 Mini is a cutting-edge, open-source language model with 3.8 billion parameters. Its compact design combines high performance with efficiency. The model was trained on the Phi-3 datasets, which consist of carefully curated synthetic data and filtered content from public websites, emphasizing high-quality information and strong reasoning capabilities. 

Following its initial training, Phi-3 Mini underwent additional refinement through supervised fine-tuning and direct preference optimization. This post-training process was designed to enhance the model's ability to follow instructions accurately and to reinforce robust safety protocols. 

### Prompt Format: 

`<|user|>\n Question <|end|>\n<|assistant|> `

 

This model is designed for both commercial and research applications in the English language. It is particularly well-suited for use cases that involve:  

1. Environments with limited memory or computational resources 

2. Scenarios where low latency is critical 

3. Tasks requiring robust reasoning capabilities, especially in mathematics and logic 

4. Processing and analyzing long-form context or large amounts of text  

The model's features make it adaptable to a wide range of applications where these factors are important considerations. 

**Original model**: [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
## Benchmark results (3.8B)

| Model | Quantization Type | Original Size | Quantized Size | Winogrande Score | HellaSwag Score |
|-------|-------------------|---------------|----------------|------------------|-----------------|
| Phi-3 | Q5_KM             | 8 GB          | 2.82 GB        | 74.30            | 76.75           |
| Phi-3 | IQ4_XS            | 8 GB          | 2.06 GB        | 76.16            | 77.25           |
| Phi-3 | Q4_KM             | 8 GB          | 2.39 GB        | 74.35            | 76.5            |

