# Descrizione
Script realizzato da @manu0466 utilizzando il linguaggio Python per la scrittura 
automatizzata del glossario e dei suoi termini. Esso prende in input i dati in formato JSON e
resittuisce i file generati in linguaggio LaTeX pronti ad essere utilizzati.

## Requisiti
1. [Python3](http://www.python.it/download/)


## Istruzioni all'uso
1. Generare il file json che rappresenterà il glossario con il comando `python Parse.py path_da_analizzare`  
2. Aggiungere i significati ad ogni parola nel file `glossario.json`
3. Generare i vari file .tex con il comando `python LatexEncode.py`

Per **aggiornare** i termini all'interno del glossario sarà sufficiente rieseguire i vari punti.
