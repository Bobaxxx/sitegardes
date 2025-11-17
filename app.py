from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='.', static_folder='.')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration email
SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))
SMTP_USER = os.environ.get('SMTP_USER')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'contact@example.com')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/realisations.html')
def realisations():
    return render_template('realisations.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        telephone = request.form.get('telephone', '')
        sujet = request.form.get('sujet')
        message = request.form.get('message')
        
        # Validation
        if not all([nom, prenom, email, sujet, message]):
            flash('Veuillez remplir tous les champs obligatoires.', 'error')
            return redirect(url_for('contact'))
        
        # Envoyer l'email
        try:
            msg = MIMEMultipart()
            msg['From'] = SMTP_USER
            msg['To'] = CONTACT_EMAIL
            msg['Subject'] = f"Contact Pascal Gardes: {sujet}"
            
            body = f"""
Nouveau message de contact

Nom: {nom} {prenom}
Email: {email}
Téléphone: {telephone or 'Non renseigné'}
Sujet: {sujet}

Message:
{message}
"""
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            flash('Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.', 'success')
        except Exception as e:
            print(f"Erreur envoi email: {e}")
            flash('Une erreur est survenue lors de l\'envoi. Veuillez réessayer ou nous contacter directement.', 'error')
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# Servir les fichiers statiques (images, etc.)
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/<path:filename>')
def static_files(filename):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg')):
        return send_from_directory('.', filename)
    return '', 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

