### Check if django is able to locate and load template

from django.template import loader  
print loader.get_template('home.html')


### Install django alternate method
    
    pip install https://www.djangoproject.com/download/1.0.4/tarball/    


### Find django version 
     python -c "import django; print(django.get_version())"   
     
     python
     import django
     django.VERSION
     
### Super user
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
     
### Exit virtualenv
    deactivate


### South 
    pip install south
    
    ./manage.py schemamigration my-app --initial
    ./manage.py migrate my-app
    
    ./manage.py schemamigration my-app --auto
    ./manage.py migrate my-app
    
    ./manage.py migrate my-app --fake
    
### Check for any errors in the construction of your models
    ./manage.py validate
    
    
