# CharacterForge — Visione e Architettura

> **Documento:** 01 — Visione e Architettura  
> **Versione documento:** 1.0  
> **Stato:** Architecture Baseline  
> **Progetto:** ComfyUI-CharacterForge

---

## 1. Visione

CharacterForge è un sistema parametrico per la costruzione, trasformazione e rappresentazione coerente di asset visivi.

L'obiettivo non è creare esclusivamente personaggi, ma fornire un framework capace di descrivere e mantenere l'identità di:

- esseri umani;
- creature;
- animali;
- esseri antropomorfi;
- oggetti;
- veicoli;
- tecnologia;
- edifici;
- ambienti;
- elementi naturali;
- materiali;
- mondi e scenari.

CharacterForge deve separare l'identità dell'asset dal modo in cui l'asset viene rappresentato.

La stessa identità deve poter essere rappresentata:

- da differenti angolazioni;
- con differenti camere;
- in differenti ambienti;
- con differenti condizioni atmosferiche;
- con differenti illuminazioni;
- attraverso differenti linguaggi artistici;
- attraverso differenti stili cinematografici;
- attraverso trasformazioni controllate.

### Principio fondamentale

> **Cambiare la rappresentazione non deve significare perdere l'identità dell'asset.**

---

## 2. Principi architetturali

### 2.1 Asset Identity First

Ogni asset deve possedere un'identità persistente.

L'identità deve essere separata da:

- prompt;
- workflow;
- modello;
- stile;
- camera;
- ambiente;
- singola immagine.

Un'immagine è una rappresentazione di un asset, non l'asset stesso.

### 2.2 Builder First

CharacterForge deve essere costruito come un sistema di costruzione parametrica.

I preset sono scorciatoie configurative, non sostituti del sistema.

L'utente deve poter controllare progressivamente:

- anatomia;
- aspetto;
- materiali;
- abbigliamento;
- ambiente;
- luce;
- atmosfera;
- camera;
- stile;
- trasformazioni.

### 2.3 Modularità

Ogni responsabilità importante deve appartenere a un modulo identificabile.

Gli Engine devono essere indipendenti dalle implementazioni interne degli altri Engine.

La comunicazione deve avvenire attraverso modelli dati e interfacce condivise.

### 2.4 Preset senza dipendenza dal Core

Un preset può configurare il sistema.

Un preset non deve contenere la logica fondamentale del sistema.

Questo permette di:

- aggiungere preset senza modificare il Core;
- aggiornare il Core senza riscrivere tutti i preset;
- testare separatamente dati e logica.

### 2.5 ComfyUI come integrazione

ComfyUI è il livello di integrazione e visualizzazione del framework.

La logica CharacterForge non deve essere duplicata inutilmente nei nodi ComfyUI.

La direzione architetturale è:

```
ComfyUI Node
    ↓
CharacterForge Core
    ↓
Engine
    ↓
Asset State
    ↓
Output / Conditioning / Workflow
```

---

## 3. Modello concettuale

L'oggetto centrale del sistema è l'**Asset**.

```
Asset
│
├── Identity
│   ├── id
│   ├── name
│   ├── type
│   └── version
│
├── Subject
│   ├── anatomy
│   ├── appearance
│   ├── materials
│   └── identifiers
│
├── Environment
│   ├── location
│   ├── weather
│   ├── season
│   ├── time
│   └── atmosphere
│
├── Camera
│   ├── viewpoint
│   ├── position
│   ├── lens
│   ├── framing
│   └── composition
│
├── Style
│   ├── visual language
│   ├── medium
│   ├── era
│   └── cinematic profile
│
└── Transformations
```

Questa struttura è concettuale e costituisce la direzione del modello dati futuro.

---

## 4. Core

Il Core costituisce il livello comune a tutti gli Engine.

```
core/
├── asset
├── identity
├── parameters
├── registry
└── validation
```

### Asset

Rappresenta l'unità principale del sistema.

### Identity

Contiene gli elementi che permettono di distinguere e mantenere coerente un asset.

### Parameters

Contiene i parametri strutturati utilizzati dagli Engine.

### Registry

Gestisce:

- asset;
- tipi;
- preset;
- stili;
- profili;
- identificatori persistenti.

### Validation

Verifica che lo stato dell'asset sia coerente.

---

## 5. Engine Architecture

Gli Engine rappresentano responsabilità specializzate.

```
engines/
├── human/
├── creature/
├── object/
├── nature/
├── environment/
├── camera/
├── cinematography/
└── transformation/
```

### 5.1 Human Engine

Gestisce la costruzione parametrica di soggetti umani.

Responsabilità:

- anatomia;
- proporzioni;
- struttura corporea;
- volto;
- occhi;
- capelli;
- pelle;
- mani;
- piedi;
- abbigliamento;
- accessori;
- caratteristiche distintive.

