import rok_scraper, stack_scraper, wwr_scraper
import csv, re

db = {}

def jobs(query):
  if not db.get(query):
    result = []
    result += rok_scraper.scrape(query)
    result += stack_scraper.scrape(query)
    result += wwr_scraper.scrape(query)
    db[query] = result
  return db[query]

def export_to_csv(query):
  filename = "export_csv/" + re.sub(r'[\\/*?:"<>|]'," ", query) + ".csv" ## /export_csv won't work
  # if not os.path.exists(filename): ## skip this if exists
  file = open(filename, mode="w")
  writer = csv.writer(file)
  writer.writerow(["Title", "Company", "Link"])
  for job in db[query]:
    writer.writerow(list(job.values()))
  return filename