#!/usr/bin/env python3
"""
Script pour remplacer les projets statiques dans realisations.html
par un chargement dynamique depuis les fichiers JSON
"""

# Lire le fichier existant
with open('realisations.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver le début et la fin de la section des projets
start_marker = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">'
end_marker = '</div>\n</div></div>\n</div>\n</main>'

start_index = content.find(start_marker)
end_index = content.find(end_marker, start_index)

if start_index == -1 or end_index == -1:
    print("❌ Erreur: Marqueurs non trouvés")
    exit(1)

# Construire le nouveau contenu avec le conteneur vide et le script de chargement
new_grid_content = '''<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3" id="projectsGrid">
<!-- Les projets seront chargés dynamiquement depuis les fichiers JSON -->
<div class="col-span-full flex justify-center items-center py-20">
<div class="text-center">
<div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-black"></div>
<p class="mt-4 text-neutral-600">Chargement des réalisations...</p>
</div>
</div>
</div>
</div></div>
</div>
</main>

<script>
// Fonction pour charger et afficher les projets depuis les JSON
async function loadProjects() {
    try {
        // Récupérer la liste des fichiers JSON
        const response = await fetch('content/realisations/');
        
        // Si on ne peut pas lister les fichiers, on les charge un par un
        // On sait qu'il y en a 98, on va essayer de les charger
        const projects = [];
        
        // Charger tous les fichiers JSON (on pourrait optimiser avec un manifest)
        const categories = ['escaliers', 'portails', 'garde-corps', 'passerelles-terrasses', 'pergolas', 'verrieres', 'autres'];
        
        // Charger tous les fichiers
        const files = await fetch('content/realisations/manifest.json')
            .then(r => r.ok ? r.json() : null)
            .catch(() => null);
        
        if (!files) {
            // Fallback: utiliser un glob pattern (ne fonctionne pas en JS)
            // On va hardcoder les noms de fichiers pour l'instant
            console.error('Manifest non trouvé, chargement direct impossible');
            return;
        }
        
        // Charger chaque fichier JSON
        for (const file of files) {
            try {
                const data = await fetch(`content/realisations/${file}`).then(r => r.json());
                if (data.published !== false) {
                    projects.push(data);
                }
            } catch (e) {
                console.error(`Erreur chargement ${file}:`, e);
            }
        }
        
        // Afficher les projets
        displayProjects(projects);
        
    } catch (error) {
        console.error('Erreur chargement projets:', error);
        document.getElementById('projectsGrid').innerHTML = `
            <div class="col-span-full text-center py-20">
                <p class="text-red-600">Erreur de chargement des projets</p>
            </div>
        `;
    }
}

function displayProjects(projects) {
    const grid = document.getElementById('projectsGrid');
    grid.innerHTML = '';
    
    // Mélanger l'ordre si on affiche tous les projets
    const shuffledProjects = [...projects].sort(() => Math.random() - 0.5);
    
    shuffledProjects.forEach(project => {
        const projectDiv = document.createElement('div');
        projectDiv.className = 'group relative aspect-square block overflow-hidden cursor-pointer project-item animate-on-scroll';
        projectDiv.dataset.title = project.title;
        projectDiv.dataset.category = project.category;
        projectDiv.dataset.description = project.description;
        projectDiv.dataset.materials = project.materials;
        projectDiv.dataset.location = project.location;
        projectDiv.dataset.year = project.year;
        projectDiv.dataset.image = project.image;
        
        projectDiv.innerHTML = `
            <img alt="${project.category}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" src="${project.image}"/>
            <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-40 transition-opacity duration-300 flex items-center justify-center">
                <span class="material-symbols-outlined text-white text-5xl opacity-0 group-hover:opacity-100 transition-opacity">zoom_in</span>
            </div>
        `;
        
        grid.appendChild(projectDiv);
    });
    
    // Réactiver les animations et le lightbox
    initializeProjectListeners();
    observeAnimations();
}

function initializeProjectListeners() {
    const lightbox = document.getElementById('lightbox');
    const projectItems = document.querySelectorAll('.project-item');
    
    projectItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            
            const title = item.dataset.title;
            const description = item.dataset.description;
            const category = item.dataset.category;
            const materials = item.dataset.materials;
            const location = item.dataset.location;
            const year = item.dataset.year;
            const image = item.dataset.image;
            
            document.getElementById('lightboxTitle').textContent = title;
            document.getElementById('lightboxDescription').textContent = description;
            document.getElementById('lightboxCategory').textContent = category;
            document.getElementById('lightboxMaterials').textContent = materials;
            document.getElementById('lightboxLocation').textContent = location;
            document.getElementById('lightboxYear').textContent = year;
            document.getElementById('lightboxImage').src = image;
            
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });
}

function observeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const scrollObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.classList.add('visible');
                }, index * 100);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.project-item').forEach((el) => {
        scrollObserver.observe(el);
    });
}

// Charger les projets au chargement de la page
window.addEventListener('DOMContentLoaded', loadProjects);
</script>'''

# Remplacer le contenu
new_content = content[:start_index] + start_marker + '\n' + new_grid_content

# Trouver le script de filtrage et le mettre à jour
filter_script_start = new_content.find('// Filter functionality')
if filter_script_start != -1:
    # Le script de filtrage doit être adapté pour fonctionner avec le chargement dynamique
    print("✓ Script de filtrage trouvé, à adapter manuellement")

# Écrire le nouveau fichier
with open('realisations_dynamic.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Fichier realisations_dynamic.html créé!")
print("⚠️  ATTENTION: Le chargement dynamique nécessite un serveur web (ne fonctionne pas en file://)")
print("⚠️  Il faut également créer un fichier manifest.json avec la liste des fichiers")