### 5.2 Creature Engine

Gestisce:

- animali;
- creature;
- creature fantasy;
- creature biologiche;
- creature antropomorfe;
- ibridi;
- anatomie non umane.

Responsabilità:

- morfologia;
- anatomia;
- pelliccia;
- piume;
- scaglie;
- corna;
- ali;
- arti speciali;
- caratteristiche biologiche o fantastiche.

### 5.3 Object & Technology Engine

Gestisce:

- oggetti;
- strumenti;
- veicoli;
- robot;
- dispositivi;
- macchinari;
- tecnologia;
- oggetti fantasy;
- oggetti fantascientifici.

Parametri previsti:

- geometria;
- materiali;
- componenti;
- scala;
- usura;
- stato;
- dettagli funzionali.

### 5.4 Nature & Matter Engine

Gestisce elementi naturali e materia.

Esempi:

- acqua;
- fuoco;
- ghiaccio;
- fumo;
- nebbia;
- roccia;
- legno;
- metallo;
- vegetazione;
- terra;
- sabbia;
- cristallo;
- energia.

### 5.5 Environment & World Engine

Gestisce il mondo nel quale l'asset viene rappresentato.

Responsabilità:

- interni;
- esterni;
- città;
- foreste;
- montagne;
- deserti;
- spazio;
- edifici;
- stanze;
- strade;
- paesaggi;
- architettura;
- epoca;
- clima;
- stagione;
- ora del giorno;
- condizioni atmosferiche.

---

## 6. Style Engine

Lo Style Engine determina il linguaggio visivo con cui l'asset viene rappresentato.

Non costruisce direttamente l'identità dell'asset.

```
Style Engine
├── Anime
├── Cinematic
├── Retro
├── Western
├── Artistic
└── Custom
```

Il sistema cinematico costituisce un sottosistema specializzato.

```
Cinematic
├── Directors
└── Profiles
    ├── Skin
    ├── Lighting
    ├── Lens
    ├── Film Stock
    ├── Grain
    ├── Color
    ├── Atmosphere
    └── Camera
```

Il database cinematico già esistente deve essere preservato durante la futura riorganizzazione.

---

## 7. Camera Engine

La Camera deve essere indipendente dallo Style Engine.

Parametri previsti:

```
Camera
├── position
├── viewpoint
├── distance
├── angle
├── height
├── lens
├── focal length
├── aperture
├── depth of field
├── framing
└── composition
```

La separazione permette di rappresentare lo stesso asset attraverso differenti viste senza modificarne l'identità.

---

## 8. Cinematography Engine

La Cinematography Engine combina i parametri visivi necessari alla rappresentazione fotografica o cinematografica.

Può utilizzare:

- profili di illuminazione;
- lenti;
- film stock;
- grana;
- colore;
- atmosfera;
- pelle;
- camera;
- profili cinematografici.

Lo Style Engine seleziona il linguaggio visivo.

Il Cinematography Engine definisce come quel linguaggio viene fotografato o filmato.

I due sistemi devono rimanere separabili.

---

## 9. Transformation Engine

Il Transformation Engine modifica un asset mantenendo esplicito il rapporto tra:

```
stato precedente
        ↓
trasformazione
        ↓
stato successivo
```

Una trasformazione deve poter distinguere:

- parametri modificati;
- parametri preservati;
- parametri derivati.

Esempi:

```
Character
    ↓
age +10
```

```
Character
    ↓
different clothing
```

```
Vehicle
    ↓
damaged version
```

```
Environment
    ↓
winter version
```

---

## 10. Reference Sheet System

Il Reference Sheet è un sistema centrale di rappresentazione dell'identità.

Non è limitato ai personaggi.

Deve essere applicabile a:

- personaggi;
- creature;
- animali;
- oggetti;
- veicoli;
- edifici;
- ambienti;
- altri asset supportati.

### Esempio: personaggio

```
             FRONT

LEFT      CHARACTER      RIGHT

              BACK

       Facial Details
       Identifiers
       Proportions
       Palette
       Materials
```

### Esempio: veicolo

```
Front
Rear
Left
Right
Top
Bottom
Interior
Details
```

### Esempio: ambiente

```
Wide
North
South
East
West
Details
```

Il Reference Sheet deve diventare uno strumento per verificare la coerenza dell'identità attraverso differenti rappresentazioni.

---

## 11. Preset Architecture

I preset sono configurazioni dati.

Struttura concettuale:

```
preset_styles/
├── anime/
├── cinematic/
├── retro_80s/
├── western/
└── artistic/
```

Il sistema attualmente contiene:

- **128** preset anime;
- **202** preset cinematic;
- **4** preset retro_80s;
- ulteriori categorie già presenti nel repository.

Il database esistente deve essere preservato.

I preset futuri dovranno poter essere aggiunti senza modificare la logica centrale.

---

