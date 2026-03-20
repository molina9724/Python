import requests, bs4

res = requests.get("https://autbor.com/example3.html")
res.raise_for_status()
example_soup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(example_soup))

elems = example_soup.select("#author")
print(len(elems))
print(str(elems))
print(elems[0].get_text())
print(elems[0].attrs)

p_elemes = example_soup.select("p")
for index, element in enumerate(p_elemes):
    print(element.text)

span_elem = example_soup.select("span")
print(span_elem[0])
print(span_elem[0].get("id"))
