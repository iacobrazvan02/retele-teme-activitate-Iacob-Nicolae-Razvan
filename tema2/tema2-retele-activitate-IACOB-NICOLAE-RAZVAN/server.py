import socket

HOST        = '127.0.0.1'
PORT        = 9999
BUFFER_SIZE = 1024

clienti_conectati = {}
stocare_mesaje = {}
contor_id = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("=" * 50)
print(f"  SERVER UDP pornit pe {HOST}:{PORT}")
print("  Asteptam mesaje de la clienti...")
print("=" * 50)

while True:
    try:
        date_brute, adresa_client = server_socket.recvfrom(BUFFER_SIZE)
        mesaj_primit = date_brute.decode('utf-8').strip()

        parti = mesaj_primit.split(' ', 1)
        comanda = parti[0].upper()
        argumente = parti[1] if len(parti) > 1 else ''

        print(f"\n[PRIMIT] De la {adresa_client}: '{mesaj_primit}'")

        if comanda == 'CONNECT':
            if adresa_client in clienti_conectati:
                raspuns = "EROARE: Esti deja conectat la server."
            else:
                clienti_conectati[adresa_client] = True
                nr_clienti = len(clienti_conectati)
                raspuns = f"OK: Conectat cu succes. Clienti activi: {nr_clienti}"
                print(f"[SERVER] Client nou conectat: {adresa_client}")

        elif comanda == 'DISCONNECT':
            if adresa_client in clienti_conectati:
                del clienti_conectati[adresa_client]
                raspuns = "OK: Deconectat cu succes. La revedere!"
                print(f"[SERVER] Client deconectat: {adresa_client}")
            else:
                raspuns = "EROARE: Nu esti conectat la server."

        elif comanda in ['PUBLISH', 'DELETE', 'LIST']:
            if adresa_client not in clienti_conectati:
                raspuns = "EROARE: Trebuie sa fii conectat pentru a folosi aceasta comanda."
            
            elif comanda == 'PUBLISH':
                if not argumente:
                    raspuns = "EROARE: Mesajul nu poate fi gol."
                else:
                    stocare_mesaje[contor_id] = {"text": argumente, "autor": adresa_client}
                    raspuns = f"OK: Mesaj publicat cu ID={contor_id}"
                    contor_id += 1

            elif comanda == 'DELETE':
                try:
                    id_cautat = int(argumente)
                    if id_cautat not in stocare_mesaje:
                        raspuns = f"EROARE: Mesajul cu ID={id_cautat} nu a fost gasit."
                    else:
                        if stocare_mesaje[id_cautat]["autor"] == adresa_client:
                            del stocare_mesaje[id_cautat]
                            raspuns = f"OK: Mesajul cu ID={id_cautat} a fost sters cu succes."
                        else:
                            raspuns = "EROARE: Poti sterge doar mesajele publicate de tine!"
                except ValueError:
                    raspuns = "EROARE: ID-ul trebuie sa fie un numar intreg valid."

            elif comanda == 'LIST':
                if not stocare_mesaje:
                    raspuns = "INFO: Nu exista mesaje publicate."
                else:
                    linii = ["Mesaje disponibile:"]
                    for msg_id, info in stocare_mesaje.items():
                        marcare_autor = " (al tau)" if info["autor"] == adresa_client else ""
                        linii.append(f"  ID={msg_id}: {info['text']}{marcare_autor}")
                    raspuns = "\n".join(linii)

        else:
            raspuns = f"EROARE: Comanda '{comanda}' este necunoscuta. Comenzi valide: CONNECT, DISCONNECT, PUBLISH, DELETE, LIST"

        server_socket.sendto(raspuns.encode('utf-8'), adresa_client)
        print(f"[TRIMIS]  Catre {adresa_client}: '{raspuns}'")

    except KeyboardInterrupt:
        print("\n[SERVER] Oprire server...")
        break
    except Exception as e:
        print(f"[EROARE] {e}")

server_socket.close()
print("[SERVER] Socket inchis.")