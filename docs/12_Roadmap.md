# 12 — Roadmap

## 1. Scopo

Questo documento definisce la roadmap ufficiale di implementazione di CharacterForge.

I documenti 01–11 hanno definito:

- visione;
- architettura;
- Style Engine;
- Human Engine;
- Creature Engine;
- Object & Technology Engine;
- Nature & Matter Engine;
- Environment & World Engine;
- Camera & Cinematography Engine;
- Transformation Engine;
- Reference Sheet System;
- integrazione ComfyUI.

La roadmap trasforma queste specifiche in una sequenza operativa.

L'obiettivo è evitare:

- sviluppo casuale;
- riscritture premature;
- duplicazione;
- dipendenze circolari;
- perdita delle funzionalità esistenti;
- introduzione di sistemi non ancora necessari.

---

## 2. Principio della Roadmap

CharacterForge deve essere sviluppato dal basso verso l'alto.

La sequenza generale è:

```
Documentation
↓
Domain Core
↓
Schemas
↓
Validation
↓
Registries
↓
Adapters
↓
Engines
↓
Nodes
↓
Reference System
↓
Transformation System
↓
Workflow Integration
↓
Legacy Migration
↓
Production Hardening
```

Una fase non deve essere considerata completata semplicemente perché il codice esiste.

Ogni fase richiede:

- implementazione;
- test;
- verifica runtime;
- documentazione;
- criterio di completamento.

---

## 3. Stato iniziale

Al momento della roadmap CharacterForge dispone già di:

- custom nodes funzionanti;
- Style Transfer;
- LoRA Style Combinator;
- controller Human;
- Weighted Conditioning;
- Hybrid Latent Switch;
- Scene Interrogator;
- libreria anime;
- libreria cinematic;
- profili camera;
- profili lighting;
- film stock;
- grain;
- color;
- atmosphere;
- numerosi director presets;
- workflow esistenti;
- test iniziali.

Questa infrastruttura costituisce il punto di partenza.

Non deve essere considerata legacy inutilizzabile.

Deve diventare la base della migrazione.

---

## 4. Phase 0 — Baseline

### Obiettivo

Congelare il comportamento funzionante prima delle modifiche architetturali.

### Attività

Registrare:

- package version;
- Python version;
- ComfyUI version;
- Torch version;
- CUDA availability;
- GPU;
- node count;
- preset count;
- anime style count;
- cinematic style count;
- import status;
- workflow status;
- test status.

### Output

Un baseline riproducibile.

### Criterio di completamento

Il baseline può essere eseguito nuovamente dopo ogni modifica strutturale.

---

## 5. Phase 1 — Domain Core

### Obiettivo

Creare il nucleo concettuale condiviso.

Componenti iniziali:

- Entity;
- Identity;
- EntityState;
- Variant;
- Transformation;
- Metadata.

### Regola

Il Domain Core non deve dipendere da ComfyUI.

### Output

Strutture Python semplici, serializzabili e testabili.

### Criterio di completamento

È possibile creare, validare e serializzare una Entity senza avviare ComfyUI.

---

## 6. Phase 2 — Schemas

### Obiettivo

Definire contratti strutturali stabili.

Gli schema devono descrivere almeno:

- Entity;
- Identity;
- State;
- Variant;
- Transformation;
- Camera;
- Style;
- Reference;
- Metadata.

### Output

Schema versionati.

### Criterio di completamento

Una struttura valida e una struttura non valida possono essere distinte automaticamente.

---

## 7. Phase 3 — Validation

### Obiettivo

Costruire il sistema di validazione comune.

Livelli:

- domain;
- engine;
- node;
- workflow;
- runtime.

### Attività

Definire:

- error types;
- validation results;
- warnings;
- fatal errors;
- compatibility errors.

### Criterio di completamento

Gli errori strutturali sono diagnosticabili senza ricorrere a errori generici.

---

## 8. Phase 4 — Serialization

### Obiettivo

Rendere persistenti le strutture CharacterForge.

Devono essere serializzabili almeno:

- Entity;
- State;
- Variant;
- Transformation;
- Camera;
- Style;
- Reference configuration;
- Metadata.

### Requisiti

La serializzazione deve essere:

