# Retrieval Notes

Goal of the project : It investigates retrieval-based example selection for multilingual emotion classification

## Dataset

We use the XED annotated dataset because all languages for our project are inluded.

Languages: Greek, Russian, German, Chinese

## Chunking 

In XED 1 chunk = 1 sentence

## Embeddings

We use multilingual-e5-base at the prototype retrieving part because its easy to handle with and we will change to multilingual-e5-large

- multilingual embeddings
- support all four languages

## Retrieval

- FAISS : dense semantic similarity search between embeddings
- bm25: lexical similarity search in tokens

## planned pipelines

Text -> sentence chunks -> Embeddings -> FAISS Index -> similarity retrieval
Text -> sentence chunks -> tokens -> bm25 -> lexical retrieval

## Current progress

So far, we have implemented the first retrieval prototype:

1. Loaded the Greek, Russian, German and Chinese XED dataset
2. Applied basic preprocessing only for the Greek one (to explore how it works)
3. Used sentence-level chunking for both FAISS and bm25
4. Loaded the e5-multilingual-base (https://huggingface.co/intfloat/multilingual-e5-base)
5. Generated dense embeddings for the first 1000 Greek chunks (sentences).  
6. Implemented semantic retrieval using FAISS (https://ai.meta.com/tools/faiss/). FAISS uses mathematical shortcuts, clustering, 
   and advanced indexing to filter the search space and retrieve nearest neighbors in milliseconds. 
7. Implemented lexical retrieval using BM25 (it takes tokens/words, not embeddings)  
8. Queries in Greek: query_1 for joy, query_2 for sadness
9. Scores for the top 5


## To do

1. Same procedure for all languages
2. The emotion labels are available in XED dataset, but they are still not integrated into the retrieval pipelines.
3. The prototype currently uses only 1000 examples from the Greek dataset for testing.
4. Compare FAISS semantic retrieval with bm25 lexical retrieval
5. Test cross-lingual semantic retrieval.
6. Use only the train split for the retrieval index.
7. No retrieval evaluation has been done.
8. Future evaluation of retrieval quality using ndcg metric. It measures how good a ranking is by considering both the relevance and position.
   or label overlap@k

## Citation

@article{muhammad2025brighterbridginggaphumanannotated,
  title = {BRIGHTER: BRIdging the Gap in Human-Annotated Textual Emotion Recognition Datasets for 28 Languages},
  author = {Muhammad, Shamsuddeen Hassan and Ousidhoum, Nedjma and Abdulmumin, Idris and Wahle, Jan Philip and Ruas, Terry and Beloucif, Meriem and de Kock, Christine and Surange, Nirmal and Teodorescu, Daniela and Ahmad, Ibrahim Said and Adelani, David Ifeoluwa and Aji, Alham Fikri and Ali, Felermino D. M. A. and Alimova, Ilseyar and Araujo, Vladimir and Babakov, Nikolay and Baes, Naomi and Bucur, Ana-Maria and Bukula, Andiswa and Cao, Guanqun and Cardenas, Rodrigo Tufino and Chevi, Rendi and Chukwuneke, Chiamaka Ijeoma and Ciobotaru, Alexandra and Dementieva, Daryna and Gadanya, Murja Sani and Geislinger, Robert and Gipp, Bela and Hourrane, Oumaima and Ignat, Oana and Lawan, Falalu Ibrahim and Mabuya, Rooweither and Mahendra, Rahmad and Marivate, Vukosi and Piper, Andrew and Panchenko, Alexander and Porto Ferreira, Charles Henrique and Protasov, Vitaly and Rutunda, Samuel and Shrivastava, Manish and Udrea, Aura Cristina and Wanzare, Lilian Diana Awuor and Wu, Sophie and Wunderlich, Florian Valentin and Zhafran, Hanif Muhammad and Zhang, Tianhui and Zhou, Yi and Mohammad, Saif M.},
  journal = {arXiv preprint arXiv:2502.11926},
  year = {2025}
}

## Work done but not in the last version included

1. Dataset XED loaded
2. Prototype Retrieval with Greek implemented
3. Greek will not be used in the project because we did not find a good one dataset






