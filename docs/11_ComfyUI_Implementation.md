# 11 — ComfyUI Implementation

## 1. Scopo

Questo documento definisce come l'architettura di CharacterForge viene tradotta in una implementazione concreta all'interno di ComfyUI.

L'obiettivo non è soltanto creare nuovi nodi.

L'obiettivo è costruire un'architettura software coerente nella quale:

- Entity Engines;
- Style Engine;
- Camera & Cinematography Engine;
- Transformation Engine;
- Reference Sheet System;
- conditioning;
- workflow;
- preset;
- metadata;
- validazione;

possano convivere senza diventare un insieme di nodi indipendenti e difficili da mantenere.

L'implementazione deve essere:

- modulare;
- testabile;
- estendibile;
- compatibile con ComfyUI;
- compatibile con i componenti esistenti;
- deterministica quando richiesto;
- progressivamente migrabile;
- documentata.

---

## 2. Principio fondamentale

CharacterForge deve essere trattato come un sistema software sopra ComfyUI, non come una semplice raccolta di custom node.

ComfyUI fornisce:

- graph execution;
- node system;
- workflow serialization;
- model loading;
- conditioning;
- latent processing;
- image processing;
- execution infrastructure.

CharacterForge fornisce:

- entity representation;
- identity;
- state;
- transformation;
- styles;
- cinematography;
- reference sheets;
- presets;
- high-level generation logic.

La responsabilità deve rimanere separata.

---

## 3. ComfyUI come Execution Layer

Il modello architetturale concettuale è:

```
CharacterForge Domain Model
```

↓

```
CharacterForge Engine Layer
```

↓

```
CharacterForge Node Layer
```

↓

```
ComfyUI Execution Graph
```

↓

```
Model / Conditioning / Latent / Image Processing
```

CharacterForge non deve duplicare le responsabilità fondamentali di ComfyUI quando queste sono già disponibili.

---

## 4. Domain Layer

Il Domain Layer rappresenta la logica indipendente dall'interfaccia ComfyUI.

Dovrà contenere progressivamente concetti come:

- Entity;
- Identity;
- State;
- Variant;
- Transformation;
- View;
- Reference Sheet;
- Style Profile;
- Camera Profile;
- Environment;
- Material;
- Component;
- Metadata.

Il Domain Layer deve poter essere testato senza avviare ComfyUI.

Questo è fondamentale per mantenere test rapidi e affidabili.

---

## 5. Engine Layer

Gli Engine devono implementare la logica specializzata.

Architettura concettuale:

- Human Engine;
- Creature Engine;
- Object & Technology Engine;
- Nature & Matter Engine;
- Environment & World Engine;
- Camera & Cinematography Engine;
- Style Engine;
- Transformation Engine;
- Reference Sheet System.

Gli Engine devono evitare dipendenze circolari.

---

## 6. Node Layer

I ComfyUI Nodes rappresentano l'interfaccia tra il Domain/Engine Layer e il graph di ComfyUI.

Un nodo dovrebbe:

- ricevere dati;
- validare input;
- invocare un Engine;
- produrre output strutturati;
- evitare di contenere logica di dominio eccessivamente complessa.

La regola è:

```
Node = Adapter
Engine = Logic
Domain = Data and Rules
```

---

## 7. Tipi di output

CharacterForge deve poter produrre diversi tipi logici.

Esempi:

- Entity;
- Entity State;
- Transformation;
- Variant;
- Reference Configuration;
- View Configuration;
- Style Configuration;
- Camera Configuration;
- Prompt Specification;
- Conditioning Specification;
- Reference Sheet Specification;
- Metadata.

Non tutto deve diventare immediatamente un nuovo ComfyUI data type.

Durante le prime fasi possono essere utilizzate strutture Python serializzabili, purché il contratto sia documentato.

---

## 8. Shared Entity Core

L'implementazione futura deve convergere verso un modello condiviso.

Struttura concettuale:

