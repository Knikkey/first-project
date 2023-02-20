q_words = ("who", "what", "when", "where", "why", "how")


def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    if phrase.startswith(q_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
