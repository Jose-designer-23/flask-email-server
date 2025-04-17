``
# flask-email-server

Este es un servidor de correo electrónico simple desarrollado con Flask y la librería `google-api-python-client` para enviar correos electrónicos utilizando la API de Gmail a través de la autenticación OAuth2.

## Requisitos Previos:

* **Python:** Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **pip:** `pip` es el gestor de paquetes de Python, que probablemente ya esté instalado si tienes una versión reciente de Python. Lo necesitarás para instalar las dependencias del proyecto. Puedes verificar si lo tienes instalado abriendo tu terminal o símbolo del sistema y ejecutando `pip --version`. Si no está instalado, puedes seguir las instrucciones en [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).
* **Dependencias:** Este proyecto utiliza varias librerías de Python que están listadas en el archivo `requirements.txt`. Una vez que tengas Python y `pip` instalados, deberás instalar estas dependencias. Abre tu terminal o símbolo del sistema, navega al directorio donde clonaste el repositorio y ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Configuración en Google Cloud:

1.  **Crear la cuenta de Google Cloud:** Deberás ir a la página de Google Cloud Platform ([https://cloud.google.com/](https://cloud.google.com/)) y seguir el proceso para crear una cuenta. Esto generalmente implica aceptar los términos de servicio y configurar un perfil de facturación (aunque puedas optar por la capa gratuita, te pedirán información de pago para verificar tu identidad).

    > **Nota importante:** Para utilizar este servidor de correo, necesitarás configurar una cuenta en Google Cloud. Google Cloud generalmente requiere la configuración de información de facturación, incluso para acceder a la capa gratuita. Por favor, revisa la documentación de la capa gratuita de Google Cloud para entender los límites de uso.

2.  **Crear un nuevo proyecto en Google Cloud:** Una vez que tengas tu cuenta, crea un nuevo proyecto. Dale un nombre descriptivo.

3.  **Habilitar la API de Gmail:**
    * Ve a la sección de "APIs y servicios" en tu proyecto de Google Cloud.
    * Haz clic en "+ HABILITAR APIS Y SERVICIOS".
    * Busca "Gmail API" y habilítala.

4.  **Configurar la pantalla de consentimiento de OAuth:**
    * Ve a "APIs y servicios" -> "Credenciales" -> "Pantalla de consentimiento de OAuth".
    * Selecciona el "Tipo de usuario" como "Externo" (a menos que tu organización tenga requisitos específicos).
    * Completa la información requerida (Nombre de la aplicación, correo electrónico de asistencia del usuario, etc.).
    * En la sección de "Alcances", haz clic en "+ AÑADIR ALCANCES" y busca y selecciona `https://mail.google.com/`. Guarda los cambios.

5.  **Crear credenciales de OAuth 2.0:**
    * Ve a "APIs y servicios" -> "Credenciales".
    * Haz clic en "+ CREAR CREDENCIALES" y selecciona "ID de cliente de OAuth".
    * Selecciona el "Tipo de aplicación" como "Aplicación web".
    * Dale un nombre a tu cliente OAuth 2.0 (por ejemplo, "Servidor de Correo Flask").
    * En "URI de redireccionamiento autorizados", puedes dejarlo en blanco por ahora, ya que esta aplicación es un backend.
    * Haz clic en "CREAR".
    * Se generará tu "ID de cliente" y tu "Secreto de cliente". **Descarga estas credenciales en formato JSON y guárdalas en un lugar seguro.**

## Configuración de Variables de Entorno:

* Deberás configurar las siguientes variables de entorno en tu sistema operativo:
    * **En Windows:**
        1.  Abre el "Panel de Control".
        2.  Ve a "Sistema y seguridad" -> "Sistema".
        3.  Haz clic en "Configuración avanzada del sistema" en la barra lateral izquierda.
        4.  En la ventana emergente, haz clic en el botón "Variables de entorno...".
        5.  En la sección de "Variables de usuario" o "Variables del sistema", haz clic en "Nuevo..." para cada variable:
            * **Nombre de la variable:** `GOOGLE_CLIENT_ID`
                **Valor de la variable:** Tu ID de cliente de Google Cloud.
            * **Nombre de la variable:** `GOOGLE_CLIENT_SECRET`
                **Valor de la variable:** Tu secreto de cliente de Google Cloud.
        6.  Haz clic en "Aceptar" en todas las ventanas para guardar los cambios. **Es posible que necesites reiniciar tu terminal o IDE para que los cambios en las variables de entorno se hagan efectivos.**

* Tu aplicación Flask leerá estas variables de entorno directamente desde tu sistema operativo para autenticarse con Google Cloud.

## Cómo Ejecutar el Servidor:

Una vez que hayas configurado las variables de entorno y hayas instalado todas las dependencias, puedes ejecutar el servidor Flask con el siguiente comando desde la raíz del directorio del proyecto:

```bash
python SMTP_OUATH2.py
```

Una vez que el servidor se esté ejecutando, podrás acceder a la página de inicio de sesión de la aplicación abriendo tu navegador en la siguiente dirección:

```
http://localhost:5000/login
```

Desde ahí, podrás interactuar con las funcionalidades de envío de correo electrónico.

## Funcionalidades:

Este servidor de correo electrónico Flask permite a los usuarios enviar correos electrónicos a través de una interfaz web simple. La página principal ofrece las siguientes opciones:

1.  **Autorizar aplicación:** Esta función guía al usuario para autorizar la cuenta de correo electrónico que se añadió previamente en los usuarios de prueba de la cuenta de Google Cloud. Al hacer clic en "Continuar" en la pantalla de consentimiento, se proporciona un código que debe ser copiado.

2.  **Ingresar código:** En esta sección, el usuario pega el código copiado en el paso anterior y hace clic en "Enviar". Un mensaje confirmará si la autenticación ha sido exitosa, indicando que ya se pueden enviar correos electrónicos.

3.  **Formulario de mensajes:** Al acceder a esta opción ("Ir al formulario de mensajes"), el usuario encontrará campos para ingresar el correo electrónico del destinatario, el asunto del correo y el cuerpo del mensaje que desea enviar. Al finalizar y enviar el formulario, se mostrará una confirmación indicando si el correo se ha enviado correctamente.

## Próximas Mejoras:

* Soporte para adjuntar archivos a los correos electrónicos.

## Licencia:

MIT License

## Autor:

Jose-designer-23
```
