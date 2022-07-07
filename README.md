# django-app
A small webapp to generate time schedule for classes. 
<br><br>
Link to deployed app-
* http://www.searchtool.top/`<route>`    
  eg. - http://www.searchtool.top/api/class/
<br><br>
Routes- 
* /api/class  
	(GET) - show all class data (Each data is also a link to --> /api/class/id)
	(POST)- input: class number, strength of class, number of sections(max. 3), subjects(must be five)
	Button('Generate Schedule') - link --> /api/generate  

* /api/class/id  
	(GET) - show class data by id   
	Button('Delete') - delete class data by id  

* /api/teacher  
	(GET) - show all teacher data (Each data is also a link to --> /api/teeacher/id)
	(POST)- input: teacher name, class, subject  

* /api/teacher/id  
	(GET) - show teacher data by id
	Button('Delete') - delete teacher data by id  

* /api/generate  
	(GET) - get CSV file report of generated schedule  



Project Tree-

`project
│
│   db.sqlite3
│   manage.py
│
├───project
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           settings.cpython-39.pyc
│           urls.cpython-39.pyc
│           wsgi.cpython-39.pyc
│           __init__.cpython-39.pyc
│
└───scheduler
    │   admin.py
    │   apps.py
    │   models.py
    │   tests.py
    │   urls.py
    │   views.py
    │   __init__.py
    │
    ├───migrations
    │   │   0001_initial.py
    │   │   0002_remove_class_id_alter_class_class_num_and_more.py
    │   │   0003_teacher.py
    │   │   0004_alter_teacher_subject.py
    │   │   0005_class_sections.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │
    │
    ├───templates
    │       show_class.html
    │       show_teachers.html
    │
    └───__pycache__`  
    



Usage-
* install Python>=3.9
* open terminal in top most 'project' directory
* run - pip install django
* run - python manage.py runserver
* go to browser and search - http://localhost:8000/<route>


 
