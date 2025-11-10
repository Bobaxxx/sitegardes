# 🎨 PHASE 2 : INSTALLATION INTERFACE ADMIN (DÉTAILLÉE)

## 🎯 OBJECTIF
Installer Decap CMS pour avoir une interface graphique type WordPress permettant au propriétaire de modifier facilement les photos et contenus du site.

---

## 📋 DEUX MÉTHODES POSSIBLES

### 🟢 MÉTHODE A : GitHub OAuth (RECOMMANDÉE - GRATUIT)
- ✅ Totalement gratuit
- ✅ Authentification via GitHub
- ✅ Configuration simple
- ⚠️ Nécessite un compte GitHub pour chaque utilisateur

### 🔵 MÉTHODE B : Netlify Identity (PLUS CONVIVIAL)
- ✅ Interface de connexion email/mot de passe
- ✅ Pas besoin de comprendre GitHub
- ✅ Invitation par email
- ⚠️ Nécessite un compte Netlify (gratuit)
- ⚠️ Configuration un peu plus longue

**Je vous explique les DEUX méthodes en détail :**

---

# 🟢 MÉTHODE A : GITHUB OAUTH (GRATUIT & SIMPLE)

## ✅ AVANTAGES
- Entièrement gratuit
- Pas besoin de service externe
- Fonctionne directement avec GitHub
- Configuration en 10 minutes

## ⚙️ ÉTAPES DÉTAILLÉES

### **Étape A.1 : Créer une GitHub OAuth App**

1. Allez sur : **https://github.com/settings/developers**
2. Cliquez sur **"OAuth Apps"** dans le menu de gauche
3. Cliquez sur le bouton vert **"New OAuth App"**
4. Remplissez le formulaire :

```
Application name: Pascal Gardes Site Admin
Homepage URL: https://bobaxxx.github.io/sitegardes
Application description: Interface d'administration pour le site Pascal Gardes
Authorization callback URL: https://api.netlify.com/auth/done
```

5. Cliquez sur **"Register application"**

6. Vous arrivez sur une page avec :
   - **Client ID** (visible directement) → COPIEZ-LE
   - Cliquez sur **"Generate a new client secret"**
   - **Client Secret** apparaît → COPIEZ-LE IMMÉDIATEMENT (ne sera plus visible)

**📝 NOTEZ CES 2 VALEURS :**
```
Client ID: Iv1.xxxxxxxxxxxx
Client Secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### **Étape A.2 : Créer un service d'authentification**

**PROBLÈME :** Le Client Secret ne peut pas être mis dans le code (sécurité).

**SOLUTION :** Utiliser un service proxy gratuit.

**Option 1 : Utiliser Netlify (même sans héberger dessus)**

1. Allez sur : https://app.netlify.com
2. Connectez-vous avec GitHub
3. Cliquez **"Add new site"** → **"Import an existing project"**
4. Sélectionnez GitHub → `Bobaxxx/sitegardes`
5. Settings :
   ```
   Build command: (laisser vide)
   Publish directory: / 
   ```
6. Cliquez **"Deploy site"**
7. Une fois déployé, allez dans **"Site settings"**
8. Dans le menu : **"Access control"** → **"OAuth"**
9. Sous **"Authentication providers"**, cliquez **"Install provider"**
10. Sélectionnez **"GitHub"**
11. Collez votre **Client ID** et **Client Secret**
12. Cliquez **"Install"**

**✅ Authentification configurée !**

---

### **Étape A.3 : Mettre à jour la configuration CMS**

Je vais créer un fichier config.yml mis à jour :

**Fichier `admin/config.yml` :**
```yaml
backend:
  name: github
  repo: Bobaxxx/sitegardes
  branch: master

# Pour utiliser via Netlify OAuth
site_url: https://bobaxxx.github.io/sitegardes
# OU si vous déployez aussi sur Netlify :
# site_url: https://votre-site.netlify.app

media_folder: "images/realisations"
public_folder: "images/realisations"

# Reste de la config déjà créée...
```

---

### **Étape A.4 : Tester l'admin**

1. Allez sur : **https://bobaxxx.github.io/sitegardes/admin/**
2. Cliquez **"Login with GitHub"**
3. Autorisez l'application
4. ✅ Vous entrez dans l'interface admin !

---

---

# 🔵 MÉTHODE B : NETLIFY IDENTITY (PLUS CONVIVIAL)

## ✅ AVANTAGES
- Interface de connexion email/mot de passe (pas besoin de GitHub)
- Invitation d'utilisateurs par email
- Parfait pour quelqu'un qui ne connaît pas GitHub
- Gestion des utilisateurs simplifiée

## ⚙️ ÉTAPES DÉTAILLÉES

### **Étape B.1 : Créer un compte Netlify**

1. Allez sur : **https://app.netlify.com/signup**
2. Cliquez sur **"Sign up with GitHub"**
3. Connectez-vous avec votre compte GitHub
4. Autorisez Netlify à accéder à GitHub
5. ✅ Compte créé !

---

### **Étape B.2 : Déployer le site sur Netlify**

6. Sur Netlify, cliquez **"Add new site"** → **"Import an existing project"**
7. Cliquez sur **"Deploy with GitHub"**
8. Cherchez et sélectionnez **"sitegardes"** dans la liste
9. Paramètres de build :
   ```
   Branch to deploy: master
   Build command: (laisser vide)
   Publish directory: /
   ```
10. Cliquez **"Deploy bobaxxx-sitegardes"** (ou le nom proposé)
11. ⏳ Attendez 1-2 minutes
12. ✅ Site déployé ! Vous avez maintenant 2 URLs :
    - GitHub Pages : `https://bobaxxx.github.io/sitegardes/`
    - Netlify : `https://nom-aleatoire-123.netlify.app/`

---

### **Étape B.3 : Activer Netlify Identity**

13. Sur votre site Netlify, cliquez sur **"Site configuration"**
14. Dans le menu de gauche : **"Identity"**
15. Cliquez sur **"Enable Identity"**
16. ✅ Identity activé !

---

### **Étape B.4 : Activer Git Gateway**

17. Toujours dans **"Identity"**, scrollez jusqu'à **"Services"**
18. Trouvez **"Git Gateway"** et cliquez **"Enable Git Gateway"**
19. ✅ Git Gateway activé !

**🎉 L'interface admin est maintenant fonctionnelle !**

---

### **Étape B.5 : Ajouter le script Identity au site**

Je vais ajouter un script dans toutes vos pages HTML :

<function_calls>
<invoke name="search_replace">
<parameter name="file_path">/Users/julesmarcon/Documents/sitegardes/index.html
