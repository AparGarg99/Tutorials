### How to Deploy Streamlit Apps to Heroku

1. Create An Account Heroku by signing up.
2. Install Heroku CLI
3. Open folder you want to deploy (in this case app5_penguins_classification_WITH_DEPLOYMENT)
4. Right click mouse and open Git Bash
5. Local Git initialization
```
git init
git add .
git commit -m “initial commit”
```
6. Push app from local to heroku
```
heroku login
heroku create <NAME OF YOUR APP>
git remote -v
git push heroku master

```
