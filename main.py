"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, redirect, send_file
import job_scraper

app = Flask("Job Scraper")

@app.route("/")
def home():
  return render_template("main.html")

@app.route("/detail")
def detail():
  query = request.args.get("query")
  if not query:
    return redirect("/")
  jobs = job_scraper.jobs(query.lower())
  return render_template("detail.html",
                          query=query.lower(),
                          jobs=jobs)

@app.route("/export/<query>")
def export(query):
  filename = job_scraper.export_to_csv(query.lower())
  return send_file(filename, as_attachment=True)

app.run(host="0.0.0.0")