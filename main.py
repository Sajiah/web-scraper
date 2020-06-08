from bs4 import BeautifulSoup
import requests

search = input("Enter Search Term:")
params = {"q": search}
print(params)

# Requests is a python http library
r = requests.get("https://www.bing.com/search", params=params)
print(r.url)

# Beautiful soup is a python library that pulls out data from HTML and XML files
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
print(results)
links = results.findAll("li", {"class": "b_algo"})
print(links)
# List of the items found from the results
for item in links:
    # This simply gets the text of it
    item_text = item.find("a").text
    # This gets the attribute for ex background color or href of the element
    item_href = item.find("a").attrs["href"]
    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Summary:", item.find("a").parent.parent.find("p").text)
        children = item.children
        for child in children:
            print("Child: ", child)

        # Get Sibling of h2
        sibling = item.find("h2")
        print("Next sibling of h2 is:", sibling.next_sibling)


