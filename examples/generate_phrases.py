from mc import PhraseGenerator
from mc.builtin import validators

text = """Markov studied Markov processes in the early 20th century, 
publishing his first paper on the topic in 1906. Markov processes in 
continuous time were discovered long before Andrey Markov's work in the early 
20th century in the form of the Poisson process. Markov was interested in 
studying an extension of independent random sequences, motivated by a disagreement 
with Pavel Nekrasov who claimed independence was necessary for the weak law of 
large numbers to hold. In his first paper on Markov chains, published in 1906, 
Markov showed that under certain conditions the average outcomes of the Markov chain
would converge to a fixed vector of values, so proving a weak law of large numbers without
the independence assumption, which had been commonly regarded as a 
requirement for such mathematical laws to hold. Markov later used Markov chains to
study the distribution of vowels in Eugene Onegin, written by Alexander Pushkin, and proved a 
central limit theorem for such chains."""  # Source: https://en.wikipedia.org/wiki/Markov_chain

samples = text.replace("\n", "").split(". ")  # Sentences of the text above
generator = PhraseGenerator(samples)
phrases = generator.generate_phrases(count=2, validators=[validators.chars_count(maximal=75)])
print(phrases)
# example output:
# >>> ['markov was interested in 1906', "in continuous time were discovered long before andrey markov's work in 1906"]
