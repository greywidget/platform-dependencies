from bs4 import BeautifulSoup
import re

"""See https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start
"""

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>"""

soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.prettify())

# print(soup.title)

# print(soup.title.string)

# print(soup.title.parent.name)

# print(soup.p)

# print(soup.p["class"])

# print(soup.a)

# print(soup.find_all("a"))

# print(soup.find(id="link3"))

# for link in soup.find_all("a"):
#     print(link.get("href"))

# print(soup.get_text())

# tag = soup.p
# print(type(tag))
# print(tag.name)
# print(tag["class"])
# print(tag.attrs)

# tag = soup.a
# print(tag.string)

# for item in soup.find_all("a"):
#     print(item.string)

# head_tag = soup.head
# print(head_tag)
# print(head_tag.contents)
# title_tag = head_tag.contents[0]
# print(title_tag.contents)

# for child in title_tag.children:
# print(child)

# for child in head_tag.descendants:
# print(child)

# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

# print(list(soup.children))

# for string in soup.strings:
#     print(repr(string))

# for string in soup.stripped_strings:
#     print(repr(string))

# title_tag = soup.title
# print(title_tag)
# print(title_tag.parent)
# print(title_tag.string)
# print(title_tag.string.parent)

# link = soup.a
# print(link)

# for parent in link.parents:
#     print(parent.name)

# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", "html.parser")
# print(sibling_soup.prettify())
# print(sibling_soup.b.next_sibling)
# print(sibling_soup.c.previous_sibling)

# print(soup.a)
# temp = soup.a.next_sibling
# print(temp)
# temp = temp.next_sibling
# print(temp)

# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# for sibling in soup.find(id="link3").previous_siblings:
#     print(sibling)

# last_a_tag = soup.find("a", id="link3")
# print(repr(last_a_tag))
# print(repr(last_a_tag.next_sibling))
# print(last_a_tag.next_element)
# print(repr(last_a_tag.previous_element))
# print(last_a_tag.previous_element.next_element)
# print()
# for element in last_a_tag.next_elements:
#     print(repr(element))

# print(soup.find_all("b"))
# print()
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)
# print()
# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)

# for item in soup.find_all(["a", "b"]):
#     print(item)

# for tag in soup.find_all(True):
#     print(tag.name)


def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")


items = soup.find_all(has_class_but_no_id)
for item in items:
    print(item)
