from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def scrape(query):
  result = []
  url = f"https://stackoverflow.com/jobs?r=true&q={query}"
  page = requests.get(url, headers=headers)
  if not page.status_code == 200:
    print(f"Cannot scrape {query} in remote jobs")
    return
  soup = BeautifulSoup(page.text, "html.parser")
  number_of_jobs = int(soup.select("span.description.fc-light.fs-body1")[0].text.strip()[:-4])
  if number_of_jobs > 0:
    jobs = soup.find("div", class_="listResults").findAll("div", class_="js-result", recursive=False)
    for block in jobs:
      job = block.findAll("div", class_="grid")[1].find("div", class_="fl1")
      title = job.find("h2").text
      company = job.find("h3").find("span").text
      link = "https://stackoverflow.com" + job.find("h2").find("a").get("href")
      result.append({
        "title": title,
        "company": company,
        "link": link
      })
  return result