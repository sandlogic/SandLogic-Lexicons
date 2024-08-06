# Nxcode-CQ-7B-orpo 

### Introduction

Nxcode-CQ-7B-orpo is a Monolithic Preference Optimization without Reference Model fine-tune of Qwen/CodeQwen1.5-7B. It has been trained on 100k samples of high-quality ranking data, making it a powerful tool for code generation and understanding.

### Performance

The model has been evaluated using EvalPlus, showing impressive results across various benchmarks:

| Benchmark | Pass@1 Score |
|-----------|--------------|
| HumanEval | 86.6         |
| HumanEval+ | 83.5        |
| MBPP (v0.2.0) | 82.3     |
| MBPP+ (v0.2.0) | 70.4    |

Original model - [Nxcode-CQ-7B-orpo](https://huggingface.co/NTQAI/Nxcode-CQ-7B-orpo)

To generate solutions, we use a simple template:

```python
"Complete the following Python function:\n{prompt}"
```

### Intended Use Cases

1. **Code Generation**: Nxcode-CQ-7B-orpo excels at generating Python code based on function descriptions or partial implementations. It can help developers quickly prototype solutions or fill in missing parts of their code.
2. **Code Completion**: The model can be used to suggest completions for partially written code, helping developers write code more efficiently.
3. **Error Understanding**: While not explicitly trained for this task, the model's deep understanding of code structures can potentially help in identifying and explaining coding errors.
4. **Programming Education**: The model can be used as a tool for learning programming, providing explanations and examples of various coding concepts and patterns.

### Evaluation of Quantized Model

 | Tasks                | Version  | Metric          |    Value |    Stderr |
 |---------------------:|---------:|-----------------:|---------:|----------:|
 | code2text_go         |        1 |  smoothed_bleu_4 |   2.7888 |    0.2845 |
 | code2text_java       |        1 | smoothed_bleu_4 |   0.4786 |    0.1314 |
 | code2text_javascript |        1 |  smoothed_bleu_4 |   4.6840 |    0.3061 |
 | code2text_php        |        1 |  smoothed_bleu_4 |   1.1990 |    0.1641 |
 | code2text_python     |        1 |  smoothed_bleu_4 |   3.7506 |    0.3094 |
 | code2text_ruby       |        3 |  smoothed_bleu_4 |   4.1161 |    0.3948 |