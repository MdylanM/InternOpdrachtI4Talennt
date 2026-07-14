# Fuel Invoice PDF Processor

## Projectbeschrijving

Dit project zet een PDF met brandstoftransacties om naar een gestructureerd CSV-bestand. De applicatie leest een brandstoffactuur of -bijlage uit, verwijdert irrelevante tekst, groepeert de transacties per kenteken en schrijft de resultaten weg naar een CSV-bestand. Het doel is om een analyse uit te voeren op de kosten en kilometerstanden om onder andere fraude te checken.

Het project is geschreven in Python en maakt gebruik van **pdfplumber** voor het uitlezen van PDF-documenten en **regular expressions (regex)** voor het herkennen van de gegevens.

---

# Werking

De verwerking bestaat uit vier stappen:

1. PDF uitlezen
2. Tekst opschonen
3. Tekst splitsen per kenteken
4. CSV genereren

De `main.py` voert deze stappen achter elkaar uit.

```text
PDF
 │
 ▼
Extract PDF text
 │
 ▼
Clean invoice text
 │
 ▼
Split by license plate
 │
 ▼
Extract transactions
 │
 ▼
CSV output
```

---

# Projectstructuur

```text
project/
│
├── data/
│   └── brandstof.pdf
│
├── output/
│
├── pdf_preprocessed.py
├── main.py
└── README.md
```

---

# Functionaliteiten

## 1. PDF uitlezen

`extract_pdf_text()`

Leest iedere pagina van de PDF uit met behulp van `pdfplumber`.

### Functionaliteit

- Opent het PDF-bestand.
- Leest iedere pagina afzonderlijk.
- Slaat de tekst van iedere pagina op.
- Vangt fouten af zoals:
  - Bestand bestaat niet.
  - Corrupte PDF.
  - Geen leesrechten.

---

## 2. Tekst opschonen

`clean_brandstof_text()`

Niet alle tekst uit de PDF is relevant.

Deze functie:

- verwijdert alle tekst vóór **"Brandstof Bijlage"**;
- zoekt het eerste kenteken;
- stopt zodra dezelfde kentekenlijst opnieuw begint.

Hierdoor blijft alleen de relevante transactietabel over.

---

## 3. Splitsen per kenteken

`split_kentekens()`

De overgebleven tekst wordt opgesplitst in blokken.

Ieder blok bevat:

- één kenteken;
- alle transacties die bij dat kenteken horen.

Voorbeeld:

```text
Kenteken ABC-123

01-01-2025 ...
02-01-2025 ...
03-01-2025 ...
```

---

## 4. Omzetten naar CSV

`text_to_csv()`

Met behulp van reguliere expressies worden de transacties uit ieder kentekenblok gehaald.

Voor iedere transactie worden de volgende gegevens opgeslagen:

- Kenteken
- Datum
- Bonnummer
- Locatie
- Land
- Kilometerstand
- Pasnummer
- Brandstof
- VV
- Aantal (L/kWh)
- Bedrag
- BTW

Het resultaat wordt opgeslagen als een CSV-bestand.

---

# CSV-uitvoer

Voorbeeld:

| Kenteken | Datum | Bonnummer | Locatie | Land | KmStand | Pasnummer | Brandstof | VV | Aantal (L/kWh) | Bedrag | BTW |
|----------|--------|-----------|----------|-------|---------|------------|------------|----|----------------|---------|-----|
| ABC-123 | 01-06-2025 | 12345 | Rotterdam | NL | 150234 | 98765 | Diesel | Ja | 42,50 | 76,20 | 21% |

---

# Benodigde packages

Installeer de benodigde packages met:

```bash
pip install pdfplumber pdfminer.six
```

---

# Gebruik

Plaats het PDF-bestand in de map:

```text
data/
```

met de naam:

```text
brandstof.pdf
```

Voer vervolgens het programma uit:

```bash
python main.py
```

Na het uitvoeren wordt automatisch een CSV-bestand aangemaakt:

```text
output.csv
```

---

# Foutafhandeling

De applicatie bevat foutafhandeling voor onder andere:

- Ontbrekende PDF-bestanden.
- Corrupte PDF-bestanden.
- Geen toegang tot bestanden.
- Fouten tijdens het uitlezen van individuele pagina's.

Wanneer een pagina niet kan worden gelezen, wordt een waarschuwing gelogd en gaat de verwerking verder met de volgende pagina.

---

# Gebruikte technieken

- Python 3
- pdfplumber
- pdfminer.six
- pathlib
- csv
- logging
- regular expressions (regex)

---

# Mogelijke uitbreidingen

- Ondersteuning voor meerdere PDF-formaten.
- Verwerken van meerdere PDF-bestanden tegelijk.
- Export naar Excel (`.xlsx`).
- Unit tests.
- Configuratie via een configuratiebestand.
- Command-line argumenten voor invoer- en uitvoerbestanden.

---

# Auteur

Ontwikkeld als een preprocessing-pipeline voor het automatisch omzetten van brandstoffacturen naar een gestructureerd CSV-bestand voor verdere analyse.