- deterministica;
- leggibile;
- versionabile;
- compatibile con migrazioni future.

---

## 9. Phase 5 — Registry System

### Obiettivo

Creare registri centralizzati.

Registri previsti:

- Entity Registry;
- Style Registry;
- Camera Registry;
- Preset Registry;
- Transformation Registry;
- Reference Registry.

### Regola

I registry non devono diventare contenitori di logica di dominio.

Devono principalmente:

- registrare;
- recuperare;
- validare;
- indicizzare.

---

## 10. Phase 6 — Style Engine Migration

### Obiettivo

Portare l'infrastruttura Style esistente verso il nuovo modello.

### Priorità

1. Anime.
2. Artistic.
3. Retro.
4. Western.
5. Cinematic.
6. Director profiles.
7. Camera profiles.
8. Film profiles.
9. Lighting.
10. Atmosphere.

### Regola fondamentale

I preset esistenti devono continuare a funzionare.

### Criterio di completamento

Un nuovo Style Registry può esporre gli stili esistenti senza richiedere modifiche ai preset individuali.

---

## 11. Phase 7 — Cinematic Preservation

### Obiettivo

Normalizzare la libreria cinematografica senza perderne il contenuto.

Devono essere preservati:

- director styles;
- skin profiles;
- lighting profiles;
- lens profiles;
- film stocks;
- grain profiles;
- color profiles;
- atmosphere profiles;
- camera profiles.

### Attività

Separare progressivamente:

- look;
- camera;
- lighting;
- film;
- grain;
- color;
- atmosphere.

### Criterio di completamento

I preset cinematici continuano a produrre gli stessi parametri semantici principali dopo la normalizzazione.

---

## 12. Phase 8 — Human Engine

### Obiettivo

Costruire il primo Engine completo sopra il Domain Core.

### Integrazione

Gli attuali:

- Gender Controller;
- Ethnicity Controller;
- Body Controller;

devono diventare adapter o componenti dell'Human Engine.

### Funzioni

- identity;
- demographics;
- age;
- anatomy;
- face;
- skin;
- hair;
- eyes;
- clothing;
- accessories;
- distinctive traits;
- identity persistence;
- variants.

### Criterio di completamento

Un Human può essere creato, modificato, serializzato e trasformato mantenendo la propria identità.

---

## 13. Phase 9 — Creature Engine

### Obiettivo

Implementare il modello generalizzato delle creature.

Priorità:

- taxonomy;
- morphology;
- anatomy;
- appendages;
- head;
- eyes;
- mouth;
- surface;
- fur;
- feathers;
- scales;
- coloration;
- expression;
- pose;
- equipment;
- identity.

### Criterio di completamento

Il sistema supporta creature non umane e antropomorfe senza ricorrere a una semplice estensione del Human Controller.

---

## 14. Phase 10 — Object & Technology Engine

### Obiettivo

Creare il modello degli oggetti.

Priorità:

- geometry;
- components;
- materials;
- surface;
- condition;
- wear;
- damage;
- repair;
- functional state;
- technology;
- vehicles;
- robots.

### Criterio di completamento

Un oggetto può essere rappresentato come entità persistente con componenti e stato indipendenti.

---

## 15. Phase 11 — Nature & Matter Engine

### Obiettivo

Rappresentare materia, fenomeni naturali e sistemi dinamici.

Priorità:

- materials;
- water;
- fire;
- ice;
- rock;
- soil;
- sand;
- snow;
- vegetation;
- clouds;
- fog;
- smoke;
- dust;
- weather;
- phase;
- flow.

### Criterio di completamento

Il sistema distingue chiaramente materia persistente, stato della materia e fenomeno transitorio.

---

## 16. Phase 12 — Environment & World Engine

### Obiettivo

Costruire la rappresentazione strutturata degli ambienti.

Priorità:

- world;
- region;
- zone;
- area;
- biome;
- terrain;
- architecture;
- interior;
- exterior;
- atmosphere;
- weather;
- time;
- season;
- spatial relations.

### Criterio di completamento

Un ambiente può essere rappresentato indipendentemente dall'immagine finale e collegato alle entità presenti nella scena.

---

## 17. Phase 13 — Camera & Cinematography Engine

### Obiettivo

