# bouts de code utiles

## __progress bar__
la barre de progression est un objet qui permet de faire une barre de chargement. 

Elle a de nombreuses options:

- steps: le nombre d'étapes
- text: le texte à afficher a gauche de la bar
- pattern_bar: le string de la partie remplie de la barre
- pattern_space: le string de la partie vide de la barre
- lenght: la longueur de la barre
- show_steps: afficher ou non le nombre d'étapes effectuées sur le total
- show_time: afficher ou non le temps écoulé sur le temps total

Exemple d'utilisation:

```python
from myLibrary import bar
Bar = bar("chargement", steps=10, lenght=50, show_time=False)

for _ in range(10):
    Bar.next()
```

## Methodes

- next(): avance la barre de chargement
- stop(): arrête la barre de chargement