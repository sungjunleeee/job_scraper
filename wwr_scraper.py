from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def scrape(query):
  result = []
  url = f"https://weworkremotely.com/remote-jobs/search?term={query}"
  page = requests.get(url, headers=headers)
  if not page.status_code == 200:
    print(f"Cannot scrape {query} in remote jobs")
    return
  soup = BeautifulSoup(page.text, "html.parser")
  jobs = soup.find("section", id="category-2")
  if jobs:
    jobs = jobs.findAll("li")[:-1]
    for job in jobs:
      title = job.find("span", class_="title").text
      company = job.find("span", class_="company").text
      link = "https://weworkremotely.com" + job.findAll("a")[1].get("href")
      result.append({
        "title": title,
        "company": company,
        "link": link
      })
  return result