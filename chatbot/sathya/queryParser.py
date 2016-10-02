import nltk
import re
import time
from nltk.tree import Tree

'''
#Sample test cases
exampleArray = ['The incredibly intimidating NLP scares people away who are sissies.']


contentArray = ['What can you tell me about India?',
		'Tell me about India.',
		'Tell me about India',
		'What is the population of India',
		'What is the currency of U.S.A',
		'Who is president of China',
		'what is the area of a triangle']
'''

grammar = r"""
    	NBAR:
        	{<NN.*|JJ>*<NN.*>}  # Nouns and Adjectives, terminated with Nouns        
    	NP:
        	{<NBAR><IN><NBAR>}
        	{<NBAR>} # Above, connected with in/of/etc...
"""

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()

def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    return word

def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40)
    return accepted

def get_terms(tree):
    for leaf in leaves(tree):
        term = [ w for w,t in leaf if acceptable_word(w) ]
        yield term

def processLanguage(query):
    words = []
    try:    	
	chunker = nltk.RegexpParser(grammar)
        tokenized = nltk.word_tokenize(query)
        tagged = nltk.pos_tag(tokenized)
	print tagged
	tree = chunker.parse(tagged)
   	terms = get_terms(tree)

	for term in terms:
    	   for word in term:
        	words.append(word)
           
        return words

    except Exception, e:
        print str(e)
