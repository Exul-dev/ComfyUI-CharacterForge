# CharacterForge — Style Engine

> **Documento:** 02 — Style Engine  
> **Versione documento:** 1.0  
> **Stato:** Architecture Baseline  
> **Progetto:** ComfyUI-CharacterForge  
> **Dipendenza:** 01 — Visione e Architettura

---

## 1. Scopo

Lo Style Engine definisce il linguaggio visivo utilizzato per rappresentare un Asset CharacterForge.

Lo Style Engine non deve possedere l'identità dell'Asset.

Deve invece trasformare uno stato di Asset già definito in una rappresentazione coerente con uno stile selezionato.

Il principio è:

```
Asset Identity
      ↓
Style Engine
      ↓
Visual Language
      ↓
Representation
```

Lo stile deve quindi essere considerato una proprietà della rappresentazione e non dell'identità fondamentale dell'asset.

---

## 2. Responsabilità

Lo Style Engine deve essere responsabile di:

- catalogazione degli stili;
- recupero degli stili;
- classificazione;
- descrizione;
- composizione;
- compatibilità;
- intensità;
- prompt style-conditioning;
- denoise raccomandato;
- suggerimenti LoRA;
- profili stilistici;
- normalizzazione;
- integrazione con il sistema cinematico.

Non deve essere responsabile di:

- identità dell'asset;
- anatomia dell'asset;
- generazione dell'immagine;
- gestione diretta del modello AI;
- gestione della GPU;
- gestione del workflow ComfyUI.

---

## 3. Stato attuale

Il repository possiede già una libreria di preset organizzata per categorie.

Struttura attuale:

```
preset_styles/
├── retro_80s/
├── anime/
├── western/
├── artistic/
└── cinematic/
```

Il registry principale è:

```
preset_styles/__init__.py
```

Il registry importa le categorie e costruisce:

```
STYLE_PRESETS
```

attraverso l'unione dei database:

```
RETRO_80S_STYLES
ANIME_STYLES
WESTERN_STYLES
ARTISTIC_STYLES
CINEMATIC_STYLES
```

---

## 4. Categorie attuali

Le categorie attualmente definite sono:

| Categoria | Stato |
|---|---|
| Anime | Implementata |
| Cinematic | Implementata |
| Retro 80s | Implementata |
| Western | Implementata |
| Artistic | Implementata |

La categoria Cinematic costituisce un sottosistema particolarmente strutturato.

---

## 5. Anime Style Database

Il database Anime contiene attualmente **128 stili** verificati nel runtime CharacterForge.

Gli stili sono organizzati come moduli Python separati all'interno di:

```
preset_styles/anime/
```

Il sistema StyleTransferNode carica il database Anime attraverso una funzione dedicata.

Sono presenti due strategie di caricamento:

1. import relativo del package;
2. fallback tramite inserimento della root CharacterForge nel sys.path.

Questo permette al nodo di continuare a funzionare anche in determinati contesti di caricamento differenti.

### Priorità

Quando un nome esiste sia nei preset storici sia nel database Anime, il database Anime ha priorità.

Questo comportamento deve essere preservato durante la futura rifattorizzazione.

---

## 6. Cinematic Style Database

Il database Cinematic contiene attualmente **202 preset** verificati nel runtime.

La struttura è organizzata per registi e profili tecnici condivisi.

Sono attualmente presenti numerosi moduli cinematografici specializzati, tra cui:

- Hitchcock;
- Kubrick;
- Leone;
- Coppola;
- Scorsese;
- Spielberg;
- Fincher;
- Nolan;
- Villeneuve;
- Kurosawa;
- Bergman;
- Fellini;
- Tarkovsky;
- Antonioni;
- Godard;
- Welles;
- Ford;
- Wilder;
- Lean;
- Buñuel;
- Bresson;
- Renoir;
- Lynch;
- Cameron;
- Lucas;
- Stone;
- Tarantino;
- Coen;
- Burton;
- Eastwood;
- Zemeckis;
- Ridley Scott;
- De Palma;
- Wong Kar-wai;
- Paul Thomas Anderson;
- Aronofsky;
- Bong Joon-ho;
- Guillermo del Toro;
- Cuarón;
- Iñárritu;
- Gareth Edwards.

La lista rappresenta la struttura attuale del database e non costituisce un limite architetturale futuro.

---

## 7. Cinematic Profiles

Il sottosistema Cinematic possiede profili tecnici condivisi.

Le categorie attuali sono:

