# Descrizione 
Script in Python realizzato da [@manu0466](https://github.com/orgs/NPE-Developers/people/manu0466) che permette la creazione delle tabelle per il tracciamento dei test. 

## Requisiti
* [Python 3](https://www.python.org/downloads/)

## Istruzioni
**1**. Creare un file denominato `test.json` nel formato seguente:
```
{
  "type" : { 
    "id_config": string,
    "skip_not_approved": true/false,
    "tests": [
      {
        "description": string,
        "implemented": true/false,
        "approved": true/false
      },
      ...
    ]
  },
  ...
}
```
Significato dei campi:
* `type` (stringa): indicia la tipologia di test che sono contenuti in quella sezione (es. _Test di unità_, _Test strumentali_, ...).
* `id_config` (stringa): indicica come gli id che rappresentano i vari test devono essere formati. Sono permessi due identificativi particolari:
  * `#POS#`: indica la posizione del test. Ad esempio `id_config : "TU#POS#"` genererà gli id progressivi `TU1`, `TU2`, etc.
  * `[key]`: permette di selezionare un determinato elemento all'interno del JSON che rappresenta il test. Ad esempio `id_config : "TU[description]"` genererà id `TU` seguito dalla descrizione del test, per ogni test.
* `skip_not_approved` (booleano): `true` se si vuole saltare la generazione dei test **non** approvati.
* `tests` (JSONArray): contiene i vari test da generare. Ogni test contiene i seguenti campi:
   * `description` (stringa): descrizione del test.
   * `implemented` (booleano): `true` se questo test è già stato implementato, `false` altrimenti.
   * `approved` (booleano): `true` se questo test è stato approvato, `false` altrimenti

N.B. Per poter visualizzare un esempio completo, il nostro è disponibile [qui](https://github.com/NPE-Developers/documenti/blob/master/2%20-%20RP/Esterni/Piano%20di%20Qualifica/Sezioni/Test/Tabelle/test.json).

**2**. Utilizzare il comando `python Tracker.py` all'interno della cartella che contiene anche il file `test.json` precedentemente creato.
