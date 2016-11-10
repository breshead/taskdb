# taskdb

This project is meant as a local Task Manager for in house teams.


## Requirements

 * Haystack
 * Elasticsearch 2.4.1
 * django-markdown-deux
 * simplemde-markdown-editor


### Elasticsearch
I get this from https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.4.1/elasticsearch-2.4.1.deb


### SimpleMDE
https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css
https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js
	
### Markdown-deux
pip install django-markdown-deux


## Setup

git clone https://github.com/breshead/taskdb.git
cd taskdb
pip install django-markdown-deux
curl https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css > taskgui/static/simplemde.min.css
curl https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js > taskgui/static/simplemde.min.js
	
python manage.py makemigrations taskgui
python manage.py migrate
python manage.py createsuperuser (admin/doug@jshfarms.com/testing)
sqlite3 db.sqlite3 < schemadump.sql 
python manage.py runserver


