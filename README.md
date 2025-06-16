# TravelTales

https://github.com/user-attachments/assets/a289072f-23a3-4773-93fc-472e60c7ad4b

## Useful Commands
```python
python --version
python -m venv venv  # create venv in project folder (Once) 
venv\Scripts\activate
python manage.py runserver
python manage.py startapp <feature-appname>

#### After changing model -> need to migrate
python manage.py makemigrations
python manage.py migrate

#### shell for ORM based DB access and queries
python manage.py shell

#### you can run these commands (varies as per project - posts project below)
from posts.models import Post
p = Post()
p.title = "My first post"
p.save()
Post.objects.all()

#### create admin username & pw ~ superuser 
python manage.py createsuperuser

#### for PRODUCTION -> make changes in settings.py & urls.py in project folder
python manage.py collectstatic
```