```
Entity

- id
- type
- identity
- anchors
- state
- components
- variants
- transformations
- metadata
```

Questo modello deve essere comune a:

- Human;
- Creature;
- Animal;
- Object;
- Vehicle;
- Building;
- Environment;
- Material.

Gli Engine specializzati possono estendere il modello senza duplicarlo.

---

## 9. Entity ID

Ogni entità persistente deve poter avere un identificatore.

Esempio:

```
character_001
```

L'ID non deve dipendere dal nome visualizzato.

Deve permettere di mantenere la relazione tra:

- canonical reference;
- reference sheets;
- transformations;
- variants;
- workflows;
- metadata.

Gli ID devono essere stabili quando l'identità viene preservata.

---

## 10. State ID

Lo stato deve essere distinto dall'Entity ID.

Esempio:

Entity:

```
character_001
```

States:

- child;
- dult;
- elder;
- injured;
- ecovered.

Questo permette di rappresentare la stessa entità attraverso configurazioni differenti.

---

## 11. Variant ID

Le varianti devono avere un'identità derivata ma distinta.

Esempio:

```
character_001
```

Variants:

- outfit_a;
- outfit_b;
- rmor_a.

Una variante non deve diventare automaticamente una nuova Entity.

---

## 12. Transformation ID

Ogni trasformazione significativa deve poter essere identificata.

Esempio:

```
transformation_0042
```

Questo permette di collegare:

- source state;
- transformation;
- target state;
- parameters;
- history.

---

## 13. Node Categories

I nodi CharacterForge dovranno progressivamente essere organizzati per categoria.

Possibile struttura:

```
CharacterForge/Entity
CharacterForge/Human
CharacterForge/Creature
CharacterForge/Object
CharacterForge/Nature
CharacterForge/Environment
CharacterForge/Camera
CharacterForge/Style
CharacterForge/Transformation
CharacterForge/Reference
CharacterForge/Conditioning
CharacterForge/Utility
```

La classificazione deve essere stabile e leggibile nell'interfaccia di ComfyUI.

---

## 14. Existing Nodes

L'implementazione deve preservare i nodi attuali.

Tra i componenti esistenti sono presenti sistemi relativi a:

- Gender Controller;
- Ethnicity Controller;
- Body Controller;
- Weighted Conditioning;
- Hybrid Latent Switch;
- Style Transfer;
- LoRA Style Combinator;
- Scene Interrogation.

Questi componenti non devono essere eliminati soltanto perché l'architettura futura introduce nuovi Engine.

Devono essere progressivamente integrati o adattati.

---

## 15. Compatibility First

La compatibilità deve avere priorità durante la migrazione.

Un nuovo sistema non deve rompere:

- workflow esistenti;
- class names;
- node mappings;
- input names;
- output names;
- preset esistenti;
- cinematic styles;
- anime styles.

Quando una modifica breaking è inevitabile deve essere esplicitamente versionata.

---

## 16. Current Style Infrastructure

L'attuale Style Engine contiene già una quantità significativa di preset.

Sono presenti sistemi per:

- anime;
- artistic;
- cinematic;
- retro;
- western;
- director profiles;
- lighting profiles;
- lens profiles;
- film stocks;
- grain;
- color;
- atmosphere;
- camera profiles.

Questa infrastruttura deve essere preservata.

Il nuovo Style Engine deve quindi evolvere sopra l'infrastruttura esistente anziché sostituirla senza migrazione.

---

## 17. Cinematic Preservation

Il sistema cinematic esistente deve essere considerato patrimonio del progetto.

Le configurazioni dei registi e dei profili cinematici non devono essere riscritte arbitrariamente durante l'introduzione dei nuovi Engine.

La normalizzazione deve essere incrementale.

L'obiettivo è separare progressivamente:

- director style;
- camera;
- lighting;
- film stock;
- grain;
- color;
- atmosphere;

senza perdere la compatibilità con i preset già presenti.

---

## 18. Preset Loading

I preset devono essere caricati modularmente.

