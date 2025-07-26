DEV HELPERS

## Virtual Environment Setup
python3 -m venv .venv
pip3 install fastapi
pip freeze > requirements.txt

## Git config reference commands
```
git config --global -l
git config --global alias.p 'push'
git config --global alias.ci commit
git config --global --unset alias.ci
git config --global alias.cm 'commit -m'
```

## How to build and run the app
`docker compose up --build`

http://localhost:8080/docs

## Git add helpers
https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add


git add -A stages all changes

git add . stages new files and modifications, without deletions (on the current directory and its subdirectories).

git add -u stages modifications and deletions, without new files


## Update .gitignore with echo through CLI coz bash completion
Add the extra newline char, puts an extra line in between but \r didn't work as expected. Something about line endings in Unix.
`echo "app/__pycache__/"$'\n' >> .gitignore `

## Notes about database index

A database index is a data structure (often a B-tree) that improves the speed of queries on a table — especially for:

WHERE filters

ORDER BY clauses

Joins

For example, this query will be faster if username is indexed:

`SELECT * FROM notes WHERE username = 'alice';`

## How to see tables in sqlite
With the current setup, I've installed sqlite in the Docker. Exec into it and query the database. 

docker exec -it notes-app-web-1 /bin/bash

```
$ sqlite3 
sqlite> .open notes.db
sqlite> .tables
notes
sqlite> notes
```

sqlite> SELECT * from notes;
1|kgadgil|Hello World
2|kgadgil|Initial Commit

## Simulate heavy-load

```
hey -n 10000 -c 100 \
	-m POST \
	-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrZ2FkZ2lsIiwiZXhwIjoxNzUzNTYyNjExfQ.mnvDzvZa3A6gfx-Kb7VKRre_c2kHMo0wsp3IsJ-gLXo" \
	-H "Content-Type: application/json" \
	-d '{"note":"test"}' \
	http://localhost:8080/notes
```
When i run GET i get the following error 

  raise exc.TimeoutError(
sqlalchemy.exc.TimeoutError: QueuePool limit of size 5 overflow 10 reached, connection timed out, timeout 30.00 (Background on this error at: https://sqlalche.me/e/20/3o7r)
