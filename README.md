# multilingual-emotion-detection

## Overview

This project focuses on multilingual emotion detection and sentiment analysis using Natural Language Processing and Machine Learning techniques.

The main goal is to investigate whether retrieval-based example selection improves the Multilingual Emotion Evaluation and to classify various emotions like joy, happiness, surprise, fear and sadness in written text in multiple languages (German, Russian, Chinese, Greek). We compare several  multilingual emotion classification baselines, including zero-shot LLMs, few-shot prompting, fine-tuned multilingual BERT, dense retrieval with FAISS, BM25 retrieval, and reranking approaches.

## Methodology

- Preprocess multilingual datasets (Greek, Russian, German, Chinese)
- Implement a retrieval-based example selection system using multilingual-e5-base and FAISS
- Retrieve semantically similar labeled training examples for each input query
- Use retrieved strategies for Qwen3 emotion classification
- Zero-shot classification with Qwen3
- Few-shot prompting with randomly selected examples
- Fine-tuned multilingual BERT for supervised classification
- Compare dense retrieval, BM25 retrieval and reranking approaches
- Compare and evaluate multilingual classification performance across languages 

## Technologies

- Python
- PyTorch / TensorFlow
- Scikit-learn
- Pandas / NumPy
- XED Datasets (https://github.com/Helsinki-NLP/XED)
- e5-multilingual-base (https://huggingface.co/intfloat/multilingual-e5-base)
- FAISS for retrieval (https://ai.meta.com/tools/faiss/)
- Qwen3 (https://huggingface.co/collections/Qwen/qwen3)
- Sentence Transformers 

# Installation

## Prerequisities 

- Python 3.9 or higher
- Git

``

2. **Install dependencies:**
``bash
pip install --upgrade pip
pip install -r requirements.txt
pip install sentence-transformers
``

## System Architecture & RAG Pipeline

The pipeline consists of the following main components:

1. Datasets Loading 
2. Preprocessing multilingual (Greek, German, Russian, Chinese) text data.
3. Retrieval: Chunking, create embeddings, FAISS for indexing
4. LLM CLassifier: Using Qwen3 to classify the emotion of the input text.
5. Evaluation: Comparing model predictions across different languages.
6. Explainability

## Baselines

1. zero-shot LLM
  - Qwen3 predicts the emotion label without retrieved examples

2. few-shot LLM
  - Qwen3 receives randomly selected labeled examples in the prompt

3. fine-tuned Multilingual BERT
  - a supervised multilingual classifier trained directly on the emotion datasets

4. RAG-based Classification
  - the model retrieves semantically similar examples using multilingual-e5 emebddings and FAISS before classification

5. RAG + reranker
  - retrieved examples are additionally reranked before being passed to the LLM

## Evaluation & Results
We will compare the performance of  different multilingual LLMs and Retrieval strategies.
Evaluation metrics may include accuracy, precision, recall and f1-score.

....



