Un preset non dovrebbe richiedere la modifica del core per essere aggiunto.

Il caricamento deve poter:

- scoprire preset;
- validare preset;
- normalizzare preset;
- registrare preset;
- esporre preset ai nodi.

Gli errori di un singolo preset non devono compromettere inutilmente l'intero sistema quando è possibile isolarli.

---

## 19. Style Registration

Lo Style Engine deve fornire un registro centralizzato.

Concettualmente:

```
Style Registry

- style_id;
- category;
- metadata;
- parameters;
- source;
- version.
```

Il registro deve permettere ai nodi di interrogare gli stili senza conoscere la struttura interna di ogni singolo preset.

---

## 20. Camera Registration

La stessa logica deve essere applicata alle configurazioni camera.

```
Camera Registry

- camera_id;
- lens;
- focal_length;
- sensor;
- framing;
- aperture;
- focus;
- movement;
- metadata.
```

I Director Presets possono referenziare camera profiles senza duplicarne la definizione.

---

## 21. Transformation Nodes

Il Transformation Engine dovrà essere esposto gradualmente attraverso nodi dedicati.

Possibili nodi futuri:

- Entity Transformation;
- Age Transformation;
- Morphology Transformation;
- Material Transformation;
- Damage Transformation;
- State Transformation;
- Environment Transformation;
- Transformation Chain;
- Transformation History.

Non è necessario creare un nodo separato per ogni tipo se il sistema può rappresentare più trasformazioni attraverso un'interfaccia parametrica coerente.

---

## 22. Reference Nodes

Il Reference Sheet System potrà essere esposto attraverso nodi come:

- Create Reference;
- Configure Reference View;
- Build Reference Sheet;
- Create Transformation Sheet;
- Create Variant Sheet;
- Validate Identity;
- Export Reference Metadata.

I nodi devono lavorare su strutture condivise.

---

## 23. Human Nodes

L'implementazione Human dovrà progressivamente evolvere da controller isolati verso un Human Engine.

I controller esistenti possono diventare adapter.

Esempio:

```
Gender Controller
↓
Human Engine
↓
Entity State
```

Questo permette di preservare il comportamento esistente introducendo gradualmente il nuovo modello.

---

## 24. Creature Nodes

Il Creature Engine potrà essere esposto tramite:

- Creature Builder;
- Anatomy Controller;
- Morphology Controller;
- Surface Controller;
- Creature Identity;
- Creature Transformation.

L'obiettivo è evitare una semplice collezione di prompt preset.

---

## 25. Object Nodes

L'Object & Technology Engine potrà fornire:

- Object Builder;
- Component Builder;
- Material Controller;
- Damage Controller;
- Technology Controller;
- Vehicle Builder;
- Technical Reference.

---

## 26. Nature Nodes

Il Nature & Matter Engine potrà fornire:

- Material Builder;
- Matter State;
- Vegetation Builder;
- Weather Controller;
- Phenomenon Controller;
- Natural Transformation.

---

## 27. Environment Nodes

L'Environment & World Engine potrà fornire:

- Environment Builder;
- Zone Builder;
- Biome Builder;
- Terrain Controller;
- Architecture Controller;
- Weather Controller;
- Time Controller;
- Environment Reference.

---

## 28. Camera Nodes

Il Camera Engine potrà fornire:

- Camera Builder;
- Lens Profile;
- Shot Type;
- Framing;
- Depth of Field;
- Camera Movement;
- Cinematography Profile.

La camera deve essere riutilizzabile tra entità diverse.

---

## 29. Style Nodes

Lo Style Engine potrà fornire:

- Style Builder;
- Style Selector;
- Style Combiner;
- Style Transfer;
- LoRA Style Combinator;
- Style Inspector.

Le funzionalità già presenti devono essere migrate gradualmente verso un registro e una struttura comuni.

---

## 30. Conditioning Layer

Il conditioning deve essere trattato come un livello di traduzione.

