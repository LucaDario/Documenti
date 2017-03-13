# Descrizione 
Script in Python realizzato da [@manu0466](https://github.com/orgs/NPE-Developers/people/manu0466) che permette il calcolo dell'[indice di Gulpease](https://it.wikipedia.org/wiki/Indice_Gulpease) su una serie di file in formato `.tex`.

## Requisiti
* [Python 3](https://www.python.org/downloads/)

## Istruzioni
Utilizzare il comando `python Gulpease <directory>` dove `<directory>` può indicare:
1. Il percorso di una cartella. 
  In questo caso lo script ritornerà un intero che indica l'indice di Gulpease totale dato da tutti i file in formato `.tex` presenti all'interno della cartella data.
2. Il percorso di uno specifico file in formato `.tex`. 
  In questo caso lo script ritornerà un intero che rappresenta l'indice di Gulpease per quel dato file.