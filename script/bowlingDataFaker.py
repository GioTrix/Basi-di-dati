from faker import Faker
import random
from datetime import datetime, timedelta
import unicodedata

fake = Faker('it_IT')

## Dipendente
# job_titles = ["Addetto alle vendite", "Addetto all'inventario", "Addetto alla sicurezza","Manager", "Addetto pulizie","Amministratore", "Addetto alla manutenzione", "Pubbliche relazioni"]
# # apri il file in modalità di scrittura
# with open("dipendente.csv", "w") as file:
#     # scrivi l'intestazione del file csv
#     file.write("Nome,Cognome,Titolo,Stipendio,Data assunzione,Indirizzo,Telefono,Impianto\n")
#     for _ in range(100000):
#         salary = str(random.randint(1000, 5000))
#         impianto = str(random.randint(101,103))
#         date = str(fake.date_between(start_date='-10y', end_date='today'))
#         # scrivi i dati separati da virgola
#         file.write(fake.first_name() + "," + fake.last_name() + "," + random.choice(job_titles) + "," + salary + "," + date + "," + fake.address().replace(",", " ").replace("\n"," ") + "," + fake.phone_number() + "," + impianto + "\n")


## Scarpe
# brands = {"Nike": 5, "Adidas": 5.5, "Puma": 6}
# with open("scarpe.csv", "w") as file:
#     # write the csv file header
#     file.write("prezzo,taglia,marca\n")
#     for _ in range(200):
#         taglia = str(random.randint(34,46))
#         marca = random.choice(list(brands.keys()))
#         prezzo = str(brands[marca])
#         # write the data separated by comma
#         file.write(prezzo + "," + taglia + "," + marca + "\n")


## Giocatore
#apri il file in modalità di scrittura
# with open("giocatore.csv", "w") as file:
#     # scrivi l'intestazione del file csv
#     file.write("nome,cognome,data_nascita,email,telefono\n")
#     for _ in range(200000):
#         first_name = unicodedata.normalize("NFKD", fake.first_name()).encode("ascii", "ignore").decode()
#         last_name = unicodedata.normalize("NFKD", fake.last_name()).encode("ascii", "ignore").decode()
#         birthdate = fake.date_of_birth(tzinfo=None, minimum_age= 6, maximum_age=70).strftime("%Y-%m-%d")
#         # scrivi i dati separati da virgola
#         file.write(first_name + "," + last_name + "," + birthdate + "," + fake.email() + "," + fake.phone_number() + "\n")


## Partita
# apri il file in modalità di scrittura
# with open("partita.csv", "w") as file:
#     # write the csv file header
#     file.write("ora_inizio,data,id_giocatore,punteggio,ora_fine,id_pista\n")
#     for _ in range(200000):
        
#         start_time = datetime(2000, 1, 1, 9, 0)
#         end_time = datetime(2000, 1, 1, 22, 0)

#         ora_inizio = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))

#         data = fake.date_this_decade(before_today=True, after_today=False)

#         ora_fine = ora_inizio + timedelta(seconds=random.randint(1, int((end_time - ora_inizio).total_seconds())))
#         ora_fine = ora_fine.replace(year=ora_inizio.year, month=ora_inizio.month, day=ora_inizio.day)

#         if ora_fine < ora_inizio:
#             ora_fine = ora_fine + timedelta(days=1)

#         ora_inizio = ora_inizio.strftime("%H:%M")
#         data = data.strftime("%Y-%m-%d")
#         ora_fine = ora_fine.strftime("%H:%M")

#         id_giocatore = str(random.randint(401035, 601034))
        
#         punteggio = str(random.randint(0, 300))

#         id_pista = str(random.randint(1, 15))

#         # write the data separated by comma
#         file.write(ora_inizio + "," + data + "," + id_giocatore + "," + punteggio + "," + ora_fine + "," + id_pista + "\n")

## Noleggio
# with open("noleggio.csv", "w") as file:
#     # write the csv file header
#     file.write("id_giocatore,id_scarpe,ora_inizio, data, consegnato\n")
#     for _ in range(200):
        
#         start_time = datetime(2000, 1, 1, 9, 0)
#         end_time = datetime(2000, 1, 1, 22, 0)

#         ora_inizio = start_time + timedelta(seconds=random.randint(0, int((end_time - start_time).total_seconds())))

#         data = fake.date_this_decade(before_today=True, after_today=False)

#         ora_fine = ora_inizio + timedelta(seconds=random.randint(1, int((end_time - ora_inizio).total_seconds())))
#         ora_fine = ora_fine.replace(year=ora_inizio.year, month=ora_inizio.month, day=ora_inizio.day)

#         ora_inizio = ora_inizio.strftime("%H:%M")
#         data = data.strftime("%Y-%m-%d")
#         ora_fine = ora_fine.strftime("%H:%M")

#         id_giocatore = str(random.randint(401035, 601035))
        
#         id_scarpe = str(random.randint(8220, 8419))

#         consegnato = str(random.getrandbits(1))

#         # write the data separated by comma
#         file.write(id_giocatore + "," + id_scarpe + "," + ora_inizio + "," + data + "," + consegnato + "\n")




## Abbonamento
#  apri il file in modalità di scrittura
# type = ["mensile", "trimestrale", "annuale"]
with open("abbonamento.csv", "w") as file:
    # scrivi l'intestazione del file csv
    file.write("data_inizio, data_fine, tipologia, id_giocatore\n")
    for i in range(100000):

        tipologia = random.choice(type)

        id_giocatore = str(random.randint(401035, 601035))

        data_inizio = fake.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d")
        if tipologia == "mensile":
            data_fine = (datetime.strptime(data_inizio, '%Y-%m-%d') + timedelta(days=30)).strftime("%Y-%m-%d")
        elif tipologia == "trimestrale":
            data_fine = (datetime.strptime(data_inizio, '%Y-%m-%d') + timedelta(days=90)).strftime("%Y-%m-%d")
        elif tipologia == "annuale":
            data_fine = (datetime.strptime(data_inizio, '%Y-%m-%d') + timedelta(days=365)).strftime("%Y-%m-%d")
        # scrivi i dati separati da virgola
        file.write(data_inizio + "," + data_fine + "," + tipologia + "," + id_giocatore + "\n")


## Inventario
#apri il file in modalità di scrittura
with open("inventario.csv", "w") as file:
    # scrivi l'intestazione del file csv
    file.write("descrizione\n")
    for _ in range(20):
        # scrivi i dati separati da virgola
        file.write(fake.product_name() + "\n")