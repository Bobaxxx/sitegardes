# 📧 Configuration Email Professionnel - contact@jmindagency.fr

## 🎯 Objectif
Configurer un email professionnel `contact@jmindagency.fr` pour votre agence.

**⚠️ Si vous ne pouvez pas modifier/supprimer les enregistrements DNS dans OVH, consultez le guide : `DEPANNAGE_DNS_OVH.md`**

---

## ⚠️ SITUATION ACTUELLE

D'après votre zone DNS, vous utilisez actuellement **ImprovMX** pour gérer vos emails :

**Enregistrements actuels :**
- **MX 1** : `mx1.improvmx.com` (priorité 10)
- **MX 2** : `mx2.improvmx.com` (priorité 20)
- **SPF** : `v=spf1 include:spf.improvmx.com ~all`

### 📧 Capacités d'ImprovMX

**Avec le plan GRATUIT d'ImprovMX :**
- ✅ **Recevoir** des emails à `contact@jmindagency.fr`
- ✅ **Rediriger** ces emails vers une autre adresse (Gmail, Outlook, etc.)
- ❌ **PAS d'envoi SMTP** - Vous ne pouvez PAS envoyer d'emails depuis `contact@jmindagency.fr`

**Avec un plan PAYANT d'ImprovMX :**
- ✅ Recevoir des emails
- ✅ Rediriger des emails
- ✅ **Envoyer des emails via SMTP** (limité, ex: 200 emails/jour pour Premium)

**⚠️ Important :** Si vous configurez un email professionnel via OVH (ou un autre service), vous devrez **modifier ces enregistrements** pour pointer vers le nouveau service. Cela remplacera la configuration ImprovMX.

---

## 📋 ÉTAPE 1 : Choisir la Configuration

D'après l'interface que vous voyez, vous avez **2 options** :

### ✅ **Option 1 : Configuration Recommandée** (Recommandé pour débuter)

**Avantages :**
- ✅ Configuration automatique et sécurisée
- ✅ Meilleur niveau de sécurité
- ✅ Configuration rapide

**⚠️ Attention :**
- Tous les emails adressés à `@jmindagency.fr` seront **immédiatement** redirigés vers ce service
- **Votre configuration ImprovMX actuelle sera remplacée**
- Les enregistrements MX et SPF seront modifiés automatiquement

**Quand choisir cette option :**
- Si vous voulez remplacer ImprovMX par un service email professionnel complet
- Si vous voulez une configuration rapide et sécurisée
- Si vous acceptez que la configuration actuelle soit modifiée

### ⚙️ **Option 2 : Configuration Personnalisée**

**Avantages :**
- ✅ Vous contrôlez quand basculer les emails
- ✅ Vous pouvez tester avant de tout activer
- ✅ Plus de flexibilité

**Quand choisir cette option :**
- Si vous voulez garder ImprovMX en parallèle temporairement
- Si vous voulez tester avant de remplacer complètement
- Si vous avez besoin de plus de contrôle sur la transition

---

## 🚀 ÉTAPE 2 : Procédure de Configuration

### **Si vous choisissez la Configuration Recommandée :**

1. **Sélectionnez** "Configuration recommandée" (déjà sélectionné)
2. **Lisez attentivement** l'avertissement en jaune
3. **Cliquez sur "Valider"**
4. ⏳ **Attendez la configuration automatique** (quelques minutes)

### ⚠️ IMPORTANT : Période de configuration automatique

**Si vous venez juste de relier votre email à votre domaine :**

- Les enregistrements DNS peuvent être **verrouillés temporairement** pendant la configuration
- OVH peut être en train de **créer/modifier automatiquement** les enregistrements
- Vous ne pourrez peut-être **pas modifier ou supprimer** les enregistrements pendant cette période

**Que faire :**
1. **Attendez 15-30 minutes** après avoir validé la configuration
2. **Rafraîchissez la page** de la zone DNS (F5)
3. **Vérifiez si les enregistrements ont été modifiés automatiquement** :
   - Les MX ImprovMX ont-ils été remplacés par les MX OVH ?
   - Le SPF a-t-il été mis à jour ?
