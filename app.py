from flask import Flask, render_template, jsonify
from database import load_jobs_db

app = Flask(__name__)

#a list of dictionaries



@app.route("/")
def hello_world():
  jobs= load_jobs_db()
  return render_template('home.html', jobs=jobs, developer='Peilin')

#create the first API route
@app.route("/api/jobs")
def list_jobs():
  jobs= load_jobs_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)