from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from string import punctuation

#import the positive and negative words from Bing lexicon
p_words = open('positive.txt','r')
pos_words = [line.rstrip('\n') for line in p_words]
n_words = open('negative.txt','r')
neg_words = [line.rstrip('\n') for line in n_words]

#import reviews
reviews = open('scape1.csv','r')
reviews_details =  [line.rstrip('\n') for line in reviews]
#stemming lexicon and reviews
ps = PorterStemmer()
filename="labeledDataset.csv"
f=open(filename,"w")
headers="review,label\n"
f.write(headers)
for i in range(len(reviews_details)): # strip the punctuation
    for p in list(punctuation):
        reviews_details[i] = reviews_details[i].replace(p,"")
        reviews_details[i] = reviews_details[i].replace('\n',"")


#sentiment analysis using Bing lexicon        
for sentence in reviews_details:
    words=word_tokenize(sentence)
    pos_counter = 0
    neg_counter = 0
    
    for w in words:
      #  stemReview = ps.stem(w) # stemming for reviews
        f.write(w+" ")
        if w in pos_words:
            pos_counter +=1;
        if w in neg_words:
            neg_counter +=1;
        #f.write(stemReview+",")
        
    if pos_counter>neg_counter:
       f.write(","+"positive")
    if pos_counter<=neg_counter:
       f.write(","+"negative") 
    f.write("\n")
f.close()

#for w in pos_words #stemming for positive lexicon
#    ps.stem(w)
#for w in neg_words #stemming for negative lexicon
 #   ps.stem(w)

