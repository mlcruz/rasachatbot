call del /f defaults\config_default.yml 
call del /f defaults\domain_default.yml 
call del /f defaults\data\stories_default.md 
call del /f defaults\data\nlu_default.md 
call copy config.yml defaults\config_default.yml 
call copy domain.yml defaults\domain_default.yml 
call copy data\stories.md defaults\data\stories_default.md 
call copy data\nlu.md defaults\data\nlu_default.md 