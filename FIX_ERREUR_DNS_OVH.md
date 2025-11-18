# 🔧 Solution : Erreur CNAME sur OVH

## ❌ Le Problème

Vous avez une erreur car il existe déjà un enregistrement **A** pour `www.gpserrurerie.fr` (pointant vers `213.186.33.5`).

**Un CNAME ne peut pas coexister avec un A ou TXT sur le même sous-domaine.**

---

## ✅ Solution : Supprimer puis Ajouter

### ÉTAPE 1 : Supprimer l'ancien enregistrement A

1. Dans la zone DNS OVH, trouvez l'enregistrement :
   ```
   www.gpserrurerie.fr. | A | 213.186.33.5
   ```

2. Cliquez sur l'icône **🗑️ (poubelle)** à droite de cet enregistrement
3. Confirmez la suppression

### ÉTAPE 2 : Supprimer le TXT (optionnel)

Si vous n'en avez plus besoin :
1. Trouvez l'enregistrement :
   ```
   www.gpserrurerie.fr. | TXT | "3|welcome"
   ```
2. Supprimez-le aussi (ou gardez-le si c'est pour une vérification)

### ÉTAPE 3 : Ajouter le CNAME

Maintenant que l'A est supprimé, vous pouvez ajouter le CNAME :

1. Cliquez **"Ajouter une entrée"**
2. Type : **CNAME**
3. Sous-domaine : `www`
4. Cible : `sitegardes-t0lh.onrender.com`
5. TTL : 3600
6. Validez

---

## 📋 Résumé Rapide

1. ❌ **Supprimer** : `www.gpserrurerie.fr` | A | 213.186.33.5
2. ✅ **Ajouter** : `www.gpserrurerie.fr` | CNAME | sitegardes-t0lh.onrender.com

---

## ⚠️ Important

- **Ne supprimez PAS** l'enregistrement A pour `@` (domaine racine) si vous l'avez déjà configuré
- **Supprimez uniquement** l'A pour `www` qui pointe vers `213.186.33.5`
- Le TXT peut rester si nécessaire, mais généralement on peut le supprimer aussi

---

**🎯 Une fois fait, attendez 15-30 minutes puis cliquez "Verify" dans Render !**

