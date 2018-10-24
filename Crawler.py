def get_next_target(content):
    start_link = content.find('<a href=')

    if start_link==-1:
        return None, 0

    start_quote = content.find('"', start_link)
    end_quote = content.find('"', start_quote+1)
    url = content[start_quote+1:end_quote]
    return url, end_quote


def print_all_links(content):
    while True:
        url, end_quote = get_next_target(content)
        if url:
            print(url)
            content = content[end_quote:]
        else:
            break


def get_page_content(url):
    import urllib.request
    return urllib.request.urlopen(url).read().decode('utf-8')


seed = 'http://w3schools.com'
print_all_links(get_page_content(seed))