Separare definitivamente il modo in cui una scena viene vista dal modo in cui viene rappresentata.

Priorità:

- camera transform;
- target;
- shot;
- framing;
- lens;
- focal length;
- sensor;
- aperture;
- focus;
- depth of field;
- exposure;
- movement;
- cinematography profile.

### Criterio di completamento

La stessa Entity può essere renderizzata attraverso configurazioni camera differenti senza modificare la propria identità.

---

## 18. Phase 14 — Reference Sheet Core

### Obiettivo

Implementare il sistema Reference Sheet definito nel Documento 10.

Prima versione:

- canonical view;
- front;
- back;
- side;
- three-quarter;
- detail;
- metadata.

### Regola

La Reference Sheet non deve essere soltanto un collage.

Deve rappresentare una singola Entity attraverso viste coerenti.

### Criterio di completamento

Una Entity può generare una configurazione Reference Sheet riproducibile.

---

## 19. Phase 15 — Reference Sheet Types

Implementare progressivamente:

- Character Sheet;
- Creature Sheet;
- Object Sheet;
- Vehicle Sheet;
- Architecture Sheet;
- Environment Sheet;
- Material Sheet;
- Transformation Sheet;
- Technical Sheet.

### Criterio di completamento

Ogni tipo dispone di schema e validazione propri quando necessario.

---

## 20. Phase 16 — Transformation Engine

### Obiettivo

Implementare trasformazioni controllate.

Priorità:

1. State transformation.
2. Age transformation.
3. Material transformation.
4. Morphology transformation.
5. Damage.
6. Repair.
7. Environmental transformation.
8. Scale.
9. Context transformation.

### Requisiti

Ogni trasformazione deve poter indicare:

- source;
- target;
- parameters;
- scope;
- reversibility;
- provenance.

---

## 21. Phase 17 — Transformation Chains

### Obiettivo

Permettere sequenze di trasformazioni.

Esempio:

```
Adult
→ Injured
→ Recovered
→ Armored
→ Battle Damaged
```

La storia deve poter essere ricostruita.

### Criterio di completamento

È possibile identificare ogni passaggio senza perdere la relazione con l'Entity originale.

---

## 22. Phase 18 — Prompt Specification

### Obiettivo

Separare semantic model e prompt text.

Pipeline:

```
Entity
↓
Semantic Representation
↓
Prompt Specification
↓
Text / Conditioning
```

### Criterio di completamento

Un Engine non deve essere costretto a costruire direttamente stringhe prompt per comunicare con il resto del sistema.

---

## 23. Phase 19 — Conditioning Integration

### Obiettivo

Integrare la nuova semantic representation con i sistemi ComfyUI esistenti.

Devono essere considerati:

- positive conditioning;
- negative conditioning;
- weighting;
- style conditioning;
- identity information;
- camera information;
- environment information.

### Criterio di completamento

Il nuovo sistema può alimentare il workflow esistente senza sostituirlo prematuramente.

---

## 24. Phase 20 — Node Modernization

### Obiettivo

Creare i primi nodi basati sul nuovo Domain Core.

Priorità:

1. Entity Builder.
2. Entity Inspector.
3. State Builder.
4. Variant Builder.
5. Transformation Builder.
6. Reference Builder.
7. Camera Builder.
8. Style Builder.

### Regola

I nuovi nodi devono essere sottili.

La logica appartiene agli Engine.

---

## 25. Phase 21 — Existing Node Adapters

Gli attuali nodi devono essere collegati al nuovo sistema tramite adapter.

Priorità:

- Body Controller;
- Gender Controller;
- Ethnicity Controller;
- Weighted Conditioning;
- Style Transfer;
- LoRA Style Combinator;
- Hybrid Latent Switch.

### Criterio di completamento

I vecchi nodi possono essere utilizzati insieme ai nuovi senza creare due sistemi incompatibili.

---

## 26. Phase 22 — Workflow Modernization

### Obiettivo

Aggiornare progressivamente i workflow.

Ordine:

1. baseline workflow;
2. style workflow;
3. human workflow;
4. creature workflow;
5. object workflow;
6. environment workflow;
7. reference workflow;
8. transformation workflow.

### Regola