```
profiles/
├── skin.py
├── lighting.py
├── lenses.py
├── film_stock.py
├── grain.py
├── color.py
├── atmosphere.py
└── camera.py
```

Questi profili costituiscono una parte importante dell'architettura cinematografica.

### Skin

Descrive caratteristiche relative alla resa della pelle.

### Lighting

Descrive configurazioni e linguaggi di illuminazione.

### Lenses

Descrive caratteristiche ottiche.

### Film Stock

Descrive caratteristiche della pellicola o della resa equivalente.

### Grain

Descrive la struttura della grana.

### Color

Descrive la risposta cromatica.

### Atmosphere

Descrive condizioni atmosferiche e resa ambientale.

### Camera

Descrive caratteristiche fotografiche e cinematografiche della camera.

---

## 8. Cinematic Normalization

Il registry Cinematic utilizza:

```
normalize_cinematic()
```

dopo aver aggregato i preset dei singoli registi.

Il flusso attuale è:

```
Director Presets
      ↓
CINEMATIC_STYLES
      ↓
normalize_cinematic()
      ↓
Canonical Cinematic Presets
```

La normalizzazione è un elemento architetturale importante.

Il suo scopo è fornire una struttura coerente ai preset cinematici provenienti da fonti differenti.

La normalizzazione deve diventare, nel modello target, un passaggio standard del caricamento degli stili.

---

## 9. Style Registry

Il registry centrale espone attualmente:

```
STYLE_PRESETS
```

e funzioni utility per:

- ottenere uno stile per nome;
- elencare gli stili;
- filtrare per categoria;
- verificare combinazioni compatibili;
- cercare keyword;
- recuperare il prompt;
- recuperare il denoise;
- recuperare i LoRA raccomandati.

API attuale:

```
get_style_by_name()
list_available_styles()
get_styles_by_category()
get_compatible_styles()
search_styles_by_keyword()
get_style_prompt()
get_style_denoise()
get_recommended_loras()
```

Queste funzioni costituiscono la prima forma dell'API dello Style Engine.

---

## 10. Modello dati attuale

I preset attuali sono rappresentati principalmente tramite strutture dict.

Campi osservati nel sistema includono:

```
name
description
prompt
keywords
denoise
denoise_base
recommended_loras
compatible_combinations
lora_strength
structure_weight
color_boost
```

Non tutti i preset devono necessariamente possedere tutti i campi.

Questo modello è funzionale, ma rappresenta uno dei punti che dovrà essere evoluto.

---

## 11. Modello dati target

Il modello architetturale futuro dovrebbe introdurre un'entità Style strutturata.

Concettualmente:

```
Style
│
├── Identity
│   ├── id
│   ├── name
│   ├── category
│   └── version
│
├── Description
│   ├── description
│   └── keywords
│
├── Visual Language
│   ├── medium
│   ├── rendering
│   ├── linework
│   ├── color
│   ├── lighting
│   └── texture
│
├── Conditioning
│   ├── prompt
│   ├── negative_prompt
│   ├── denoise
│   └── weights
│
├── LoRA
│   ├── recommended
│   └── compatibility
│
└── Metadata
    ├── source
    ├── category
    └── tags
```

Questo non deve essere implementato immediatamente.

Prima deve essere definito il contratto dati.

---

## 12. Style Composition

CharacterForge supporta già concettualmente la combinazione di stili attraverso:

- compatible_combinations;
- LoRA Style Combinator;
- weighted conditioning;
- parametri di intensità.

La direzione target è:

```
Base Style
     +
Secondary Style
     +
Technical Profiles
     ↓
Composed Style
```

La composizione deve distinguere tra:

- fusione visiva;
- fusione dei prompt;
- fusione dei LoRA;
- fusione dei parametri;
- conflitti;
- priorità.

Non tutti gli stili devono essere combinabili arbitrariamente.

---

## 13. Style Intensity

Lo Style Transfer Node possiede attualmente:

```
style_intensity
```

come parametro di controllo.

Il concetto deve essere mantenuto e reso parte del modello Style Engine.

La futura semantica deve distinguere almeno:

- intensità 0 = influenza minima dello stile;
- intensità intermedia = influenza parziale;
- intensità 1 = influenza massima configurata.

Il comportamento numerico preciso dovrà essere definito durante l'implementazione del contratto dati.

---

## 14. Style Transfer Node

Il CharacterForgeStyleTransferNode costituisce attualmente il principale punto di accesso ComfyUI al sistema degli stili.

Il nodo:

