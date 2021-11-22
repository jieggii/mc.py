import mc

generator = mc.PhraseGenerator(samples=["hello world", "world of cuties"])


def my_formatter(string: str) -> str:
    return string.replace("e", "3")


phrase = generator.generate_phrase(formatters=[my_formatter])
print(phrase)
# example output: >>> "h3llo world of cuti3s"

phrase = generator.generate_phrase(
    formatters=[lambda string: string.replace("o", "0")]
)  # formats generated phrase like a usual sentence and replaces "o" with "0"
print(phrase)
# example output: >>> "Hell0 w0rld."
