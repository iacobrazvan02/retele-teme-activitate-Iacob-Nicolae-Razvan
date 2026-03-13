# retele-teme-activitate-Iacob-Nicolae-Razvan
teme(activitate)-retele

Tema1-dictionar de memorie

Pornirea serverului: python3 server.py
Pornirea clientului: python3 client.py

Comenzi disponibile:
ADD key value
GET key
REMOVE key
LIST
COUNT
CLEAR
UPDATE key value
POP key
QUIT

Exemple:
ADD produs1 100
GET produs1
LIST
COUNT
UPDATE produs1 200
POP produs1
QUIT
Gestionare erori

Serverul gestioneaza:

chei inexistente → ERROR invalid key
comenzi necunoscute → ERROR unknown command
format incorect al comenzilor
