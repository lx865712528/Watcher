# Data Watcher

## requirements

1. django

## path needed to modify
`watcher/settings.py Line118 SUBTASK_DATA_BASE="YOUR DATA ROOT"`

## run
`$ sh run.sh`

or

`$ python manage.py runserver 0.0.0.0:PORT`

## query
1. copy a query and remember which subtask it belongs to
2. open `http://localhost:PORT/query`, paste this question, choose right subtask, and click "submit"
