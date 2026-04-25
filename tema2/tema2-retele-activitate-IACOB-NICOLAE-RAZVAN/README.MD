teme(activitate)-retele-IACOB NICOLAE RAZVAN
Tema2-Client Server UDP
Pornirea serverului: ./start.sh (sau python3 server.py)
Pornirea clientului: python3 client.py
Comenzi disponibile: CONNECT DISCONNECT PUBLISH  DELETE  LIST EXIT
Exemple: CONNECT PUBLISH mesaj1 LIST DELETE 1 DISCONNECT EXIT
Gestionare erori
Serverul gestioneaza:
comenzi fara conectare → EROARE: Trebuie sa fii conectat
stergerea mesajelor altora → EROARE: Poti sterge doar mesajele tale
id-uri inexistente → EROARE: ID-ul nu a fost gasit
Clientul gestioneaza (local):
comenzi inainte de CONNECT → EROARE: Nu esti conectat
argumente lipsa → EROARE: Mesaj lipsa sau ID invalid