Un workflow deve essere aggiornato solo dopo che i nodi necessari sono verificati.

---

## 27. Phase 23 — Identity Persistence

### Obiettivo

Rendere l'identità persistente tra workflow e varianti.

Devono essere mantenuti:

- entity_id;
- identity anchors;
- canonical reference;
- state;
- variant;
- transformation history.

### Criterio di completamento

Una variazione controllata non crea accidentalmente una nuova identità.

---

## 28. Phase 24 — Identity Validation

### Obiettivo

Preparare il sistema alla futura verifica automatica della coerenza.

Prima versione:

- metadata consistency;
- schema consistency;
- reference linkage;
- anchor presence.

Versioni future:

- visual identity comparison;
- face consistency;
- morphology consistency;
- material consistency.

---

## 29. Phase 25 — Preset Builder

### Obiettivo

Permettere la creazione di preset senza modificare il codice core.

Un preset deve poter definire:

- metadata;
- defaults;
- constraints;
- references;
- style;
- camera;
- transformations.

### Criterio di completamento

L'aggiunta di un nuovo preset non richiede la modifica degli Engine principali.

---

## 30. Phase 26 — Asset Builder

### Obiettivo

Creare una pipeline unificata per costruire asset.

Concetto:

```
Entity Builder
↓
Identity
↓
State
↓
Appearance
↓
Environment
↓
Camera
↓
Style
↓
Reference
```

Questo diventerà progressivamente il punto di ingresso principale di CharacterForge.

---

## 31. Phase 27 — Multi-Entity Scenes

### Obiettivo

Estendere il sistema da singola Entity a scena.

Una scena può contenere:

- characters;
- creatures;
- objects;
- vehicles;
- environment;
- materials;
- camera;
- lighting;
- atmosphere.

### Criterio di completamento

Le Entity mantengono identità indipendenti ma condividono un Environment e una Camera.

---

## 32. Phase 28 — Scene Continuity

### Obiettivo

Mantenere continuità tra immagini della stessa scena.

Devono poter essere mantenuti:

- entity positions;
- relative scale;
- camera;
- environment;
- lighting;
- weather;
- time;
- state.

Questa fase prepara il terreno per storyboard e shot continuity.

---

## 33. Phase 29 — Production Workflows

### Obiettivo

Costruire workflow orientati alla produzione.

Possibili sistemi:

- asset generation;
- batch generation;
- reference generation;
- variation generation;
- transformation sequences;
- scene generation;
- shot generation.

La priorità rimane la stabilità, non il numero di funzionalità.

---

## 34. Phase 30 — Legacy Cleanup

Questa fase deve arrivare **dopo** la migrazione.

Solo a questo punto si potranno valutare:

- file duplicati;
- classi duplicate;
- vecchi adapter;
- mapping inutilizzati;
- workflow obsoleti;
- backup ormai superflui.

Ogni rimozione deve essere preceduta da:

1. ricerca degli utilizzi;
2. verifica runtime;
3. verifica workflow;
4. test;
5. commit dedicato.

---

## 35. Phase 31 — API Stabilization

### Obiettivo

Stabilizzare:

- Domain API;
- Engine API;
- Node API;
- Registry API;
- Schema API.

Dopo questa fase le modifiche breaking devono essere molto più rare.

---

## 36. Phase 32 — Performance Hardening

Ottimizzazioni:

- lazy loading;
- cache;
- registry lookup;
- import time;
- memory;
- serialization;
- workflow startup.

La performance deve essere misurata prima e dopo l'ottimizzazione.

---

## 37. Phase 33 — Runtime Hardening

Verificare:

- startup;
- reload;
- repeated execution;
- invalid preset;
- invalid entity;
- invalid workflow;
- missing dependency;
- CUDA availability;
- CPU fallback quando applicabile.

---

## 38. Phase 34 — Documentation Hardening

Aggiornare:

- README;
- installation;
- usage;
- API reference;
- troubleshooting;
- architecture docs;
- migration docs;
- examples.

La documentazione deve riflettere il codice reale.

---

## 39. Phase 35 — Test Expansion

Obiettivo minimo:

- domain tests;
- engine tests;
- node tests;
- registry tests;
- schema tests;
- serialization tests;
- workflow tests;
- integration tests;
- regression tests.

