#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]

def NextWordProbability(sampletext, word):
    from collections import Counter
    counter = Counter()
    words = sampletext.split(' ')
    for w in range(len(words) - 1):
        if words[w] == word:
            counter[words[w + 1]] += 1
    return counter

def LaterWords(sample, word, distance):
    '''
    @param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    word1_counter = NextWordProbability(sample, word)

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    total = len(word1_counter)
    from collections import defaultdict
    word2_probs = defaultdict(list)

    for word1, word1_count in word1_counter.items():
        word1_prob = word1_count / float(total)
        word2counter = NextWordProbability(sample, word1)
        for word2, word2_count in word2counter.items():
            word2_prob = word1_prob * word2_count
            word2_probs[word2].append(word2_prob)

    max_value = -1
    max_word = None

    for word2, probabilities in word2_probs.items():
        prob = reduce(lambda x, y: x * y, probabilities)
        if prob > max_value:
            max_word = word2
            max_value = prob
    
    return max_word
    
print LaterWords(sample_memo, "ahead", 2)
