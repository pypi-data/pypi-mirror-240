def check(link):
    url = link
    headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'} # User-Agent Can Be Changed To Whatever You Like
    response= requests.get(url.strip(), headers=headers, timeout=5)