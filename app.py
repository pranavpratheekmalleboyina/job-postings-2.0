from flask import Flask,render_template,jsonify
import database
from sqlalchemy import text 
app = Flask(__name__)

""" JOBS = [
    {'id': 1, 'title': 'Software Engineer', 'company': 'XYZ Corp.', 'location': 'New York','salary':'$450000'},
    {'id': 2, 'title': 'Data Scientist', 'company': 'ABC Inc.', 'location': 'San Francisco','salary':'$350000'},
    {'id': 3, 'title': 'Product Manager', 'company': 'PQR LTD.', 'location': 'London','salary':'$250000'},
    {'id': 4, 'title': 'Backend Engineer', 'company': 'Facebook', 'location': 'Boston','salary':'$650000'}
] 
 """  

@app.route('/')
def hello_world():
    jobs = database.load_jobs_from_db()
    return render_template('home.html',jobs=jobs,company_name='Pranav Consultancy')

@app.route('/api/jobs')
def list_jobs():
    jobs = database.load_jobs_from_db()
    return jsonify(jobs)

@app.route('/api/jobs/<job_id>')
def load_job(job_id):
    job = database.load_job_from_db(job_id)
    return jsonify(job)
    
if __name__ == '__main__':
    app.run(debug=True)