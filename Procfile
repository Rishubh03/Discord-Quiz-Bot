web: gunicorn quizbot.wsgi --log-file - --log-level debug
heroku config:set DISABLE_COLLECTSTATIC=1
heroku ps:scale web=1
python manage.py migrate