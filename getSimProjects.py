import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities
from nltk.corpus import stopwords


stoplist = stopwords.words('english')

#Creates the dictionary from the readme file
#This texts pre-processing only involves removing some common words in languages which carries little information
#May need to add some other tweaks to improve the data quality 
def getDict(f): 
    # f is the pickle file from which we are going to create the dictionary
    dictionary = corpora.Dictionary(line.lower().split() for line in f)
    # remove stop words and words that appear only once
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                if stopword in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)  # remove stop words
    dictionary.compactify()
    return dictionary
# Transform the corpus into bow format    
def getBOW(dictionary, f):
    # f is the pickle file from which we are going to create the bow representation of the corpus
    corpus=[];
    corpus=[dictionary.doc2bow(line.lower().split()) for line in f]
             
    return corpus

dictionary = getDict(f)
corpusBOW = getBOW(dictionary, f)
corpusTfidf = models.TfidfModel(corpusBOW) # Train the tfidf model
index = similarities.SparseMatrixSimilarity(tfidf[corpusBOW], num_features=12)

testQuery="hello world"
testQueryBow = dictionary.doc2bow(testQuery.lower().split())
testQueryTfidf = corpusTfidf[testQueryBow]
sims = index[testQueryTfidf]
print(list(enumerate(sims)))
