import spacy

# working with vectors
nlp = spacy.load('en_core_web_md')

word1 = nlp("woman")
word2 = nlp("man")
word3 = nlp("funny")

print(word1.similarity(word2))
print(word2.similarity(word3))
print(word1.similarity(word3))
print()
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print()

# working with sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
What I found interesting about the similarities between cat, monkey and banana
- 'cat' similarity with 'apple' is 0.20
- 'cat' similarity with 'banana' is 0.22
- Only a slight difference but I think the association of 'banana' and 'monkey' maybe raises the association of 'banana' with all other animals.
- A similar thing happens in my tests below. Mario is a Nintendo character so I'd expect a fairly high similarity. But Mario is also highly associated with Playstation even though he has never appeared on that console.

My own examples
- When comparing two words using similarity, it doesn't matter which word goes first, you get the same results
- The words woman and pink have a 70% higher similarity than man and pink
- The words woman and blue have a slightly lower similarity than man and blue
- 'Woman' has a higher similarity with 'work' and 'children'
- 'Man' has a higher similarity with 'money' and 'funny'
- 'Nintendo' is much more associated with 'videogames' than 'sony' and 'microsoft'
- 'Nintendo' is only slightly more associcated with 'videogames' than 'playstation'
- 'Mario' has a 0.43 similarity with 'Nintendo', 0.26 with 'Sony' and 0.05 with 'Xbox'

When running example.py with 'en_core_web_sm' instead of 'en_core_web_md':
- I get a warning message each time I tried to compare. It said the model I was using had no vectors loaded, so the results are based on only the tagger, parser and NER, which may not give useful similarity judgements
- The similarity when using 'SM' are a lot lower than when using 'MD'
'''