I test devono aumentare insieme al codice.

---

## 40. Phase 36 — Release Candidate

Prima di una major release:

- congelare API;
- congelare schema;
- verificare workflow;
- eseguire suite completa;
- verificare preset;
- verificare runtime;
- verificare installazione pulita.

Solo dopo può essere preparata una release candidate.

---

## 41. Milestone M0 — Baseline

### Deliverable

Baseline runtime riproducibile.

### Exit Criteria

- import OK;
- registration OK;
- presets OK;
- workflows baseline OK;
- tests baseline OK.

---

## 42. Milestone M1 — Domain Core

### Deliverable

Entity model funzionante.

### Exit Criteria

- identity;
- state;
- variant;
- transformation;
- metadata;
- serialization;
- validation.

---

## 43. Milestone M2 — Registry

### Deliverable

Registry centralizzati.

### Exit Criteria

- Style Registry;
- Camera Registry;
- Preset Registry;
- schema validation;
- deterministic discovery.

---

## 44. Milestone M3 — Human Engine

### Deliverable

Primo Engine completo.

### Exit Criteria

Human entity end-to-end.

---

## 45. Milestone M4 — Creature Engine

### Deliverable

Creature representation.

### Exit Criteria

Creature identity e morphology end-to-end.

---

## 46. Milestone M5 — Object Engine

### Deliverable

Object and Technology representation.

### Exit Criteria

Object identity, components e state end-to-end.

---

## 47. Milestone M6 — Nature & Environment

### Deliverable

Matter e Environment systems.

### Exit Criteria

Scena ambientale strutturata.

---

## 48. Milestone M7 — Camera

### Deliverable

Camera & Cinematography Engine.

### Exit Criteria

Camera indipendente dall'Entity e riutilizzabile.

---

## 49. Milestone M8 — Reference Sheet

### Deliverable

Reference Sheet System operativo.

### Exit Criteria

Canonical reference + multiple views + metadata.

---

## 50. Milestone M9 — Transformation

### Deliverable

Transformation Engine operativo.

### Exit Criteria

Transformation chain + provenance.

---

## 51. Milestone M10 — ComfyUI Integration

### Deliverable

Nuovi nodi integrati con il graph.

### Exit Criteria

Domain → Engine → Node → ComfyUI funzionante.

---

## 52. Milestone M11 — Identity Persistence

### Deliverable

Asset identity persistente.

### Exit Criteria

Entity → Variant → Transformation → Reference senza perdita di identità.

---

## 53. Milestone M12 — Production Pipeline

### Deliverable

Asset e scene production workflows.

### Exit Criteria

Pipeline riproducibile e documentata.

---

## 54. Milestone M13 — Stabilization

### Deliverable

API, performance e runtime stabilizzati.

### Exit Criteria

Regression suite completa e workflow verificati.

---

## 55. Definition of Done per ogni fase

Una fase è completata soltanto quando:

- codice presente;
- test presenti;
- test superati;
- documentazione aggiornata;
- runtime verificato;
- compatibilità verificata;
- eventuali migration notes aggiornate.

"Funziona sul mio sistema" non è sufficiente.

---

## 56. Regola dei checkpoint

Ogni milestone deve produrre un checkpoint Git.

Il checkpoint deve permettere di:

- tornare indietro;
- confrontare versioni;
- identificare regressioni;
- isolare problemi.

Le grandi migrazioni devono essere divise in commit comprensibili.

---

## 57. Regola anti-riscrittura

Non riscrivere un sistema esistente solo perché il nuovo design è più elegante.

Prima:

- adapter;
- test;
- migrazione;
- confronto.

La riscrittura è giustificata quando il costo di mantenere il vecchio sistema supera chiaramente il costo della migrazione.

---

## 58. Regola anti-feature-creep

Una nuova funzionalità non entra nella roadmap principale soltanto perché è interessante.

Prima deve essere verificato:

- dipendenza;
- valore architetturale;
- costo;
- impatto;
- compatibilità;
- posizione nella roadmap.

Le funzionalità non necessarie possono essere raccolte in un backlog futuro.

---

## 59. Backlog futuro

Possibili estensioni successive:

