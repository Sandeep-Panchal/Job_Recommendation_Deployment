import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import pandas as pd
import streamlit as st

# load the naukri jobs data and also jobs embedding vector
def load_data():

    # loads jobs data
    jobs_df = pd.read_csv('data/naukri_jobs_data.csv', compression='zip')

    # loads jobs embedding vector data
    jobs_vect_df = pd.read_csv('data/naukri_jobs_vector_v5.csv', header=None, compression='zip')

    return jobs_df, jobs_vect_df


# load the universal sentence encoder model from tf hub
def load_use_model():

    # loads the universal sentence encoder model
    use_model = hub.load('https://tfhub.dev/google/universal-sentence-encoder-large/5')
    return use_model


# getting the embedding of the text (query from user)
def embed(text, mod):
    return np.array(mod(text))


# funtion to recommend jobs
# it takes the input from the user, converts it into 512 dimension using universal sentence encoder
# jobs data converts into Nx512 dimension vector
# finds the similarity between the user input embedding vector and the jobs data embedding vector
# displays the most relevant job
@st.cache(suppress_st_warning=True)
def load_all_fun():

    # call load_jobs_data to load the naukri job data
    dfr_jobs, dfr_jobs_vect = load_data()

    # getting jobs_vect_df in numpy array
    jobs_vect = np.array(dfr_jobs_vect.to_numpy().tolist())

    # call load_use_model to load the universal sentence encoder model from tf hub
    use_model = load_use_model()

    return dfr_jobs, jobs_vect, use_model
    
def recommend(query, jobs_vect, use_model, top=5):

    # get query embeddings from universal sentence encoder
    query_vect = embed([query], use_model)

    # get similarity score, and their index
    similarity_scr = np.inner(query_vect, jobs_vect)
    idx = np.argsort(similarity_scr)
    idx_list = idx[0][::-1]

    return idx_list