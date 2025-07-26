DEV HELPERS

python3 -m venv .venv
pip3 install fastapi
pip freeze > requirements.txt

git config --global -l
git config --global alias.p 'push'
git config --global alias.ci commit
git config --global --unset alias.ci
git config --global alias.cm 'commit -m'

docker compose up --build

http://localhost:8080/docs

https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add


git add -A stages all changes

git add . stages new files and modifications, without deletions (on the current directory and its subdirectories).

git add -u stages modifications and deletions, without new files

echo "app/__pycache__/"$'\n' >> .gitignore