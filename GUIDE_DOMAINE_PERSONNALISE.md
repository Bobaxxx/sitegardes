# 🌐 Guide : Configuration d'un domaine personnalisé sur Render

## 📋 Prérequis

- Avoir acheté un nom de domaine (ex: `pascalgardes.fr`, `gardes-metallerie.com`, etc.)
- Avoir accès au panneau de gestion DNS de votre registrar (là où vous avez acheté le domaine)
- Avoir un service déployé sur Render

---

## 🔧 ÉTAPE 1 : Configurer le domaine dans Render

### 1.1 Accéder aux paramètres du service

1. Connectez-vous à votre dashboard Render : https://dashboard.render.com
2. Cliquez sur votre service **"sitegardes"**
3. Dans le menu de gauche, cliquez sur **"Settings"**
4. Scrollez jusqu'à la section **"Custom Domains"**

### 1.2 Ajouter votre domaine

1. Cliquez sur **"Add Custom Domain"**
2. Entrez votre domaine (ex: `pascalgardes.fr` ou `www.pascalgardes.fr`)
3. Render vous donnera des instructions DNS spécifiques

**⚠️ IMPORTANT :** Render vous donnera deux options :
- **Option A :** Utiliser le domaine racine (ex: `pascalgardes.fr`)
- **Option B :** Utiliser le sous-domaine www (ex: `www.pascalgardes.fr`)

**💡 RECOMMANDATION :** Configurez les DEUX pour que les deux fonctionnent !

---

## 🔧 ÉTAPE 2 : Configurer le DNS chez votre registrar

### 2.1 Trouver les informations DNS de Render

Après avoir ajouté le domaine dans Render, vous verrez quelque chose comme :

```
Type: CNAME
Name: www (ou @)
Value: sitegardes.onrender.com
```

OU

```
Type: A
Name: @
Value: 76.76.21.21 (exemple d'IP)
```

### 2.2 Configurer dans votre registrar

**Exemples de registrars courants :**

#### **OVH / Gandi / Namecheap / GoDaddy :**

1. Connectez-vous à votre espace client
2. Allez dans la gestion de vos domaines
3. Sélectionnez votre domaine
4. Cliquez sur **"DNS"** ou **"Zone DNS"** ou **"DNS Management"**

#### **Configuration pour le domaine racine (pascalgardes.fr) :**

Ajoutez/modifiez ces enregistrements :

```
Type: A
Nom: @ (ou laissez vide)
Valeur: [L'IP fournie par Render]
TTL: 3600 (ou Auto)
```

#### **Configuration pour www (www.pascalgardes.fr) :**

Ajoutez/modifiez cet enregistrement :

```
Type: CNAME
Nom: www
Valeur: sitegardes.onrender.com (ou la valeur fournie par Render)
TTL: 3600 (ou Auto)
```

### 2.3 Exemple de configuration complète

Si votre domaine est `pascalgardes.fr` et que Render vous donne :
- IP pour A record : `76.76.21.21`
- CNAME pour www : `sitegardes.onrender.com`

Votre zone DNS devrait contenir :

```
Type    Nom    Valeur                    TTL
A       @      76.76.21.21               3600
CNAME   www    sitegardes.onrender.com   3600
```

---

## ⏳ ÉTAPE 3 : Attendre la propagation DNS

1. **La propagation DNS peut prendre de 5 minutes à 48 heures**
2. En général, c'est actif en 15-30 minutes
3. Vous pouvez vérifier avec : https://dnschecker.org
   - Entrez votre domaine
   - Sélectionnez "A" ou "CNAME"
   - Vérifiez que les valeurs correspondent

---

## 🔒 ÉTAPE 4 : SSL/HTTPS automatique

**Render configure automatiquement le certificat SSL (HTTPS) !**

1. Une fois le DNS propagé, Render détectera automatiquement votre domaine
2. Il générera un certificat SSL Let's Encrypt gratuit
3. Cela peut prendre 5-10 minutes après la propagation DNS
4. Votre site sera accessible en HTTPS automatiquement

**✅ Vérification :** Dans Render, la section "Custom Domains" devrait afficher :
- ✅ Domaine vérifié
- ✅ SSL actif

---

## 🔧 ÉTAPE 5 : Redirection www vers domaine racine (optionnel mais recommandé)

Pour que `www.pascalgardes.fr` redirige vers `pascalgardes.fr` (ou vice versa) :

### Option A : Dans Render (si disponible)

1. Dans "Custom Domains", configurez les deux domaines
2. Render peut gérer la redirection automatiquement

### Option B : Dans votre code (app.py)

Ajoutez une redirection dans `app.py` :

```python
from flask import Flask, redirect, request

@app.before_request
def redirect_www():
    """Redirige www vers le domaine racine"""
    if request.host.startswith('www.'):
        return redirect(request.url.replace('www.', '', 1), code=301)
```

---

## ✅ ÉTAPE 6 : Vérifier que tout fonctionne

1. **Testez votre domaine :**
   - `https://votredomaine.fr` → Devrait afficher le site
   - `https://www.votredomaine.fr` → Devrait aussi fonctionner

2. **Vérifiez le SSL :**
   - Le cadenas vert devrait apparaître dans le navigateur
   - Pas d'avertissement de sécurité

3. **Testez les pages :**
   - Page d'accueil
   - Formulaire de contact
   - Toutes les fonctionnalités

---

## 🐛 Dépannage

### Le domaine ne fonctionne pas après 1 heure

1. **Vérifiez le DNS :**
   - Utilisez https://dnschecker.org
   - Vérifiez que les valeurs correspondent à celles de Render

2. **Vérifiez dans Render :**
   - Le domaine est-il bien ajouté ?
   - Y a-t-il des erreurs affichées ?

3. **Videz le cache DNS :**
   ```bash
   # Sur Mac/Linux
   sudo dscacheutil -flushcache
   
   # Sur Windows
   ipconfig /flushdns
   ```

### Le SSL ne fonctionne pas

1. Attendez 10-15 minutes après la propagation DNS
2. Vérifiez dans Render que le certificat est généré
3. Si ça ne fonctionne toujours pas, contactez le support Render

### Erreur "Domain not verified"

1. Vérifiez que le DNS est bien configuré
2. Attendez la propagation complète
3. Dans Render, cliquez sur "Verify" ou "Retry"

---

## 📝 Notes importantes

- **Render offre SSL gratuit** pour tous les domaines personnalisés
- **Le domaine personnalisé est gratuit** sur Render (pas de coût supplémentaire)
- **Vous pouvez avoir plusieurs domaines** pointant vers le même service
- **Les sous-domaines** (ex: `admin.pascalgardes.fr`) nécessitent une configuration séparée

---

## 🆘 Besoin d'aide ?

Si vous avez des difficultés :
1. Vérifiez la documentation Render : https://render.com/docs/custom-domains
2. Contactez le support de votre registrar pour la configuration DNS
3. Contactez le support Render si le problème persiste

---

## 📌 Checklist finale

- [ ] Domaine ajouté dans Render
- [ ] Enregistrements DNS configurés chez le registrar
- [ ] DNS propagé (vérifié sur dnschecker.org)
- [ ] SSL actif dans Render
- [ ] Site accessible via le nouveau domaine
- [ ] HTTPS fonctionne (cadenas vert)
- [ ] Toutes les pages fonctionnent correctement

---

**🎉 Une fois tout configuré, votre site sera accessible via votre domaine personnalisé !**

