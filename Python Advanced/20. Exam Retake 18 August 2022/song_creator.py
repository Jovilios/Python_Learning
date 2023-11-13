import os

def add_songs(*args):
    dict = {}

    for i in args:
        if i[0] not in dict:
            dict[i[0]] = i[1]
        else:
            dict[i[0]].extend(i[1])

    result = []

    for title, lyrics in dict.items():
        result.append(f"- {title}")
        if lyrics:
            result.extend(lyrics)

    return "\n".join(result)


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

