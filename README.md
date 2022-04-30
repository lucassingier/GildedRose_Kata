# GildedRose Ynov

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](http://forthebadge.com)

Le projet nous proviens d'un TP d'une élective "Méthodologie Tests"

## Parlons de ce projet

Il s'agit d'un exercice de refactoring basé sur le célèbre référentiel GildedRose-Refactoring-Kata maintenu par Emily Bache. 
Ce kata contient du code simple dans de nombreux langages de programmation différents qui doivent être refactorisés et améliorer la qualité du code.

### Notre équipe
- Louis Daflon
- Lucas Singier

### Choix du projet
Nous avons choisi ce sujet car il est quand même plus cool même si on a aucune idée de ce qu’est “TAFKAL80ETC” (manque de culture geek ?). 
Il est mieux structuré que le Trivia et en observant le projet en diagonale, 
les changements à appliquer sont assez explicites.

### Pré-requis

Ce qu'il est requis pour commencer avec ce projet:
- Language Python
- Une bonne tasse de café

### Les différents fichiers

- gilded_rose.py : Fichier du code source référençant les différentes classes d'objets utilisés.
- test_gilded_rose.py : Fichier de test (unittest) permettant de couvrir l'intégralité du code source.
- texttest_fixture.py : Fichier exécutant une partie du code source afin de simuler des actions possibles avec les différentes fonctions.

## Informations

Traitement des Legacy codes Commits fréquents(À chaque refactorisation de smells codes) Travail en binôme (pair programming) Application de la méthode SOLID et obtenir du clean code


## Déroulement du projet

Premièrement:
Identifier les Smells codes Résolution des erreures code+tests

Ensuite:
Refactoriser le code et le test en favorisant le polymorphisme. Mieux découper le code avec de nouvelles classes en utilisant l’héritage.

Enfin:
Publier les résultats (commits) en vérifiant bien les tests et la couverture de code.(sonarqube)



Dites comment faire pour lancer votre projet

## Projet

### Règles métier

* Tous les éléments auront les trois attributs suivants :
    * name– Nom de l'article.
    * sell_in– Le nombre de jours dans lesquels l'article doit être vendu.
    * quality– La qualité de l'article ; désigné par un entier.
* Chaque jour, la méthode update_quality()est exécutée, ce qui diminue les valeurs de sell_inet de quality chacun.
* Une fois la sell_indate passée, la valeur de quality se dégrade deux fois plus vite.
* Il existe également des règles pour chacun des éléments actuellement présents, qui sont les suivantes.
    * AgedBrie augmente sa valeur qualityavec une diminution sell_in.
    * BackstagePasses a les deux règles suivantes :
     * Lorsque sell_inla valeur est supérieure à 10 , quality augmente de 1 .
     * Lorsque sell_inla valeur est inférieure à 10 , quality augmente de 2 .
     * Lorsque sell_inla valeur est inférieure à 5 , quality augmente de 3 .
     * Lorsque sell_inla valeur est inférieure à 0 , quality est défini sur 0 .
* Sulfuras est légendaire, il quality est donc toujours à 80 et sell_insa valeur ne diminue jamais.
* Un nouvel objet - Conjured est à ajouter avec la règle suivante :
    * Les objets invoqués se dégradent quality deux fois plus vite que les objets normaux.

## Contraintes

* Il y a quelques contraintes que nous devons considérer avant de refactoriser.
* Nous ne sommes pas autorisés à modifier la Itemclasse ou les attributs de la Itemclasse.
* Les valeurs minimale et maximale de quality ne peuvent être respectivement que de 0 et 50 .

## Raison de refactoriser
* Lisibilité - La logique actuelle est très difficile à lire car tout est contenu dans une seule classe avec plusieurs instructions if-else imbriquées.
* Logique dupliquée - Il y a quelques logiques qui sont dupliquées. Cela peut être mieux écrit en utilisant une relation de classe parent-enfant.
* La mise en œuvre du nouvel élément Conjured devra modifier les instructions if-else actuelles et cela pourrait nuire à la logique existante.