4. Si les enregistrements sont toujours ceux d'ImprovMX après 30 minutes, alors vous pourrez les modifier manuellement

### **Si vous choisissez la Configuration Personnalisée :**

1. **Sélectionnez** "Configuration personnalisée"
2. **Cliquez sur "Valider"**
3. Vous pourrez ensuite configurer manuellement les paramètres

---

## 🔧 ÉTAPE 3 : Modification des Enregistrements DNS

**⚠️ IMPORTANT :** 

1. **Si vous avez choisi la "Configuration Recommandée"** et que vous venez de valider :
   - ⏳ **ATTENDEZ 15-30 minutes** - OVH peut modifier automatiquement les enregistrements
   - Rafraîchissez la zone DNS après ce délai
   - Vérifiez si les enregistrements ont été modifiés automatiquement
   - Si oui, vous n'avez rien à faire de plus ! ✅

2. **Si les enregistrements n'ont PAS été modifiés automatiquement** après 30 minutes :
   - Vous devrez les modifier manuellement (voir ci-dessous)
   - Ou contacter le support OVH

### Accéder à la Zone DNS OVH

1. Connectez-vous à **https://www.ovh.com/manager**
2. Allez dans **"Web Cloud"** → **"Domaines"**
3. Cliquez sur votre domaine **`jmindagency.fr`**
4. Cliquez sur l'onglet **"Zone DNS"**

### 📝 MODIFIER les Enregistrements MX (remplacer ImprovMX)

**Vous devez MODIFIER les enregistrements MX existants :**

**Actuellement vous avez :**
- `mx1.improvmx.com` (priorité 10)
- `mx2.improvmx.com` (priorité 20)

**Vous devez les remplacer par (si vous utilisez OVH) :**

| Type | Sous-domaine | Cible | Priorité | TTL |
|------|--------------|-------|----------|-----|
| **MX** | `@` (vide) | `mx1.mail.ovh.net` | 1 | 3600 |
| **MX** | `@` (vide) | `mx2.mail.ovh.net` | 5 | 3600 |
| **MX** | `@` (vide) | `mx3.mail.ovh.net` | 50 | 3600 |

**⚠️ Méthode recommandée : SUPPRIMER puis CRÉER (plus fiable)**

**Étape 1 : Supprimer les anciens enregistrements MX ImprovMX**

1. Dans votre zone DNS, **trouvez les 2 enregistrements MX** :
   - `mx1.improvmx.com` (priorité 10)
   - `mx2.improvmx.com` (priorité 20)

2. **Cochez la case** à gauche de chaque enregistrement MX ImprovMX

3. En haut ou en bas de la liste, cherchez un bouton **"Supprimer"** ou **"Actions"** → **"Supprimer"**

4. **Confirmez la suppression**

**Étape 2 : Créer les nouveaux enregistrements MX**

1. Cliquez sur le bouton **"Ajouter une entrée"** (généralement en haut à droite)

2. Sélectionnez **"MX"** dans le type d'enregistrement

3. **Pour le premier MX :**
   - Sous-domaine : `@` (ou laissez vide, ou tapez juste le domaine)
   - Cible : `mx1.mail.ovh.net` (ou celle fournie par votre service)
   - Priorité : `1`
   - TTL : `3600` (ou "Auto")
   - Cliquez sur **"Suivant"** ou **"Valider"**

4. **Répétez pour le deuxième MX :**
   - Cliquez sur **"Ajouter une entrée"** à nouveau
   - Type : **"MX"**
   - Sous-domaine : `@` (ou vide)
   - Cible : `mx2.mail.ovh.net`
   - Priorité : `5`
   - TTL : `3600`
   - Cliquez sur **"Valider"**

5. **Répétez pour le troisième MX (si nécessaire) :**
   - Cible : `mx3.mail.ovh.net`
   - Priorité : `50`

### 📝 MODIFIER l'Enregistrement SPF

**Actuellement vous avez :**
- `v=spf1 include:spf.improvmx.com ~all`

**Vous devez le remplacer par (si vous utilisez OVH) :**

