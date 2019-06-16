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
* resolver_problema_rastreador OR resolver_problema_login
    -utter_confirmar_problema
> check_resolver_problema


## Inicio Mostrar dados e ir embora
> check_inicio_conversa
* mostrar_meus_dados
    - utter_confirmar_problema
    - action_mostrar_dados
* fim_conversa
    - utter_perguntar_resolvido
> check_perguntar_resolvido


## Resolver problema
> check_resolver_problema 
* afirmar
    - action_verificar_erros
    - utter_perguntar_resolvido
> check_perguntar_resolvido

## Problema errado 
> check_resolver_problema 
* negar
    - utter_perguntar_pedir_humano
* afirmar
    - utter_confirmar_pedir_humano
    - utter_tchau

## Problema quer suporte mas não quer
> check_resolver_problema 
* negar
    - utter_perguntar_pedir_humano
* afirmar
    - utter_inicio

## Problema resolvido Feliz 1
> check_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* negar 
    - utter_tchau

## Problema resolvido Feliz 2
> check_perguntar_resolvido
* afirmar
    - utter_confirmar_problema_resolvido
* afirmar 
    - utter_inicio_conversa
> check_inicio_conversa

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
    - utter_inicio_conversa
> check_inicio_conversa
