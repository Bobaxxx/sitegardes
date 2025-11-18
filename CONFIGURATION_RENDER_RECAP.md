# 📋 Configuration Render - Récapitulatif Rapide

## 🚀 Configuration du Service

### Paramètres de Base
```
Name: sitegardes-v2
Region: Frankfurt
Branch: master
Root Directory: (vide)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Instance Type: Free
```

---

## 🔐 Variables d'Environnement à Configurer

### ⚠️ IMPORTANT : Copiez-collez ces valeurs dans Render

| Variable | Valeur | Notes |
|----------|--------|-------|
| `PYTHON_VERSION` | `3.11.0` | Version Python |
| `SECRET_KEY` | *(générer dans Render)* | Cliquez sur "Generate" |
| `SENDGRID_API_KEY` | `[À REMPLIR]` | Votre clé API SendGrid |
| `CONTACT_EMAIL` | `[À REMPLIR]` | Email de réception |
| `FROM_EMAIL` | `[À REMPLIR]` | Email expéditeur (vérifié dans SendGrid) |
| `FROM_NAME` | `Pascal Gardes` | Nom de l'expéditeur |
| `SENDGRID_HOST` | *(laisser vide)* | Optionnel |

---

## 📝 Instructions Rapides

### 1. Créer le Service
1. Render Dashboard → "New +" → "Web Service"
2. Connecter le repo `Bobaxxx/sitegardes`
3. Remplir les paramètres ci-dessus
4. Cliquer "Create Web Service"

### 2. Configurer les Variables
1. Aller dans "Environment"
2. Ajouter chaque variable une par une
3. Pour `SECRET_KEY`, cliquer sur "Generate"

### 3. Récupérer SendGrid API Key
1. Aller sur https://app.sendgrid.com
2. Settings → API Keys
3. Créer ou récupérer une clé
4. ⚠️ Copier immédiatement (ne sera plus visible)

### 4. Vérifier FROM_EMAIL dans SendGrid
1. SendGrid → Settings → Sender Authentication
2. Vérifier votre email ou domaine
3. ⚠️ Obligatoire pour envoyer des emails

---

## 📦 Dépendances (requirements.txt)

```
Flask==3.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
sendgrid==6.11.0
```

---

## 🌐 Configuration Domaine Personnalisé

### Après le déploiement

1. Settings → Custom Domains → Add Custom Domain
2. Entrer votre domaine (ex: `pascalgardes.fr`)
3. Configurer le DNS selon les instructions Render
4. Attendre 15-30 minutes pour la propagation
5. SSL configuré automatiquement par Render

---

## ✅ Checklist Rapide

- [ ] Service créé
- [ ] Variables d'environnement configurées
- [ ] SendGrid API Key ajoutée
- [ ] FROM_EMAIL vérifié dans SendGrid
- [ ] Service déployé
- [ ] Site accessible
- [ ] Formulaire de contact testé
- [ ] Domaine personnalisé configuré (si nécessaire)

---

## 🔗 URLs

- **Service Render :** `https://sitegardes-v2.onrender.com`
- **Domaine personnalisé :** `https://pascalgardes.fr` (après configuration)

---

**💡 Astuce :** Gardez ce fichier ouvert pendant la configuration pour copier-coller facilement !

