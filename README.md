<div style="text-align:left;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Uber_logo_2018.svg/1024px-Uber_logo_2018.svg.png" alt="Uber logo" width="300px" style="margin-left: 0px;"/>
</div>

# Description de l'entreprise 📇
Uber est l'une des startups les plus célèbres au monde. Elle a commencé en tant qu'application de covoiturage pour les personnes qui ne pouvaient pas se permettre un taxi. Aujourd'hui, Uber a étendu ses activités à la livraison de nourriture avec Uber Eats, la livraison de colis, le transport de fret et même le transport urbain avec Jump Bike et Lime, que l'entreprise a financés.

L'objectif de l'entreprise est de révolutionner les transports à travers le monde. Elle opère désormais dans environ 70 pays et 900 villes et génère plus de 14 milliards de dollars de revenus! 😮

# Projet 🚧
Un des principaux problèmes que l'équipe d'Uber a constaté est que parfois les chauffeurs ne sont pas disponibles lorsque les utilisateurs en ont besoin. Par exemple, un utilisateur peut se trouver dans le quartier financier de San Francisco alors que les chauffeurs Uber recherchent des clients dans le quartier de Castro.

Bien que les deux quartiers ne soient pas très éloignés, les utilisateurs devraient quand même attendre 10 à 15 minutes avant d'être pris en charge, ce qui est trop long. Les recherches d'Uber montrent que les utilisateurs acceptent d'attendre 5 à 7 minutes, sinon ils annuleraient leur course.

Par conséquent, l'équipe de données d'Uber souhaite travailler sur un projet où leur application recommanderait des zones chaudes dans les grandes villes à tout moment de la journée.

# Objectifs 🎯
Uber dispose déjà de données sur les prises en charge dans les grandes villes. Votre objectif est de créer des algorithmes qui détermineront où se trouvent les zones chaudes où les chauffeurs devraient se trouver. Vous devrez donc :

- Créer un algorithme pour trouver les zones chaudes
- Visualiser les résultats sur un tableau de bord

# Portée de ce projet 🖼️
Pour commencer, Uber veut essayer cette fonctionnalité à New York. Vous vous concentrerez donc uniquement sur cette ville. Les données peuvent être trouvées ici :

👉👉 [Données sur les trajets Uber](https://example.com) 👈👈

Vous devez vous concentrer uniquement sur la ville de New York pour ce projet.

# Assistants 🦮
Pour vous aider à réaliser ce projet, voici quelques conseils qui devraient vous aider :

- Le clustering est votre ami : Les techniques de clustering sont parfaitement adaptées à la tâche. Pensez-y, tous les lieux de prise en charge peuvent être regroupés en différents clusters. Vous pouvez ensuite utiliser les coordonnées des clusters pour déterminer les zones chaudes 😉
- Créez des cartes avec Plotly : Consultez la documentation de Plotly, vous pouvez créer des cartes et les remplir facilement. Bien sûr, il existe d'autres bibliothèques, mais celle-ci devrait bien faire l'affaire.
- Commencez petit pour grandir : Bien qu'Uber veuille avoir des zones chaudes par heure et par jour de la semaine, vous devriez d'abord commencer petit. Choisissez un jour à une heure donnée, puis commencez à généraliser votre approche.

# Livrable 📬
Pour mener à bien ce projet, votre équipe doit :

- Avoir une carte avec des zones chaudes utilisant n'importe quelle bibliothèque Python (Plotly ou autre).
- Vous devriez au moins décrire les zones chaudes par jour de la semaine.
- Comparer les résultats avec au moins deux algorithmes non supervisés comme KMeans et DBScan.

# Résultats 📊
La première approche avec `Kmeans` ne fournit pas des informations aussi précises qu'avec `DBScan`, où nous sommes capables de mettre en évidence des `hotspots` géographiques en lien avec des activités tout au long de la semaine.

1. `Sensibilité à la forme des clusters` : KMeans suppose que les clusters sont de forme sphérique et de taille égale, ce qui peut ne pas être le cas dans des données réelles comme les données de localisation des prises en charge d'Uber. En revanche, DBScan peut détecter des clusters de formes arbitraires et de densités variables.

2. `Détermination du nombre de clusters` : KMeans nécessite de spécifier le nombre de clusters à l'avance, ce qui peut être difficile à déterminer de manière objective. Cela peut conduire à des résultats suboptimaux si le nombre de clusters choisi n'est pas approprié. DBScan, en revanche, peut identifier le nombre de clusters de manière automatique en se basant sur des critères tels que la densité des points.

3. `Sensibilité aux valeurs aberrantes` : KMeans est sensible aux valeurs aberrantes et peut être influencé par elles lors de la définition des centroids des clusters. Cela peut conduire à des clusters mal positionnés ou à une sous-performance de l'algorithme. DBScan, en revanche, est plus robuste aux valeurs aberrantes grâce à sa méthode de détection basée sur la densité.

4. `Performance dans des clusters de densités variables` : KMeans peut avoir du mal à gérer des clusters de densités variables, où certains clusters sont plus denses que d'autres. Cela peut conduire à une mauvaise segmentation des données. DBScan, quant à lui, peut s'adapter efficacement à des clusters de densités variables en définissant les clusters en fonction de la densité locale des points.

En résumé, bien que KMeans soit un algorithme de clustering largement utilisé et efficace dans de nombreux cas, il présente des limitations dans le contexte spécifique de la recommandation de hot zones pour Uber, où les données de localisation peuvent avoir des clusters de formes et de densités variables. Dans de telles situations, `DBScan est une meilleure alternative` grâce à sa capacité à détecter des `clusters` de `forme arbitraire` et de `densité variable`, ainsi qu'à sa `robustesse aux valeurs aberrantes`.

Grâce à cette méthode nous avons relevé des informations intéressantes à différents lieux et instants à `New York` (activités professionnelles ou de loisirs à Downtown Brooklyn, Williamsburg, aéroports, Upper/Lower Manhattan). Cette méthode est fonctionnelle sur notre jeu de données d'avril 2014 et pourrait être `généralisable` sur plusieurs mois voire années, afin de `dégager des tendances`. Par exemple, il est probable que les comportements de la population varient entre l'hiver et l'été, entraînant des changements dans les hotspots. En explorant différentes échelles temporelles, nous pourrions affiner davantage notre analyse et augmenter sa pertinence.
