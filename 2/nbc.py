import numpy as np # linear algebra
import nltk
from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
import pandas as pd
from string import punctuation
from nltk.stem import PorterStemmer

data = open('stemmingReview.csv','r')
# Keeping only the neccessary columns
data_content = []
for line in data:
  line.rstrip('\n') 
  data_content.append(list(line.strip().split(',')))


p_words = open('positive_words.csv','r')
pos_words = [line.rstrip('\n') for line in p_words]
n_words = open('negative_words.csv','r')
neg_words = [line.rstrip('\n') for line in n_words]

all_words = []
all_words = nltk.FreqDist(all_words)

#word_features = list(all_words.keys())[:3000]
def feature_extraction(document):
   words = word_tokenize(document)
   words = set(words)
   pos_wordsSet=set(pos_words)
   neg_wordsSet=set(neg_words)
   features = {}
   for w in pos_wordsSet:
        features[w] = (w in words)
   for w in neg_wordsSet:
        features[w] = (w in words)
   return features

#testsets= [(content,label) for(content,label) in data_content]

featuresets = [(feature_extraction(content),label) for(content,label) in data_content]
train_set,test_set = featuresets[:4000],featuresets[4000:]
classifier = nltk.NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.accuracy(classifier,test_set)
print("the accuracy of Naive Bayes classifier is:" + str(accuracy))
classifier.show_most_informative_features(15)

