from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='.', static_folder='.')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Configuration email
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'contact@example.com')
FROM_EMAIL = os.environ.get('FROM_EMAIL', 'contact@example.com')
FROM_NAME = os.environ.get('FROM_NAME', 'Pascal Gardes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_redirect():
    return redirect('/')

@app.route('/services.html')
def services():
    return render_template('services.html')

@app.route('/realisations.html')
def realisations():
    return render_template('realisations.html')

@app.route('/mentions-legales.html')
def mentions_legales():
    return render_template('mentions-legales.html')

@app.route('/confidentialite.html')
def confidentialite():
    return render_template('confidentialite.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        telephone = request.form.get('telephone', '')
        sujet = request.form.get('sujet')
        message = request.form.get('message')
        rgpd = request.form.get('rgpd')
        
        # Validation
        if not all([nom, prenom, email, sujet, message]):
            flash('Veuillez remplir tous les champs obligatoires.', 'error')
            return redirect(url_for('contact'))
        
        # Vérification RGPD
        if not rgpd:
            flash('Vous devez accepter la politique de confidentialité pour envoyer votre message.', 'error')
            return redirect(url_for('contact'))
        
        # Envoyer l'email via SendGrid
        try:
            if not SENDGRID_API_KEY:
                flash('Configuration email manquante.', 'error')
                return redirect(url_for('contact'))
            
            import sendgrid
            from sendgrid.helpers.mail import Mail
            
            sendgrid_host = os.environ.get('SENDGRID_HOST')
            if sendgrid_host:
                sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY, host=sendgrid_host)
            else:
                sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
            
            html_content = f"""
            <h2>Nouveau message de contact</h2>
            <p><strong>Nom:</strong> {nom} {prenom}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Téléphone:</strong> {telephone or 'Non renseigné'}</p>
            <p><strong>Sujet:</strong> {sujet}</p>
            <hr>
            <p><strong>Message:</strong></p>
            <p>{message.replace(chr(10), '<br>')}</p>
            """
            
            text_content = f"""
Nouveau message de contact

Nom: {nom} {prenom}
Email: {email}
Téléphone: {telephone or 'Non renseigné'}
Sujet: {sujet}

Message:
{message}
"""
            
            message = Mail(
                from_email=(FROM_EMAIL, FROM_NAME),
                to_emails=CONTACT_EMAIL,
                subject=f"Contact Pascal Gardes: {sujet}",
                html_content=html_content,
                plain_text_content=text_content
            )
            
            sg.send(message)
            
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

# Servir le fichier JSON des réalisations
@app.route('/content/all_realisations.json')
def all_realisations():
    return send_from_directory('content', 'all_realisations.json', mimetype='application/json')

# Servir robots.txt
@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt', mimetype='text/plain')

# Servir sitemap.xml
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

@app.route('/<path:filename>')
def static_files(filename):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg')):
        return send_from_directory('.', filename)
    return '', 404

# Route spécifique pour le favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'rogné v2 logo gardes .png', mimetype='image/png')

# Route pour servir le logo directement
@app.route('/rogné v2 logo gardes .png')
def logo():
    return send_from_directory('.', 'rogné v2 logo gardes .png', mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

