DEV HELPERS

python3 -m venv .venv
pip3 install fastapi
pip freeze > requirements.txt

git config --global -l
git config --global alias.p 'push'
git config --global alias.ci commit
git config --global --unset alias.ci
git config --global alias.cm 'commit -m'