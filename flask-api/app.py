from functools import wraps
from flask import Flask, jsonify, request
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, jwt_required, get_jwt_identity
from flask_cors import CORS


# MySQL konekcija
con = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    passwd='',
    database='roostactor'
)

mycursor = con.cursor(dictionary=True)

# Inicijalizacija Flask aplikacije
app = Flask(__name__)

CORS(app)

# Konfiguracija aplikacije
app.config['JWT_SECRET_KEY'] = 'tvoj_tajni_jwt_kljuc'
jwt = JWTManager(app)

# Omogućavanje CORS-a
CORS(app)

# Funkcija za proveru uloga
def role_required(roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") not in roles:
                return jsonify({"message": "Nemate dozvolu za pristup ovoj ruti."}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# -----------------------------------------------> Login <-------------------------------------------------------

from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST'])
def login():
    forma = request.json
    upit = "SELECT * FROM korisnik WHERE email=%s"
    vrednost = (forma['email'],)
    mycursor.execute(upit, vrednost)
    korisnik = mycursor.fetchone()

    if korisnik and check_password_hash(korisnik['Lozinka'], forma['lozinka']):
        # Kreiranje JWT tokena sa dodatnim podacima (rola)
        access_token = create_access_token(
            identity=korisnik['Email'],
            additional_claims={"role": korisnik['Uloga']}
        )

        # Vraćanje tokena i korisničkih podataka u odgovoru
        return jsonify({
            "message": "Uspešno ste se prijavili.",
            "access_token": access_token,
            "userId": korisnik['IDK'],
            "uloga": korisnik['Uloga'],
            "telefon": korisnik['Telefon']
        }), 200
    else:
        return jsonify({"message": "Neispravni podaci za prijavu."}), 401

# -----------------------------------------------> Login <-------------------------------------------------------




# -----------------------------------------------> Dashboard <-------------------------------------------------------
from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from mysql.connector import connect, Error

@app.route('/dashboard/<int:id>', methods=['GET'])
@jwt_required()
def get_user_data(id):
    # Dobijamo ID korisnika iz JWT
    current_user_id = get_jwt_identity()
    print(f"JWT user ID: {current_user_id}, Requested ID: {id}")

    # Provera autorizacije
    if current_user_id != id:
        return jsonify({"message": "Nemate dozvolu da pristupite ovom korisniku"}), 403

    try:
        query = """
        SELECT IDK, ime, prezime, email, telefon, uloga 
        FROM korisnik 
        WHERE IDK = %s
        """
        mycursor.execute(query, (id,))
        korisnik = mycursor.fetchone()

        # Provera da li je korisnik pronađen
        if korisnik:
            # Formatiranje odgovora kao JSON objekta
            user_data = {
                "IDK": korisnik['IDK'],
                "ime": korisnik['ime'],
                "prezime": korisnik['prezime'],
                "email": korisnik['email'],
                "telefon": korisnik['telefon'],
                "uloga": korisnik['uloga'],
            }
            print(f"User found: {user_data}")
            return jsonify(user_data), 200
        else:
            print("User not found.")
            return jsonify({"message": "Korisnik nije pronađen"}), 404

    except Error as e:
        print(f"Database error: {e}")
        return jsonify({"message": "Greška u bazi podataka"}), 500






# -----------------------------------------------> Dashboard <-------------------------------------------------------



# -----------------------------------------------> Korisnici <-----------------------------------------------------

@app.route('/korisnici', methods=['GET'])
@jwt_required()
def get_korisnici():
    query = "SELECT IDK, Ime, Prezime, Email, Uloga FROM korisnik"
    mycursor.execute(query)
    korisnici = mycursor.fetchall()
    return jsonify(korisnici), 200

@app.route('/korisnici', methods=['POST'])
@jwt_required()
def add_korisnik():
    data = request.json
    print(data)  # Ovo će vam pomoći da proverite koji podaci stižu
    hashed_password = generate_password_hash(data['lozinka'])
    query = """
        INSERT INTO Korisnik (Ime, Prezime, Uloga, Email, Telefon, Lozinka) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (data['ime'], data['prezime'], data['uloga'], data['email'], data['telefon'], hashed_password)
    mycursor.execute(query, values)
    con.commit()
    return jsonify({"message": "Korisnik uspešno dodat"}), 201


@app.route('/korisnici/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_korisnik(id):
    query = "DELETE FROM Korisnik WHERE IDK = %s"
    mycursor.execute(query, (id,))
    con.commit()
    return jsonify({"message": "Korisnik uspešno obrisan"}), 200


@app.route('/korisnici/<int:id>', methods=['GET'])
@jwt_required()
def get_korisnik(id):
    query = "SELECT IDK, ime, prezime, email, uloga FROM korisnik WHERE IDK = %s"
    mycursor.execute(query, (id,))
    korisnik = mycursor.fetchone()  # Vraća jedan korisnik, ne listu
    if korisnik:
        return jsonify(korisnik), 200
    return jsonify({"message": "Korisnik nije pronađen"}), 404


@app.route('/korisnik-izmena/<int:id>', methods=['PUT'])
@jwt_required()
def izmeni_korisnika(id):
    # Uzimanje podataka iz JSON tela zahteva
    data = request.json

    # Provera da li su svi obavezni podaci prisutni
    if not all(key in data for key in ['ime', 'prezime', 'email', 'uloga']):
        return jsonify({"message": "Svi obavezni podaci moraju biti pruženi"}), 400

    # Priprema upita za ažuriranje korisnika
    query = """
        UPDATE korisnik
        SET ime = %s, prezime = %s, email = %s, uloga = %s
        WHERE IDK = %s
    """
    
    # Vrednosti koje se šalju u upit
    values = (data['ime'], data['prezime'], data['email'], data['uloga'], id)

    try:
        # Izvršavanje upita
        mycursor.execute(query, values)
        con.commit()

        # Provera da li je korisnik ažuriran
        if mycursor.rowcount > 0:
            return jsonify({"message": "Korisnik uspešno ažuriran"}), 200
        else:
            return jsonify({"message": "Korisnik sa datim ID-jem nije pronađen"}), 404

    except mysql.connector.Error as err:
        return jsonify({"message": f"Greška u bazi podataka: {err}"}), 500
    
# -----------------------------------------------> Korisnici <-----------------------------------------------------


    
# ------------------------------------------- Projekti -----------------------------------------------------------

@app.route('/projekti', methods=['GET'])
@jwt_required()
def get_projekti():
    query = """
    SELECT IDP, naziv, tip, status, poceo, zavrsio, progres,naziv, opis, tim
    FROM projekat
    """
    mycursor.execute(query)
    projekti = mycursor.fetchall()
    return jsonify(projekti), 200


from datetime import datetime
from flask import request, jsonify
from flask_jwt_extended import jwt_required

@app.route('/projekti', methods=['POST'])
@jwt_required()
def add_projekat():
    # Dohvatite podatke iz POST zahteva
    data = request.json
    print(data)  # Ovo će vam pomoći da proverite koji podaci stižu

    # Pretvorite stringove za 'poceo' i 'zavrsio' u datetime objekte
    poceo = datetime.strptime(data['poceo'], '%Y-%m-%d') if data.get('poceo') else None
    zavrsio = datetime.strptime(data['zavrsio'], '%Y-%m-%d') if data.get('zavrsio') else None

    # Pripremite SQL upit za unos novog projekta u bazu
    query = """
        INSERT INTO projekat (naziv, tip, status, poceo, zavrsio, progres)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    
    # Pripremite vrednosti za unos
    values = (
        data['naziv'],
        data['tip'],
        data['status'],
        poceo,
        zavrsio,
        data['progres']
    )

    # Izvršite upit i sačuvajte promene u bazi
    mycursor.execute(query, values)
    con.commit()

    return jsonify({"message": "Projekat uspešno dodat"}), 201

@app.route('/projekti/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_projekat(id):
    query = "DELETE FROM projekat WHERE IDP = %s"
    mycursor.execute(query, (id,))
    con.commit()
    return jsonify({"message": "Korisnik uspešno obrisan"}), 200


from datetime import datetime
from flask import request, jsonify
from flask_jwt_extended import jwt_required

@app.route('/projekti/<int:id>', methods=['GET'])
@jwt_required()
def get_projekat(id):
    query = """
    SELECT IDP, naziv, tip, status, poceo, zavrsio, progres,tim,opis
    FROM projekat
    WHERE IDP = %s
    """
    mycursor.execute(query, (id,))
    projekat = mycursor.fetchone()  # Use fetchone since we are expecting only one project
    
    if projekat:
        # Convert datetime objects to strings in YYYY-MM-DD format
        if projekat['poceo']:
            projekat['poceo'] = projekat['poceo'].strftime('%Y-%m-%d')
        if projekat['zavrsio']:
            projekat['zavrsio'] = projekat['zavrsio'].strftime('%Y-%m-%d')
        
        # Debugging: Log the entire response to check the status value
        print(projekat)  # This will print the whole project data including 'status'

        return jsonify(projekat), 200
    else:
        return jsonify({"message": "Projekt nije pronađen."}), 404



from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/projekat-izmena/<int:id>', methods=['PUT'])
@jwt_required()
def izmeni_projekat(id):
    # Uzimanje podataka iz JSON tela zahteva
    data = request.json

    # Provera da li su svi obavezni podaci prisutni
    if not all(key in data for key in ['naziv', 'tip', 'status', 'poceo', 'zavrsio', 'progres','tim','opis']):
        return jsonify({"message": "Svi obavezni podaci moraju biti pruženi"}), 400

    # Priprema upita za ažuriranje projekta
    query = """
        UPDATE projekat
        SET naziv = %s, tip = %s, status = %s, poceo = %s, zavrsio = %s, progres = %s,tim = %s,opis = %s
        WHERE IDP = %s
    """

    # Vrednosti koje se šalju u upit
    values = (data['naziv'], data['tip'], data['status'], data['poceo'], data['zavrsio'], data['progres'],data['tim'],data['opis'],id)

    try:
        # Izvršavanje upita
        mycursor.execute(query, values)
        con.commit()

        # Provera da li je projekat ažuriran
        if mycursor.rowcount > 0:
            return jsonify({"message": "Projekat uspešno ažuriran"}), 200
        else:
            return jsonify({"message": "Projekat sa datim ID-jem nije pronađen"}), 404

    except mysql.connector.Error as err:
        return jsonify({"message": f"Greška u bazi podataka: {err}"}), 500
    
    
@app.route('/projekat-info/<int:id>', methods=['GET'])
@jwt_required()
def get_projekatinfo(id):
    query = """
    SELECT IDP, naziv, opis, tim
    FROM projekat
    WHERE IDP = %s
    """
    mycursor.execute(query, (id,))
    projekat = mycursor.fetchone()

    if projekat:
        return jsonify({
            'naziv': projekat['naziv'],
            'opis': projekat['opis'],
            'tim': projekat['tim']
        })
    return jsonify({'error': 'Projekt nije pronađen'}), 404



@app.route('/info-izmena/<int:id>', methods=['PUT'])
@jwt_required()
def izmeni_info(id):
    # Uzimanje podataka iz JSON tela zahteva
    data = request.json

    # Provera da li su svi obavezni podaci prisutni
    if not all(key in data for key in ['naziv', 'opis', 'tim']):
        return jsonify({"message": "Svi obavezni podaci moraju biti pruženi"}), 400

    # Priprema upita za ažuriranje podataka projekta
    query = """
        UPDATE projekat
        SET naziv = %s, opis = %s, tim = %s
        WHERE IDP = %s
    """

    # Vrednosti koje se šalju u upit
    values = (data['naziv'], data['opis'], data['tim'], id)


    try:
        # Izvršavanje upita
        mycursor.execute(query, values)
        con.commit()

        # Provera da li je projekat ažuriran
        if mycursor.rowcount > 0:
            # SELECT upit za povratak ažuriranog projekta
            select_query = "SELECT IDP, naziv, opis, tim FROM projekat WHERE IDP = %s"
            mycursor.execute(select_query, (id,))
            project_data = mycursor.fetchone()  # Dobijanje podataka o projektu

            # Vraćanje ažuriranih podataka
            return jsonify(project_data), 200
        else:
            return jsonify({"message": "Projekat sa datim ID-jem nije pronađen"}), 404

    except mysql.connector.Error as err:
        # Greška u bazi podataka
        return jsonify({"message": f"Greška u bazi podataka: {err}"}), 500

# -------------------------------------------> Projekti <------------------------------------------------------
@app.route('/statistika', methods=['GET'])
@jwt_required()
def get_statistika():
    query = """
    SELECT p.Naziv, pp.Gledanost, pp.Prihodi, pp.Ocena
FROM projekat p
LEFT JOIN popularnostprojekta pp
ON p.IDP = pp.IDP;

    """
    mycursor.execute(query)
    projekti = mycursor.fetchall()
    return jsonify(projekti), 200



@app.route('/statistika/<int:id>', methods=['GET'])
@jwt_required()
def get_stat(id):
    query = """
    SELECT IDP,Gledanost, Prihodi, Ocena
    FROM popularnostprojekta 
    WHERE IDP = %s
    """
    mycursor.execute(query, (id,))
    projekat = mycursor.fetchone()  # fetchone() will return a single record for a specific ID
    if projekat:
        return jsonify({
            'Gledanost': projekat[0],
            'Prihodi': projekat[1],
            'Ocena': projekat[2]
        }), 200
    else:
        return jsonify({'message': 'Projekat nije pronađen.'}), 404


@app.route('/statistika-izmena/<int:id>', methods=['PUT'])
@jwt_required()
def izmeni_stat(id):
    # Uzimanje podataka iz JSON tela zahteva
    data = request.json

    # Provera da li su svi obavezni podaci prisutni
    if not all(key in data for key in ['Gledanost', 'Prihodi', 'Ocena']):
        return jsonify({"message": "Svi obavezni podaci moraju biti pruženi"}), 400

    # Priprema upita za ažuriranje projekta
    query = """
        UPDATE projekat
        SET Gledanost = %s, Prihodi = %s, Ocena = %s
        WHERE IDP = %s
    """

    # Vrednosti koje se šalju u upit
    values = (data['Gledanost'], data['Prihodi'], data['Ocena'],id)

    try:
        # Izvršavanje upita
        mycursor.execute(query, values)
        con.commit()

        # Provera da li je projekat ažuriran
        if mycursor.rowcount > 0:
            return jsonify({"message": "Projekat uspešno ažuriran"}), 200
        else:
            return jsonify({"message": "Projekat sa datim ID-jem nije pronađen"}), 404

    except mysql.connector.Error as err:
        return jsonify({"message": f"Greška u bazi podataka: {err}"}), 500


# -------------------------------------------> Statistika <------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True)