- automatic identity scoring;
- visual reference matching;
- storyboard;
- shot lists;
- animation;
- multi-camera;
- previs;
- camera tracking;
- asset library;
- project files;
- scene graph;
- temporal consistency;
- automated QA;
- model adapters;
- production export.

Queste funzionalità non devono anticipare il completamento del core.

---

## 60. Long-Term Architecture

La visione finale è:

```
CharacterForge

Domain
├── Entity
├── Identity
├── State
├── Variant
├── Transformation
└── Metadata

Engines
├── Human
├── Creature
├── Object
├── Nature
├── Environment
├── Camera
├── Style
├── Transformation
└── Reference

Infrastructure
├── Schemas
├── Validation
├── Registries
├── Serialization
└── Compatibility

ComfyUI
├── Nodes
├── Workflows
├── Conditioning
└── Execution
```

Questa struttura deve rimanere leggibile anche quando il progetto crescerà significativamente.

---

## 61. Priorità assolute

Quando esistono conflitti tra attività, la priorità è:

1. Correttezza.
2. Stabilità.
3. Compatibilità.
4. Testabilità.
5. Modularità.
6. Persistenza dell'identità.
7. Estensibilità.
8. Performance.
9. Nuove funzionalità.

Una funzionalità nuova non deve compromettere le fondamenta.

---

## 62. Ordine operativo immediato

Dopo il completamento della documentazione 01–12, il lavoro non deve saltare direttamente alla costruzione di decine di nodi.

L'ordine operativo iniziale sarà:

1. verificare il repository;
2. congelare il baseline;
3. definire Domain Core;
4. definire schema;
5. definire validation;
6. definire serialization;
7. definire registry;
8. creare test;
9. integrare il primo adapter;
10. verificare runtime;
11. procedere al primo Engine.

---

## 63. Primo componente reale

Il primo componente dell'architettura futura sarà il **Domain Core**.

Non sarà:

- un nuovo preset;
- un nuovo LoRA node;
- un nuovo cinematic preset;
- un nuovo Reference Sheet renderer.

Sarà la base dati semantica sulla quale tutti questi sistemi potranno successivamente convergere.

---

## 64. Primo contratto

Il primo contratto da stabilire sarà:

```
Entity
Identity
State
Variant
Transformation
Metadata
```

Questo contratto dovrà essere sufficientemente piccolo da essere stabile e sufficientemente generale da supportare:

- Human;
- Creature;
- Object;
- Vehicle;
- Building;
- Environment;
- Material.

---

## 65. Primo test architetturale

Il primo test significativo dovrà dimostrare:

1. creazione Entity;
2. assegnazione Identity;
3. creazione State;
4. creazione Variant;
5. creazione Transformation;
6. serializzazione;
7. deserializzazione;
8. verifica dell'identità;
9. confronto dei dati.

Se questo test fallisce, non bisogna procedere agli Engine superiori.

---

## 66. Primo adapter

Il primo adapter dovrebbe essere scelto tra i sistemi esistenti più semplici da collegare al Domain Core.

L'obiettivo dell'adapter non è aggiungere funzionalità.

È dimostrare che:

```
Legacy Component
↓
Adapter
↓
Domain Model
```

può funzionare senza rompere il comportamento esistente.

---

## 67. Primo Engine completo

Il Human Engine rappresenterà il primo caso completo perché dispone già di componenti funzionanti.

Il percorso previsto è:

```
Gender
+
Ethnicity
+
Body
+
Identity
+
Appearance
↓
Human Engine
↓
Human Entity
```

Successivamente il modello potrà essere esteso a:

- face;
- skin;
- hair;
- eyes;
- clothing;
- accessories;
- distinctive traits.

---

## 68. Verifica dopo ogni Engine

Dopo ogni Engine devono essere verificati:

- import;
- unit tests;
- serialization;
- validation;
- registry;
- node integration;
- workflow;
- runtime.

Non si deve accumulare una lunga serie di Engine non verificati.

---

## 69. Criterio di stabilità

CharacterForge sarà considerato architetturalmente stabile quando:

