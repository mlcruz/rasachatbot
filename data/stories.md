## Inicio Conversa Resolver Problemas Feliz 1
* inicio_conversa
    - utter_perguntar_nome
* responder_nome
    - action_receber_nome
    - utter_inicio
* resolver_problema_rastreador OR resolver_problema_pagamento OR resolver_problema_esqueci_senha OR resolver_problema_login
> check_resolver_problema

## Inicio Conversa Feliz Problema Rastreador 1
> check_resolver_problema 
* resolver_problema_rastreador
    - utter_confirmar_problema_rastreador
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau

## Inicio Conversa Feliz Problema Pagamento 1
> check_resolver_problema 
* resolver_problema_pagamento
    - utter_confirmar_problema_pagamento
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau

## Inicio Conversa Feliz Problema Esqueci Senha 1
> check_resolver_problema 
* resolver_problema_esqueci_senha
    - utter_confirmar_problema_esqueci_senha
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau

## Inicio Conversa Feliz Problema Login 1
> check_resolver_problema 
* resolver_problema_login
    - utter_confirmar_problema_login
* afirmar
    - utter_perguntar_resolvido
* afirmar
    - utter_tchau


## Inicio Conversa Triste 1
* inicio_conversa
    - utter_inicio  
* resolver_problema_rastreador
    - utter_confirmar_problema_rastreador
* negar
    - utter_perguntar_pedir_humano 
* afirmar
    - utter_confirmar_pedir_humano

## Inicio Conversa Triste 2
* inicio_conversa
    - utter_inicio  
* pedir_humano
    - utter_confirmar_pedir_humano


## Inicio Conversa Triste 3
* inicio_conversa
    - utter_inicio  
* resolver_problema_rastreador
    - utter_confirmar_problema_rastreador
* afirmar
    - utter_perguntar_resolvido
* negar
    - utter_perguntar_pedir_humano 
* afirmar
    - utter_confirmar_pedir_humano


