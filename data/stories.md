## Inicio Conversa Resolver Problemas Feliz 1
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id
    - action_receber_user_id
    - utter_inicio
* resolver_problema_rastreador
> check_resolver_problema


## Problema Rastreador 1
> check_resolver_problema 
* resolver_problema_rastreador
    - utter_confirmar_problema_rastreador
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau


## Generated Story -9140261867826249853
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id{"user_id": "b95153c1-8cd0-41a4-a3e2-b3394efb9020"}
    - action_receber_user_id
    - utter_inicio

## Generated Story -6831051140549415556
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id{"user_id": "b95153c1-8cd0-41a4-a3e2-b3394efb9020"}
    - slot{"user_id": "b95153c1-8cd0-41a4-a3e2-b3394efb9020"}
    - action_receber_user_id
    - slot{"first_name": "Fulano"}
    - slot{"last_name": "aczhtp"}
    - slot{"is_actived": true}
    - slot{"user_name": "fulano@email.com"}
    - utter_inicio
* resolver_problema_rastreador
    - rewind
* mostrar_meus_dados
    - action_mostrar_dados
    - utter_inicio
* pedir_humano
    - utter_confirmar_pedir_humano

## Generated Story 5459356589743638153
* afirmar
    - rewind
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id
    - rewind
* responder_user_id{"user_id": "3F628CB7-F0C5-4F56-A720-3F5BBD44C2EA"}
    - slot{"user_id": "3F628CB7-F0C5-4F56-A720-3F5BBD44C2EA"}
    - action_receber_user_id
    - slot{"first_name": "Beltrano"}
    - slot{"last_name": "aqqerp"}
    - slot{"is_actived": true}
    - slot{"user_name": "beltrano@email.com"}
    - utter_inicio
* mostrar_meus_dados
    - action_mostrar_dados
    - utter_inicio
* fim_conversa
    - utter_tchau

## Generated Story 2827390774901534600
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id{"user_id": "b95153c1-8cd0-41a4-a3e2-b3394efb9020"}
    - slot{"user_id": "b95153c1-8cd0-41a4-a3e2-b3394efb9020"}
    - action_receber_user_id
    - slot{"first_name": "Fulano"}
    - slot{"last_name": "aczhtp"}
    - slot{"is_actived": true}
    - slot{"user_name": "fulano@email.com"}
    - utter_inicio
* mostrar_meus_dados
    - action_mostrar_dados
    - slot{"rastreadores": {"tk": ["tracker"]}}
    - utter_inicio
* fim_conversa
    - utter_tchau
