# What is FastAPI?
* FastAPI is used for Model Deployment i.e. generating a Model Endpoint URL.
* Steps - 
    1. We first make `api.py` file that contains pipeline - loading model, loading input, processesing input
    2. We run this `api.py` file using cmd that deploys the model locally and generates a localhost Model Endpoint URL. Note: We can deploy the model on cloud too i.e. generate remote Endpoint URL.
* So we have an input in `streamlit_app.py` file. That input goes to the Endpoint URL that loads the model and processes input using api.py file and returns the output back to the `streamlit_app.py` file.

# Usage
1. Go to Anaconda prompt
```
uvicorn myapp:app --reload
```
2. Open the following link on browser<br>
http://127.0.0.1:8000/docs


# Deployment of model on Heroku Cloud (i.e. Remote Endpoint URL)
1. Create an Heroku account by signing up.
2. Install Heroku CLI
3. Open folder you want to deploy (in this case FastAPI)<br>
<b>Note:</b> The folder must contain app.py, Procfile, requirements.txt
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
