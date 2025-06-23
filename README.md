
# Motor de Recomandare Sustenabil

Acest proiect reprezintă un sistem de recomandare hibrid pentru rețete alimentare, care ține cont de:
- Preferințele utilizatorului (PPI)
- Sănătate (HSI)
- Sustenabilitate ecologică (ESI)
- Explicații ale alegerilor (XAI)

## Structura fișierelor

- `preprocessing.py`: preprocesarea datasetului (`greenrec_dataset.csv`)
- `content_based.py`: recomandări bazate pe similaritatea ingredientelor
- `hybrid_model.py`: sistem hibrid cu scoruri normative
- `app_cli.py`: interfață în linia de comandă
- `app_web.py`: interfață web (Flask)
- `templates/index.html`: formular pentru input
- `templates/results.html`: afișarea recomandărilor

## Instrucțiuni de rulare

### 1. Preprocesare

Asigură-te că ai fișierul `greenrec_dataset.csv` în același folder. Apoi rulează:

```bash
python preprocessing.py
```

### 2. Interfață CLI

```bash
python app_cli.py
```

### 3. Interfață Web

Asigură-te că ai Flask instalat:

```bash
pip install flask
```

Rulează aplicația web:

```bash
python app_web.py
```

Accesează `http://127.0.0.1:5000` în browser.

## Cerințe

- Python 3.7+
- Flask
- pandas, scikit-learn

## Autor

Proiect educațional susținut de un model de recomandare responsabil și sustenabil.
