import requests
import random


x = random.randrange(2, 27, 1)


def downloadmeme():

    # json is used for web dictionary
    r = requests.get(
        "https://www.reddit.com/r/memes.json", headers={"User-agent": "your bot 0.1"}
    )

    link = r.json()["data"]["children"][x]["data"]["url"]

    p = requests.get(link)
    with open("meme.jpg", "wb") as f:
        f.write(p.content)

    return
