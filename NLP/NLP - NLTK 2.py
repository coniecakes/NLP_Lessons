from nltk.book import text6, text3, text1, text2, text4

#let us search the text for every occurrence of a given word, together with some context.
print()
print ("Showing all CONCORDANCE for a word")
text3.concordance('King')
print()
# text6.concordance('swallow')

# # #find other words which appear in the same contexts as the specified word; list most similar words first
text6.similar('King')
print ('The Book of Genesis')
print ("\nShowing all words that are found in similar contxt as the given word\n")
text6.similar('Bridge')
print()
# # #
# # #have some fun - allow nltk to build a paragraph from the text using words selected at random
# # print ("\nShowing paragraph from words selected by NLTK\n")
text6.generate()
# # #
# # #how a word is dispersed in the text
# text3.dispersion_plot(['God'])