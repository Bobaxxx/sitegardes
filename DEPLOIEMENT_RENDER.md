# Déploiement sur Render

## Configuration requise

### Variables d'environnement à configurer sur Render :

1. **SECRET_KEY** : Générée automatiquement par Render (ou définissez-en une)
2. **SMTP_SERVER** : Serveur SMTP (ex: `smtp.gmail.com`)
3. **SMTP_PORT** : Port SMTP (généralement `587`)
4. **SMTP_USER** : Votre adresse email pour l'envoi
5. **SMTP_PASSWORD** : Mot de passe d'application (pas le mot de passe normal)
6. **CONTACT_EMAIL** : Email où recevoir les messages du formulaire

### Configuration Gmail (exemple)

1. Activez l'authentification à 2 facteurs sur votre compte Gmail
2. Générez un mot de passe d'application :
   - Allez dans Paramètres Google > Sécurité
   - Activez la validation en 2 étapes
   - Créez un mot de passe d'application
   - Utilisez ce mot de passe dans `SMTP_PASSWORD`

### Déploiement

1. Connectez votre dépôt GitHub à Render
2. Sélectionnez le service "Web Service"
3. Render détectera automatiquement le `render.yaml`
4. Configurez les variables d'environnement dans le dashboard Render
5. Déployez !

Le site sera accessible à l'URL fournie par Render.

