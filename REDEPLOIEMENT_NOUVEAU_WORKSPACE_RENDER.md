# 🔄 Redéploiement dans un Nouveau Workspace Render

## 📋 Pourquoi ce guide ?

Vous avez atteint la limite de domaines personnalisés gratuits sur votre workspace Render actuel. Ce guide vous permet de créer un nouveau service dans un nouveau workspace pour avoir un nouveau quota de domaines.

---

## 🎯 ÉTAPE 1 : Créer un Nouveau Service sur Render

### 1.1 Accéder à Render

1. Allez sur **https://dashboard.render.com**
2. Si vous avez plusieurs workspaces, vous pouvez :
   - Créer un nouveau workspace (optionnel)
   - OU utiliser un workspace existant différent

### 1.2 Créer le Nouveau Service

1. Cliquez sur **"New +"** en haut à droite
2. Sélectionnez **"Web Service"**
3. Connectez votre repository GitHub :
   - Si pas encore connecté : **"Connect account"** → Autorisez Render
   - Sélectionnez le repository : **`Bobaxxx/sitegardes`** (ou votre repo)

---

## ⚙️ ÉTAPE 2 : Configuration du Service

### 2.1 Paramètres de Base

```
Name: sitegardes-v2
     (ou sitegardes-new, ou tout autre nom unique)

Region: Frankfurt (Europe)
       (ou la région la plus proche de vos visiteurs)

Branch: master
       (ou la branche principale de votre repo)

Root Directory: (LAISSER VIDE)
               (le code est à la racine du repo)

Runtime: Python 3

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app
```

### 2.2 Plan

```
Instance Type: Free
              (ou Starter $7/mois si vous voulez éviter la mise en veille)
```

---

## 🔐 ÉTAPE 3 : Variables d'Environnement

**⚠️ IMPORTANT :** Vous devez configurer TOUTES ces variables dans le nouveau service.

### 3.1 Dans Render Dashboard

1. Après avoir créé le service, allez dans **"Environment"** (menu de gauche)
2. Cliquez sur **"Add Environment Variable"**
3. Ajoutez chaque variable une par une :

### 3.2 Liste Complète des Variables

| Key | Value | Description |
|-----|-------|-------------|
| `PYTHON_VERSION` | `3.11.0` | Version de Python |
| `SECRET_KEY` | *(générer)* | Clé secrète Flask (cliquez sur "Generate" dans Render) |
| `SENDGRID_API_KEY` | `[VOTRE_CLÉ]` | Clé API SendGrid pour l'envoi d'emails |
| `CONTACT_EMAIL` | `[VOTRE_EMAIL]` | Email où recevoir les messages du formulaire |
| `FROM_EMAIL` | `[VOTRE_EMAIL]` | Email expéditeur (doit être vérifié dans SendGrid) |
| `FROM_NAME` | `Pascal Gardes` | Nom de l'expéditeur |
| `SENDGRID_HOST` | *(optionnel)* | Host SendGrid si nécessaire (laisser vide si pas besoin) |

### 3.3 Comment Récupérer vos Valeurs

#### **SECRET_KEY**
- Dans Render, quand vous ajoutez la variable, cliquez sur **"Generate"** à côté du champ
- OU générez-en une vous-même : https://randomkeygen.com/ (utilisez "CodeIgniter Encryption Keys")

#### **SENDGRID_API_KEY**
- Allez sur https://app.sendgrid.com
- **Settings** → **API Keys**
- Créez une nouvelle clé ou récupérez votre clé existante
- ⚠️ **Copiez-la immédiatement**, elle ne sera plus visible après !

#### **CONTACT_EMAIL et FROM_EMAIL**
- Utilisez l'email où vous voulez recevoir les messages
- Exemple : `contact@pascalgardes.fr` ou `gpserrurerie@outlook.fr`
- ⚠️ **FROM_EMAIL doit être vérifié dans SendGrid** :
  - Allez sur SendGrid → **Settings** → **Sender Authentication**
  - Vérifiez votre email ou domaine

#### **SENDGRID_HOST**
- Généralement **LAISSER VIDE**
- À remplir seulement si SendGrid vous a donné un host spécifique

---

## 🚀 ÉTAPE 4 : Déployer

### 4.1 Créer le Service

1. Vérifiez que toutes les variables sont configurées
2. Cliquez sur **"Create Web Service"**
3. Render va :
   - Cloner votre repo
   - Installer les dépendances
   - Démarrer le service

### 4.2 Vérifier le Déploiement

1. Attendez 2-3 minutes
2. Dans les **"Logs"**, vous devriez voir :
   ```
   Running on http://0.0.0.0:10000
   ```
3. L'URL du service sera : `https://sitegardes-v2.onrender.com` (ou le nom que vous avez choisi)

### 4.3 Tester le Site

1. Cliquez sur l'URL du service
2. Vérifiez que :
   - ✅ La page d'accueil s'affiche
   - ✅ Les images se chargent
   - ✅ Le formulaire de contact fonctionne
   - ✅ Les réalisations s'affichent

---

## 🌐 ÉTAPE 5 : Configurer le Domaine Personnalisé

### 5.1 Ajouter le Domaine dans Render

