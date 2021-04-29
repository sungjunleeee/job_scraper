from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def scrape(query):
  result = []
  url = f"https://remoteok.io/remote-{query}-jobs"
  page = requests.get(url, headers=headers)
  if not page.status_code == 200:
    print(f"Cannot scrape {query} in remote jobs")
    return
  soup = BeautifulSoup(page.text, "html.parser")
  # table = soup.find("table", id="jobsboard")
  jobs = soup.findAll("tr", class_="job")
  for job in jobs:
    title = job.find("h2", itemprop="title").text
    company = job.find("h3", itemprop="name").text
    link = "https://remoteok.io" + job.find("a", class_="preventLink").get("href")
    result.append({
      "title": title,
      "company": company,
      "link": link
    })
  return result