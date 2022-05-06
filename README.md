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
- show_time_left: afficher ou non le temps restant

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


## Methodes

- next(): avance la barre de chargement
- stop(): arrête la barre de chargement