1. Dans votre nouveau service, allez dans **"Settings"**
2. Scrollez jusqu'à **"Custom Domains"**
3. Cliquez sur **"Add Custom Domain"**
4. Entrez votre domaine (ex: `pascalgardes.fr`)

### 5.2 Configurer le DNS

Render vous donnera les instructions DNS. Généralement :

#### **Pour le domaine racine (pascalgardes.fr) :**
```
Type: A
Nom: @ (ou laissez vide)
Valeur: [IP fournie par Render]
TTL: 3600
```

#### **Pour www (www.pascalgardes.fr) :**
```
Type: CNAME
Nom: www
Valeur: sitegardes-v2.onrender.com (ou la valeur fournie)
TTL: 3600
```

### 5.3 Attendre la Propagation

- ⏳ 15-30 minutes généralement
- Vérifiez avec : https://dnschecker.org
- Render configurera automatiquement le SSL (HTTPS)

---

## 🔄 ÉTAPE 6 : Mettre à Jour le Code (si nécessaire)

### 6.1 Lien Canonical

Si vous avez un lien canonical dans `index.html`, mettez-le à jour :

**Fichier : `index.html` (ligne 15)**

```html
<!-- Avant -->
<link rel="canonical" href="https://bobaxxx.github.io/sitegardes/"/>

<!-- Après -->
<link rel="canonical" href="https://pascalgardes.fr/"/>
```

### 6.2 Autres URLs Codées en Dur

Vérifiez s'il y a d'autres URLs à mettre à jour dans le code.

---

## 📝 ÉTAPE 7 : Ancien Service (Optionnel)

### 7.1 Garder l'Ancien Service

- Vous pouvez garder l'ancien service actif pendant la transition
- Cela permet de tester le nouveau avant de couper l'ancien

### 7.2 Supprimer l'Ancien Service

Une fois que tout fonctionne sur le nouveau service :

1. Allez sur l'ancien service dans Render
2. **Settings** → **Delete Service**
3. ⚠️ **Attention :** Cette action est irréversible !

---

## ✅ Checklist Complète

### Configuration Render
- [ ] Nouveau service créé
- [ ] Repository GitHub connecté
- [ ] Build Command : `pip install -r requirements.txt`
- [ ] Start Command : `gunicorn app:app`
- [ ] Plan sélectionné (Free ou Starter)

### Variables d'Environnement
- [ ] `PYTHON_VERSION` = `3.11.0`
- [ ] `SECRET_KEY` générée
- [ ] `SENDGRID_API_KEY` configurée
- [ ] `CONTACT_EMAIL` configuré
- [ ] `FROM_EMAIL` configuré (et vérifié dans SendGrid)
- [ ] `FROM_NAME` = `Pascal Gardes`
- [ ] `SENDGRID_HOST` configuré (si nécessaire)

### Déploiement
- [ ] Service déployé avec succès
- [ ] Logs montrent "Running on http://0.0.0.0:XXXX"
- [ ] Site accessible via l'URL Render
- [ ] Page d'accueil fonctionne
- [ ] Images se chargent
- [ ] Formulaire de contact fonctionne

### Domaine Personnalisé
- [ ] Domaine ajouté dans Render
- [ ] Enregistrements DNS configurés
- [ ] DNS propagé (vérifié sur dnschecker.org)
- [ ] SSL actif (cadenas vert)
- [ ] Site accessible via le domaine personnalisé

### Code
- [ ] Lien canonical mis à jour (si nécessaire)
- [ ] Autres URLs mises à jour (si nécessaire)

---

## 🐛 Dépannage

### Le service ne démarre pas

1. **Vérifiez les logs** dans Render
2. **Erreur "Module not found"** :
   - Vérifiez que `requirements.txt` contient toutes les dépendances
   - Vérifiez le Build Command

### Le formulaire de contact ne fonctionne pas

1. **Vérifiez les variables d'environnement** :
   - `SENDGRID_API_KEY` est-elle correcte ?
   - `FROM_EMAIL` est-il vérifié dans SendGrid ?
   - `CONTACT_EMAIL` est-il valide ?

2. **Vérifiez les logs** pour voir les erreurs

### Le domaine ne fonctionne pas

1. **Vérifiez le DNS** sur dnschecker.org
2. **Attendez 30-60 minutes** pour la propagation
3. **Vérifiez dans Render** que le domaine est bien ajouté

---

## 📊 Résumé des Informations

### Configuration du Service
```
Name: sitegardes-v2
Region: Frankfurt
Branch: master
Build: pip install -r requirements.txt
Start: gunicorn app:app
```

### Variables Requises
```
PYTHON_VERSION=3.11.0
SECRET_KEY=[généré]
SENDGRID_API_KEY=[votre clé]
CONTACT_EMAIL=[votre email]
FROM_EMAIL=[votre email vérifié]
FROM_NAME=Pascal Gardes
SENDGRID_HOST=[optionnel]
```

### Dépendances (requirements.txt)
```
Flask==3.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
sendgrid==6.11.0
```

---

## 🆘 Besoin d'Aide ?

Si vous rencontrez des problèmes :
1. Vérifiez les logs dans Render
2. Vérifiez que toutes les variables sont configurées
3. Testez le formulaire de contact
4. Contactez le support Render si nécessaire

---

**🎉 Une fois tout configuré, votre site sera accessible via votre nouveau service Render avec votre domaine personnalisé !**