```
Domain Model
↓
Semantic Representation
↓
Prompt Specification
↓
Conditioning
↓
ComfyUI Model
```

Questo evita che il Domain Layer diventi dipendente direttamente dal testo del prompt.

---

## 31. Prompt Specification

CharacterForge deve poter rappresentare semanticamente un prompt prima di convertirlo in testo.

Esempio concettuale:

```
Entity:
Human

Identity:
female_001

State:
adult

View:
three_quarter_front

Camera:
85mm

Style:
cinematic_fincher

Environment:
urban_night
```

Questo può poi essere trasformato in una rappresentazione testuale o in altri conditioning.

---

## 32. Prompt Assembly Rules

Il sistema deve definire una gerarchia.

Esempio:

```
Identity
>
Structure
>
State
>
View
>
Camera
>
Environment
>
Style
>
Secondary Details
```

La gerarchia concreta può essere configurabile.

L'obiettivo è evitare che un dettaglio stilistico sovrascriva accidentalmente una caratteristica identitaria.

---

## 33. Negative Conditioning

Il sistema deve poter supportare negative conditioning senza incorporarlo rigidamente negli Engine.

I negativi devono poter essere associati a:

- style;
- view;
- model family;
- workflow;
- entity type.

Devono essere modulari.

---

## 34. Model Independence

CharacterForge non deve dipendere concettualmente da un singolo modello generativo.

L'architettura deve poter lavorare con differenti pipeline quando le interfacce lo consentono.

Il Domain Model deve rimanere indipendente da:

- checkpoint specifico;
- VAE specifico;
- sampler specifico;
- scheduler specifico.

---

## 35. Workflow Architecture

I workflow devono essere considerati configurazioni di esecuzione.

Non devono diventare il luogo principale della logica di dominio.

Il workflow dovrebbe orchestrare:

- input;
- nodes;
- model pipeline;
- conditioning;
- generation;
- post-processing;
- output.

La semantica dell'asset deve provenire dai sistemi CharacterForge.

---

## 36. Workflow Versioning

I workflow devono essere versionati.

Una modifica ai nodi può richiedere una nuova versione del workflow.

Il sistema deve evitare che un workflow vecchio venga interpretato in modo silenziosamente differente.

Quando possibile:

- migrazione automatica;
- warning;
- compatibility layer.

---

## 37. Workflow Metadata

I workflow CharacterForge dovrebbero poter includere metadata come:

- CharacterForge version;
- workflow version;
- entity schema version;
- style version;
- camera version;
- transformation version.

Questo permette di diagnosticare problemi di compatibilità.

---

## 38. Serialization Boundaries

Devono essere definiti confini chiari tra:

- Python runtime objects;
- serialized entity data;
- ComfyUI node inputs;
- workflow JSON;
- image metadata.

Non bisogna affidarsi a strutture Python non serializzabili nei punti in cui ComfyUI richiede dati persistenti.

---

## 39. Validation Layer

La validazione deve avvenire a più livelli.

### Domain Validation

Controlla la correttezza semantica.

### Engine Validation

Controlla la compatibilità con lo specifico Engine.

### Node Validation

Controlla input e output del nodo.

### Workflow Validation

Controlla la compatibilità del graph.

### Runtime Validation

Controlla ciò che può essere verificato solo durante l'esecuzione.

---

## 40. Error Strategy

Gli errori devono essere:

- espliciti;
- leggibili;
- localizzati;
- riproducibili;
- testabili.

Un errore di un preset non dovrebbe apparire come un errore generico del modello.

Un errore di serializzazione non dovrebbe apparire come un errore CUDA.

La diagnostica deve mantenere il contesto.

---

## 41. Logging

CharacterForge deve poter utilizzare logging strutturato.

Le informazioni utili includono:

- node;
- engine;
- entity;
- state;
- transformation;
- style;
- camera;
- workflow;
- version;
- error type.

Il logging dettagliato deve poter essere controllato.

---

## 42. Determinism and Seeds