- il Domain Core è indipendente da ComfyUI;
- gli Engine dipendono dal Domain Core;
- i Nodes dipendono dagli Engine;
- i workflow orchestrano i Nodes;
- gli stili sono registrati;
- le camere sono registrate;
- le trasformazioni sono persistenti;
- le Reference Sheets sono collegate alle Entity;
- gli identity anchors sono persistenti;
- i test coprono i contratti principali.

---

## 70. Criterio di maturità

CharacterForge sarà considerato maturo quando sarà possibile:

1. creare un asset;
2. assegnargli un'identità;
3. modificarne lo stato;
4. creare varianti;
5. applicare trasformazioni;
6. definirne ambiente;
7. definirne camera;
8. applicare uno stile;
9. generare una Reference Sheet;
10. inviarlo a ComfyUI;
11. mantenere metadata e provenance;
12. riprodurre il processo.

---

## 71. Criterio di produzione

Il sistema sarà orientato alla produzione quando potrà gestire una scena composta da più Entity mantenendo:

- identità;
- stato;
- posizione;
- ambiente;
- camera;
- stile;
- trasformazioni;
- riferimenti.

Questo rappresenta il passaggio da semplice character generator a sistema di asset generation.

---

## 72. Criterio di estensibilità

A regime, aggiungere:

- una nuova creatura;
- un nuovo veicolo;
- un nuovo materiale;
- un nuovo ambiente;
- un nuovo stile;
- una nuova camera;
- una nuova trasformazione;

non dovrebbe richiedere la modifica del core.

Questo è uno dei principali indicatori di successo architetturale.

---

## 73. Criterio di manutenzione

Il progetto deve poter essere mantenuto senza conoscere ogni dettaglio dell'intero repository.

Un developer deve poter individuare rapidamente:

- dove sono le Entity;
- dove sono gli Engine;
- dove sono i preset;
- dove sono gli stili;
- dove sono le camere;
- dove sono le trasformazioni;
- dove sono i nodi;
- dove sono i test.

La struttura del repository deve comunicare l'architettura.

---

## 74. Criterio di compatibilità

La nuova architettura non è completata se per funzionare richiede la distruzione del sistema esistente.

Il risultato corretto è:

```
Existing CharacterForge
+
New Architecture
=
Migrated CharacterForge
```

Non:

```
Existing CharacterForge
→ Delete
→ Rewrite Everything
```

---

## 75. Criterio di qualità

Ogni componente deve essere valutato secondo:

- chiarezza;
- coerenza;
- testabilità;
- isolamento;
- compatibilità;
- estensibilità;
- documentazione.

La quantità di codice non rappresenta la qualità.

---

## 76. Criterio di semplicità

La complessità deve essere introdotta soltanto quando risolve un problema reale.

Un'astrazione deve esistere perché:

- evita duplicazione;
- definisce un contratto;
- permette estensione;
- migliora testabilità;
- protegge la compatibilità.

Non deve esistere semplicemente perché l'architettura può averla.

---

## 77. Roadmap sintetica

La sequenza principale è:

```
01 Baseline
02 Domain Core
03 Schemas
04 Validation
05 Serialization
06 Registries
07 Style Migration
08 Human Engine
09 Creature Engine
10 Object Engine
11 Nature & Matter
12 Environment
13 Camera
14 Reference Sheet
15 Transformation
16 Prompt Specification
17 Conditioning
18 Node Modernization
19 Legacy Adapters
20 Workflow Modernization
21 Identity Persistence
22 Multi-Entity
23 Production Pipeline
24 Legacy Cleanup
25 Stabilization
```

---

## 78. Roadmap di priorità

### P0 — Fondamenta

- Domain;
- schema;
- validation;
- serialization;
- registry.

### P1 — Engine

- Human;
- Creature;
- Object;
- Nature;
- Environment.

### P2 — Representation

- Camera;
- Style;
- Reference;
- Transformation.

### P3 — Integration

- Nodes;
- Conditioning;
- Workflows;
- Compatibility.

### P4 — Production

- Multi-entity;
- continuity;
- batch;
- asset library;
- QA.

---

## 79. Regola finale di sviluppo

Quando una scelta tecnica è incerta, scegliere prima la soluzione che:

- preserva i dati;
- preserva l'identità;
- preserva la compatibilità;
- può essere testata;
- può essere sostituita;
- non blocca l'evoluzione futura.

