# flask-email-server

This is a simple email server developed with Flask and the `google-api-python-client` library for sending emails using the Gmail API via OAuth2 authentication.

## Prerequisites:

* **Python:** Make sure you have Python 3 installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **pip:** `pip` is the Python package manager, which is likely already installed if you have a recent version of Python. You'll need it to install the project's dependencies. You can check if you have it installed by opening your terminal or command prompt and running `pip --version`. If it's not installed, you can follow the instructions at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).
* **Dependencies:** This project uses several Python libraries that are listed in the `requirements.txt` file. Once you have Python and `pip` installed, you'll need to install these dependencies. Open your terminal or command prompt, navigate to the directory where you cloned the repository, and run the following command:

```bash
pip install -r requirements.txt
```

## Setup on Google Cloud:

1. **Create a Google Cloud account:** You'll need to go to the Google Cloud Platform page ([https://cloud.google.com/](https://cloud.google.com/)) and follow the process to create an account. This usually involves accepting the terms of service and setting up a billing profile (even if you opt for the free tier, you'll be asked for payment information to verify your identity).

> **Important Note:** To use this mail server, you'll need to set up a Google Cloud account. Google Cloud generally requires billing information to be set up, even to access the free tier. Please review the Google Cloud Free Tier documentation to understand usage limits.

2. **Create a new Google Cloud project:** Once you have your account, create a new project. Give it a descriptive name.

3. **Enable the Gmail API:**
* Go to the "APIs and Services" section in your Google Cloud project.
* Click "+ ENABLE APIS AND SERVICES".
* Search for "Gmail API" and enable it.

4. **Configure the OAuth consent screen:**
* Go to "APIs & Services" -> "Credentials" -> "OAuth Consent Screen".
* Select the "User Type" as "External" (unless your organization has specific requirements).
* Complete the required information (App name, user support email, etc.).
* In the "Scopes" section, click "+ ADD SCOPES" and search for and select 'https://mail.google.com/'. Save the changes.

5. **Create OAuth 2.0 credentials:**
* Go to "APIs & Services" -> "Credentials".
* Click "+ CREATE CREDENTIALS" and select "OAuth Client ID".
* Select the "Application Type" as "Web Application".
* Give your OAuth 2.0 client a name (for example, "Flask Mail Server").
* Under "Authorized Redirect URIs," you can leave it blank for now, as this application is a backend.
* Click "CREATE."
* Your "Client ID" and "Client Secret" will be generated. **Download these credentials in JSON format and store them in a safe place.**

## Setting Environment Variables:

* You'll need to configure the following environment variables on your operating system:
* **On Windows:**
1. Open the "Control Panel."
2. Go to "System and Security" -> "System."
3. Click "Advanced system settings" in the left sidebar.
4. In the pop-up window, click the "Environment Variables..." button.
5. In the "User Variables" or "System Variables" section, click "New..." for each variable:
* **Variable name:** `GOOGLE_CLIENT_ID`
**Variable value:** Your Google Cloud Client ID.
* **Variable name:** `GOOGLE_CLIENT_SECRET`
**Variable value:** Your Google Cloud Client Secret.
6. Click "OK" in all windows to save the changes. **You may need to restart your terminal or IDE for the environment variable changes to take effect.**

* Your Flask application will read these environment variables directly from your operating system to authenticate with Google Cloud.

## How to Run the Server:

Once you've set up the environment variables and installed all the dependencies, you can run the Flask server with the following command from the root of the project directory:

```bash
python SMTP_OUATH2.py

Once the server is running, you can access the application's login page by opening your browser at the following address:

```
http://localhost:5000/login
```

From there, you can interact with the email sending features.

## Features:

This Flask email server enables users to send emails through a straightforward web interface. The main page presents the following options:

1.  **Authorize Application:** This function guides the user to authorize the email account that was previously added as a test user in the Google Cloud account. After clicking "Continue" on the consent screen, a code will be provided, which the user must copy.

2.  **Enter Code:** In this section, the user pastes the copied code from the previous step and clicks "Submit." A confirmation message will indicate whether the authentication was successful, confirming that emails can now be sent.

3.  **Message Form:** By selecting "Go to Message Form," the user will find fields to input the recipient's email address, the email subject, and the body of the message. Upon completing and submitting the form, a confirmation will appear indicating whether the email was sent successfully.


## Upcoming Improvements:

* Support for attaching files to emails.

## License:

MIT License

## Author:

Jose-designer-23