| Type | Sous-domaine | Valeur | TTL |
|------|--------------|--------|-----|
| **TXT** | `@` (vide) | `v=spf1 include:mx.ovh.com ~all` | 3600 |

**⚠️ Méthode recommandée : SUPPRIMER puis CRÉER**

**Étape 1 : Supprimer l'ancien enregistrement SPF ImprovMX**

1. Dans votre zone DNS, **trouvez l'enregistrement TXT** avec la valeur :
   - `v=spf1 include:spf.improvmx.com ~all`

2. **Cochez la case** à gauche de cet enregistrement

3. Cliquez sur **"Supprimer"** ou **"Actions"** → **"Supprimer"**

4. **Confirmez la suppression**

**Étape 2 : Créer le nouvel enregistrement SPF**

1. Cliquez sur **"Ajouter une entrée"**

2. Sélectionnez **"TXT"** dans le type d'enregistrement

3. Remplissez les champs :
   - Sous-domaine : `@` (ou laissez vide)
   - Valeur : `v=spf1 include:mx.ovh.com ~all` (ou celle fournie par votre service)
   - TTL : `3600` (ou "Auto")

4. Cliquez sur **"Suivant"** → **"Confirmer"** ou **"Valider"**

**⚠️ Note :** Les valeurs exactes (serveurs MX et SPF) dépendent de votre fournisseur d'email. Vérifiez dans la documentation de votre service email (OVH, Google Workspace, Microsoft 365, etc.)

**💡 Si vous ne savez pas quelles valeurs utiliser :**
- Consultez la documentation de votre service email professionnel
- Ou contactez le support de votre fournisseur d'email

### Enregistrements DKIM (pour la sécurité)

Votre fournisseur d'email vous fournira les valeurs DKIM spécifiques. Ajoutez-les comme enregistrements TXT.

---

## ⏳ ÉTAPE 4 : Attendre la Propagation DNS

- **La propagation DNS prend 15-30 minutes** (parfois jusqu'à 1h)
- Vous pouvez vérifier sur **https://dnschecker.org** :
  1. Entrez `jmindagency.fr`
  2. Sélectionnez **"MX"** ou **"TXT"**
  3. Vérifiez que les valeurs correspondent

---

## 📱 ÉTAPE 5 : Configurer votre Client Email

Une fois l'email configuré, vous pouvez l'utiliser avec :

### **Configuration IMAP (pour recevoir et envoyer)**

**Serveur de réception (IMAP) :**
- Serveur : `ssl0.ovh.net`
- Port : `993`
- Sécurité : SSL/TLS
- Identifiant : `contact@jmindagency.fr`
- Mot de passe : (celui que vous avez défini)

**Serveur d'envoi (SMTP) :**
- Serveur : `ssl0.ovh.net`
- Port : `465`
- Sécurité : SSL/TLS
- Identifiant : `contact@jmindagency.fr`
- Mot de passe : (celui que vous avez défini)

### **Configuration POP (alternative)**

**Serveur de réception (POP) :**
- Serveur : `ssl0.ovh.net`
- Port : `995`
- Sécurité : SSL/TLS

---

## ✅ ÉTAPE 6 : Tester votre Email

1. **Envoyez un email de test** depuis `contact@jmindagency.fr` vers une autre adresse
2. **Répondez** à cet email pour vérifier la réception
3. **Vérifiez** que les emails arrivent bien dans votre boîte

---

## 🐛 Résolution des erreurs DNS

### Erreur "Record does not exist" lors de la modification

**Solution :** Supprimer puis recréer les enregistrements au lieu de les modifier.

### Erreur lors de la suppression

Si vous obtenez une erreur lors de la suppression des enregistrements, voici les solutions :

#### ✅ Solution 1 : Vérifier les permissions et le mode de la zone DNS

1. **Vérifiez que vous êtes bien connecté** avec un compte administrateur
2. **Vérifiez le mode de la zone DNS** :
   - Dans OVH, allez dans **"Zone DNS"**
   - Regardez si la zone est en mode **"Lecture seule"** ou **"Écriture"**
   - Si elle est en lecture seule, vous devez la passer en mode écriture

#### ✅ Solution 2 : Vérifier si les enregistrements sont verrouillés

Certains enregistrements peuvent être protégés ou verrouillés :

1. **Regardez les enregistrements MX et TXT** dans votre zone DNS
2. **Vérifiez s'il y a une icône de cadenas** ou un indicateur de protection
3. Si c'est le cas, vous devrez peut-être déverrouiller la zone DNS d'abord

#### ✅ Solution 3 : Utiliser l'API OVH ou le support

Si la suppression ne fonctionne toujours pas :

1. **Contactez le support OVH** : Ils peuvent supprimer les enregistrements pour vous
2. **Utilisez l'API OVH** (si vous êtes à l'aise avec les APIs)
3. **Vérifiez si ImprovMX a un verrou** sur ces enregistrements

