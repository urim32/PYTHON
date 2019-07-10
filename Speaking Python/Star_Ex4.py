quote = "some people drink from the fountain of knowledge, others just gargle."
VOWELS = "aeiou"

my_list = [i for i, c in enumerate(quote) if c in VOWELS]

print(my_list)
