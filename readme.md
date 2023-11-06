## Author: Suchir Naik

## Overview
Welcome to my personal project where I explore Word2Vec embeddings and their practical applications. In this endeavor, I will be working with a toxic comment dataset, a document from a previous assignment (HW1), and two additional documents. The key tool at my disposal is the Gensim package, which is a versatile framework for working with Word2Vec embeddings.

### Useful Python Packages
- Gensim: [Gensim Documentation](https://radimrehurek.com/gensim/models/word2vec.html)
- Gensim Pretrained Word2Vec Embeddings: [Pretrained Models](https://radimrehurek.com/gensim/models/word2vec.html#pretrained-models)

### Dataset
The dataset I'm using for this project is the same toxic comment dataset employed in previous assignments (HW3-4). This dataset contains toxic comments, so it's essential to exercise caution when working with it. You can access both the training and test sets [here](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data).

For Word2Vec tasks, I will be focusing on the toxic label (toxic=1 or 0).

## Word2Vec Tasks
The primary objective of this project is to delve into Word2Vec embeddings and explore their practical applications. It's important to note that I'll be using pretrained embeddings and not training my own Word2Vec models.

### compare_texts_w2v(file_one, file_two, k = 10)
This function serves to compare two datasets at the word level using Word2Vec embeddings. It identifies the k most common non-stop words in each file and calculates their similarity. This comparison will be based on the top k words and their similarity scores, leveraging cosine similarity.

### doc_overview_w2v(text_file, k=10, n=5)
This function aims to provide a summary of the top k words and their nearest neighbors for a given document using Word2Vec embeddings. It will identify similar words for each of the top k words and present an overview within my report.

## Task Calls
To demonstrate the tasks, I will make the following function calls:

- `compare_texts_word2vec(NOT_TOXIC_subset, TOXIC_subset, k = 5)`
- `compare_texts_word2vec(NOT_TOXIC_subset, TOXIC_subset, k = 10)`
- `compare_texts_word2vec(NOT_TOXIC_subset, TOXIC_subset, k = 20)`

I will create the subset files manually as the Word2Vec function does not generate them automatically.

The document overviews will be called as follows:

- `doc_overview_w2v("warofworlds.txt", k = 5, n = 5)`
- `doc_overview_w2v("on_liberty.txt", k = 5, n = 5)`
- `doc_overview_w2v("kingarthur.txt", k = 5, n = 10)`

