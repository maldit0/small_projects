import re

from Glossary import Glossary

url_1 = 'https://runestone.academy/runestone/books/published/thinkcspy/'


def get_href(href):
    return href and re.compile("Glossary").search(href)


def get_links(soup):
    soup_href = soup.find_all(href=get_href)
    urls = [(url_1 + str(x).split('"')[3]) for x in soup_href]
    return urls


def main():
    g = Glossary(url_1 + "index.html")
    urls = get_links(g.soup)

    list_content = [Glossary(url) for url in urls]

    with open('prueba.txt', 'w') as t:
        for n, each in enumerate(list_content):
            each.fix_content()
            t.write(str(n) + '.-' + each.title + '\n')
            t.write(each.content)


if __name__ == '__main__':
    main()
