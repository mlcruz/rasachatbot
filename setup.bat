REM python -m venv env
REM call %cd%\env\Scripts\activate.bat
REM call curl https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz --output "pt_vectors.vec.gz"
REM call pip install -r requirements.txt
REM call pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
REM mkdir tmp\pt_vectors_wiki_lg
REM python -m spacy init-model pt tmp/pt_vectors_wiki_lg --vectors-loc pt_vectors.vec.gz
REM python -m spacy link tmp/pt_vectors_wiki_lg pt
REM rasa init --no-prompt