## 12. ComfyUI Integration

I nodi ComfyUI costituiscono l'interfaccia operativa.

La logica deve progressivamente essere spostata verso moduli riutilizzabili.

Architettura desiderata:

```
             COMFYUI
                │
                ▼
        CharacterForge Nodes
                │
                ▼
              Core
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
    Engines   Style   Reference
       │      Engine     Sheet
       └────────┼────────┘
                ▼
              Output
```

I nodi non devono contenere copie indipendenti della stessa logica.

---

## 13. Dependency Rules

### Regola 1 — Core

Il Core non deve dipendere dai nodi ComfyUI.

### Regola 2 — Engines

Gli Engine non devono dipendere direttamente da specifici nodi ComfyUI.

### Regola 3 — Preset

Il sistema dei preset deve essere principalmente data-driven.

### Regola 4 — Style e Camera

Style Engine e Camera Engine devono rimanere separabili.

### Regola 5 — Reference Sheet

Il Reference Sheet deve consumare lo stato dell'asset senza diventarne il proprietario.

### Regola 6 — Transformation

Il Transformation Engine deve operare sul modello dell'asset.

### Regola 7 — Single Source of Truth

Una funzione comune deve avere una sola implementazione canonica.

### Regola 8 — Backup

I backup non devono essere caricati come implementazioni operative.

### Regola 9 — Versioning

Le versioni devono avere una sorgente canonica.

### Regola 10 — Testing

Ogni nuovo modulo significativo deve avere almeno un test.

---

## 14. Stato dell'implementazione attuale

Il runtime verificato utilizza:

- Python **3.12.10**;
- PyTorch **2.14.0+cu130**;
- CUDA disponibile;
- NVIDIA GeForce RTX 4090 Laptop GPU.

Nodi registrati: **7**.

### Nodi

```
CharacterForgeGenderController
CharacterForgeEthnicityController
CharacterForgeBodyController
CharacterForgeWeightedConditioning
CharacterForgeHybridLatentSwitch
CharacterForgeStyleTransferNode
CharacterForgeLoRAStyleCombinator
```

### Database stili

| Categoria | Numero |
|---|---:|
| Anime | 128 |
| Cinematic | 202 |
| Retro 80s | 4 |
| Totale dichiarato dal runtime | 333 |

Il runtime ha confermato **333 preset disponibili**.

---

## 15. Debito architetturale noto

### 15.1 Versioning

Sono presenti versioni differenti in:

- package principale;
- package nodes;
- tests;
- singoli moduli.

Deve essere introdotta una sorgente canonica della versione.

### 15.2 LoRA Style Combinator

Sono presenti più implementazioni della classe:

```
nodes/lora_style_combinator.py
nodes/LoRAStyleCombinator.py
nodes/style_transfer_node.py
```

Dovrà essere mantenuta una sola implementazione canonica.

### 15.3 Backup Code

Sono presenti copie sotto:

```
nodes/_backup_conditioning_fix_20260923/
```

Devono essere trattate come archivio e non come sorgente runtime.

### 15.4 Node Registration

La registrazione deve essere centralizzata e prevedibile.

---

## 16. Strategia di migrazione

La riorganizzazione non deve essere distruttiva.

Ordine previsto:

```
1. Documentazione
        ↓
2. Core Model
        ↓
3. Registry
        ↓
4. Style Interfaces
        ↓
5. Engine Interfaces
        ↓
6. Reference Sheet Model
        ↓
7. Migrazione progressiva dei nodi
        ↓
8. Eliminazione dei duplicati
        ↓
9. Consolidamento del versioning
        ↓
10. Test completo
```

Non devono essere rimossi componenti funzionanti prima che la loro sostituzione sia verificata.

---

## 17. Roadmap architetturale

1. Visione e Architettura
2. Style Engine
3. Human Engine
4. Creature Engine
5. Object & Technology Engine
6. Nature & Matter Engine
7. Environment & World Engine
8. Camera & Cinematography Engine
9. Transformation Engine
10. Reference Sheet System
11. ComfyUI Implementation
12. Roadmap

Ogni fase deve produrre:

- documentazione;
- modello dati necessario;
- implementazione;
- test;
- verifica runtime.

---

## 18. Principio finale

CharacterForge non deve diventare una raccolta di preset o nodi indipendenti.

Deve diventare un sistema coerente nel quale:

```
IDENTITÀ
   ↓
ASSET
   ↓
PARAMETRI
   ↓
ENGINE
   ↓
STILE + CAMERA + AMBIENTE
   ↓
TRASFORMAZIONE
   ↓
REFERENCE SHEET
   ↓
RAPPRESENTAZIONE
```

L'immagine finale è il risultato.

L'asset, la sua identità e il suo stato sono il centro del sistema.

---

**Stato del documento:** Architecture Baseline  
**Prossimo documento:** 02 — Style Engine
