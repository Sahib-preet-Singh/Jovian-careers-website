from flask import Flask, render_template, jsonify
app=Flask(__name__)
JOBS=[{
      'id':1,
      'title': 'Data Analyst',
      'Location':'Bangaluru',
      'Salary':  '1000000'
      },
      {
      'id':2,
      'title': 'Data Scientist',
      'Location':'Chennai',
      'Salary':  '1200000'
      },
      {
      'id':3,
      'title': 'Data Engineer',
      'Location':'Mumbai',
      },
      {
      'id':4,
      'title': 'Software Developer',
      'Location':'Delhi',
      'Salary':  '900000'
      } 
    ]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs") 
def list_jobs():
  return jsonify(JOBS)

if __name__=='__main__':
   app.run(host='0.0.0.0',debug=True)