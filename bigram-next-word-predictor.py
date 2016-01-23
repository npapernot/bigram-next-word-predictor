from collections import defaultdict

def build_conditional_probabilities(corpus):
	"""
	The function takes as its input a corpus string (words separated by 
	spaces) and returns a 2D dictionnary of probabilities P(next|current) of
	seeing a word "next" conditionnaly to seeing a word "current". 
	"""

	# First we parse the string to build a double dimension dictionnary that
	# returns the conditional probabilities.

	# We parse the string to build a first dictionnary indicating for each
	# word, what are the words that follow it in the string. Repeated next
	# words are kept so we use a list and not a set. 

	tokenized_string = corpus.split()
	previous_word = ""
	dictionnary = defaultdict(list)

	for current_word in tokenized_string:
		if previous_word != "":
			dictionnary[previous_word].append(current_word)
		previous_word = current_word
		
	# We know parse dictionnary to compute the probability each observed
	# next word for each word in the dictionnary. 

	for key in dictionnary.keys():
		next_words = dictionnary[key]
		unique_words = set(next_words) # removes duplicated
		nb_words = len(next_words)
		probabilities_given_key = {}
		for unique_word in unique_words:
			probabilities_given_key[unique_word] = \
				float(next_words.count(unique_word)) / nb_words
		dictionnary[key] = probabilities_given_key

	return dictionnary


def bigram_next_word_predictor(conditional_probabilities, current, next_candidate):
	"""
	The function takes as its input a 2D dictionnary of probabilities 
	P(next|current) of seeing a word "next" conditionnaly to seeing a word 
	"current", the current word being read, and a next candidate word, and
	returns P(next_candidate|current).
	"""

	# We look for the probability corresponding to the 
	# current -> next_candidate pair

	if conditional_probabilities.has_key(current):
		if conditional_probabilities[current].has_key(next_candidate):
			return conditional_probabilities[current][next_candidate]

	# If current -> next_candidate pair has not been observed in the corpus,
	# the corresponding dictionnary keys will not be defined. We return 
	# a probability 0.0

	return 0.0

# An example corpus to try out the function
corpus = "the cat is red the cat is green the cat is blue the dog is brown"

# We call the conditional probability dictionnary builder function
conditional_probabilities = build_conditional_probabilities(corpus)

# Some sample queries to the bigram predictor
assert bigram_next_word_predictor(conditional_probabilities, "the", "cat") == 0.75
assert bigram_next_word_predictor(conditional_probabilities, "is", "red") == 0.25
assert bigram_next_word_predictor(conditional_probabilities, "", "red") == 0.0

