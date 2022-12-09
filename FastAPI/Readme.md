# Methods to deploy an ML Project
There are 3 methods to deploy your system (in ascending order of code separability):

1. **Project (Model + App) -** The entire project is deployed on a cloud service like AWS ElasticBeankstalk.
2. **Model | App (Processing + UI) -** Model is uploaded to a cloud storage bucket. User gives input to App. The App loads the model using model url, does the prediction using it and returns the result. The result is presented to to the user. This App is deployed on another cloud service.
3. **API (Model + Processing) | App (UI) -** Model is wrapped inside an API which also does the prediction and return results. This API is deployed on a cloud service 1 and we get the model Endpoint URL. User gives input to App. App goes to the Endpoint URL to load model, process input, return output. The result is presented to to the user. This App is deployed on another cloud service 2.

In this tutorial, we'll learn Method 3 which is most widely used in industry.

# What is FastAPI?
FastAPI is a service used to create **API (Model + Processing)** mentioned in Method 3 above and generating an Endpoint URL for the same.

# Steps to run API on local machine (i.e. Local Endpoint URL)
1. Train and save the model - `model_development.ipynb`
2. Make `api.py` file that contains pipeline - loading model, loading input, processesing input.
3. Run this `api.py` file using Anaconda prompt that deploys the model locally.
```
uvicorn api:app --reload
```
This will give us the localhost Model Endpoint URL http://127.0.0.1:8000.

FastAPI provides a cool in-built feature of Swagger UI which is a UI where we can go and test our model. If we add "/docs" at the end of the Endpoint URL, it will open up Swagger UI http://127.0.0.1:8000/docs.

4. Follow the [guide](https://github.com/AparGarg99/Tutorials/blob/master/FastAPI/Convert%20to%20Python%20request.docx) to see how you can automatically get the code that shows how to use this localhost Model Endpoint URL or model directly from a python script instead of Swagger UI. Paste this code in `streamlit_app.py` file.
5. So now, we have an input in `streamlit_app.py` file. That input goes to the Endpoint URL (that loads the model and processes input using `api.py` file) and returns the output back to the `streamlit_app.py` file.


# Deployment of API on Heroku Cloud (i.e. Remote Endpoint URL)
After testing the `streamlit_app.py` with localhost Model Endpoint URL, we can deploy it on cloud and generate remote Endpoint URL.

1. Create an Heroku account by signing up.
2. Install Heroku CLI
3. Go to the project folder <br>
<b>Note:</b> The folder must contain `api.py`, `Procfile`, `requirements.txt`
4. Right click mouse and open Git Bash
5. Local Git initialization
```
git init
git add .
git commit -m "initial commit"
```
6. Push API from local to heroku
```
heroku login
heroku create <NAME OF YOUR APP>
git push heroku master
```

# References
* Basics: https://www.youtube.com/watch?v=WU65u9d-97c&list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7&index=1
* For Tabular Data ML: https://www.youtube.com/watch?v=C82lT9cWQiA
* For Image Data ML: https://www.youtube.com/watch?v=aMldpZF6GBU
* Use API as Python request: https://www.youtube.com/watch?v=aMldpZF6GBU
* Deployment of model on GCP (Method 2): https://www.youtube.com/watch?v=fw6NMQrYc6w
* Deployment of model on IBM Cloud (Method 2): https://www.youtube.com/watch?v=yqkISICHH-U&list=PLgNJO2hghbmid6heTu2Ar68CzJ344nUHy&index=4
