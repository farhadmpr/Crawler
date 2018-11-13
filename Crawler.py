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
        res = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
    except:
        res=""
    return res


def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return []


def add_page_to_index(index, url, content):
    words=content.split()
    for word in words:
        add_to_index(index, word, url)


def union(list1, list2):
    for e in list2:
        if e not in list1:
            list1.append(e)


def lookup_best(keyword, index, ranks):
    # todo
    return


def compute_ranks(graph):
    d=0.9 #damping factor
    num_loops = 10
    num_pages = len(graph)

    ranks={}
    for page in graph:
        rank[page]= 1.0 / num_pages

    for i in range(num_loops):
        new_ranks = {}
        for page in graph:
            new_ranks = (1-d) / num_pages
            for node in graph:
                if page in graph[node]:
                    new_ranks = new_ranks + d * (ranks[node]/len(graph[node]))
            new_ranks[page] = new_ranks
        ranks=new_ranks
    return ranks


def crawl(seed="https://stackoverflow.com"):
    """
    Crawl web using Breadth-First-Search
    """
    to_crawl = [seed]
    crawled = []
    index = {}
    graph = {}
    i=0

    while to_crawl:
        url = to_crawl.pop(0)
        if url not in crawled:
            content = get_page_content(url)
            add_page_to_index(index, url, content)
            out_links = get_all_links(content)

            graph[url] = out_links


            union(to_crawl, out_links)
            #to_crawl=list(set().union(to_crawl, links))
            crawled.append(url)
            i+=1
            print(i, url)
            if len(crawled) == 30000: break
    return index, graph

crawl()
