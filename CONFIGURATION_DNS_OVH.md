# ⚡ Configuration DNS OVH - Guide Rapide

## 🎯 Ce que vous devez faire

Configurer 2 enregistrements DNS dans OVH pour pointer vers Render.

---

## 📝 ÉTAPE 1 : Accéder à la Zone DNS OVH

1. Connectez-vous à **https://www.ovh.com/manager**
2. Allez dans **"Web Cloud"** → **"Domaines"**
3. Cliquez sur votre domaine **`gpserrurerie.fr`**
4. Cliquez sur l'onglet **"Zone DNS"**

---

## ⚙️ ÉTAPE 2 : Configurer les Enregistrements

### 2.1 Pour le domaine racine (gpserrurerie.fr)

**Option A : ANAME/ALIAS (recommandé si disponible)**

1. Cliquez sur **"Ajouter une entrée"**
2. Sélectionnez **"ANAME"** (ou **"ALIAS"** si disponible)
3. Remplissez :
   ```
   Sous-domaine: @ (ou laissez vide)
   Cible: sitegardes-t0lh.onrender.com
   TTL: 3600 (ou Auto)
   ```
4. Cliquez **"Suivant"** → **"Confirmer"**

**Option B : A Record (si ANAME non disponible)**

1. Cliquez sur **"Ajouter une entrée"**
2. Sélectionnez **"A"**
3. Remplissez :
   ```
   Sous-domaine: @ (ou laissez vide)
   Cible: 216.24.57.1
   TTL: 3600 (ou Auto)
   ```
4. Cliquez **"Suivant"** → **"Confirmer"**

### 2.2 Pour www (www.gpserrurerie.fr)

1. Cliquez sur **"Ajouter une entrée"**
2. Sélectionnez **"CNAME"**
3. Remplissez :
   ```
   Sous-domaine: www
   Cible: sitegardes-t0lh.onrender.com
   TTL: 3600 (ou Auto)
   ```
4. Cliquez **"Suivant"** → **"Confirmer"**

---

## ✅ Résumé des Enregistrements à Ajouter

| Type | Sous-domaine | Cible | TTL |
|------|--------------|-------|-----|
| **ANAME** (ou **A**) | `@` (vide) | `sitegardes-t0lh.onrender.com` (ou `216.24.57.1` pour A) | 3600 |
| **CNAME** | `www` | `sitegardes-t0lh.onrender.com` | 3600 |

---

## ⏳ ÉTAPE 3 : Attendre la Propagation

1. **La propagation DNS prend 15-30 minutes** (parfois jusqu'à 1h)
2. Une fois fait, retournez sur Render
3. Cliquez sur **"Verify"** à côté de chaque domaine
4. Render vérifiera automatiquement et activera le SSL

---

## 🔍 Vérifier que ça fonctionne

### Vérifier le DNS

Allez sur **https://dnschecker.org** :
1. Entrez `gpserrurerie.fr`
2. Sélectionnez **"A"** ou **"CNAME"**
3. Vérifiez que les valeurs correspondent

### Vérifier dans Render

1. Retournez sur Render → Custom Domains
2. Cliquez **"Verify"** pour chaque domaine
3. Si tout est bon, vous verrez ✅ "Domain verified" et "SSL active"

---

## 🐛 Si ça ne fonctionne pas

### Le DNS ne se propage pas

- Attendez 30-60 minutes
- Vérifiez sur dnschecker.org
- Videz le cache DNS de votre navigateur

### Erreur "Domain not verified" dans Render

- Vérifiez que les enregistrements DNS sont bien configurés
- Attendez la propagation complète
- Cliquez sur "Verify" à nouveau dans Render

### Le site ne charge pas

- Vérifiez que le service Render est actif (pas en veille)
- Vérifiez les logs dans Render
- Testez avec l'URL Render directement : `https://sitegardes-t0lh.onrender.com`

---

## 📌 Checklist Rapide

- [ ] Connecté à OVH Manager
- [ ] Zone DNS de `gpserrurerie.fr` ouverte
- [ ] Enregistrement ANAME/A pour `@` ajouté
- [ ] Enregistrement CNAME pour `www` ajouté
- [ ] Attendu 15-30 minutes
- [ ] Cliqué sur "Verify" dans Render
- [ ] SSL actif dans Render
- [ ] Site accessible via `https://gpserrurerie.fr`

---

**💡 Astuce :** Si vous avez déjà des enregistrements A ou CNAME pour `@` ou `www`, **modifiez-les** au lieu d'en créer de nouveaux !

---

**🎉 Une fois configuré, votre site sera accessible via `https://gpserrurerie.fr` !**

