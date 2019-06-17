## Inicio Conversa Feliz
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id
    - action_receber_user_id
    - utter_inicio
> check_inicio_conversa

## Inicio Conversa Feliz 1
* fim_conversa
    - utter_perguntar_pedir_humano
* negar 
    - utter_perguntar_nome
* responder_user_id
    - action_receber_user_id
    - utter_inicio
> check_inicio_conversa

## Inicio Conversa Triste
* pedir_humano
    - utter_confirmar_pedir_humano
    - utter_tchau

## Inicio Conversa Triste 2
* inicio_conversa
    - utter_perguntar_nome
* pedir_humano
    - utter_confirmar_pedir_humano
    - utter_tchau

## Inicio Conversa Triste 3
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id
    - action_receber_user_id
    - utter_inicio
* pedir_humano
    - utter_confirmar_pedir_humano
    - utter_tchau

## Inicio Conversa Triste 4
* inicio_conversa
    - utter_perguntar_nome
* fim_conversa
    - utter_perguntar_pedir_humano
* afirmar 
    - utter_confirmar_pedir_humano
    - utter_tchau

## Inicio Conversa Triste 4
* fim_conversa
    - utter_perguntar_pedir_humano
* afirmar 
    - utter_confirmar_pedir_humano
    - utter_tchau

## Inicio Resolver Problemas
> check_inicio_conversa
* resolver_problema_rastreador OR resolver_problema_conta
    -utter_confirmar_problema
* afirmar
    - action_verificar_erros
    - utter_perguntar_resolvido
> check_perguntar_resolvido

## Inicio Mostrar dados e ir embora
> check_inicio_conversa
* mostrar_meus_dados
    - utter_confirmar_problema
    - action_mostrar_dados
    - utter_perguntar_resolvido
> check_perguntar_resolvido

## Problema errado 
> check_inicio_conversa
* resolver_problema_rastreador OR resolver_problema_conta
    -utter_confirmar_problema
* afirmar
    - action_verificar_erros
    - utter_perguntar_resolvido
* negar
    - utter_perguntar_pedir_humano
* afirmar
    - utter_confirmar_pedir_humano
    - utter_tchau

## Problema quer suporte mas não quer
> check_inicio_conversa
* resolver_problema_rastreador OR resolver_problema_conta
    -utter_confirmar_problema
* afirmar
    - action_verificar_erros
    - utter_perguntar_resolvido
* negar
    - utter_perguntar_pedir_humano
* negar
    - utter_inicio

## Problema resolvido Feliz 1
> check_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* afirmar 
    - utter_tchau

## Problema resolvido Feliz 2
> check_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* negar 
    - utter_inicio

## Problema resolvido Triste 1
> check_perguntar_resolvido
* negar
    - utter_perguntar_pedir_humano
* afirmar
    - utter_confirmar_pedir_humano
    - utter_tchau

## Problema resolvido Triste 2
> check_perguntar_resolvido
* negar
    - utter_perguntar_pedir_humano
* negar
    - utter_inicio

## Generated Story 1437006683169653924
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
    - utter_confirmar_problema
* afirmar
    - action_verificar_erros
    - utter_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* negar
    - utter_tchau

## Generated Story 8017354459056436804
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
    - utter_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* negar
    - utter_tchau

## Generated Story -2658281139604451543
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
    - utter_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* negar
    - utter_tchau

## Generated Story -5470599146534550759
* inicio_conversa
    - utter_perguntar_nome
* responder_user_id
    - action_receber_user_id
    - utter_inicio
* pedir_humano
    - rewind
* fim_conversa
    - utter_perguntar_pedir_humano
* afirmar
    - utter_confirmar_pedir_humano
    - utter_tchau
