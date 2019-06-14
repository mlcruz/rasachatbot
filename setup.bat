@echo off
python -m venv env
call %cd%\env\Scripts\activate.bat
call curl https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz --output "pt_vectors.vec.gz"
call pip install -r requirements.txt
call pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
mkdir tmp\pt_vectors_wiki_lg
python -m spacy init-model pt tmp/pt_vectors_wiki_lg --vectors-loc pt_vectors.vec.gz
python -m spacy link tmp/pt_vectors_wiki_lg pt
rasa init --no-prompt

call del /f actions.py
call del /f config.yml
call del /f domain.yml
call del /f data\nlu.md
call del /f data\stories.md

call copy defaults\actions_default.yml actions.py
call copy defaults\config_default.yml config.yml
call copy defaults\domain_default.yml domain.yml
call copy defaults\data\stories_default.md data\stories.md
call copy defaults\data\nlu_default.md data\nlu.md
call rmdir /S /Q models
rasa train