1. riceve l'immagine;
2. riceve Model, CLIP e VAE;
3. espone un menu degli stili;
4. risolve il preset selezionato;
5. costruisce il conditioning stilistico;
6. applica i parametri di stile;
7. produce l'output del workflow.

Il menu comprende:

```
Preset storici
+
Anime Database
+
Cinematic Database
```

Il nodo dispone inoltre di fallback quando i database non vengono caricati.

Questa caratteristica deve essere preservata.

---

## 15. Preset storici

Il StyleTransferNode contiene ancora una serie di preset incorporati.

Il gruppo attuale comprende:

```
cartoon
anime
ghibli
comic
watercolor
pixel_art
retro_80s_anime
retro_80s_photography
vhs_retro
synthwave_80s
custom_combo
```

Questi preset rappresentano una fase precedente dell'architettura.

La direzione target è trasferirli progressivamente nel registry dei preset, mantenendo però la compatibilità con i workflow esistenti.

---

## 16. LoRA Style Combinator

Il repository possiede un nodo dedicato alla combinazione di LoRA.

Responsabilità attuale:

- selezione LoRA;
- combinazione;
- pesi;
- compatibilità;
- suggerimenti;
- combinazioni testate.

Il nodo rappresenta un componente importante del futuro Style Engine, ma deve essere separato concettualmente dal registry degli stili.

La direzione target è:

```
Style Registry
      ↓
Style Definition
      ↓
LoRA Recommendation
      ↓
LoRA Composition
```

Il LoRA Combinator non deve diventare il proprietario del concetto di Style.

---

## 17. Separazione Style / LoRA

Uno stile e un LoRA non sono la stessa entità.

Uno Style può:

- non richiedere LoRA;
- suggerire un LoRA;
- richiedere più LoRA;
- essere ottenuto tramite prompt;
- essere ottenuto attraverso una combinazione.

Il modello target deve quindi evitare:

```
Style == LoRA
```

e utilizzare:

```
Style
  ├── Prompt
  ├── Parameters
  └── Optional LoRA Strategy
```

---

## 18. Compatibilità

La compatibilità stilistica deve essere trattata come informazione esplicita.

Il sistema attuale supporta:

```
get_compatible_styles(style_name)
```

La futura architettura dovrebbe distinguere:

- compatibile;
- incompatibile;
- combinabile con limitazioni;
- dominante;
- subordinato.

La logica esatta sarà definita nella fase di implementazione del contratto Style.

---

## 19. Ricerca e Discovery

Lo Style Engine deve consentire la ricerca per:

- nome;
- categoria;
- keyword;
- tag;
- autore o fonte;
- epoca;
- linguaggio visivo;
- tecnologia;
- medium;
- caratteristiche tecniche.

L'attuale search_styles_by_keyword() costituisce il primo livello di questo sistema.

La ricerca avanzata dovrà essere introdotta successivamente senza rompere l'API esistente.

---

## 20. Style Layering

La direzione architetturale target prevede più livelli:

```
STYLE
  │
  ├── Base Visual Language
  │
  ├── Era
  │
  ├── Medium
  │
  ├── Rendering
  │
  ├── Lighting
  │
  ├── Color
  │
  ├── Texture
  │
  └── Cinematic Profile
```

Questo consente di evitare una proliferazione infinita di preset.

Un preset dovrebbe poter rappresentare una configurazione coerente di più dimensioni stilistiche.

---

## 21. Style Engine e Cinematography Engine

I due sistemi devono rimanere distinti.

### Style Engine

Risponde alla domanda:

> Qual è il linguaggio visivo?

### Cinematography Engine

Risponde alla domanda:

> Come viene fotografato o filmato questo linguaggio visivo?

Esempio concettuale:

```
Style:
    1990s anime

Cinematography:
    35mm
    soft key light
    shallow depth of field
    film grain
    warm color response
```

Questo permette di utilizzare lo stesso Style con differenti approcci fotografici.

---

## 22. Style Engine e Camera Engine

La camera non deve essere incorporata obbligatoriamente nello stile.

Uno stile può suggerire una camera, ma la camera deve rimanere modificabile.

```
Style
  ↓
Camera Recommendation
  ↓
User Override
  ↓
Final Camera
```

Questo principio è fondamentale per mantenere il Builder-first design.

---

## 23. Style Engine e Asset Identity

Lo Style Engine non deve modificare direttamente:

- identità;
- anatomia fondamentale;
- identificatori;
- struttura persistente dell'asset.

