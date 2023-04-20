import random

nouns = ['betoneuse', 'zehno','chien', 'oiseau', 'poisson','patate douce','pot de yaourt','bus']
verbs = ['mange', 'court', 'vole', 'nage','tape','se regale','vend','rentre','se la foudroie', 'se la racle']
articles = ['le', 'la', 'un', 'une','des','avec un','ce bon vieux','sans le','dans']

def generate_subject():
    return random.choice(articles) + " " + random.choice(nouns)

def generate_verb():
    return random.choice(verbs)

def generate_object():
    return random.choice(articles) + " " + random.choice(nouns)


def generate_sentence():
    subject = generate_subject()
    verb = generate_verb()
    obj = generate_object()
    return subject + " " + verb + " " + obj + "."


print(generate_sentence())

