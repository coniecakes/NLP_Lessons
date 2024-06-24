import nltk
import io

sent1 = 'He invited near and dear to attend the party.'
tok1 = nltk.word_tokenize(sent1)
tagged_tok1 = nltk.pos_tag(tok1)
print (tagged_tok1)

sent2 = 'Come near and listen.'
tok2 = nltk.word_tokenize(sent2)
tagged_tok2 = nltk.pos_tag(tok2)
print (tagged_tok2)

sent3 = 'He went near and explained.'
tok3 = nltk.word_tokenize(sent3)
tagged_tok3 = nltk.pos_tag(tok3)
print (tagged_tok3)

sent4 = 'She is my near relation.'
tok4 = nltk.word_tokenize(sent4)
tagged_tok4 = nltk.pos_tag(tok4)
print (tagged_tok4)


# CC: conjunction, coordinating
# FW: foreign word
# IN: preposition or conjunction, subordinating
# JJ: adjective or numeral, ordinal
# NN: noun, common, singular or mass
# NNP: noun, proper, singular
# NNPS: noun, proper, plural
# NNS: noun, common, plural
# PRP: pronoun, personal
# RB: adverb
# VB: verb, base form
# VBD: verb, past tense