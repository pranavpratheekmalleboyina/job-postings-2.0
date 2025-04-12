from flask import Flask,render_template,jsonify,request
import database
from sqlalchemy import text 
app = Flask(__name__)

@app.route('/') #this is the root page
def hello_world():
    jobs = database.load_jobs_from_db()
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')  #to display all the jobs from the database
def list_jobs():
    jobs = database.load_jobs_from_db()
    return jsonify(jobs)

@app.route('/api/jobs/<job_id>') #to retrieve a particular job from the database
def load_job(job_id):
    job = database.load_job_from_db(job_id)
    if not job:
        return "Sorry,Not Found!!",404
    return render_template('jobdetails.html',job=job)

@app.route('/api/jobs/<job_id>/apply',methods=['post'])   
def apply_to_job(job_id):
     data = request.form
     job = database.load_job_from_db(job_id)
     status = database.save_application_to_db(job_id,data)
     return render_template('application_submitted.html',job=job,application=data)
    
if __name__ == '__main__':
    app.run(debug=True)
    
