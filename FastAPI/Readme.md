### Usage

1. Go to Anaconda prompt
```
uvicorn myapp:app --reload
```
2. Open the following link on browser<br>
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


### How to Deploy Streamlit Apps to Heroku

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
6. Push app from local to heroku
```
heroku login
heroku create <NAME OF YOUR APP>
git push heroku master
```

### References
* https://www.youtube.com/watch?v=WU65u9d-97c&list=PLZoTAELRMXVPgsojPOHF9i0u2L83-m9P7&index=1
* https://www.youtube.com/watch?v=C82lT9cWQiA
