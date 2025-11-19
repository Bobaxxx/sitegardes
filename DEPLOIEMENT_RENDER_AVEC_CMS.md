# 🚀 Déploiement sur Render : Site + CMS

## 📋 Structure

Vous avez deux projets séparés :
- **`sitegardes/`** : Site web Flask (Pascal Gardes)
- **`cmsadmin/`** : CMS Admin (gestion de contenu)

## 🎯 Solution : Deux services Render séparés

Render ne peut pas déployer deux services depuis deux repos différents dans un seul `render.yaml`. Il faut créer **deux services séparés** sur Render.

---

## 📝 ÉTAPE 1 : Déployer le Site Web (sitegardes)

### 1.1 Sur Render.com

1. Allez sur **https://render.com**
2. Cliquez **"New +"** → **"Web Service"**
3. Connectez le repository **`Bobaxxx/sitegardes`**

### 1.2 Configuration

```
Name: sitegardes
Region: Frankfurt (ou votre choix)
Branch: master
Root Directory: (laisser vide)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: python app.py
```

### 1.3 Variables d'environnement

| Key | Value |
|-----|-------|
| `PYTHON_VERSION` | `3.11.0` |
| `SECRET_KEY` | (généré automatiquement) |
| `SENDGRID_API_KEY` | (votre clé) |
| `CONTACT_EMAIL` | (votre email) |
| `FROM_EMAIL` | (votre email) |
| `FROM_NAME` | `Pascal Gardes` |
| `SENDGRID_HOST` | (si nécessaire) |

### 1.4 Plan

```
Instance Type: Free
```

### 1.5 Créer le service

Cliquez **"Create Web Service"**

**URL obtenue :** `https://sitegardes.onrender.com`

---

## 📝 ÉTAPE 2 : Déployer le CMS (cmsadmin)

### 2.1 Sur Render.com

1. Toujours sur Render, cliquez **"New +"** → **"Web Service"**
2. Connectez le repository **`Bobaxxx/cmsadmin`** (ou le repo où se trouve cmsadmin)

### 2.2 Configuration

```
Name: jmind-cms
Region: Frankfurt
Branch: main (ou master selon votre repo)
Root Directory: (laisser vide)
Runtime: Node
Build Command: npm install && npm run build
Start Command: npm run start
```

### 2.3 Variables d'environnement

| Key | Value |
|-----|-------|
| `NODE_ENV` | `production` |
| `DATABASE_URL` | (votre URL PostgreSQL Neon) |
| `JWT_SECRET` | (généré automatiquement) |
| `SESSION_SECRET` | (généré automatiquement) |

### 2.4 Plan

```
Instance Type: Free
```

### 2.5 Créer le service

Cliquez **"Create Web Service"**

**URL obtenue :** `https://jmind-cms.onrender.com`

---

## 🔗 Lier le CMS au Site

### Option 1 : Lien dans le footer (déjà fait)

Le site a déjà un lien "Administration" dans le footer qui pointe vers `/admin/`.

**Pour que ça fonctionne avec le CMS externe :**

Modifiez le lien dans `index.html` :

```html
<!-- Avant -->
<a href="/admin/">Administration</a>

<!-- Après -->
<a href="https://jmind-cms.onrender.com" target="_blank">Administration</a>
```

### Option 2 : Sous-domaine (recommandé)

Si vous avez un domaine personnalisé :

1. **Site web :** `https://pascalgardes.fr`
2. **CMS :** `https://admin.pascalgardes.fr`

Dans Render :
- Allez dans les settings de chaque service
- Ajoutez votre domaine personnalisé
- Configurez les DNS chez votre registrar

---

## 🔄 Workflow Complet

```
┌─────────────────────────────────────┐
│  PASCAL se connecte au CMS          │
│  https://jmind-cms.onrender.com     │
├─────────────────────────────────────┤
│  1. Ajoute/modifie une réalisation  │
│  2. Upload une photo                │
│  3. Clique "Save"                   │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  LE CMS FAIT AUTOMATIQUEMENT        │
├─────────────────────────────────────┤
│  1. Crée/modifie le JSON            │
│  2. Upload l'image sur GitHub       │
│  3. Met à jour all_realisations.json│
│  4. Fait un commit sur GitHub       │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  LE SITE SE MET À JOUR              │
├─────────────────────────────────────┤
│  1. Render détecte le commit        │
│  2. Redéploie automatiquement       │
│  3. Les nouvelles données apparaissent│
└─────────────────────────────────────┘
```

---

## ⚙️ Configuration GitHub

Le CMS doit avoir accès au repository GitHub du site :

1. Allez sur **GitHub** → **Settings** → **Developer settings** → **Personal access tokens**
2. Créez un token avec les permissions `repo`
3. Dans le CMS, configurez ce token (voir la doc du CMS)

---

## 🎯 URLs Finales

- **Site web :** `https://sitegardes.onrender.com`
- **CMS Admin :** `https://jmind-cms.onrender.com`

---

## 📝 Checklist

- [ ] Site web déployé sur Render
- [ ] CMS déployé sur Render
- [ ] Variables d'environnement configurées
- [ ] GitHub token configuré dans le CMS
- [ ] Lien "Administration" mis à jour
- [ ] Test d'ajout de contenu depuis le CMS
- [ ] Vérification que le site se met à jour

---

## 🐛 Problèmes Courants

### Le CMS ne peut pas accéder à GitHub
→ Vérifiez que le token GitHub a les permissions `repo`
→ Vérifiez que le token est bien configuré dans les variables d'environnement du CMS

### Le site ne se met à jour pas
→ Vérifiez que Render est bien connecté au repo GitHub
→ Vérifiez les logs de déploiement dans Render

### Service en veille (plan gratuit)
→ Les services gratuits Render se mettent en veille après 15 min d'inactivité
→ Premier accès prend 30-60 secondes (réveil du service)
→ Solution : Passer au plan payant ($7/mois/service) pour qu'il reste actif

---

## ✅ Une fois tout configuré

Pascal pourra :
- ✅ Se connecter au CMS depuis chez lui
- ✅ Gérer ses réalisations 24/7
- ✅ Les modifications apparaissent automatiquement sur le site
- ✅ Sans intervention de votre part

**Tout est prêt ! 🚀**






