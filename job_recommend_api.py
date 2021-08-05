from flask import Flask, request, render_template, url_for
from job_recommend_code import load_all_fun, recommend

# initiate flask app
app = Flask(__name__)

# render the home page
@app.route('/')
def home():
    return render_template('job_recommend_ui.html')

# create route for recommending jobs
@app.route('/recommend_jobs', methods = ['POST'])
# @cache.cached(timeout=1)
def recommend_jobs():
    if request.method == 'POST':

        dfr_jobs, jobs_vect, use_model = load_all_fun()
        query = request.form['user-query']

        idx_list = recommend(query, jobs_vect, use_model)

        jobs_data_list = []
        # display similar jobs
        for i in range(10):
            jobs_data_dic = {}
            job_idx = idx_list[i]
            jobs_data_dic['title'] = dfr_jobs['Job Title'].iloc[job_idx]
            jobs_data_dic['domain'] = dfr_jobs['Job Domain'].iloc[job_idx]
            jobs_data_dic['description'] = dfr_jobs['Job Description'].iloc[job_idx]
            jobs_data_list.append(jobs_data_dic)
        
    return render_template('job_recommend_ui.html', jobs_data_list=jobs_data_list)

if __name__ == '__main__':
    app.run(debug = False)