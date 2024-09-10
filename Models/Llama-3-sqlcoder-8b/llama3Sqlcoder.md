## Llama-3-sqlcoder-8b

## Overview

We've quantized the llama-3-sqlcoder-8b model, a powerful text-to-SQL generator, into Q5_KM and Q4_KM variants for improved efficiency.

## Original Model

- **Name**: llama-3-sqlcoder-8b
- **Developer**: Defog, Inc.
- **Type**: Text-to-SQL
- **Base Model**: Meta-Llama-3-8B-Instruct
- **License**: CC-by-SA-4.0

## Capabilities

Generates SQL queries for Postgres, Redshift, and Snowflake databases from natural language questions.

## Prompt

```
<|begin_of_text|><|start_header_id|>user<|end_header_id|>
Generate a SQL query to answer this question: {user_question}
{instructions}
DDL statements:
{create_table_statements}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
The following SQL query best answers the question {user_question}:
```

## Intended Use

1. SQL query generation
2. Database interaction assistance
3. Data analysis support
4. SQL education