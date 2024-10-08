import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='triggered',
                              host='127.0.0.1', port=3306,
                              database='bowling')
cursor = cnx.cursor()

# Load the data.dipendente from the CSV file
def load_dipendente():
 with open('dipendente.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         nome = columns[0]
         cognome = columns[1]
         ruolo = columns[2]
         stipendio = columns[3]
         data_assunzione = columns[4]
         indirizzo = columns[5]
         telefono = columns[6]
         id_impianto = columns[7]
         cursor.execute("""INSERT INTO dipendente (nome, cognome, ruolo, stipendio, data_assunzione, indirizzo, telefono, id_impianto)
         VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
         """, (nome, cognome, ruolo, stipendio, data_assunzione, indirizzo, telefono, id_impianto))
         cnx.commit()


#Load data.giocatore from the CSV file
def load_giocatore():
 with open('giocatore.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         nome = columns[0]
         cognome = columns[1]
         data_nascita = columns[2]
         email = columns[3]
         telefono = columns[4]

         cursor.execute("""INSERT INTO giocatore (nome,cognome,data_nascita,email,telefono)
         VALUES (%s, %s, %s, %s, %s)
         """, (nome,cognome,data_nascita,email,telefono))
         cnx.commit()


# Load the data.scarpe from the CSV file
def load_scarpe():
 with open('scarpe.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         prezzo = columns[0]
         taglia = columns[1]
         marca = columns[2]
         cursor.execute("""INSERT INTO scarpe (prezzo, taglia, marca)
         VALUES (%s, %s, %s)
         """, (prezzo, taglia, marca))
         cnx.commit()


# #load data.partita
def load_partita():
 with open('partita.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         ora_inizio = columns[0]
         data = columns[1]
         id_giocatore = columns[2]
         punteggio = columns[3]
         ora_fine = columns[4]
         id_pista = columns[5]

         cursor.execute("""INSERT INTO partita (ora_inizio,data,id_giocatore,punteggio,ora_fine,id_pista)
         VALUES (%s, %s, %s, %s, %s,%s)
         """, (ora_inizio,data,id_giocatore,punteggio,ora_fine,id_pista))
         cnx.commit()

# #load data.noleggio
def load_noleggio():
 with open('noleggio.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         id_giocatore = columns[0]
         id_scarpe = columns[1]
         ora_inizio = columns[2]
         data = columns[3]
         consegnato = columns[4]

         cursor.execute("""INSERT INTO noleggio (id_giocatore,id_scarpe,ora_inizio, data, consegnato)
         VALUES (%s, %s, %s, %s, %s)
         """, (id_giocatore,id_scarpe,ora_inizio, data, consegnato))
         cnx.commit()

#load data.abbonamento
def load_abbonamento():
 with open('abbonamento.csv', 'r') as file:
     lines = file.readlines()
     lines =  lines[1:]
     for line in lines:
         columns = line.strip().split(',')
         data_inizio = columns[0]
         data_fine = columns[1]
         tipologia = columns[2]
         id_giocatore = columns[3]

         cursor.execute("""INSERT INTO abbonamento (data_inizio, data_fine, tipologia, id_giocatore)
         VALUES (%s, %s, %s, %s)
         """, (data_inizio, data_fine, tipologia, id_giocatore))
         cnx.commit()


# Close the cursor and the database connection
cursor.close()
cnx.close()