Quando richiesto, il sistema deve propagare il seed.

Il seed deve poter essere associato a:

- transformation;
- variant generation;
- view generation;
- image generation.

Un seed non deve essere usato come sostituto dell'identità.

Stesso seed non significa necessariamente stessa identità.

---

## 43. Performance

La nuova architettura non deve introdurre overhead inutile.

Priorità:

- caricamento lazy;
- cache;
- registri persistenti in memoria;
- validazione efficiente;
- evitare scansioni ripetute dei preset;
- evitare duplicazione dei dati;
- evitare caricamenti GPU non necessari.

La generazione immagini rimane responsabilità della pipeline ComfyUI.

---

## 44. Memory Management

CharacterForge deve rispettare il modello di gestione memoria della configurazione ComfyUI dell'utente.

Non deve introdurre meccanismi che forzino inutilmente:

- caricamento completo dei modelli;
- duplicazione dei tensori;
- trasferimenti GPU superflui;
- copie massive in RAM.

I componenti puramente descrittivi devono rimanere leggeri.

---

## 45. Offload Compatibility

L'architettura deve essere compatibile con configurazioni ComfyUI che utilizzano:

- CPU offload;
- RAM offload;
- VRAM management;
- low VRAM modes;
- lazy loading.

CharacterForge non deve presumere che tutto risieda permanentemente in VRAM.

---

## 46. GPU Boundary

Gli Engine di dominio devono rimanere preferibilmente indipendenti dalla GPU.

Le operazioni GPU devono essere concentrate nei livelli che ne hanno effettivamente bisogno.

Questo permette di:

- testare il dominio senza CUDA;
- usare CPU per validazione;
- ridurre consumo memoria;
- migliorare portabilità.

---

## 47. Thread Safety

I registri globali devono essere progettati con attenzione.

Particolare attenzione deve essere posta a:

- style registry;
- camera registry;
- preset registry;
- caches.

Il caricamento ripetuto del modulo non deve produrre duplicazioni incontrollate.

---

## 48. Import Architecture

Gli import devono evitare cicli.

Regola concettuale:

```
Domain
↓
Engines
↓
Nodes
↓
ComfyUI integration
```

Un Engine non dovrebbe importare un Node per utilizzare la propria logica.

---

## 49. Package Initialization

I file __init__.py devono avere responsabilità limitate.

Devono principalmente:

- registrare moduli;
- esporre versioni;
- costruire mapping;
- inizializzare registri necessari.

La logica complessa deve rimanere nei moduli appropriati.

---

## 50. Node Registration

La registrazione dei nodi deve essere centralizzata e leggibile.

Devono essere evitati:

- mapping duplicati;
- classi duplicate;
- import ridondanti;
- alias ambigui;
- registrazioni multiple della stessa classe.

Ogni nodo deve avere un'identità chiara.

---

## 51. Duplicate Detection

Il progetto deve prevedere controlli per rilevare:

- file duplicati;
- classi duplicate;
- mapping duplicati;
- preset duplicati;
- style ID duplicati;
- camera ID duplicati.

Questo è particolarmente importante durante la migrazione dell'architettura attuale.

---

## 52. Legacy Compatibility

I componenti legacy devono essere mantenuti finché esistono workflow che li utilizzano.

La migrazione deve seguire:

```
Legacy
↓
Adapter
↓
New Engine
↓
New API
```

Quando un componente legacy viene eliminato, deve esistere una motivazione documentata.

---

## 53. Adapter Pattern

Gli adapter sono fondamentali per la migrazione.

Esempio:

```
Legacy Body Controller
↓
Human Engine Adapter
↓
Human State
```

Questo permette di modernizzare il core senza interrompere immediatamente il comportamento esistente.

---

## 54. API Stability

Le API interne devono essere versionabili.

Quando possibile:

- mantenere firme esistenti;
- aggiungere nuovi parametri in modo compatibile;
- utilizzare default sicuri;
- documentare breaking changes.

La stabilità dell'API è importante quanto quella dei workflow.