#### ✅ Solution 4 : Modifier directement les valeurs (sans supprimer)

Si la suppression ne fonctionne pas, essayez de **modifier directement les valeurs** :

**Pour les MX :**
1. Cliquez sur le bouton **"..."** à droite de l'enregistrement MX
2. Sélectionnez **"Modifier"**
3. **Remplacez uniquement la valeur "Cible"** :
   - Ancienne : `mx1.improvmx.com`
   - Nouvelle : `mx1.mail.ovh.net` (ou celle de votre service)
4. **Modifiez la priorité** si nécessaire
5. Cliquez sur **"Valider"**

**Pour le SPF (TXT) :**
1. Cliquez sur le bouton **"..."** à droite de l'enregistrement TXT
2. Sélectionnez **"Modifier"**
3. **Remplacez uniquement la valeur** :
   - Ancienne : `v=spf1 include:spf.improvmx.com ~all`
   - Nouvelle : `v=spf1 include:mx.ovh.com ~all` (ou celle de votre service)
4. Cliquez sur **"Valider"**

#### ✅ Solution 5 : Vérifier le format des valeurs

Assurez-vous que :
- Les valeurs MX se terminent par un **point (.)** : `mx1.mail.ovh.net.` (avec le point final)
- Les valeurs TXT sont entre **guillemets** si nécessaire : `"v=spf1 include:mx.ovh.com ~all"`

#### ✅ Solution 6 : Attendre et réessayer

Parfois, il y a un délai ou une synchronisation en cours :
1. **Attendez 5-10 minutes**
2. **Rafraîchissez la page** (F5)
3. **Réessayez la suppression**

### Autres causes possibles

- **L'enregistrement a déjà été supprimé** : Vérifiez qu'il existe encore dans la liste
- **Problème de cache** : Rafraîchissez la page (F5) et réessayez
- **Permissions** : Assurez-vous d'avoir les droits de modification sur la zone DNS
- **Zone DNS externe** : Si la zone DNS est gérée ailleurs, vous devez la modifier là-bas

---

## 🔍 Vérification et Dépannage

### Vérifier que les enregistrements DNS sont corrects

Allez sur **https://mxtoolbox.com/SuperTool.aspx** :
1. Entrez `jmindagency.fr`
2. Sélectionnez **"MX Lookup"**
3. Vérifiez que les serveurs MX sont corrects

### Problèmes courants

