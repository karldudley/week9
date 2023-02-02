import spacy
nlp = spacy.load('en_core_web_sm')

# create list and strings
gardenpathSentences = []
sentence1 = "The old man the boat."
sentence2 = "The florist sent the flowers was pleased."
sentence3 = "We painted the wall with cracks."
sentence4 = "When Fred eats food gets thrown."
sentence5 = "The dog that I had really loved bones."

# append sentence to list
gardenpathSentences.append(sentence1)
gardenpathSentences.append(sentence2)
gardenpathSentences.append(sentence3)
gardenpathSentences.append(sentence4)
gardenpathSentences.append(sentence5)

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print([(token.orth_, token.pos_) for token in doc])

# use spacy.explain to understand the different entity types
print("\n", spacy.explain("DET"), spacy.explain("AUX"), spacy.explain("ADP"), spacy.explain("PROPN"), spacy.explain("ADV"))

'''
Entity 1 - Auxiliary
An auxiliary word is a verb that lacks inherent semantic meaning but instead modifies the meaning of another verb (e.g. be, can, could).

In the garden path sentence "The florist sent the flowers was pleased.", spacy marks "was" as auxiliary. This makes sense because it is being used to modify the verb "sent" in the past tense.
'''

'''
Entity 2 - Adposition
Adpositions (also known as prepositions or postpositions) are a class of words used to express spatial or temporal relations (e.g. in, under, towards, before) or mark semantic roles (e.g. of, for).

In the garden path sentence "We painted the wall with cracks.", spacy marks "with" as an adpostion. This makes sense because it is being used to spatially describe the "wall".

'''
