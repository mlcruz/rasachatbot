
## intent:afirmar
- sim
- claro
- ok
- certo
- tudo bem
- Tudo bem

## intent:fim_conversa
- tchau
- até mais
- vou embora
- obrigado
- até logo

## intent:inicio_conversa
- Olá
- Oi
- Acorda
- olá

## intent:negar
- não
- nunca
- nem a pau
- nada a ver
- claro que não

## intent:receber_nome
- Adriana
- Ana
- Maria
- Sandra
- Juliana
- Antônio
- Carlos
- Francisco
- João
- José
- Bruna
- Camila
- Jéssica
- Letícia
- Amanda
- Lucas
- Luiz
- Matheus
- Guilherme
- Pedro
- Alice
- Isabella


## intent:cadastrar_rastreador
- cadastrar o [GPS](rastreador) com telefone [013-991776914](n_telefone) imei [111222333444555](imei) da [vivo](apn)
- cadastrar o telefone [013-991776914](n_telefone) da [vivo](apn)
- cadastrar o [GPS](rastreador) com telefone [013-991776914](n_telefone)
- [GPS](rastreador) [013-991776914](n_telefone) [111222333444555](imei) [vivo](apn)
- [013-991776914](n_telefone) [111222333444555](imei) [vivo](apn)
- cadastrar o [013-991776914](n_telefone)


## synonym:rastreador
- Suntech
- TK102
- TK103
- GPS
- TK102
- Celular
- Smartphone
- Iphone
- Android

## synonym:apn
- Vivo
- Oi
- Claro
- Claro-m2m
- Nextel
- Tim

## regex:n_telefone
- 0\d{2}\-\d{9}

## regex:imei
- \d{15}
