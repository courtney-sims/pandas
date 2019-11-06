""" Parses a file of paragraphs and returns a paragraph at random.
    This app uses these functions to display random facts about pandas.
    Panda facts available in the data folder."""

def paragraphs(parsefile):
    """Turns a file of text into a paragraph-separated list."""
    f = open(parsefile, 'r')

    facts = f.read()

    f.close()

    return facts.split("\n\n")

def randomfact(factfile):
    """Returns a random element from a list."""
    facts = paragraphs(factfile)
    length = len(facts)

    import random
    randfact = random.randrange(0, length)

    return facts[randfact]
