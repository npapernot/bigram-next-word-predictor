# bigram-next-word-predictor
A simple bigram next word predictor implemented in Python. The predictor is
composed of two functions. The first function `build_conditional_probabilities`
takes as an input a corpus and returns a dictionnary of conditional 
probabilities by bigram. The second function `bigram_next_word_predictor`
takes the dictionnary built by the first function along with a current word
`current` and a next word candidate `next_candidate` and returns the
conditional probability of reading the next word candidate knowing that we are
reading the current word, according to the model learned on the corpus.  


