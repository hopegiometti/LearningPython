# print("Say Something:")

# def say_something(s):
#     all = []
#     if s == "\end":
#         print(all)
#     else:
#         print("Say Something:")
#         all.append(s)

# say_something()

def sentence_maker(phrase):
    q_words = ("how", "what", "when", "where", "who")
    capitalized = phrase.capitalize()

    if phrase.startswith(q_words):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


