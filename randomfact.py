

def paragraphs(parsefile):
    f = open(parsefile, 'r')

    facts = f.read()

    return facts.split("\n\n")
    

def randomfact(factfile):
    facts = paragraphs(factfile)
    length = len(facts)

    import random
    randfact = random.randrange(0,length)

    return facts[randfact]


