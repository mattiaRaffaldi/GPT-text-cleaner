# Script di Anonimizzazione Dati Sensibili

## Descrizione
Questo script Python è progettato per anonimizzare i dati sensibili all'interno di un testo, mantenendo il contesto e la leggibilità della frase. È in grado di identificare e sostituire entità come nomi propri, nomi di aziende, percorsi di rete e porzioni di codice, utilizzando sostituzioni realistiche e coerenti.

## Funzionalità
- Identifica entità sensibili in italiano e inglese, come:
  - Nomi propri di persone
  - Nomi di aziende
  - Luoghi geografici
- Sostituisce le entità riconosciute con nomi, aziende e luoghi predefiniti, preservando il significato originale del testo.
- Genera un mapping tra il testo originale e le sostituzioni effettuate, per eventuale tracciamento.

## Requisiti
- Python 3.x
- Le librerie Python seguenti:
  - `spacy`
  - `random` (inclusa di default in Python)

## Installazione
1. Clona questo repository o scarica i file.
2. Crea un ambiente virtuale:
   ```bash
   python -m venv venv
