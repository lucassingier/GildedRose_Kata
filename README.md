# GildedRose Ynov

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](http://forthebadge.com)

Le projet nous proviens d'un TP d'une élective "Méthodologie Tests"

![alt text](https://www.zupimages.net/up/22/17/o34l.png)

## Parlons de ce projet

Source: https://prograide.com/pregunta/2181/comment-ajouter-des-images-au-fichier-readmemd-sur-github
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


## Identification des smells code
Lors du démarrage du projet, nous avons détecter des smells code (mauvaises pratiques de conception qui conduisent à l’apparition de défauts).

```python
def update_quality(self):
  for item in self.items:
      if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
          if item.quality > 0:
              if item.name != "Sulfuras, Hand of Ragnaros":
                  item.quality = item.quality - 1
      else:
          if item.quality < 50:
              item.quality = item.quality + 1
              if item.name == "Backstage passes to a TAFKAL80ETC concert":
                  if item.sell_in < 11:
                      if item.quality < 50:
                          item.quality = item.quality + 1
                  if item.sell_in < 6:
                      if item.quality < 50:
                          item.quality = item.quality + 1
      if item.name != "Sulfuras, Hand of Ragnaros":
          item.sell_in = item.sell_in - 1
      if item.sell_in < 0:
          if item.name != "Aged Brie":
              if item.name != "Backstage passes to a TAFKAL80ETC concert":
                  if item.quality > 0:
                      if item.name != "Sulfuras, Hand of Ragnaros":
                          item.quality = item.quality - 1
              else:
                  item.quality = item.quality - item.quality
          else:
              if item.quality < 50:
                  item.quality = item.quality + 1
```
Le smell code est identifié pour plusieurs raisons:
- La fonction est trop longue
- Beaucoup de code dupliqué
- Beaucoup trop de boucles ( on s'y perd )

Nous allons donc dans un premier temps éclaircir cette fonction afin d'y voir un peu plus clair !
Nous allons prendre en compte chacun des paramètres (noms d'items) et faire un boucle qui servira un peu comme un switch.

```python
def update_quality(self):
        Age = "Aged Brie"
        Backstage = "Backstage passes to a TAFKAL80ETC concert"
        Sulfuras = "Sulfuras, Hand of Ragnaros"
        
        for item in self.items:
            if item.name == Sulfuras:
                item.sell_in = 0 #TO DO Enlever le critère sell_in de Sulfuras car ne se périme pas
            else:
                item.sell_in -= 1 #Tous les items diminuent leur sell_in de 1

            if item.name == Age:
                if item.quality < 50:
                    item.quality += 1
                item.sell_in -= 1
                if item.sell_in < 0:
                item.sell_in -= 1 #Tous les items diminuent leur sell_in de 1 chaque fin de journée
                if item.name == Age:
                    if item.quality < 50:
                        item.quality += 1

            elif item.name == Backstage:
                if item.quality < 50:
                    item.quality += 1.
                if item.sell_in < 11:
                    item.quality += 1
                    if item.sell_in < 6:
                        item.quality += 1
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0

            elif item.name == Sulfuras:
                if item.quality < 50:
                    if item.sell_in < 0:
                        if item.quality < 50:
                            item.quality += 1
                elif item.name == Backstage:
                    if item.quality < 50:
                        item.quality += 1.
                    if item.sell_in < 11:
                        item.quality += 1
            else:
                if item.quality > 0:
                    item.quality -= 1
                if item.sell_in < 0:
                        if item.sell_in < 6:
                            item.quality += 1
                    if item.sell_in < 0:
                        item.quality = 0
                else:
                    if item.quality > 0:
                        item.quality -=1
                        item.quality -= 1
                    if item.sell_in < 0:
                        if item.quality > 0:
                            item.quality -=1
                  
```
Ce code servira de base pour les prochaines amélioration, cela reste du smell code temporaire.
Nous savons maintenant comment se décompose la fonction et comment bien l'utilisée et la refactorisée.

Tout d'abord, nous allons ajouter la partie Conjured (maudite):

```python
def update_quality(self):
        Age = "Aged Brie"
        Backstage = "Backstage passes to a TAFKAL80ETC concert"
        Sulfuras = "Sulfuras, Hand of Ragnaros"
        Conjured = "Conjured item"

        for item in self.items:
            if item.name == Sulfuras:
                item.sell_in = 0 #TO DO Enlever le critère sell_in de Sulfuras car ne se périme pas
            else:
                item.sell_in -= 1 #Tous les items diminuent leur sell_in de 1 à chaque fin de journée

                if item.name == Age:
                    if item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 0:
                        if item.quality < 50:
                            item.quality += 1
                elif item.name == Backstage:
                    if item.quality < 50:
                        item.quality += 1.
                        if item.sell_in < 11:
                            item.quality += 1
                            if item.sell_in < 6:
                                item.quality += 1
                        if item.sell_in < 0:
                            item.quality = 0
                            
                 # Ajout de la partie Conjured pour les items communs
                 
                elif item.name == Conjured:
                    if item.sell_in < 2:
                        if item.quality > 3:
                            item.quality -= 4
                    else:item.quality -= 2
             
                else:
                    if item.quality > 0:
                        item.quality -= 1
                    if item.sell_in < 0:
                        if item.quality > 0:
                            item.quality -=1
                            item.quality -= 1
```
La partie Conjured placée, il est maintenant venu le temps de passer aux choses sérieuses et de se débarasser de cette fonction disgracieuse.
Pour ce faire, nous allons simplement découper la fonction en plusieurs classes.
- Classe Item (Ne change pas)
```python
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
```
- Classe GildedRose ( Executera les classes en fonction du nom de l'item)
```python
class GildedRose(object):
    def __init__(self, items):
        self.items = items
        
    def update_quality(self):
        
        for item in self.items:
            if item.name == "Aged Brie":
                AgedBrie.update_quality(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                Backstage.update_quality(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                Sulfuras.update_quality(item)
            elif item.name == "Conjured item":
                Conjured.update_quality(item)
            else:
                CommonItem.update_quality(item)
```
- CommonItem (Hérite de Item) Execute l'update pour les objets communs
```python
class CommonItem(Item):
    max_quality = 50
    def decrease_sellin(self):
        self.sell_in -= 1

    def update_quality(self):
        self.sell_in -= 1
        if self.sell_in <= 0:
            self.quality = max(0, self.quality - 2)
        else:
            self.quality = max(0, self.quality - 1)
```
- AgedBrie Execute l'update pour cette item précis (Hérite de CommonItem)
```python
class AgedBrie(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.quality < CommonItem.max_quality:
            self.quality += 1
```                            
- Sulfuras Execute l'update pour cette item précis (Hérite de CommonItem)
```python
class Sulfuras(CommonItem):
    def update_quality(self):
        self.sell_in = 0
```
- Backstage Execute l'update pour cette item précis (Hérite de CommonItem)
```python
class Backstage(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.quality < CommonItem.max_quality:
            self.quality += 1
        if 11 > self.sell_in > 5:
            self.quality += 1
        elif 6 > self.sell_in > 0:
            self.quality += 2
        if self.sell_in < 0:
            self.quality = 0
        if self.quality > CommonItem.max_quality:
            self.quality = CommonItem.max_quality
```
- Conjured Execute l'update pour cette item précis (Hérite de CommonItem)
```python
class Conjured(CommonItem):
    def update_quality(self):
        CommonItem.decrease_sellin(self)
        if self.sell_in <= 0:
            self.quality = max(0, self.quality - 4)
        else:
            self.quality = max(0, self.quality - 2)
```
## Les Tests
Nous avons fait plusieurs cas de tests afin de pouvoir couvrir la totalité des items présents sur plusieurs cas.

### AgedBrie

```python
   def test_AgedBrie_should_increase_quality_1(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    def test_AgedBrie_should_never_has_quality_more50(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        # JOUR +1 
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        # JOUR +2
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_AgedBrie_decrease_sellin_1(self):
        items = [Item("Aged Brie", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)

```
### Backstage

```python
   def test_Backstage_between_11_and_5_sellin_should_increase_quality_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 35)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(37, items[0].quality)

    def test_Backstage_less_5_sellin_should_increase_quality_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(43, items[0].quality)

    def test_Backstage_less_0_sellin_should_be_quality_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 30)]
        gilded_rose = GildedRose(items)
        # Jour +1
        gilded_rose.update_quality()
        # Jour +2
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_Backstage_should_never_has_quality_more50(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_Backstage_decrease_sellin_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
```
### Sulfuras
```python
    def test_Sulfuras_quality_never_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)

    def test_Sulfuras_sellin_always_zero(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 50, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
    
    def test_Sulfuras_sellin_always_zero_never_expired(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
```
### Items Communs
```python
    def test_classic_item_decrease_1_all(self):
        items = [Item("Item commun", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].quality) and self.assertEquals(9, items[0].sell_in)

    def test_classic_item_less_0_sellin_decrease_2_quality(self):
        items = [Item("Item commun", -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality)
```
### Conjured Items
```python
    def test_conjured_item_decrease_1_sellin_2_quality(self):
        items = [Item("Conjured item", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(8, items[0].quality) and self.assertEquals(9, items[0].sell_in)

    def test_conjured_item_less_0_sellin_decrease_1_sellin_2_quality(self):
        items = [Item("Conjured item", -5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(6, items[0].quality) and self.assertEquals(-6, items[0].sell_in)
    
    def test_conjured_item_quality_never_negative(self):
        items = [Item("Conjured item", -40, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality) and self.assertEquals(-41, items[0].sell_in)
```
## Couverture de code
### Avant refactorisation
![alt text](https://zupimages.net/up/22/17/0nk5.png)
### Après refactorisation
![alt text](https://zupimages.net/up/22/17/suei.png)
