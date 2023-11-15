#!/bin/zsh

cd "$(dirname "$0")" || exit 1;

# create custom virtual environment
python3 -m venv build-env
source ./build-env/bin/activate
pip install -r ./requirements.txt
pyinstaller --noconfirm --clean --onefile --name supabase-secrets-generator main.py
deactivate
rm -rf ./build-env
rm -rf ./build
chmod a+x ./dist/supabase-secrets-generator
