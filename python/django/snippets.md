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
