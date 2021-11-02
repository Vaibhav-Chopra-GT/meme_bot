import requests


def downloadmeme():
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    # json is used for web dictionary
    link = r.json()["url"]

    p = requests.get(link)
    with open("meme.jpg", "wb") as f:
        f.write(p.content)
    return
