# CharacterForge — Creature Engine

**Documento:** 04 — Creature Engine  
**Versione architetturale:** 1.0  
**Stato:** Baseline progettuale  
**Data:** 2026-09-24  

---

## 1. Scopo

Il **Creature Engine** è il sottosistema responsabile della definizione strutturata di creature, animali, esseri fantastici, esseri fantascientifici e forme antropomorfe all'interno di CharacterForge.

Il motore non deve essere concepito come un semplice generatore di prompt.

Il suo compito è descrivere una creatura come una **entità strutturata, coerente e persistente**, separando:

- identità
- anatomia
- morfologia
- materiali biologici
- caratteristiche superficiali
- comportamento
- equipaggiamento
- stile
- ambiente
- camera
- trasformazioni

Il Creature Engine deve inoltre poter condividere principi e infrastruttura con il Human Engine senza diventare dipendente da una specifica anatomia umana.

---

## 2. Principio fondamentale

Il principio centrale è:

> **La creatura è un'entità prima di essere uno stile visivo.**

Una stessa creatura deve poter essere rappresentata come:

- fotografia naturalistica
- concept art
- illustrazione fantasy
- anime
- fumetto
- cinematografia
- videogame asset
- pixel art
- creature design
- altro stile compatibile

senza perdere la propria identità.

---

## 3. Modello concettuale

Il modello generale può essere rappresentato come:

```
Creature
├── identity
├── taxonomy
├── morphology
├── anatomy
├── appendages
├── head
├── surface
├── coloration
├── materials
├── expression
├── pose
├── behavior
├── clothing_equipment
├── distinctive_traits
├── variation_rules
└── transformation_state
```

La struttura definitiva sarà definita durante l'implementazione.

---

## 4. Identity Layer

L'Identity Layer identifica la creatura nel tempo.

Può comprendere:

- identity_id
- nome interno
- identity seed
- specie o archetype
- caratteristiche permanenti
- tratti distintivi
- struttura anatomica
- pattern cromatici persistenti
- vincoli di variazione

Esempio:

```
identity_id: "creature_001"
identity_seed: 728194
```

L'identificatore deve rimanere stabile anche quando cambiano:

- stile
- illuminazione
- camera
- ambiente
- posa
- espressione
- condizioni atmosferiche

---

## 5. Creature Categories

Il sistema deve supportare almeno le seguenti macro-categorie:

### 5.1 Animali

- mammiferi
- uccelli
- rettili
- anfibi
- pesci
- insetti
- aracnidi
- molluschi
- altre forme animali

### 5.2 Creature fantastiche

- draghi
- grifoni
- chimere
- demoni
- esseri elementali
- creature mitologiche
- creature originali

### 5.3 Creature fantascientifiche

- alieni
- organismi bio-tecnologici
- esseri sintetici
- creature mutanti
- organismi extraterrestri

### 5.4 Creature antropomorfe

- animali antropomorfi
- creature umanoidi
- ibridi uomo-animale
- specie originali con anatomia umanoide

Le categorie sono descrittive e non devono limitare la costruzione di nuove specie.

---

## 6. Taxonomy Layer

La tassonomia descrive l'origine o la classificazione della creatura.

Può comprendere:

- kingdom
- phylum
- class
- species
- subtype
- fantasy archetype
- custom taxonomy

Non tutte le creature devono possedere una tassonomia biologica reale.

Per creature inventate deve essere possibile utilizzare:

```
taxonomy:
  type: fictional
  species: custom_dragon
```

La tassonomia non deve determinare automaticamente lo stile visivo.

---

## 7. Archetype System

Gli archetipi possono fornire una base iniziale.

Esempi:

- wolf
- fox
- feline
- reptile
- bird
- insect
- dragon
- humanoid
- aquatic
- avian
- serpentine
- insectoid

L'archetipo è un punto di partenza, non una limitazione.

Il sistema deve permettere di creare:

```
base_archetype: feline
custom_morphology: true
```

---

## 8. Morphology System

La Morphology Layer definisce la forma generale.

Parametri possibili:

- altezza
- lunghezza
- larghezza
- massa
- volume
- simmetria
- rapporto testa/corpo
- rapporto tronco/arti
- curvatura
- proporzioni
- postura naturale

La morfologia deve essere distinta dallo stile.

---

## 9. Anatomy System

L'Anatomy System descrive la struttura interna ed esterna della creatura.

Categorie:

