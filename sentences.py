"""
Author: Vitor Hugo Santos de Freitas

04 Prove Assignment: Writing Functions

"""


import random

# Lists of words
determiners = ["One", "Some", "A", "The"]
nouns = ["girl", "child", "bird", "dog", "rabbit", "car", "cats", "boys", "children", "birds"]
verbs = ["talked", "drinks", "will run", "laugh", "drank", "will talk", "ate", "grew"]
prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

def get_determiner():
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == "single":
        return random.choice(nouns)
    else:
        return random.choice(nouns) + "s"

def get_verb(tense):
    return random.choice(verbs)

def get_preposition():
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

def make_sentence():
    quantity = random.choice(["single", "plural"])
    tense = random.choice(["past", "present", "future"])
    
    determiner = get_determiner()
    noun = get_noun(quantity)
    verb = get_verb(tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
    return sentence

def main():
    for _ in range(6):
        sentence = make_sentence()
        print(sentence)

if __name__ == "__main__":
    main()
