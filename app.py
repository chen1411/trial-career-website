from flask import Flask, render_template, jsonify

app = Flask(__name__)

#a list of dictionaries
JOBS=[
  {
    'ID': 1,
    'Title': 'Data Analyst',
    'Location': 'Raffles, Singapore',
    'Salary': '$4500'
  },
    {
    'ID': 2,
    'Title': 'Data Scientist',
    'Location': 'Raffles, Singapore',
    'Salary': '$6000'
  },
    {
    'ID': 3,
    'Title': 'BE Developer',
    'Location': 'Raffles, Singapore',
    'Salary': '$6000'
  }
  
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, developer='Peilin')

#create the first API route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)