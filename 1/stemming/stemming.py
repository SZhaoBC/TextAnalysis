from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
p_words = open('positive.txt','r')
pos_words = [line.rstrip('\n') for line in p_words]
n_words = open('negative.txt','r')
neg_words = [line.rstrip('\n') for line in n_words]
data = open('labeledDataset.csv','r')
data_content = []
for line in data:
  line.rstrip('\n') 
  data_content.append(list(line.strip().split(',')))

#stemming for positive lexicon
filename="positive_words.csv"
f=open(filename,"w")
for w in pos_words: 
  f.write(ps.stem(w)+"\n")
f.close()
#stemming for negative lexicon
filename="negative_words.csv"
f=open(filename,"w")
for w in neg_words: 
    f.write(ps.stem(w)+"\n")
f.close()

filename = "stemmingReview.csv"
f=open(filename,"w")
for(content,label) in data_content:
    contentWords = word_tokenize(content)
    for w in contentWords:
        f.write(ps.stem(w).lower()+" ")
    f.write(",")    
    f.write(label+"\n")
print(ps.stem(content))
print(ps.stem("did"))
f.close()
