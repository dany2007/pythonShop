import sqlite3
import pyinputplus

con = sqlite3.connect("product_db.db")

print("Bine ati venit!")

nume = input("Va rugam sa va introduceti numele:")
nume = nume.capitalize()

cursor = con.cursor()
query = f"select Nume_produs from products group by Nume_produs"
cursor.execute(query)
query_produse = cursor.fetchall()

produse_disponibile = []

for produs in query_produse:
    produse_disponibile.append(produs[0])

print(produse_disponibile)

produs_ales = pyinputplus.inputMenu(produse_disponibile,
                                    "Va rugam sa alegeti un produs din cele disponibie: \n",
                                    numbered=True)

query = f"select Varianta from products where Nume_produs='{produs_ales}'"
cursor.execute(query)

print(f'Produsul ales este {produs_ales}')

variante_disponibile = []
query_produse = cursor.fetchall()
for varianta in query_produse:
    variante_disponibile.append(varianta[0])

varianta_aleasa = pyinputplus.inputMenu(variante_disponibile,
                                        "Variantele disponibile petru acest produs sunt: \n",
                                        numbered=True)

query = f"select pret from products where Nume_produs='{produs_ales}' AND Varianta='{varianta_aleasa}'"
cursor.execute(query)
pret = cursor.fetchone()

print(f"Ati ales produsul {produs_ales} cu varianta {varianta_aleasa}, costul total este {pret[0]}$")

query = f"insert into tranzactii(nume_client, produs_cumparat, varianta_produsului, suma_cheltuita) " \
        f"VALUES ('{nume}','{produs_ales}','{varianta_aleasa}','{pret[0]}')"
cursor.execute(query)

con.commit()
con.close()

print("Finished")
