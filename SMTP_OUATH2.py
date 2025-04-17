from flask import Flask, request, redirect, url_for, session, render_template
from flask_mail import Mail
from requests_oauthlib import OAuth2Session
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import os
import re
import pickle
import base64

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

# Configuración de la clave secreta para sesiones
app.secret_key = 'tu_clave_secreta_segura'

# Variables de entorno para mayor seguridad
CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
SCOPES = ['https://mail.google.com/']

# Configuración del flujo Out-of-Band
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"


@app.route('/login')
def login():
    # Crear la sesión OAuth2
    oauth2_session = OAuth2Session(
        CLIENT_ID,
        redirect_uri=REDIRECT_URI,
        scope=SCOPES
    )

    # Generar la URL de autorización
    authorization_url, state = oauth2_session.authorization_url(
        "https://accounts.google.com/o/oauth2/auth",
        access_type='offline',
        include_granted_scopes='true'
    )

    # Guardar el estado en la sesión para verificarlo después
    session['state'] = state

    # Renderizar la plantilla HTML y pasar la URL de autorización
    return render_template('Login_correo.html', authorization_url=authorization_url)

@app.route('/oauth2callback', methods=['GET', 'POST'])
def oauth2callback():
    if request.method == 'GET':
        # Renderizar el formulario HTML para ingresar el código
        return render_template('Ingresar_codigo.html')
    elif request.method == 'POST':
        # Obtener el código de autorización ingresado por el usuario
        code = request.form.get('code')

        # Crear la sesión OAuth2
        oauth2_session = OAuth2Session(
            CLIENT_ID,
            redirect_uri=REDIRECT_URI,
            scope=SCOPES
        )

        # Intercambiar el código por un token
        token = oauth2_session.fetch_token(
            "https://oauth2.googleapis.com/token",
            code=code,
            client_secret=CLIENT_SECRET
        )

        # Guardar las credenciales en un archivo seguro
        with open('token.pickle', 'wb') as token_file:
            pickle.dump(token, token_file)

        return "Autenticación exitosa. Ahora puedes enviar correos."

def get_credentials():
    # Cargar las credenciales guardadas
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token_file:
            token = pickle.load(token_file)
            creds = Credentials(
                token=token['access_token'],
                refresh_token=token.get('refresh_token'),
                token_uri="https://oauth2.googleapis.com/token",
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                scopes=SCOPES
            )
    return creds

def es_correo_valido(correo):
    # Expresión regular para validar correos electrónicos
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Obtener los datos del formulario
        destinatario = request.form.get('destinatario')
        asunto = request.form.get('asunto')
        cuerpo = request.form.get('cuerpo')

        # Validar el correo electrónico
        if not es_correo_valido(destinatario):
            return "Error: El correo electrónico ingresado no es válido.", 400

        # Redirigir a la ruta de envío de correo con los datos
        return redirect(url_for('enviar_correo', destinatario=destinatario, asunto=asunto, cuerpo=cuerpo))

    # Renderizar el formulario HTML
    return render_template('Formulario_correo.html')


@app.route('/enviar_correo')
def enviar_correo():
    # Obtener los datos del formulario desde los parámetros de la URL
    destinatario = request.args.get('destinatario')
    asunto = request.args.get('asunto')
    cuerpo = request.args.get('cuerpo')

    creds = get_credentials()
    if not creds:
        return redirect('/login')

    try:
        # Crear el servicio de Gmail con las credenciales obtenidas
        service = build('gmail', 'v1', credentials=creds)

        # Crear el mensaje en formato MIME
        mensaje = MIMEText(cuerpo)
        mensaje['to'] = destinatario
        mensaje['subject'] = asunto

        # Codificar el mensaje en base64
        raw_message = base64.urlsafe_b64encode(mensaje.as_bytes()).decode('utf-8')
        message = {'raw': raw_message}

        # Enviar el mensaje
        send_message = service.users().messages().send(userId="me", body=message).execute()
        return f"Correo enviado a {destinatario}: {send_message['id']}"
    except Exception as error:
        return f"Error al enviar el correo: {error}"

if __name__ == '__main__':
    app.run(debug=True)