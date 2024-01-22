from flask import Flask, render_template,jsonify
app = Flask(__name__)
Jobs = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  
  {
    'id': 2,
    'title': 'Cyber Security Analyst',
    'location': 'Dubai, UAE',
    'salary': 'Dirahm. 10,000'
  },
  
  {
    'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Remote'
  },
  
  {
    'id': 4,
    'title': 'BackEnd Engineer',
    'location': 'Dehli, India',
    'salary': 'Rs. 5,00,000'
  },
]
@app.route('/')

def hello():
  return render_template('home.html',Jobs =Jobs, company_name = 'Jovian')
@app.route('/jobs')
def joblists():
  return jsonify(Jobs)

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)