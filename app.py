from flask import Flask,render_template,jsonify
import database
from sqlalchemy import text 
app = Flask(__name__)

@app.route('/')
def hello_world():
    jobs = database.load_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = database.load_jobs_from_db()
    return jsonify(jobs)

@app.route('/api/jobs/<job_id>')
def load_job(job_id):
    job = database.load_job_from_db(job_id)
    if not job:
        return "Sorry,Not Found!!",404
    
    return render_template('jobdetails.html',job=job)
    
if __name__ == '__main__':
    app.run(debug=True)