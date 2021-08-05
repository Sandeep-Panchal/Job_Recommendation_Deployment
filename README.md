# Job Recommendation
<br>
<hr>
<br>

### Objective:
 - Given the skills, job description, job title or any job related keyword, it should be able to recommend the more relevant jobs

<br>
<hr>
<br>

## Approach:
 - **Text Data Embedding:**
    - Embedding of text data is done with **_Universal Sentence Encoder_** which converts any text size to **512 dimension vector**. It has the potential to preserve the semantic meaning of the text data.
    - I have used the **V5** of **_Universal Sentence Encoder_**. You can download or load the module from here: https://tfhub.dev/google/universal-sentence-encoder-large/5
    - To get the sample code on implementation of **_Universal Sentence Encoder_**, visit https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder
 - **Frontend UI Framework:**
    - **_HTML_** for structuring the UI.
    - **_CSS_** for styling the UI.
    - **_BootStrap_** to add more user friendly styles.
 - **API Creation:**
    - Flask Framework

<br>
<hr>
<br>

## Repository Folders/Files:
 - **data:**
    - **naukri_jobs_data.csv**  data prepared from the raw data obtained from kaggle.
    - **naukri_jobs_vector_v5.csv** is the array of vectors saved in pandas dataframe obtained by embedding the text data using **_Universal Sentence Encoder_**.
    - The above 2 files are saved in zip format. To load these files, parameter compression should be passed in pandas read csv code like pd.read_csv('data/file.csv', compression='zip')
    - Data Source: https://www.kaggle.com/PromptCloudHQ/jobs-on-naukricom
 - **static:** Contains the file css_styles.css for styling the UI.
 - **templates:** Contains the file job_recommend_ui.html for structuring the UI.
 - **job_data_embedding_preparation.ipynb:** Code to clean and preprocess the raw data.
 - **job_recommend_api.py:** Python script to create API using Flask web framework.
 - **job_recommend_code.py:** Python script to load the preprocessed data, embedding vector data, universal sentence encoder module, and finding the most similar jobs.
 - **Procfile:** Contains one line command to instruct which file to run.
 - **requirements.txt:** Contains the required libraries to be installed while deploying.

<br>
<hr>
<br>

## Steps to Run in Local System:
 - **Clone the repository** by following the steps mentioned here: https://github.com/Sandeep-Panchal/Job_Recommendation_Deployment/issues/1#issuecomment-893166854
 - Install the libraries mentioned in the **requirements.txt** file.
 - Open the **Anaconda prompt** or **CMD prompt**, go to the directory where the above cloned files are present.
 - In the **Anaconda prompt** or **CMD prompt**, type **python job_recommend_api.py**.
 - A **localhost link** is displayed. Copy-paste the link in the browser and **home page of job recommendation** will be displayed.
 - Enter your query in the input field and click on the Search button.

 - **Note:** It should be noted that, when deployed in localhost, when entered a query first time, it takes around 1 minute to output. In the first run, it takes 1 minute to load the modules and files. After first run, if you enter queries any number of times, it displays the result within a second. This is because, in the first run, after loading the modules and files, it gets stored in the cache. From the second run, instead of freshly loading everything, it will fetch the loaded data from the cache.**

<br>
<hr>
<br>

## Future Work:
 - I tried deploying the job recommendation in **heroku** and **AWS EC2 Instance**. As tensorflow installation size is large and due to size limit in  **heroku** and **AWS EC2 Instance** platform, it is failing to deploy.
 - Plan to deploy with some work-around or hacks.
