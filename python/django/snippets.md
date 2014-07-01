#### Check if django is able to locate and load template
	from django.template import loader   
	print loader.get_template('home.html') 


#### Install django from tar ball 

    pip install https://www.djangoproject.com/download/1.0.4/tarball/    


#### Find django version 
     python -c "import django; print(django.get_version())"   
     
     python
     import django
     django.VERSION
     
     
#### Super user
     ./manage.py changepassword admin
     
     ./manage.py createsuperuser
     
     from django.contrib.auth.models import User
     user = User.objects.get(username='normaluser')
     user.is_superuser = True
     user.save()
    
     python manage.py shell
     from django.contrib.auth.models import User
     User.objects.filter(is_superuser=True)
     usr = User.objects.get(username='your username')
     usr.set_password('raw password')
     usr.save()
     
#### Exit virtualenv
    deactivate


#### South 
    pip install south
    
    ./manage.py schemamigration my-app --initial
    ./manage.py migrate my-app
    
    ./manage.py schemamigration my-app --auto
    ./manage.py migrate my-app
    
    ./manage.py migrate my-app --fake


#### Reset south migrations - delete ghost migrations
    rm <app-dir>/migrations/*
    python manage.py schemamigration <app-name> --initial
    python manage.py migrate <app-name> 0001 --fake  --delete-ghost-migrations
    
    
#### Check for any errors in the construction of your models
    ./manage.py validate
    

#### ipython notebook for django
##### Install
	pip install django-shell-ipydb
#### Run
	./manage.py shell_ipynb
	
#### Run django shell with ipython or bpython or normal shell 
	./manage.py shell --interface ipython
	./manage.py shell -i ipython
	./manage.py shell -i bpython
	./manage.py shell --plain
	
#### Install django debug toolbar for better debugging.
	pip install django-debug-toolbar
	
#### Installed celery & django celery
	pip install Celery django-celery
	
	For Ubuntu install rabbitmq for celery to work 
	apt-get install rabbitmq-server 
	
	./manage.py celeryd -l info 
	
	celery help
	celery -A my_app worker -l info
	celery status
	
	
	
	
    
    
