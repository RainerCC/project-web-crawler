import codecs

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if(start_link == -1):
        return None, 0
    
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
                 
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            return links
        

f = codecs.open('sample-page.txt', encoding='utf-8')

page = f.read()

f.close()

print (get_all_links(page))