- scheletro concettuale
- torso
- collo
- testa
- arti
- articolazioni
- coda
- ali
- pinne
- tentacoli
- corna
- zanne
- artigli
- mandibola
- occhi
- organi sensoriali

Non tutte le creature devono possedere tutte le componenti.

Il modello deve quindi essere modulare.

---

## 10. Modular Anatomy

L'anatomia deve essere costruibile per componenti.

Esempio:

```
Creature
├── torso
├── four_legs
├── tail
├── horns
├── wings
└── head
```

Una creatura può quindi possedere:

- due gambe
- quattro gambe
- sei gambe
- nessuna gamba
- ali
- più ali
- tentacoli
- pinne
- appendici personalizzate

senza richiedere un nuovo engine per ogni categoria.

---

## 11. Appendage System

Le appendici sono componenti indipendenti.

Categorie:

- arms
- legs
- wings
- tails
- horns
- antlers
- tentacles
- fins
- claws
- mandibles
- antennae
- custom appendages

Ogni appendice può avere:

- tipo
- numero
- posizione
- dimensione
- forma
- orientamento
- materiale
- colore
- simmetria
- variazione

---

## 12. Head System

La testa deve essere indipendente dal resto dell'anatomia.

Parametri:

- forma
- dimensione
- muso
- mandibola
- mascella
- fronte
- corna
- orecchie
- antenne
- occhi
- dentatura
- becco
- organi sensoriali

La struttura deve permettere teste non umanoidi.

---

## 13. Eye System

Gli occhi devono poter essere definiti indipendentemente.

Parametri:

- numero
- posizione
- dimensione
- forma
- orientamento
- colore
- pupilla
- iride
- luminosità
- riflessi
- membrana
- disposizione

Il sistema deve supportare anche:

- un occhio
- due occhi
- più occhi
- occhi laterali
- occhi frontali
- occhi multipli su appendici

---

## 14. Mouth and Dentition System

La bocca deve essere trattata come un componente anatomico.

Possibili parametri:

- posizione
- apertura
- dimensione
- forma
- mandibola
- denti
- zanne
- becchi
- lingua
- strutture interne

La dentizione può essere persistente e quindi contribuire all'identità.

---

## 15. Surface System

La superficie della creatura deve essere modellata come materiale.

Categorie principali:

- fur
- feathers
- scales
- skin
- hide
- shell
- chitin
- mucus
- metal
- synthetic tissue
- crystal
- stone
- elemental material
- custom material

Ogni materiale può avere:

- colore
- roughness
- specularity
- texture
- density
- pattern
- wear
- wetness
- translucency

---

## 16. Fur System

La pelliccia può essere descritta attraverso:

- lunghezza
- densità
- direzione
- texture
- volume
- colore
- pattern
- variazioni
- bagnato/asciutto
- stato del pelo

Il sistema deve distinguere:

**materiale**

da

**pattern**.

---

## 17. Feather System

Per creature aviarie o ibride:

- lunghezza
- densità
- disposizione
- struttura
- colore
- pattern
- usura
- bagnatura
- lucentezza

Le piume devono poter essere associate a specifiche regioni anatomiche.

---

## 18. Scale and Shell System

Per rettili, creature corazzate e organismi simili:

- forma delle squame
- dimensione
- densità
- disposizione
- sovrapposizione
- colore
- pattern
- lucentezza
- usura

Per gusci:

- spessore
- forma
- materiale
- texture
- pattern
- danni

---

## 19. Coloration System

La colorazione deve essere indipendente dall'anatomia.

Può comprendere:

- base color
- secondary color
- tertiary color
- gradient
- spots
- stripes
- bands
- patches
- bioluminescence
- iridescence

I pattern devono poter essere associati a regioni anatomiche.

---

## 20. Pattern Persistence

I pattern caratteristici possono diventare parte dell'identità.

Esempio:

```
distinctive_traits:
  - white facial stripe
  - asymmetric dark patch
  - red eye
```

Una variazione stilistica non deve eliminare automaticamente questi elementi.

---

## 21. Sexual Dimorphism

Quando pertinente, il sistema può rappresentare differenze sessuali della specie.

Il modello deve poter descrivere:

- dimensione
- massa
- corna
- piumaggio
- colorazione
- strutture accessorie
- altri tratti morfologici

La caratteristica deve essere opzionale e dipendente dalla specie.

---

## 22. Age and Growth

Le creature possono avere uno stadio di crescita.

Possibili stati:

- juvenile
- adolescent
- adult
- mature
- elderly

L'età può influenzare:

- dimensione
- proporzioni
- massa
- colorazione
- superficie
- corna
- dentatura
- usura

Per creature longeve può essere utilizzato un modello di crescita personalizzato.

---

## 23. Expression System

L'espressione deve essere separata dall'identità.

Può comprendere:

- neutral
- aggressive
- fearful
- curious
- happy
- sad
- alert
- predatory
- defensive

Le espressioni possono influenzare:

- occhi
- bocca
- postura
- orecchie
- coda
- piumaggio
- muscolatura

ma non devono modificare la struttura permanente.

---

## 24. Pose System

La posa deve essere separata dall'anatomia.

Possibili categorie:

- standing
- sitting
- lying
- walking
- running
- jumping
- flying
- swimming
- attacking
- resting
- custom

Il sistema deve poter utilizzare vincoli anatomici per evitare pose incompatibili.

---

## 25. Behavior Layer

Il comportamento rappresenta caratteristiche dinamiche.

Esempi:

- predatory
- social
- territorial
- defensive
- curious
- nocturnal
- aquatic
- aerial

Il comportamento può influenzare la descrizione della scena e la posa, ma non deve diventare automaticamente parte dell'identità visiva.

---

## 26. Clothing and Equipment

Creature antropomorfe o fantasy possono utilizzare:

- armature
- vestiti
- bardature
- selle
- collari
- accessori
- equipaggiamento
- oggetti trasportati

L'equipaggiamento deve essere separato dal corpo.

Ogni elemento può essere:

- permanente
- opzionale
- temporaneo

---

## 27. Distinctive Traits

I tratti distintivi devono avere una priorità elevata durante la ricostruzione dell'identità.

Esempi:

- corno spezzato
- occhio cieco
- cicatrice
- pattern asimmetrico
- zanna mancante
- coda danneggiata
- piuma particolare
- squama differente
- parte del corpo modificata

Questi attributi possono essere marcati come persistenti.

---

## 28. Identity Persistence

Il Creature Engine deve garantire continuità tra rappresentazioni.

La stessa creatura deve poter cambiare:

- stile
- camera
- illuminazione
- ambiente
- posa
- espressione
- clima
- equipaggiamento

senza diventare automaticamente una nuova creatura.

Concettualmente:

```
CreatureIdentity
      │
      ├── Style
      ├── Camera
      ├── Environment
      ├── Lighting
      ├── Pose
      └── Equipment
```

---

## 29. Controlled Variation

La variazione deve essere controllabile per componente.

Esempio:

```
variation:
  anatomy: 0.1
  coloration: 0.2
  surface: 0.3
  equipment: 0.8
```

Questi valori sono concettuali.

L'API definitiva sarà definita durante l'implementazione.

---

## 30. Hybrid Creature System

Il Creature Engine deve supportare creature composte.

Esempio:

```
hybrid:
  base:
    - feline
    - reptile
  features:
    - feline_head
    - reptile_scales
    - wings
    - long_tail
```

Il sistema deve distinguere:

- componente di origine
- componente risultante
- caratteristiche ereditate
- caratteristiche sostituite
- caratteristiche aggiunte

---

## 31. Anthropomorphic System

Le creature antropomorfe devono poter utilizzare componenti del Human Engine senza diventare automaticamente umani.

Esempio:

```
Creature
├── animal_head
├── humanoid_torso
├── humanoid_arms
├── digitigrade_legs
└── animal_tail
```

Questa architettura rende possibile creare:

- beastfolk
- furry characters
- creature humanoids
- fantasy species
- alien humanoids

mantenendo la separazione tra engine.

---

## 32. Human / Creature Boundary

Il confine tra Human Engine e Creature Engine deve essere esplicito.

### Human Engine

Specializzato nella rappresentazione umanoide.

### Creature Engine

Specializzato nella rappresentazione non umana e ibrida.

### Shared Core

Entrambi possono condividere:

- identity
- variation
- serialization
- validation
- traits
- materials
- transformation metadata

Il core condiviso non deve imporre anatomia umana alle creature.

---

## 33. Prompt Representation

Il Creature Engine deve poter generare una rappresentazione semantica testuale.

Esempio:

```
large quadrupedal reptilian creature,
four muscular legs,
dark green scales,
long armored tail,
two curved horns,
amber eyes,
asymmetric facial scar
```

Il prompt è una rappresentazione derivata.

