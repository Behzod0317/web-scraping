import requests
from bs4 import BeautifulSoup
import pandas as pd

all_in_ones  = []
for page_number in range(0, 100, 20):
    url = f"https://stadion.uz/news/pages/{page_number}"

    req = requests.get(url=url)
    soup = BeautifulSoup(req.content, "html.parser")


    all_item = soup.find_all("h1", class_="newstitle")
    item_images = soup.find_all("img", id="news_img")
    

    for i in zip(all_item, item_images):
        link = i[0].a.get("href")
        title = i[0].text
        image = i[1].get("src")

        all_in_ones.append([title, link, image])

def get_data(link):
  reqs = requests.get(link)
  soup = BeautifulSoup(reqs.content, "html.parser")
  try:
    title = soup.find("h1", class_ = "newstitle").text
    image = soup.find("img", id = "news_img").get('src')
    content = soup.find("div", id = "news_container").text
  except:
    title, image, content = None, None, None
  print(title)
  return [title, image, content]

all_data = []
for page in all_in_ones:
  all_data.append(get_data(page[1]))


columns = ['Sarlavha', "Rasm manzili", "Yangilik matni"]

df = pd.DataFrame(data=all_data, columns=columns)
print(df)