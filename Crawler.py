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


def get_all_links(content):
    """
    Takes the content of a web page and
    returns all of its links in a list.
    """
    links=[]
    while True:
        url, end_quote = get_next_target(content)
        if url:
            links.append(url)
            content = content[end_quote:]
        else:
            break
    return links


def get_page_content(url):
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
    except:
        res=""
    return res


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0]==keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])

def lookup(index, keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

    
def crawl(seed="https://www.wikipedia.org"):
    """
    Crawl web using Breadth-First-Search
    """
    to_crawl = [seed]
    crawled = []
    while to_crawl:
        url = to_crawl.pop(0)
        if url not in crawled:
            links = get_all_links(get_page_content(url))
            #union(to_crawl, links)
            to_crawl=list(set().union(to_crawl, links))
            crawled.append(url)
            print(url)
            if len(crawled) == 3000: break
    return crawled

crawl()
