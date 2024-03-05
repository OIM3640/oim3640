# Build your own bitly (URL shortening) service
# 'www.babson.edu' -> 't3trfe' (a random string)
# 'www.google.com' -> 'gdst45'

import random
import string


url_to_short = {}
short_to_url = {}


def shorten_url(url):
    """convert the original url to a shorter url, return the short url"""
    if url in url_to_short:
        return url_to_short[url]
    else:
        availables = string.ascii_letters + string.digits
        short = "".join(random.choices(availables, k=6))
        url_to_short[url] = short
        short_to_url[short] = url
        return short


original = "www.babson.edu"
short_url = shorten_url(original)

print("bit.ly\\" + short_url)
print("bit.ly\\" + shorten_url(original))

print(short_to_url[short_url])
