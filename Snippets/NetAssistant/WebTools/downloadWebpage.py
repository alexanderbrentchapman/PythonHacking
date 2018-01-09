import urllib


def download_webpage(url, save_name):
    urllib.request.urlretrieve(url=url, filename=save_name)