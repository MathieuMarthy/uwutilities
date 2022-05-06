# bouts de code utiles

## __progress bar__
la barre de progression est un objet qui permet de faire une barre de chargement. 

Elle a de nombreuses options:

    Args:
        steps (int): le nombre de d'étapes
        text (str): le message afficher a gauche de la barre
        pattern_bar (str): le motif de la barre
        pattern_space (str): le motif de l'espace
        lenght (int): la longueur de la barre
        show_steps (bool): afficher les étapes sur le nombre d'étapes total
        show_time (bool): afficher le temps passé sur le temps total
        show_time_left (bool): afficher le temps restant

Exemple d'utilisation:

### Code

```python
from uwutilities import bar
import time

Bar = bar(steps=10, text="chargement", lenght=50)

for _ in range(10):
    Bar.next()
    time.sleep(1)
```
### Resultat
```
chargement | ██████████████████████████████                    | 60% [ steps:  6 / 10 | finished in: 0:00:03 ]
```


### Methodes

- next(): avance la barre de chargement
- stop(): arrête la barre de chargement

## __String_tools__
Cette classe permet de modifier des string facilement.

### Methodes


### - replace
    Args:
        string (str): le string à modifier
        *args (str): les strings à remplacer par pair

    Returns:
        str: le string modifié

#### Code
```python
a = "Hello World"
a = string.replaces(a, "Hello", "Hi", "World", "Earth")
print(a) -> "Hi Earth"
```
### - replaces
    Args:
        string (str): le string à modifier
        index (int): l'index du caractère à remplacer
        char (str): le caractère qui remplace

    Returns:
        str: le string modifié

#### Code
```python
a = "Hello World"
a = string.replace(a, 4, "a")
print(a) -> "Hella World"
```

# __Import__
Cette classe permet d'importer des variable depuis un fichier avec le format
```variable = value```

### Methodes

### get
	Args:
		file (str): the file to import from
		variables (str): the variables to import

	Returns:
		tuple: the imported variables
