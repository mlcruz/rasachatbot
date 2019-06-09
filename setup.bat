call %cd%\env\Scripts\activate.bat
call curl https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.pt.300.vec.gz --output "pt_vectors"
call pip install -r requirements.txt
call pip install rasa-x --extra-index-url https://pypi.rasa.com/simple