**❌ Les emails ne sont pas reçus :**
- Vérifiez que les enregistrements MX sont corrects
- Attendez la propagation DNS complète (jusqu'à 1h)
- Vérifiez les spams/courrier indésirable

**❌ Les emails ne peuvent pas être envoyés :**
- Vérifiez les paramètres SMTP
- Vérifiez que l'enregistrement SPF est correct
- Vérifiez que le port 465 ou 587 n'est pas bloqué

**❌ Erreur d'authentification :**
- Vérifiez votre identifiant : `contact@jmindagency.fr`
- Vérifiez votre mot de passe
- Assurez-vous d'utiliser SSL/TLS

---

## 📌 Checklist Rapide

- [ ] **Identifié la configuration actuelle** (ImprovMX)
- [ ] Choisi entre configuration recommandée ou personnalisée
- [ ] Cliqué sur "Valider" dans l'interface
- [ ] Attendu la configuration automatique
- [ ] **Modifié les enregistrements MX** (remplacer ImprovMX)
- [ ] **Modifié l'enregistrement SPF** (remplacer ImprovMX)
- [ ] Vérifié que les nouveaux enregistrements sont corrects
- [ ] Attendu 15-30 minutes pour la propagation DNS
- [ ] Configuré le client email (IMAP/SMTP)
- [ ] Testé l'envoi et la réception d'emails
- [ ] Vérifié que tout fonctionne correctement

---

## 💡 Recommandations

1. **Pour commencer rapidement :** Choisissez la **Configuration Recommandée**
2. **Pour plus de contrôle :** Choisissez la **Configuration Personnalisée**
3. **Sécurité :** Utilisez toujours SSL/TLS pour vos connexions email
4. **Mot de passe :** Utilisez un mot de passe fort et unique
5. **Sauvegarde :** Notez vos identifiants dans un gestionnaire de mots de passe

---

## 🎉 Une fois configuré

Votre email `contact@jmindagency.fr` sera prêt à être utilisé pour :
- ✅ Recevoir des emails professionnels
- ✅ Envoyer des emails depuis votre domaine
- ✅ Communiquer avec vos clients de manière professionnelle

---

---

## 🔄 Transition depuis ImprovMX

### Avant de modifier

1. **Notez vos configurations ImprovMX actuelles** (au cas où vous voudriez revenir en arrière)
2. **Vérifiez si vous avez des emails importants** dans ImprovMX à sauvegarder
3. **Informez les personnes qui utilisent** des adresses email sur ce domaine

### Après la modification

1. **Les emails envoyés à `@jmindagency.fr`** iront vers le nouveau service
2. **ImprovMX ne recevra plus d'emails** pour ce domaine
3. **La propagation DNS prend 15-30 minutes** avant que tout soit actif

### Si vous voulez garder ImprovMX en parallèle

Vous pouvez configurer des sous-domaines spécifiques pour ImprovMX (ex: `forward@jmindagency.fr`) et utiliser le domaine principal pour le service email professionnel.

---

---

## 💡 Alternative : Garder ImprovMX + Utiliser Gmail pour l'envoi

Si vous voulez **garder ImprovMX** pour recevoir des emails mais **pouvoir envoyer** depuis `contact@jmindagency.fr`, vous pouvez :

### Option : Gmail SMTP avec adresse personnalisée

1. **Gardez ImprovMX** pour recevoir les emails (pas besoin de modifier les DNS)
2. **Configurez Gmail** pour envoyer en tant que `contact@jmindagency.fr` :
   - Dans Gmail : Paramètres → Comptes et importation → "Envoyer des messages en tant que"
   - Ajoutez `contact@jmindagency.fr`
   - Utilisez les paramètres SMTP de Gmail
   - Générez un mot de passe d'application Google

**Avantages :**
- ✅ Pas besoin de modifier les DNS
- ✅ Recevez via ImprovMX (redirection vers votre Gmail)
- ✅ Envoyez via Gmail en tant que `contact@jmindagency.fr`
- ✅ Gratuit (si vous avez déjà Gmail)

**Inconvénients :**
- ⚠️ Limité à 500 emails/jour (limite Gmail)
- ⚠️ L'adresse d'expéditeur peut parfois afficher "via gmail.com"

### Comparaison : ImprovMX vs Email Professionnel Complet

| Fonctionnalité | ImprovMX (Gratuit) | ImprovMX (Payant) | Email Pro (OVH/Google/Microsoft) |
|----------------|-------------------|-------------------|----------------------------------|
| Recevoir emails | ✅ | ✅ | ✅ |
| Rediriger emails | ✅ | ✅ | ✅ |
| Envoyer emails | ❌ | ✅ (limité) | ✅ (illimité) |
| Boîte email dédiée | ❌ | ❌ | ✅ |
| Stockage | ❌ | ❌ | ✅ (plusieurs Go) |
| Coût | Gratuit | ~5-10€/mois | ~3-6€/mois |

**💡 Astuce :** Si vous avez des questions ou des problèmes, contactez le support de votre fournisseur d'email (OVH, etc.)

