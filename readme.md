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


# Controlepunten Brandstoftransacties

## 1. Hoogste brandstofkosten

Controleer de voertuigen of bestuurders met de hoogste brandstofkosten.

> **Opmerking:** Hoge brandstofkosten betekenen niet automatisch dat er sprake is van fraude, maar deze dossiers verdienen als eerste aandacht.

---

## 2. Ontbrekende kilometerstanden

Controleer transacties waarbij de kilometerstand **0 km** is.

### Controle nodig

Bij brandstoftransacties dient de bestuurder uit te leggen waarom geen kilometerstand is ingevoerd.

### Geen probleem

Een kilometerstand van **0 km** is normaal bij transacties zoals:

- Wasbeurten
- Smeermiddelen

---

## 3. Kilometerontwikkeling

Controleer of de kilometerstanden logisch oplopen.

### Controlepunten

- Teruglopende kilometerstanden.
- Onrealistische sprongen in de kilometerstand.

---

## 4. Opvallende tankfrequentie

Controleer het aantal transacties per bestuurder per maand.

Denk hierbij aan:

- Tankbeurten
- Wasbeurten
- Smeermiddelen
- Shoptransacties

Een opvallend hoog aantal transacties kan aanleiding zijn voor nader onderzoek.

---

## 5. Locaties

Controleer of de tanklocaties logisch zijn ten opzichte van de werkzaamheden van de bestuurder.

### Voorbeelden van logische locaties

- Reeuwijk → Gouda
- Utrecht → Bodegraven
- Schiedam → Bodegraven
- Nieuwegein

Deze locaties lijken normaal.

### Extra controle

Bestuurders die regelmatig op onverwachte of ver afgelegen locaties tanken, verdienen extra aandacht. Dit hoeft niet direct op fraude te wijzen (bijvoorbeeld consultants of buitendienstmedewerkers), maar is wel een controlepunt.

---

## 6. Grote tankinhouden

Controleer transacties waarbij:

- 60–70 liter wordt getankt in een kleine auto.
- Meerdere keren op dezelfde dag wordt getankt.

Dit zijn vaak duidelijke indicatoren die nader onderzocht moeten worden.

---

# Samenvatting van de bevindingen

### Controle nodig

- Ontbrekende kilometerstanden.
- Auto's met uitzonderlijk hoge maandelijkse brandstofkosten.
- Bestuurders die zeer frequent tanken.

### Geen bijzonderheden

- Geen teruglopende kilometerstanden.
- Geen dubbele tankingen op dezelfde dag.
- Geen extreem grote tankvolumes.

---

# Aanbevolen controles voor een controller

Voor een uitgebreidere analyse kunnen de volgende controles worden uitgevoerd:

- Berekening van het aantal kilometers per liter per bestuurder.
- Detectie van tanken voordat de tank redelijkerwijs leeg kan zijn.
- Controle of meer liters worden getankt dan de maximale tankinhoud van het voertuig.
- Vergelijking van het werkelijke brandstofverbruik met de fabrieksopgave.
- Detectie van tanktransacties in de avond, het weekend of tijdens vakanties.
- Toekennen van een fraudescore per bestuurder (0–100).
- Automatisch dashboard met risicoclassificatie:
  - 🟢 Groen (laag risico)
  - 🟠 Oranje (nader onderzoek)
  - 🔴 Rood (hoog risico)
---

# Auteur

Ontwikkeld als een preprocessing-pipeline voor het automatisch omzetten van brandstoffacturen naar een gestructureerd CSV-bestand voor verdere analyse.
