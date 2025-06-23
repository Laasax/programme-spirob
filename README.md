
> Open this page at [https://laasax.github.io/programme-spirob/](https://laasax.github.io/programme-spirob/)

# Spirob - TUS - Tentacule Ultra Sophistiqué
## 1.1. Descriptif du projet
Le projet est à l’initiative d’un professeur de technologie du collège Les Hautes Ourmes de Rennes.
Il s'agit de la conception et du développement d'un tentacule biomimétique, s'inspirant des propriétés d'un tentacule de poulpe ou d'une trompe d'éléphant. Cette approche repose sur le mimétisme, une stratégie qui consiste à s'inspirer du fonctionnement des êtres vivants pour concevoir une nouvelle solution de bras robotique.
Le tentacule Spirobs sera conçu de manière à reproduire des mouvements fluides et adaptatifs similaires à ceux observés dans la nature. Ce projet implique plusieurs disciplines techniques, notamment la modélisation 3D, l'électronique, la programmation embarquée et un contrôle à distance via Bluetooth.

## 1.2. Objectifs
L'objectif principal du projet est de fournir un outil pédagogique permettant aux collégiens de découvrir les principes fondamentaux de la programmation et de la robotique dans le cadre de la matière Technologie.
Impression 3D : Mettre en place l’impression du tentacule et trouver le filament correspondent (pour correspondre à l’élasticité du bras)
Développement d'une librairie logicielle : Fournir des méthodes simples par le biais d’une librairie pour l’utiliser sur l’interface Makecode de Microsoft, afin qu’elle soit facilement utilisée par les collégiens.
Intégration d’un moyen communicant sans fil : Utilisation du module Bluetooth intégré de la carte MicroBit.

## 1.3. Composition des membres du projet
Pour réaliser ce projet, la composition de ce groupe sera composée de :
* Binta Ba
* Mouhsine Ben Chakrina
* Hugo Colombel
* Alexandre Bloino

# 2. Pré-requis

Installer les librairies suivantes:
* Radio

# 3. Pins utilisés

Voici l'ensemble des pins utilisés par rapport à la carte électronique conçu pour ce projet.

* P0	: Controle Moteur 1
* P1	: Feedback Moteur 1
* P2	: Feedback Moteur 2
* P3	: Mesure intensité Moteur 1
* P8	: Controle Moteur 2
* P10	: Mesure intensité Moteur 2

# 4. Description du dépot Github

Ce dépot Github comporte principalement la partie programmation sur Makecode de la tentacule.

## 4.1 Dossier Ressources

Ce dossier possède tous les plans et schémas pour réaliser le Spirob.
* Electronique:
Le schéma électronique est fait avec le logiciel Proteus, un gerber est fournie pour refaire des cartes.
* CAO 3D:
La réalisation 3D est faite avec le logiciel Solidworks, tous les fichiers STL sont fournies pour pouvoir les imprimer (boitier, tentacule...)

## 4.2 Dossier Images

Ce dossier permet de répertorier les captures d'écran / photo liés au projet, permettant de le contextualiser.

# 5. Fonctionnement du programme

## 5.1 Importer le programme 

### 5.1.1 Carte émettrice
Pour la carte émettrice, la librairie Radio doit être importée.
Dans ce programme, il faut prendre la fonction Radio Set Group, la mettre dans la boucle Setup, il faut ensuite, dans la boucle infini, envoyé l'orientation "roll" toutes les 50ms sur la communication radio.

![alt text](https://github.com/Laasax/programme-spirob/blob/master/Images/emission.png?raw=true)

### 5.1.2 Carte réceptrice
Pour la carte réceptrice, il faut importer le dépot Git depuis le bouton extension, puis coller le lien Git.

![alt text](https://github.com/Laasax/programme-spirob/blob/master/Images/importation_du_programme.png?raw=true)

## 5.2 Fonctionnement
Afin de faire fonctionner le Spirob, il faut alimenter les 2 cartes MicroBit et alimenter la carte des servomoteurs.
Lorsque tout est alimenté, il suffit d'orienter de gauche à droite pour apprécier les mouvements de la tentacule.