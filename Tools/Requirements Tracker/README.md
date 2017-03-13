# Descrizione 
Script in Python realizzato da [@manu0466](https://github.com/orgs/NPE-Developers/people/manu0466) che permette la generazione dei file in linguaggio LaTeX per il tracciamento dei requisiti con le rispettive classi e packages.

## Requisiti
* [Python 3](https://www.python.org/downloads/)

## Istruzioni
**1**. Creare un file JSON di nome `requirements.json` formato come segue:
```
{
   "NomePackage1" : { 
        "Classe1Package1" : {
            "requisiti: [
                "CodiceRequisito1",
                "CodiceRequisito2",
                ...
            ]
        },
        "Classe2Package1: : {
            "requisiti" : [
                ...
            ]
        }
   },
   "NomePackage2" : {
        "Classe1Package2" : {
            "requisiti" : [
                ...
            ]
        }
   },
   ...
}
```
Per un esempio più dettagliato potete osservare come noi abbiamo costruito il nostro [qui](https://github.com/NPE-Developers/documenti/blob/master/2%20-%20RP/Esterni/Definizione%20di%20Prodotto/Sezioni/TracciamentoRequisiti/requirements.json).

**2**. Utilizzare il comando `python Tracker.py` nella stessa cartella all'interno della quale è situato il file `requirements.json` per generare i file in formato`.tex`.

## Bug noti
* Se vengono utilizzati due pacchetti simili tra loro (es. `mario.rossi` e `luigi.rossi`) tutti i requisiti del secondo verranno inclusi nel primo. 
