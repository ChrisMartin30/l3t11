# L3T11 - Compulsory Task 1

import spacy
nlp = spacy.load('en_core_web_sm')

# Create a list containing garden path sentences

gardenpathSentences = ["The Inuit can fish in their new factory in town.", 
                       "The man who hunts ducks out on weekends.",
                       "Mary gave the child the dog bit a Band-Aid.",      ### Changed from example given which lacked "the dog bit"
                       "That Jill is never here hurts.",
                       "The cotton clothing is made of grows in Mississippi."]


# Tokenise each sentence in the list and perform named entity recognition
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    for ent in nlp_sentence.ents:
        print(ent.text, ent.label_)
#  Inuit NORP    Mary PERSON    Jill PERSON    Mississippi GPE


# Tokenise each sentence in the list and perform entity recognition

for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print([token.orth_ for token in nlp_sentence if not token.is_punct | token.is_space])

    for token in nlp_sentence:
        if not token.is_punct | token.is_space:
            print(token, token.tag_, token.dep_, token.pos_)
    print()


print("dobj:",spacy.explain("dobj"))
print("pobj:",spacy.explain("pobj"))
print("nsubj:",spacy.explain("nsubj"))
print("nns:", spacy.explain("NNS"))
print("RP:", spacy.explain("RP"))
print("prt:", spacy.explain("prt"))
print("ccomp:", spacy.explain("ccomp"))
print("in:", spacy.explain("IN"))
print("mark:", spacy.explain("mark"))
print("GPE:", spacy.explain("GPE"))
print("NNP:", spacy.explain("NNP"))
print("compound:", spacy.explain("compound"))
print("nsubjpass:", spacy.explain("nsubjpass"))
print("MD:", spacy.explain("MD"))
print("PRP$:", spacy.explain("PRP$"))




# Write a comment about 2 entities you looked up.

# In the sentence "The man who hunts ducks out on weekends." I looked up what spaCy 
# categorises the "ducks" as. It classifies it as a noun, however in the sentence 
# it is being used as a verb, in that he "ducks out" or "leaves".

# In the sentence "The Inuit can fish in their new factory in town." I looked up what
# spaCy classifies "fish" as. It classifies it as a verb, presumably as it interprets 
# it to mean "the Inuit may fish". In the sentence however it is being used as a noun, 
# as in "the Inuit put fish (e.g. cod) into cans".