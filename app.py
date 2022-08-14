import os
import urllib.request

if __name__ == "__main__":

    try:
        url = input("Enter the Spotify URL of a playlist, album, artist page or podcast:\n")
        r = urllib.request.urlopen(url).read().decode("utf-8")

        img = r.split("<meta property=\"og:image\" content=\"")[1].split("\"")[0]
        uri = r.split("<meta property=\"og:url\" content=\"https://open.spotify.com/")[1].split("/")[1].split("\"")[0]
        title = r.split("<meta property=\"og:title\" content=\"")[1].split("\"")[0]

        dir = os.path.abspath(__file__ + "/../arts/")

        if not os.path.exists(dir):
            os.mkdir(dir)

        urllib.request.urlretrieve(img, f"{dir}/{uri}.jpg")

        print(f"{title} cover art downloaded successfully!")

    except:
        print("Invalid input")