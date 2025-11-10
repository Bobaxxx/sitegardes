# 🔐 CONFIGURATION GITHUB OAUTH - ÉTAPES DÉTAILLÉES

## ✅ VOS IDENTIFIANTS GITHUB OAUTH APP

```
Client ID:     Ov23liKKhPn8kDKCbCRL
Client Secret: b1fd6aac75203f1dcf0f0a7ccc2733455053c121
```

⚠️ **IMPORTANT : Ne JAMAIS mettre le Client Secret directement dans le code public !**

---

## 🛠️ CONFIGURATION AVEC NETLIFY (PROXY OAUTH GRATUIT)

### **Étape 1 : Créer un compte Netlify**

1. Allez sur : **https://app.netlify.com/signup**
2. Cliquez sur **"Sign up with GitHub"**
3. Connectez-vous avec votre compte GitHub (Bobaxxx)
4. Autorisez Netlify
5. ✅ Compte créé !

---

### **Étape 2 : Importer votre site sur Netlify**

6. Sur le dashboard Netlify, cliquez **"Add new site"** → **"Import an existing project"**
7. Cliquez sur **"Deploy with GitHub"**
8. Sélectionnez le repository **"sitegardes"**
9. Dans "Build settings" :
   ```
   Branch to deploy: master
   Build command: (laisser VIDE)
   Publish directory: /
   ```
10. Cliquez **"Deploy bobaxxx-sitegardes"**
11. ⏳ Attendez 1-2 minutes
12. ✅ Site déployé sur Netlify !

**📝 NOTEZ L'URL NETLIFY :** 
Exemple : `https://superb-starfish-123abc.netlify.app`

---

### **Étape 3 : Configurer GitHub OAuth sur Netlify**

13. Sur votre site Netlify, cliquez sur **"Site configuration"**
14. Menu gauche : **"Access & security"** → **"OAuth"**
15. Sous **"Authentication providers"**, cliquez **"Install provider"**
16. Sélectionnez **"GitHub"**
17. Entrez vos identifiants :
    ```
    Client ID:     Ov23liKKhPn8kDKCbCRL
    Client Secret: b1fd6aac75203f1dcf0f0a7ccc2733455053c121
    ```
18. Cliquez **"Install"**
19. ✅ OAuth configuré !

---

### **Étape 4 : Activer Git Gateway**

20. Toujours dans "Site configuration"
21. Menu gauche : Cliquez sur **"Identity"**
22. Cliquez sur **"Enable Identity"**
23. Scrollez jusqu'à **"Services"** → **"Git Gateway"**
24. Cliquez **"Enable Git Gateway"**
25. ✅ Git Gateway activé !

---

### **Étape 5 : Mettre à jour le fichier config.yml**

Le fichier `admin/config.yml` doit pointer vers votre site Netlify ou GitHub Pages.

**Si vous utilisez les DEUX (GitHub Pages + Netlify) :**
```yaml
backend:
  name: git-gateway
  branch: master

site_url: https://bobaxxx.github.io/sitegardes
# OU
# site_url: https://votre-site.netlify.app
```

**Si vous utilisez UNIQUEMENT GitHub Pages avec proxy Netlify :**
Vous devrez créer un service séparé (plus complexe).

---

## 🎯 RÉSULTAT FINAL

**Avec cette configuration :**

1. **Le site public** : `https://bobaxxx.github.io/sitegardes/`
2. **Interface admin** : `https://bobaxxx.github.io/sitegardes/admin/`
3. **Connexion** : Via GitHub OAuth (compte GitHub requis)

**OU**

1. **Le site public** : Sur GitHub Pages ET/OU Netlify
2. **Interface admin** : Sur les 2 aussi
3. **Connexion** : Via Netlify Identity (email/mot de passe)

---

## 💡 RECOMMANDATION FINALE

**UTILISEZ NETLIFY** pour tout (hébergement + admin) car :
- ✅ Configuration plus simple
- ✅ Tout au même endroit
- ✅ Interface admin garantie de fonctionner
- ✅ Connexion email/mot de passe (plus simple pour le propriétaire)
- ✅ Vous pourrez quand même utiliser un domaine perso plus tard

**Ensuite, si vous voulez vraiment GitHub Pages, on peut rediriger, mais Netlify c'est mieux pour l'admin.**

---

## ❓ PROCHAINE ÉTAPE POUR VOUS

**Faites l'Étape 1 et 2** (créer compte Netlify + importer le site).

**Puis dites-moi :** "Site importé sur Netlify"

Et je vous guide pour les étapes 3-4 ! 🚀

