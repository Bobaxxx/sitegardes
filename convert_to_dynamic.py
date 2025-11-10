#!/usr/bin/env python3
"""
Convertir realisations.html pour charger dynamiquement depuis all_realisations.json
"""

with open('realisations.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Trouver les indices de début et fin de la section des projets
start_line = None
end_line = None

for i, line in enumerate(lines):
    if '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">' in line:
        start_line = i
    if start_line and '</div>\n' == line and i > start_line + 10:
        # Vérifier si c'est bien la fermeture de la section projets
        if i < len(lines) - 5 and '</div></div>' in lines[i+1]:
            end_line = i + 3  # Inclure les fermetures
            break

if not start_line or not end_line:
    print("❌ Erreur: Impossible de trouver la section des projets")
    exit(1)

print(f"✓ Section des projets trouvée: lignes {start_line} à {end_line}")

# Nouveau contenu pour la grille (vide, sera remplie dynamiquement)
new_grid = '''<div class="bg-white">
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3" id="projectsGrid">
<!-- Les projets seront chargés dynamiquement depuis content/all_realisations.json -->
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
'''

# Reconstruire le fichier
new_lines = lines[:start_line-1] + [new_grid] + lines[end_line+1:]

# Trouver et remplacer le script de chargement
script_start = None
for i, line in enumerate(new_lines):
    if '// Lightbox functionality' in line:
        script_start = i
        break

if script_start:
    # Insérer le nouveau script de chargement AVANT le script lightbox
    loading_script = '''
    // ==================================================
    // CHARGEMENT DYNAMIQUE DES PROJETS DEPUIS JSON
    // ==================================================
    let allProjectsData = [];
    
    async function loadProjects() {
        try {
            const response = await fetch('content/all_realisations.json');
            const data = await response.json();
            allProjectsData = data.realisations;
            
            console.log(`✅ ${allProjectsData.length} projets chargés`);
            displayProjects(allProjectsData);
            
        } catch (error) {
            console.error('❌ Erreur chargement projets:', error);
            document.getElementById('projectsGrid').innerHTML = `
                <div class="col-span-full text-center py-20">
                    <p class="text-red-600">Erreur de chargement des projets. Veuillez réessayer.</p>
                </div>
            `;
        }
    }
    
    function displayProjects(projects, shuffle = false) {
        const grid = document.getElementById('projectsGrid');
        grid.innerHTML = '';
        
        // Mélanger l'ordre si demandé (quand on affiche tous les projets)
        const projectsToDisplay = shuffle ? [...projects].sort(() => Math.random() - 0.5) : projects;
        
        projectsToDisplay.forEach(project => {
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
        observeProjectAnimations();
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
    
    function observeProjectAnimations() {
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
    
    // ==================================================
'''
    
    new_lines.insert(script_start, loading_script)
    
    # Maintenant trouver et mettre à jour le script de filtrage
    filter_start = None
    for i, line in enumerate(new_lines):
        if '// Filter functionality' in line:
            filter_start = i
            break
    
    if filter_start:
        # Trouver la ligne avec allProjects = document.querySelectorAll('.project-item');
        for i in range(filter_start, min(filter_start + 20, len(new_lines))):
            if 'const allProjects = document.querySelectorAll' in new_lines[i]:
                # Remplacer par une version qui filtre depuis allProjectsData
                new_lines[i] = "        // Les projets seront filtrés depuis allProjectsData\n"
                break
        
        # Trouver la partie qui filtre les projets et la remplacer
        for i in range(filter_start, min(filter_start + 100, len(new_lines))):
            if '// Filter projects' in new_lines[i]:
                # Trouver le bloc de code jusqu'à la fermeture
                end_filter = i
                bracket_count = 0
                for j in range(i, min(i + 30, len(new_lines))):
                    if 'allProjects.forEach' in new_lines[j]:
                        end_filter = j
                        # Trouver la fermeture de ce forEach
                        for k in range(j, min(j + 20, len(new_lines))):
                            if '});' in new_lines[k] and 'filter' not in new_lines[k].lower():
                                end_filter = k + 1
                                break
                        break
                
                # Nouveau code de filtrage
                new_filter_code = '''                // Filter projects from allProjectsData
                if (filterValue === 'all') {
                    displayProjects(allProjectsData, true); // Shuffle pour "Tous"
                } else {
                    const filtered = allProjectsData.filter(p => p.category === filterValue);
                    displayProjects(filtered, false);
                }
'''
                new_lines = new_lines[:i] + [new_filter_code] + new_lines[end_filter:]
                break

# Écrire le nouveau fichier
with open('realisations.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ realisations.html converti pour chargement dynamique!")
print("✅ Les projets seront chargés depuis content/all_realisations.json")