Deve invece produrre una trasformazione rappresentazionale.

```
Persistent Asset
      ↓
Style
      ↓
Styled Representation
```

Questo è particolarmente importante per il Reference Sheet System.

---

## 24. Style Engine e Reference Sheet

Il Reference Sheet deve poter rappresentare lo stesso asset attraverso differenti stili.

Esempio:

```
Asset A
 │
 ├── Anime
 ├── Cinematic
 ├── Watercolor
 └── Retro 80s
```

L'identità dell'Asset deve rimanere la stessa.

Lo stile è una variabile di rappresentazione.

---

## 25. Fallback e Robustezza

Il sistema attuale utilizza fallback per il caricamento dei database.

Questo principio deve essere mantenuto.

Un errore in un database opzionale non dovrebbe impedire il caricamento completo di CharacterForge quando esiste un percorso sicuro alternativo.

Tuttavia, il sistema target dovrà distinguere chiaramente:

- errore recuperabile;
- preset mancante;
- registry incompleto;
- errore strutturale;
- errore critico.

Il fallback non deve nascondere errori architetturali reali.

---

## 26. Single Source of Truth

Il futuro Style Engine deve avere una sola sorgente canonica per ogni concetto.

Attualmente esistono ancora:

- preset nel registry;
- preset storici dentro StyleTransferNode;
- database Anime;
- database Cinematic;
- logiche LoRA separate.

La migrazione dovrà progressivamente convergere verso:

```
Style Registry
      ↓
Style Definitions
      ↓
Consumers
      ├── Style Transfer
      ├── LoRA
      ├── Reference Sheet
      ├── Prompt Builder
      └── Future Engines
```

Non devono essere mantenute copie indipendenti dello stesso stile.

---

## 27. Versioning

Lo Style Engine deve possedere una strategia di versioning coerente.

Ogni Style dovrebbe poter essere identificato attraverso:

```
style_id
style_version
engine_version
```

Una modifica al formato dati non deve necessariamente invalidare tutti gli stili esistenti.

La compatibilità dovrà essere gestita attraverso normalizzazione e migrazione.

---

## 28. Test

Lo Style Engine dovrà essere testabile senza avviare necessariamente l'intero workflow ComfyUI.

Test minimi futuri:

- caricamento registry;
- conteggio preset;
- recupero per ID;
- ricerca;
- filtro categoria;
- validazione schema;
- normalizzazione cinematic;
- compatibilità;
- composizione;
- fallback;
- versioning.

Il runtime attuale ha già dimostrato il caricamento dei database Anime e Cinematic.

---

## 29. Migrazione prevista

La migrazione dello Style Engine deve essere non distruttiva.

Ordine:

```
1. Documentare il comportamento attuale
        ↓
2. Definire Style Schema
        ↓
3. Creare Style Registry canonico
        ↓
4. Migrare i preset storici
        ↓
5. Collegare Anime
        ↓
6. Collegare Cinematic
        ↓
7. Collegare profili tecnici
        ↓
8. Collegare LoRA
        ↓
9. Migrare Style Transfer Node
        ↓
10. Eliminare duplicazioni
        ↓
11. Test completo
```

Nessun database funzionante deve essere eliminato durante le prime fasi.

---

## 30. Stato target

Lo Style Engine finale dovrà consentire:

```
Asset
   ↓
Style Selection
   ↓
Style Composition
   ↓
Technical Profiles
   ↓
Optional LoRA Strategy
   ↓
Camera / Cinematography
   ↓
Reference Representation
```

L'utente deve poter partire:

- da un preset;
- da un builder;
- da una combinazione;
- da uno stile esistente;
- da uno stile custom.

Il preset è quindi un punto di partenza, non un limite.

---

## 31. Principio finale

Lo Style Engine di CharacterForge non deve diventare un semplice elenco di prompt.

Deve diventare un sistema strutturato capace di descrivere un linguaggio visivo.

La direzione finale è:

```
STYLE
=
VISUAL LANGUAGE
+
PARAMETERS
+
OPTIONAL PROFILES
+
OPTIONAL LORA STRATEGY
+
COMPATIBILITY
+
METADATA
```

L'identità dell'asset rimane separata.

La camera rimane separata.

La cinematografia rimane separata.

La trasformazione rimane separata.

Il risultato è uno Style Engine modulare, estendibile e compatibile con il Builder-first design di CharacterForge.

---

**Stato del documento:** Architecture Baseline  
**Documento successivo:** 03 — Human Engine
