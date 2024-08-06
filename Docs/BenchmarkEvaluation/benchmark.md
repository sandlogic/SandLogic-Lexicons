# Benchmark Evaluation

To rigorously assess the performance of our quantized models, we employ a set of well-established benchmarks. These benchmarks help us evaluate the trade-offs between model size, computational efficiency, and accuracy across various language understanding tasks.

## 1. HellaSwag

### Description
HellaSwag is a commonsense reasoning benchmark that challenges models to choose the most plausible continuation of a given scenario from multiple options. It is specifically designed to test a model's ability to understand context and apply commonsense knowledge.


### Purpose
HellaSwag evaluates the model's capacity to understand context and make commonsense inferences, which are crucial for natural language understanding tasks.

### Dataset Source
The HellaSwag benchmark data was obtained from the link provided [dataset](https://github.com/klosax/hellaswag_text_data). 

## 2. MMLU (Massive Multitask Language Understanding)

### Description
MMLU is a comprehensive benchmark designed to assess a model's performance across a wide spectrum of language understanding tasks. It encompasses various domains including natural language inference, reading comprehension, and question answering.

### Purpose
MMLU assesses the model's versatility and capability to perform consistently well across different types of language understanding tasks, providing a holistic view of its linguistic competence.

### Dataset Source
The MMLU benchmark was executed using the LLM Harness tool with a limit of 50.

### Framework 
[LM Evaluation Harness ](https://github.com/EleutherAI/lm-evaluation-harness)
## 3. Winogrande

### Description
Winogrande is a benchmark for commonsense reasoning, based on the Winograd Schema Challenge. It consists of pairs of sentences that differ by only one or two words. The task is to determine which of two possible referents is more plausible in the given context.


### Purpose
Winogrande tests the model's ability to understand nuanced language and make commonsense judgments, which are essential for advanced natural language processing applications.

### Dataset Source
The Winogrande benchmark data was obtained from the link provided [dataset](https://huggingface.co/datasets/ikawrakow/winogrande-eval-for-llama.cpp/raw/main/winogrande-debiased-eval.csv) 

