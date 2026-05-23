# multilingual-emotion-detection

## Gruppenname

RAGTag Crew

## Team Members

- Katharina Maier
- Kristina Terekhova
- Evanthia Tsigkana
- Jingyi Wang

## Overview

This project focuses on multilingual emotion detection and sentiment analysis using Natural Language Processing and Machine Learning techniques.

The goal is to build a Retrieval-Augmented Generation (RAG) system to classify various emotions like joy, happiness, surprise, fear and sadness in written text in multiple languages (German, Russian, Chinese, Greek) and compare the performance of different models and retrievals. 

## Methodology

- Preprocessing multilingual text databases (Greek, Russian, German, Chinese) annotated by humans 
- Implement a retrieval system based on multilingual-e5-base 
- Explore different emotion classification techniques
- Train and evaluate deep learning models
- Compare model performance across languages 

## Technologies

- Python
- PyTorch / TensorFlow
- Scikit-learn
- Pandas / NumPy
- Hugging Face Transformers 
- XED Datasets
- e5-multilingual-base (Hugging Face)
- FAISS for retrieval
- Qwen3
- Sentence Transformers

# Installation

## Prerequisities 

- Python 3.9 or higher
- Git

## Setup Instructions

1. **Clone the repository:**
``bash
git clone https://lrz.de

cd multilingual-emotion-detection
``

2. **Install dependencies:**
``bash
pip install --upgrade pip
pip install -r requirements.txt
``

## System Architecture & RAG Pipeline

The pipeline consists of the following main components:

1. Document Loading: Preprocessing multilingual (Greek, German, Russian, Chinese) text data.
2. Vector Database: Storing text embeddings for fast similarity search.
3. Retrieval: Chunking, create embeddings, FAISS for indexing
4. LLM CLassifier: Using Qwen3 to classify the emotion of the input text.
5. Evaluation: Comparing model predictions across different languages.
6. Explainability

## Evaluation & Results
We will compare the performance of  different multilingual LLMs and Retrieval strategies.
Evaluation metrics may include accuracy, precision, recall and f1-score.

....



