Il modello strutturato rimane la fonte primaria.

---

## 34. Conditioning Representation

Quando supportato dal backend, il modello può essere trasformato in conditioning.

Pipeline:

```
Creature Model
      ↓
Semantic Representation
      ↓
Prompt / Conditioning
      ↓
Style Engine
      ↓
Camera / Cinematography
      ↓
ComfyUI
```

Il Creature Engine non deve dipendere da un singolo checkpoint o modello.

---

## 35. Style Separation

Il principio deve rimanere identico al Human Engine:

> Creature Engine definisce cosa è la creatura. Style Engine definisce come viene rappresentata.

Esempio:

```
Creature:
  reptilian
  quadrupedal
  four horns
  dark scales
  amber eyes

Style:
  cinematic
  anamorphic
  low key
  film grain
```

La stessa creatura deve poter essere convertita in altri stili senza ricostruzione manuale.

---

## 36. Reference Sheet Integration

Il Creature Engine deve essere progettato per il Reference Sheet System.

Una Reference Sheet potrà includere:

- front
- back
- left
- right
- three-quarter
- profile
- full body
- head close-up
- anatomical details
- appendage details
- expression variants
- material close-ups
- equipment variants

Il Reference Sheet System decide le viste.

Il Creature Engine garantisce la coerenza dell'entità.

---

## 37. Material Consistency

Quando la creatura possiede materiali complessi, il sistema deve mantenere coerenza tra viste.

Esempio:

Una creatura con:

- pelle
- squame
- corna
- artigli

deve mantenere questi materiali nelle diverse angolazioni.

La variazione di illuminazione non deve essere interpretata come variazione del materiale.

---

## 38. Environment Compatibility

Le creature possono essere associate a un ambiente.

Possibili dati:

- habitat
- bioma
- temperatura
- umidità
- terreno
- acqua
- atmosfera
- gravità
- ambiente alieno

Tali parametri appartengono principalmente all'Environment / World Engine.

Il Creature Engine deve esporre soltanto le caratteristiche necessarie per la compatibilità.

---

## 39. Transformation Compatibility

Il Creature Engine deve supportare trasformazioni.

Esempi:

- animale → creatura fantasy
- umano → creatura
- creatura → forma antropomorfa
- creatura → cyborg
- creatura → forma elementale
- creatura giovane → adulta

Una trasformazione deve produrre una relazione tra identità origine e identità derivata.

Concettualmente:

```
Source Creature
      ↓
Transformation
      ↓
Derived Creature
```

La derivazione deve essere tracciabile.

---

## 40. Preset Architecture

I preset delle creature non devono essere hard-coded nel core.

Struttura concettuale:

```
CreaturePreset
├── metadata
├── taxonomy
├── morphology
├── anatomy
├── appendages
├── surface
├── coloration
├── traits
└── behavior
```

Devono essere supportati:

- preset ufficiali
- preset personalizzati
- preset importati
- preset derivati
- archetipi

---

## 41. Validation Rules

Il Creature Engine deve validare:

- tipi dei parametri
- valori ammessi
- numero delle appendici
- componenti incompatibili
- preset esistenti
- riferimenti anatomici
- schema version
- identity_id
- trasformazioni valide

Gli errori devono essere espliciti.

---

## 42. Anatomical Constraints

Il sistema futuro dovrebbe poter esprimere vincoli anatomici.

Esempi:

- una zampa deve essere collegata al torso
- un'ala deve avere un punto di origine
- una coda deve avere una posizione anatomica
- un'articolazione deve avere limiti di movimento
- una pinna deve essere compatibile con la regione anatomica

Non è necessario implementare un simulatore biomeccanico completo.

L'obiettivo iniziale è impedire configurazioni palesemente incoerenti.

---

## 43. Serialization

Il modello della creatura deve essere serializzabile.

Possibili formati:

- JSON
- YAML
- metadata ComfyUI
- formato CharacterForge

La serializzazione deve consentire:

- salvataggio
- caricamento
- duplicazione
- modifica
- confronto
- versionamento
- derivazione

---

## 44. Schema Versioning

Ogni creatura salvata dovrebbe includere una versione dello schema.

Esempio:

```
schema_version: "1.0"
identity_id: "creature_001"
```

Questo permette future migrazioni senza perdere asset esistenti.

---

## 45. Determinism

Una creatura salvata deve poter essere ricostruita semanticamente.

Devono essere preservati almeno:

- identity_id
- schema version
- caratteristiche strutturali
- preset utilizzati
- tratti persistenti
- parametri di variazione
- seed quando necessario

Il determinismo visivo assoluto non può essere garantito indipendentemente dal modello generativo.

Il determinismo richiesto è principalmente **strutturale e semantico**.

---

## 46. Error Handling

Gli errori devono distinguere almeno:

- invalid anatomy
- invalid appendage
- invalid material
- unknown preset
- schema mismatch
- invalid transformation
- conflicting traits
- invalid variation
- missing identity

Non devono essere convertiti silenziosamente in una creatura differente.

---

## 47. Test Strategy

Il Creature Engine dovrà essere verificato su più livelli.

### Unit Test

Test di:

- identity
- taxonomy
- morphology
- anatomy
- appendages
- surface
- coloration
- traits
- serialization

### Integration Test

Verifica con:

- Human Engine
- Style Engine
- Reference Sheet System
- Transformation Engine
- Environment Engine

### Regression Test

Le creature salvate in versioni precedenti devono rimanere leggibili dopo gli aggiornamenti dello schema.

---

## 48. Migration Strategy

La migrazione deve essere incrementale.

### Fase 1

Definire il modello Creature.

### Fase 2

Definire anatomy e morphology modules.

### Fase 3

Definire surface e material system.

### Fase 4

Creare validator e serializer.

### Fase 5

Integrare Style Engine.

### Fase 6

Integrare Reference Sheet System.

### Fase 7

Integrare Transformation Engine.

### Fase 8

Integrare Environment / World Engine.

Nessun componente esistente deve essere eliminato senza test di sostituzione.

---

## 49. Stato attuale

CharacterForge dispone già di sistemi orientati principalmente alla costruzione di soggetti umanoidi e alla gestione dello stile.

Non è ancora verificata l'esistenza di un Creature Engine centralizzato con il modello descritto in questo documento.

Questo documento definisce quindi una **destinazione architetturale**.

Non deve essere interpretato come dichiarazione di funzionalità già implementate.

---

## 50. Debito architetturale previsto

La futura implementazione dovrà evitare:

- duplicazione di modelli anatomici
- preset hard-coded
- dipendenza diretta dai nodi UI
- dipendenza da un singolo modello generativo
- promozione del prompt a fonte primaria dell'identità
- duplicazione tra Human e Creature Engine

Particolare attenzione dovrà essere posta al confine tra:

- Creature Model
- Human Model
- Shared Identity Core
- Style Engine
- Transformation Engine

---

## 51. Relazione con gli altri Engine

La pipeline concettuale è:

```
Creature Engine
      ↓
Style Engine
      ↓
Camera Engine
      ↓
Cinematography Engine
      ↓
Environment / World Engine
      ↓
Transformation Engine
      ↓
Reference Sheet System
      ↓
ComfyUI
```

L'ordine reale potrà variare in base al workflow.

I confini logici devono però rimanere separati.

---

## 52. Extensibility

Il Creature Engine deve essere estendibile.

Nuovi moduli potranno essere aggiunti per:

- bioluminescenza
- venature
- organi esterni
- elementi magici
- elementi cybernetici
- simbiosi
- mutazioni
- materiali alieni
- strutture elementali
- anatomie procedurali

L'aggiunta di una nuova categoria non dovrebbe richiedere la modifica del core.

---

## 53. Shared Entity Architecture

In futuro Human Engine e Creature Engine dovrebbero poter essere visti come specializzazioni di un modello più generale:

```
Entity
├── Identity
├── Morphology
├── Materials
├── Traits
├── Variation
├── Style Binding
├── Transformation State
└── Metadata
```

Specializzazioni:

```
Entity
├── Human
└── Creature
```

Questo concetto non deve essere implementato prematuramente.

Prima devono essere stabilizzati i modelli Human e Creature.

---

## 54. Regola architetturale finale

Il Creature Engine deve garantire una separazione netta tra:

**CHE COSA È LA CREATURA**

e

**COME VIENE RAPPRESENTATA**.

Il primo appartiene al Creature Engine.

Il secondo appartiene agli engine di stile, camera, cinematografia, ambiente e trasformazione.

Il risultato desiderato è una creatura:

- identificabile
- persistente
- serializzabile
- modificabile
- trasformabile
- riutilizzabile
- compatibile con Reference Sheet
- indipendente dallo stile
- indipendente dal modello generativo

---

# Fine Documento 04
