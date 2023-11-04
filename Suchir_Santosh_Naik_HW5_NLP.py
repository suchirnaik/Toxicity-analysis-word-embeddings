#To run the program please follow the following steps:
#I have entered the relative paths of all files. So please store the files in the same location as this python file
#Line 15 and line 65 are where the pretrained models are loaded. Please change the file name if you are using a different model I have shared than the default one.
# The Default pretrained model currently used is glove-twitter-25.txt 

#Loading the necessary libraries
import nltk
from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

#Defining the function
def compare_texts_w2v(file_one, file_two, k=10):
    #Loading the pretrained word2vec model
    w2v_model = KeyedVectors.load_word2vec_format('glove-twitter-25.txt', binary=False)
    #The below lines read the first CSV file into a Pandas dataframe, extract the 'comment_text' column into a list, tokenize the text into words, 
    #convert all words to lowercase, remove non-alphabetic words, and remove stop words for both the datasets.
    df_one = pd.read_csv(file_one, nrows=10000).dropna(subset=['comment_text'])
    text_one = df_one['comment_text'].tolist()
    tokens_one = [nltk.word_tokenize(text) for text in text_one]
    tokens_one = [[token.lower() for token in tokens if token.isalpha()] for tokens in tokens_one]
    tokens_one = [[token for token in tokens if token not in nltk.corpus.stopwords.words('english')] for tokens in tokens_one]
    df_two = pd.read_csv(file_two, nrows=10000).dropna(subset=['comment_text'])
    text_two = df_two['comment_text'].tolist()
    tokens_two = [nltk.word_tokenize(text) for text in text_two]
    tokens_two = [[token.lower() for token in tokens if token.isalpha()] for tokens in tokens_two]
    tokens_two = [[token for token in tokens if token not in nltk.corpus.stopwords.words('english')] for tokens in tokens_two]
    #The below lines count the frequency of all words in both lists of tokens, and extract the k most common words from each list.
    top_k_words_one = [word for word, _ in nltk.FreqDist([word for tokens in tokens_one for word in tokens]).most_common(k)]
    top_k_words_two = [word for word, _ in nltk.FreqDist([word for tokens in tokens_two for word in tokens]).most_common(k)]
    #The below lines create two lists of word embeddings, one for each CSV file, by looking up each word in the Word2Vec pretrained model.
    embeddings_one = []
    for word in top_k_words_one:
        if word in w2v_model:
            embeddings_one.append(w2v_model[word])

    embeddings_two = []
    for word in top_k_words_two:
        if word in w2v_model:
            embeddings_two.append(w2v_model[word])

    #The below line calculates the cosine similarity between the two sets of embeddings and takes the mean similarity score.
    similarity_score = cosine_similarity(embeddings_one, embeddings_two).mean()

    # Printing the summary 
    print('Comparison between {} and {}'.format(file_one, file_two))
    print('Top {} words in {}:'.format(k, file_one))
    print(top_k_words_one)
    print('Top {} words in {}:'.format(k, file_two))
    print(top_k_words_two)
    print('Similarity score based on top {} words: {:.4f}'.format(k, similarity_score))

#Calling the above function
compare_texts_w2v('toxic_comments.csv', 'non_toxic_comments.csv', k=10)
compare_texts_w2v('toxic_comments.csv', 'non_toxic_comments.csv', k=5)
compare_texts_w2v('toxic_comments.csv', 'non_toxic_comments.csv', k=20)


#importing the necessary functions
from gensim.models import KeyedVectors
import nltk

def doc_overview_w2v(text_file, k=10, n=5):
    #Loading the pretrained word2vec model
    w2v_model = KeyedVectors.load_word2vec_format('glove-twitter-25.txt', binary=False)

    # Reading the text file
    with open(text_file, 'r') as file:
        text = file.read()

    #The below lines tokenize the text into words using the NLTK library, convert all words to lowercase, and remove non-alphabetic words and stop words.
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in nltk.corpus.stopwords.words('english')]

    #The below line counts the frequency of each word in the token list, and selects the k most frequent non-stop words.
    top_k_words = [word for word, _ in nltk.FreqDist(tokens).most_common(k)]

    #The below lines create a dictionary named similar_words that maps each top word to a list n similar words. Also if a top word is not present in the Word2Vec model, it is skipped.
    similar_words = {}
    for word in top_k_words:
        if word in w2v_model:
            similar_words[word] = [similar_word for similar_word, _ in w2v_model.most_similar(word)[:n]]

    # Print the summary
    print('Document: {}'.format(text_file))
    print('Top {} frequent non-stopwords:'.format(k))
    print(top_k_words)
    print('Most similar words for each top word:')
    for word, similar in similar_words.items():
        print('{}: {}'.format(word, similar))
        
#Calling the functions       
doc_overview_w2v('world_of_war.txt', k=5, n=5)
doc_overview_w2v('on_liberty.txt', k=5, n=5)
doc_overview_w2v('kingarthur.txt', k=5, n=10)