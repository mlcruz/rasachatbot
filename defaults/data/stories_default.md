## Inicio Conversa Resolver Problemas Feliz 1
* inicio_conversa
    - utter_perguntar_nome
* responder_nome
    - action_receber_nome
    - utter_inicio
* resolver_problema_rastreador
> check_resolver_problema


## Inicio Conversa Feliz Problema Rastreador 1
> check_resolver_problema 
* resolver_problema_rastreador
    - utter_confirmar_problema_rastreador
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau

## Inicio Conversa Triste 2
* inicio_conversa
    - utter_perguntar_nome
* responder_nome
    - action_receber_nome
    - utter_inicio 
* pedir_humano
    - utter_confirmar_pedir_humano





