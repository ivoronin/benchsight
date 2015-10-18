# Benchsight
Web app for inspecting benchmark results.
Currently, only SPEC CPU data is being used.

## Requirements
See requirements.txt

## Running
```
$ python manage.py syncdb
$ python manage.py cpu2006_import
$ python manage.py runserver
```

## Hosted version
http://benchsight.azurewebsites.net/
