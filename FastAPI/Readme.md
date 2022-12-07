# What is FastAPI?
FastAPI is used for Model Deployment i.e. generating a Model Endpoint URL.

# Steps
1. We first make `api.py` file that contains pipeline - loading model, loading input, processesing input.
2. We run this `api.py` file using Anaconda prompt that deploys the model locally.
```
uvicorn api:app --reload
```
This will give us the localhost Model Endpoint URL http://127.0.0.1:8000.

FastAPI provides a cool in-built feature of Swagger UI which is a UI where we can go and test our model. If we add "/docs" at the end of the Endpoint URL, it will open up Swagger UI http://127.0.0.1:8000/docs.

3. Follow [guide](https://github.com/AparGarg99/Tutorials/blob/master/FastAPI/Convert%20to%20Python%20request.docx) to see how you can automatically get the python script that shows how to use this localhost Model Endpoint URL or model directly from a python script instead of Swagger UI.
4. So now, we have an input in `streamlit_app.ipynb` file. That input goes to the Endpoint URL that loads the model and processes input using `api.py` file and returns the output back to the `streamlit_app.ipynb` file.


# Deployment of model on Heroku Cloud (i.e. Remote Endpoint URL)
After testing the `streamlit_app.ipynb` with localhost Model Endpoint URL, we can deploy it on cloud and generate remote Endpoint URL.

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
* For ML: https://www.youtube.com/watch?v=C82lT9cWQiA
* Use API as Python request: https://www.youtube.com/watch?v=aMldpZF6GBU
