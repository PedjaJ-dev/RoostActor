# Flask API - Evidencija Studenata

Ovaj projekat je API koji koristi Flask za evidenciju studenata sa MySQL bazom podataka. API koristi JWT autentifikaciju i omogućava različite funkcije za profesore i administratore.

## Potrebni Koraci za Podesavanje

### 1. Pokretanje XAMPP-a

Pre nego što nastavite, uverite se da ste pokrenuli XAMPP i da je **MySQL** server aktivan. Koristiće se **phpMyAdmin** za upravljanje bazom podataka.

### 2. Kloniranje Projekta

Prvo, klonirajte ovaj projekat na vaš računar:  

  ```sh
git clone <link-do-repozitorijuma>
cd <ime-repozitorijuma>
```

### 3. Instalacija zavisnosti

Pokrenite u terminalu sledeće komande:

  ```sh
pip install Flask  
pip install mysql-connector-python  
pip install werkzeug  
pip install flask-jwt-extended 
```
 
### 4. Import baze podataka

Pokrenite phpMyAdmin a liknite na http://localhost/phpmyadmin, i kliknite na Import.  
Odaberite fajl evidencija_studenata.sql.  
Kliknite na Go.  

### 5. Login podaci

Za pristup API-ju:  
  
Profesor:  
Email: test@test.com  
Lozinka: password  

Administrator:  
Email: test2@test.com  
Lozinka: password  