La reversibilità è una caratteristica architetturale.

---

## 80. Stato del Master Blueprint

Con questo documento vengono completati i dodici documenti principali:

1. Visione e Architettura.
2. Style Engine.
3. Human Engine.
4. Creature Engine.
5. Object & Technology Engine.
6. Nature & Matter Engine.
7. Environment & World Engine.
8. Camera & Cinematography Engine.
9. Transformation Engine.
10. Reference Sheet System.
11. ComfyUI Implementation.
12. Roadmap.

Il Master Blueprint definisce quindi la direzione architetturale completa di CharacterForge.

---

## 81. Prossimo ciclo di lavoro

Il prossimo ciclo non consiste nella scrittura di un ulteriore documento architetturale.

Consiste nell'inizio dell'implementazione controllata.

Prima attività:

**Baseline del repository e definizione del Domain Core.**

Prima di modificare il codice devono essere raccolti:

- stato Git;
- struttura effettiva;
- test attuali;
- runtime;
- mapping;
- preset;
- workflow;
- dipendenze;
- versioni.

---

## 82. Regola di non distruzione

Durante il primo ciclo di implementazione:

- non eliminare duplicati;
- non cancellare backup;
- non spostare massivamente file;
- non riscrivere i nodi esistenti;
- non modificare la cinematica esistente;
- non modificare la libreria anime;
- non modificare workflow funzionanti.

Prima si costruisce il nuovo livello.

Successivamente si migra.

---

## 83. Regola di verifica

Ogni modifica deve seguire:

```
Modify
↓
Test
↓
Inspect
↓
Runtime Check
↓
Commit
```

Se un passaggio fallisce, si interrompe la sequenza e si corregge prima di procedere.

---

## 84. Regola di documentazione

Quando il comportamento del codice diverge dalla documentazione:

- non ignorare la differenza;
- non assumere automaticamente che il codice sia corretto;
- verificare quale dei due rappresenta il comportamento desiderato;
- aggiornare esplicitamente il componente corretto.

La documentazione e il codice devono convergere.

---

## 85. Regola di identità

L'identità dell'asset è un requisito trasversale.

Ogni nuovo sistema deve chiedersi:

**Questa operazione modifica l'identità o modifica soltanto lo stato, la variante, la rappresentazione o lo stile?**

Questa distinzione deve rimanere coerente in:

- Human;
- Creature;
- Object;
- Nature;
- Environment;
- Transformation;
- Reference;
- Camera;
- Style.

---

## 86. Regola di separazione

La domanda fondamentale di ogni nuovo componente è:

**Sto definendo che cosa è l'asset, dove si trova, come viene trasformato, come viene visto o come viene stilizzato?**

Queste responsabilità non devono essere confuse.

---

## 87. Regola di crescita

CharacterForge deve poter crescere in complessità senza crescere nella stessa misura in accoppiamento.

La crescita desiderata è:

```
More Features
≠
More Coupling
```

L'architettura deve permettere l'aggiunta di funzionalità attraverso moduli indipendenti.

---

## 88. Final Principle

La roadmap non è un elenco rigido di funzionalità.

È un ordine di dipendenze.

Prima vengono costruite le fondamenta che rendono possibili le funzionalità successive.

La direzione complessiva è:

```
DOCUMENTATION
→ DOMAIN
→ SCHEMA
→ VALIDATION
→ REGISTRY
→ ENGINES
→ REPRESENTATION
→ TRANSFORMATION
→ NODES
→ WORKFLOWS
→ PRODUCTION
```

Il risultato finale deve essere un CharacterForge nel quale:

- ogni asset possiede una identità;
- ogni stato è rappresentabile;
- ogni variante è controllabile;
- ogni trasformazione è tracciabile;
- ogni riferimento è coerente;
- ogni camera è indipendente;
- ogni stile è modulare;
- ogni ambiente è strutturato;
- ogni componente è testabile;
- ogni preset è estendibile;
- ComfyUI rimane il motore di esecuzione;
- l'architettura CharacterForge rimane il modello semantico superiore.

Il Master Blueprint è ora completo.

La fase successiva è l'implementazione del **Domain Core**, partendo da un baseline verificato e senza distruggere l'infrastruttura CharacterForge già funzionante.
