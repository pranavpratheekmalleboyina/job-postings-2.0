from flask import Flask,render_template,jsonify
app = Flask(__name__)

JOBS = [
    {'id': 1, 'title': 'Software Engineer', 'company': 'XYZ Corp.', 'location': 'New York','salary':'$450000'},
    {'id': 2, 'title': 'Data Scientist', 'company': 'ABC Inc.', 'location': 'San Francisco','salary':'$350000'},
    {'id': 3, 'title': 'Product Manager', 'company': 'PQR LTD.', 'location': 'London','salary':'$250000'},
    {'id': 4, 'title': 'Backend Engineer', 'company': 'Facebook', 'location': 'Boston','salary':'$650000'}
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name='Pranav Consultancy')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)