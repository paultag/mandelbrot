Mandelbrot
==========

Setup

```
virtualenv virt
source virt/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Importing data

```
./manage.py migrate
./manage.py loadsalesforce ~/staff.csv
./manage.py loadmappings ~/mappings/
./manage.py loadgithub
./manage.py loadpriorities
./manage.py runserver
```
