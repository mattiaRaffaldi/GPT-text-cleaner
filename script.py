import argparse
import spacy
import random
from names_dataset import NameDataset

# Carica i modelli di spaCy per italiano e inglese
nlp_it = spacy.load("it_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

# Crea un'istanza di NameDataset per accedere alle wordlist
nd = NameDataset()

# Funzioni per ottenere nomi casuali e luoghi casuali
def get_random_name():
    first_name, last_name = "", ""
    while not first_name and not last_name:
        first_name = random.choice(list(nd.get_top_names(n=100, country_alpha2='IT')))  # Nomi italiani
        last_name = random.choice(list(nd.get_top_names(n=100, country_alpha2='IT')))    # Cognomi italiani
    return f"{first_name.capitalize()} {last_name.capitalize()}"

def get_random_company():
    company_list = ["TechCorp", "Imprese Innovazioni", "StartupLab", "AziendaCool SPA", "GlobalTech Solutions"]
    return random.choice(company_list)

def get_random_place():
    places = ["Roma", "Milano", "Torino", "New York", "Londra", "Parigi", "Tokyo"]
    return random.choice(places)

# Funzione per generare sostituzioni realistiche
def generate_placeholder(ent, lang):
    if ent.label_ == 'PERSON':
        return get_random_name()
    elif ent.label_ == 'ORG':
        return get_random_company()
    elif ent.label_ in ['GPE', 'LOC']:
        return get_random_place()
    return ent.text  # Se non è un'entità conosciuta, ritorna il testo originale

def anonymize_text(text):
    """Anonimizza entità sensibili mantenendo il contesto della frase."""
    # Analizza il testo sia in italiano che in inglese
    doc_it = nlp_it(text)
    doc_en = nlp_en(text)
    
    mapping = {}
    anonymized_text = text

    # Combina entità da entrambi i modelli (italiano e inglese)
    all_entities = list(doc_it.ents) + list(doc_en.ents)

    for ent in all_entities:
        placeholder = generate_placeholder(ent, lang="it" if ent in doc_it.ents else "en")
        mapping[ent.text] = placeholder
        anonymized_text = anonymized_text.replace(ent.text, placeholder)

    return anonymized_text, mapping

# Funzione principale
def main():
    # Definisci l'argomento da linea di comando utilizzando argparse
    parser = argparse.ArgumentParser(description="Anonimizza un testo con nomi, aziende e luoghi casuali.")
    parser.add_argument("input_text", type=str, help="Il testo da anonimizzare.")
    
    # Parsing degli argomenti
    args = parser.parse_args()

    # Prendi il testo in input dall'utente
    input_text = args.input_text

    # Anonimizza il testo
    anonymized_text, mapping = anonymize_text(input_text)

    # Mostra l'output
    print("Testo anonimizzato:\n", anonymized_text)
    print("\nMapping:\n", mapping)

# Esegui la funzione main
if __name__ == "__main__":
    main()