---

## 55. Testing Architecture

I test devono essere organizzati per livello.

```
tests/
├── domain/
├── engines/
├── nodes/
├── presets/
├── styles/
├── camera/
├── transformation/
├── reference/
├── workflows/
└── integration/
```

La struttura concreta può evolvere, ma deve riflettere l'architettura.

---

## 56. Domain Tests

Devono essere eseguibili senza ComfyUI quando possibile.

Devono verificare:

- entity;
- identity;
- state;
- variant;
- transformation;
- serialization;
- validation.

Questi test devono essere veloci.

---

## 57. Engine Tests

Devono verificare la logica degli Engine.

Esempi:

- Human constraints;
- Creature morphology;
- Object components;
- Material state;
- Environment hierarchy;
- Camera configuration;
- Style normalization;
- Transformation continuity;
- Reference Sheet generation.

---

## 58. Node Tests

Devono verificare:

- input types;
- defaults;
- output types;
- execution;
- error handling;
- ComfyUI compatibility.

Quando possibile non devono richiedere una generazione GPU completa.

---

## 59. Integration Tests

Gli integration test devono verificare:

- node registration;
- preset discovery;
- style registry;
- workflow loading;
- complete graph execution;
- interoperability tra Engine.

I test GPU devono essere separati dai test puramente logici.

---

## 60. Regression Tests

Ogni bug corretto deve poter diventare un regression test quando ragionevole.

Questo è particolarmente importante per:

- workflow;
- node mappings;
- preset loading;
- conditioning;
- cinematic styles;
- serialization.

---

## 61. Documentation

Ogni nuovo Engine deve avere:

- architecture document;
- API notes;
- examples;
- tests;
- migration notes.

Il codice non deve diventare l'unica fonte di verità.

La documentazione architetturale rimane il riferimento principale per il comportamento previsto.

---

## 62. Current Repository Structure

La struttura target deve evolvere verso qualcosa di simile:

```
ComfyUI-CharacterForge/
├── docs/
├── nodes/
├── engines/
├── domain/
├── styles/
├── presets/
├── schemas/
├── workflows/
├── tests/
├── examples/
├── config/
├── __init__.py
├── README.md
├── requirements.txt
└── CHANGELOG.md
```

La migrazione deve essere incrementale.

Non è necessario creare immediatamente tutte le directory.

---

## 63. Existing Repository Preservation

Durante la migrazione devono essere preservati:

- repository Git;
- workflow funzionanti;
- preset;
- cinematic library;
- anime library;
- test esistenti;
- backup utili;
- compatibilità.

Nessun file deve essere cancellato soltanto perché appare ridondante senza prima verificare il suo utilizzo.

---

## 64. Duplicate Module Cleanup

Il repository attuale contiene aree che richiedono una futura normalizzazione, inclusi moduli duplicati o versioni parallele.

Prima di rimuovere qualsiasi duplicato devono essere verificati:

- import;
- runtime registration;
- workflow references;
- test references;
- Git history;
- compatibilità.

La pulizia deve avvenire in una fase dedicata.

Non deve essere eseguita durante la semplice introduzione dell'architettura.

---

## 65. Versioning Strategy

CharacterForge deve distinguere almeno:

- package version;
- engine version;
- schema version;
- preset version;
- workflow version.

Un singolo numero di versione non è sempre sufficiente a descrivere la compatibilità interna.

Le versioni devono essere utilizzate soprattutto quando cambiano contratti strutturali.

---

## 66. Configuration

La configurazione globale deve essere separata dalla logica.

Possibili configurazioni:

- preset paths;
- style paths;
- cache;
- logging;
- validation;
- compatibility mode.

I default devono essere sicuri.

---

## 67. External Dependencies

Le nuove dipendenze devono essere introdotte solo quando necessarie.

Prima di aggiungere una libreria bisogna valutare:

- funzione;
- peso;
- compatibilità;
- manutenzione;
- licenza;
- impatto su installazione;
- disponibilità nell'ambiente ComfyUI.

