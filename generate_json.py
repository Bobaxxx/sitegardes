#!/usr/bin/env python3
import os
import json
from pathlib import Path

# Mapping des dossiers vers les catégories du CMS
category_mapping = {
    "autres": "Autre",
    "escaliers": "Escalier",
    "garde-corps": "Garde-corps",
    "passerelles-terrasses": "Passerelle",
    "pergolas": "Pergola",
    "portails": "Portail",
    "verrieres": "Verrière"
}

# Descriptions par catégorie
descriptions = {
    "Escalier": "Escalier métallique sur mesure, alliant robustesse et esthétique.",
    "Portail": "Portail sur mesure en métal, adapté à vos besoins et à votre style.",
    "Garde-corps": "Garde-corps sur mesure alliant sécurité et design.",
    "Passerelle": "Passerelle ou terrasse en structure métallique sur mesure.",
    "Pergola": "Pergola sur mesure en acier ou aluminium.",
    "Verrière": "Verrière sur mesure avec finitions soignées.",
    "Autre": "Création sur mesure en métallerie."
}

# Créer le dossier content/realisations s'il n'existe pas
os.makedirs("content/realisations", exist_ok=True)

# Scanner les images
images_dir = Path("images/realisations")
count = 0

for category_folder in images_dir.iterdir():
    if not category_folder.is_dir():
        continue
    
    category_name = category_folder.name
    category = category_mapping.get(category_name, "Autre")
    
    for image_file in category_folder.iterdir():
        if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
            count += 1
            
            # Nom du fichier sans extension
            image_name = image_file.stem
            
            # Nom du fichier JSON
            json_filename = f"2024-{category_name}-{image_name.lower()}.json"
            json_path = Path("content/realisations") / json_filename
            
            # Créer le contenu JSON
            data = {
                "title": f"{category} - {image_name}",
                "category": category,
                "description": descriptions.get(category, "Réalisation sur mesure en métallerie."),
                "materials": "Acier",
                "location": "Lantriac, Haute-Loire",
                "year": "2024",
                "image": str(image_file).replace("\\", "/"),
                "published": True,
                "order": 0
            }
            
            # Écrire le fichier JSON
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Créé: {json_filename}")

print(f"\n🎉 {count} fichiers JSON créés avec succès !")

