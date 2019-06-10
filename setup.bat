python -m venv env
call %cd%\env\Scripts\activate.bat
call curl https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz --output "pt_vectors.vec.gz"
call pip install -r requirements.txt
call pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
mkdir tmp\pt_vectors_wiki_lg
python -m spacy init-model pt tmp/pt_vectors_wiki_lg --vectors-loc pt_vectors.vec.gz
python -m spacy link tmp/pt_vectors_wiki_lg pt
rasa init --no-prompt
call del /f config.yml
call copy config_default.yml config.yml
call rmdir /S /Q models
rasa train
