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