CharacterForge deve rimanere il più possibile leggero.

---

## 68. Backward Compatibility

La compatibilità deve essere considerata su tre livelli:

### API Compatibility

Vecchi import e classi.

### Workflow Compatibility

Vecchi graph ComfyUI.

### Data Compatibility

Vecchi preset e configurazioni.

Una migrazione completa deve considerare tutti e tre.

---

## 69. Migration Phases

L'implementazione deve procedere per fasi.

### Phase A

Documentazione e contratti.

### Phase B

Domain Core.

### Phase C

Registry e schemas.

### Phase D

Adapters per sistemi esistenti.

### Phase E

Nuovi Engine.

### Phase F

Nuovi Nodes.

### Phase G

Reference Sheet.

### Phase H

Transformation.

### Phase I

Workflow modernization.

### Phase J

Legacy cleanup.

Nessuna fase deve essere saltata senza una ragione documentata.

---

## 70. First Implementation Rule

Il primo codice della nuova architettura non deve essere il Reference Sheet renderer.

Deve essere il **Domain Core minimo**.

Prima devono essere definiti:

- Entity;
- Identity;
- State;
- Variant;
- Transformation;
- metadata.

Successivamente gli Engine potranno utilizzare queste strutture.

---

## 71. Second Implementation Rule

Dopo il Domain Core devono essere introdotti:

- schema;
- validation;
- serialization;
- registry.

Questo crea fondamenta stabili prima dell'aggiunta di molti nodi.

---

## 72. Third Implementation Rule

I sistemi esistenti devono essere collegati attraverso adapter.

Non bisogna riscrivere contemporaneamente:

- Body Controller;
- Gender Controller;
- Ethnicity Controller;
- Style Transfer;
- LoRA systems;
- Cinematic presets.

La migrazione deve essere controllabile.

---

## 73. ComfyUI Node Contract

Ogni nodo CharacterForge deve definire chiaramente:

- INPUT_TYPES;
- RETURN_TYPES;
- RETURN_NAMES;
- FUNCTION;
- CATEGORY;
- OUTPUT_NODE quando necessario.

Il comportamento deve essere documentato.

I nomi devono rimanere stabili dopo la pubblicazione salvo breaking change esplicita.

---

## 74. Lazy Discovery

Preset e stili possono essere scoperti e caricati in modo lazy quando appropriato.

Questo riduce:

- tempo di startup;
- memoria;
- import overhead.

Tuttavia, la discovery deve essere deterministica.

Lo stesso repository deve produrre lo stesso registry logico.

---

## 75. Cache Strategy

Le cache devono essere utilizzate per:

- preset parsing;
- schema compilation;
- style normalization;
- registry discovery.

Non devono conservare inutilmente:

- grandi tensori;
- immagini;
- modelli GPU;

quando questi appartengono già alla gestione di ComfyUI.

---

## 76. Metadata Propagation

Quando un'entità attraversa il workflow, i metadata importanti devono poter essere propagati.

Esempio:

```
Entity
→ Transformation
→ Reference
→ Prompt
→ Generation
```

Il risultato dovrebbe poter conservare almeno:

- entity_id;
- state_id;
- variant_id;
- transformation_id;
- style_id;
- camera_id;
- seed;
- version.

---

## 77. Image Metadata

Quando tecnicamente possibile, informazioni non sensibili relative alla generazione possono essere associate all'immagine.

Devono essere considerate:

- entity reference;
- view;
- style;
- camera;
- transformation;
- workflow version.

La metadata strategy deve evitare di rendere obbligatoria una modifica al formato immagine quando non necessaria.

---

## 78. Failure Isolation

Un problema in un componente non dovrebbe compromettere inutilmente gli altri.

Esempio:

Un preset cinematico non valido non dovrebbe impedire il caricamento di tutti gli altri preset validi.

Un Reference Sheet non valido non dovrebbe impedire l'esecuzione di un workflow che non lo utilizza.

