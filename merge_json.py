#!/usr/bin/env python3
import json
import os
from pathlib import Path

# Charger tous les fichiers JSON
realisations = []
realisations_dir = Path('content/realisations')

for json_file in sorted(realisations_dir.glob('*.json')):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if data.get('published', True):  # Inclure seulement les publiés
            realisations.append(data)

# Créer le fichier consolidé
output = {
    "realisations": realisations,
    "count": len(realisations)
}

with open('content/all_realisations.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✅ {len(realisations)} réalisations mergées dans content/all_realisations.json")