L'isolamento deve essere applicato dove tecnicamente possibile.

---

## 79. Security and Safety of Loading

I preset e le configurazioni devono essere trattati come dati.

Il caricamento deve evitare esecuzioni arbitrarie quando un formato dichiarativo è sufficiente.

Particolare attenzione deve essere posta a:

- path traversal;
- import dinamici;
- file esterni;
- serializzazione;
- configurazioni non attendibili.

---

## 80. Development Workflow

Lo sviluppo deve seguire una sequenza controllata:

1. documentare;
2. definire schema;
3. implementare;
4. testare;
5. verificare runtime;
6. aggiornare workflow;
7. aggiornare documentazione;
8. versionare.

Non deve essere introdotto codice complesso senza test corrispondenti.

---

## 81. Runtime Verification

Dopo ogni modifica strutturale significativa devono essere verificati almeno:

- import CharacterForge;
- node registration;
- preset loading;
- style registry;
- cinematic registry;
- workflow compatibility.

Quando la modifica riguarda GPU o conditioning devono essere eseguiti anche test runtime appropriati.

---

## 82. Git Strategy

Le modifiche architetturali devono essere facilmente reversibili.

Si raccomanda di mantenere commit focalizzati:

- domain core;
- schemas;
- registry;
- adapters;
- engines;
- nodes;
- workflows;
- cleanup.

Non bisogna mischiare una grande migrazione architetturale con una pulizia indiscriminata del repository.

---

## 83. Current Runtime Baseline

Prima di introdurre il nuovo Domain Core deve essere conservato un baseline runtime.

Il baseline deve verificare:

- import package;
- version;
- node count;
- node registration;
- preset count;
- cinematic count;
- anime count;
- style transfer;
- existing workflows.

Questo baseline permette di capire immediatamente se una modifica ha causato una regressione.

---

## 84. Definition of Done

Un nuovo componente CharacterForge è considerato pronto quando:

- documentato;
- implementato;
- testato;
- validato;
- integrato;
- compatibile con il runtime;
- registrato;
- versionato.

La sola presenza del file Python non è sufficiente.

---

## 85. Anti-Patterns

Devono essere evitati:

- mega-file;
- mega-node;
- logica duplicata;
- preset hardcoded nel core;
- prompt concatenati senza schema;
- mapping duplicati;
- import circolari;
- global state incontrollato;
- fallback silenziosi;
- dipendenze inutili;
- modifiche distruttive;
- migrazioni simultanee non verificabili.

---

## 86. Architecture Boundary

La separazione fondamentale deve essere:

**Domain**

Che cos'è l'entità?

**Engine**

Come viene elaborata?

**Node**

Come viene esposta a ComfyUI?

**Workflow**

Come viene orchestrata?

**Model Pipeline**

Come viene generata l'immagine?

Questa separazione deve rimanere leggibile anche quando il progetto cresce.

---

## 87. Future Expansion

L'architettura deve poter supportare in futuro:

- asset libraries;
- persistent projects;
- multi-character scenes;
- animation;
- storyboard;
- shot lists;
- batch generation;
- identity tracking;
- automatic consistency analysis;
- production pipelines;
- external asset import/export;
- model-specific adapters.

Queste funzionalità non devono essere implementate prematuramente.

Devono essere rese possibili dall'architettura.

---

## 88. Final Principle

CharacterForge deve utilizzare ComfyUI come **execution environment**, non come sostituto del proprio modello concettuale.

ComfyUI esegue.

CharacterForge definisce:

- identità;
- stato;
- trasformazione;
- variante;
- riferimento;
- stile;
- camera;
- ambiente;
- struttura.

La direzione architetturale è:

```
Entity → State → Transformation → Reference → View → Camera → Style → Conditioning → ComfyUI Execution
```

Questo permette di trasformare CharacterForge da una raccolta di custom node in un sistema coerente di costruzione, trasformazione e rappresentazione di asset visivi persistenti.
