# CharacterForge — Object & Technology Engine

**Documento:** 05 — Object & Technology Engine  
**Versione architetturale:** 1.0  
**Stato:** Baseline progettuale  
**Data:** 2026-09-24  

---

## 1. Scopo

L'**Object & Technology Engine** è il sottosistema responsabile della definizione strutturata di oggetti, strumenti, veicoli, macchinari, dispositivi tecnologici, robot e manufatti all'interno di CharacterForge.

Il motore deve trattare un oggetto come una **entità persistente e strutturata**, non come una semplice descrizione testuale.

Il modello deve separare:

- identità
- geometria
- componenti
- materiali
- colori
- superfici
- funzionalità
- stato
- usura
- danni
- tecnologia
- equipaggiamento
- stile
- ambiente
- camera
- trasformazioni

---

## 2. Principio fondamentale

Il principio centrale è:

> **L'oggetto è un'entità prima di essere una rappresentazione visiva.**

Lo stesso asset deve poter essere rappresentato come:

- fotografia di prodotto
- fotografia cinematografica
- concept art
- illustrazione
- anime
- fumetto
- videogame asset
- blueprint
- render tecnico
- pixel art
- fantascienza
- fantasy

senza perdere la propria identità strutturale.

---

## 3. Modello concettuale

Il modello generale può essere rappresentato come:

```
Object
├── identity
├── category
├── morphology
├── geometry
├── components
├── materials
├── surface
├── coloration
├── markings
├── functionality
├── technology
├── condition
├── damage
├── accessories
├── distinctive_traits
├── variation_rules
└── transformation_state
```

La struttura definitiva sarà definita durante l'implementazione.

---

## 4. Identity Layer

L'Identity Layer garantisce la continuità dell'asset.

Può comprendere:

- identity_id
- nome interno
- identity seed
- categoria
- modello
- caratteristiche permanenti
- componenti persistenti
- materiali persistenti
- marcature distintive
- vincoli di variazione

Esempio:

```
identity_id: "object_001"
identity_seed: 391824
```

L'identità deve rimanere stabile quando cambiano:

- stile
- camera
- illuminazione
- ambiente
- sfondo
- posa o orientamento
- stato controllato
- condizioni atmosferiche

---

## 5. Object Categories

Il sistema deve supportare almeno:

### 5.1 Oggetti comuni

- mobili
- utensili
- contenitori
- strumenti
- decorazioni
- dispositivi personali

### 5.2 Equipaggiamento

- strumenti professionali
- attrezzature
- dispositivi di protezione
- kit
- accessori tecnici

### 5.3 Veicoli

- automobili
- motociclette
- biciclette
- camion
- autobus
- treni
- imbarcazioni
- aeromobili
- veicoli spaziali

### 5.4 Tecnologia

- computer
- terminali
- dispositivi elettronici
- robot
- droni
- macchinari
- apparecchiature industriali

### 5.5 Oggetti immaginari

- artefatti fantasy
- tecnologia fantascientifica
- manufatti alieni
- dispositivi magici
- oggetti futuristici

Le categorie sono estendibili.

---

## 6. Category vs Identity

La categoria descrive cosa rappresenta un oggetto.

L'identità identifica **quello specifico oggetto**.

Esempio:

```
category: vehicle
type: motorcycle
identity_id: motorcycle_001
```

Un secondo modello di motocicletta può appartenere alla stessa categoria senza condividere la stessa identità.

---

## 7. Morphology Layer

La Morphology Layer descrive la forma generale.

Parametri:

- altezza
- larghezza
- profondità
- lunghezza
- volume
- massa apparente
- proporzioni
- simmetria
- silhouette

Per i veicoli possono essere aggiunti:

- wheelbase
- ground clearance
- cabin proportion
- body proportion

Per oggetti complessi:

- ingombro
- componenti principali
- forma globale

---

## 8. Geometry System

La geometria rappresenta la struttura fisica dell'oggetto.

Può comprendere:

- forma primaria
- forme secondarie
- superfici
- spigoli
- curvature
- giunzioni
- aperture
- pannelli
- supporti
- articolazioni

Il modello non deve richiedere necessariamente una mesh 3D.

La geometria può essere rappresentata semanticamente quando il backend è puramente generativo.

---

## 9. Component System

Gli oggetti complessi devono poter essere composti da componenti.

Esempio:

```
Vehicle
├── chassis
├── body
├── wheels
├── windows
├── lights
├── seats
└── engine
```

Ogni componente può possedere:

- component_id
- type
- position
- dimensions
- material
- color
- state
- visibility
- persistence

---

## 10. Component Hierarchy

I componenti possono avere relazioni gerarchiche.

Esempio:

```
vehicle
└── body
    ├── front_panel
    ├── rear_panel
    ├── left_door
    ├── right_door
    └── roof
```

La gerarchia consente di modificare una parte senza ricostruire necessariamente l'intero asset.

---

## 11. Functional Layer

La funzionalità descrive lo scopo dell'oggetto.

Esempi:

- cutting
- transport
- communication
- storage
- protection
- measurement
- computation
- propulsion
- illumination
- construction

La funzionalità è metadata semantico e non deve essere confusa con la rappresentazione visiva.

---

## 12. Technology Layer

Per oggetti tecnologici possono essere descritti:

- tecnologia
- fonte energetica
- interfaccia
- sensori
- comunicazione
- automazione
- capacità
- livello tecnologico
- componenti elettronici
- componenti meccanici

Per tecnologia immaginaria:

```
technology:
  category: fictional
  level: advanced
  power_source: unknown
```

---

## 13. Material System

I materiali devono essere indipendenti dallo stile.

Categorie:

- metal
- steel
- aluminum
- wood
- plastic
- glass
- ceramic
- stone
- leather
- fabric
- carbon_fiber
- composite
- rubber
- crystal
- synthetic
- unknown
- custom

Ogni materiale può avere:

- colore
- roughness
- reflectivity
- transparency
- translucency
- texture
- density
- wear
- contamination

---

## 14. Multi-Material Objects

Un singolo oggetto può possedere più materiali.

Esempio:

```
car:
  body: painted_metal
  windows: glass
  tires: rubber
  interior: leather
```

La struttura dei materiali deve essere associata ai componenti quando necessario.

---

## 15. Surface System

La superficie descrive lo stato visivo del materiale.

Parametri:

- smooth
- rough
- polished
- brushed
- scratched
- dirty
- dusty
- wet
- rusty
- burned
- cracked
- worn

Lo stato della superficie deve essere modificabile senza cambiare automaticamente il materiale di base.

---

## 16. Coloration System

La colorazione comprende:

- base color
- secondary color
- accent color
- gradient
- pattern
- stripes
- decals
- markings
- camouflage
- emissive elements

Il colore deve essere separato dal materiale.

---

## 17. Marking System

Le marcature possono essere parte dell'identità.

Esempi:

- logo
- numero
- seriale
- livrea
- insegna
- simbolo
- decalcomania
- codice
- pattern distintivo

Ogni marcatura può essere:

- permanente
- temporanea
- opzionale

---

## 18. Damage System

I danni devono essere modellati separatamente dallo stato normale.

Categorie:

- scratch
- dent
- crack
- broken component
- missing component
- burn mark
- corrosion
- bullet damage
- impact damage
- deformation

Un danno può essere:

- permanente
- temporaneo
- riparabile

Il sistema non deve modificare silenziosamente l'identità originale.

---

## 19. Condition System

Lo stato generale dell'oggetto può essere rappresentato come:

- new
- pristine
- used
- worn
- damaged
- heavily damaged
- abandoned
- restored

La condition deve poter essere modificata senza generare automaticamente un nuovo asset.

---

## 20. Wear and Aging

L'usura può influenzare:

- colore
- superficie
- graffi
- ruggine
- sporco
- deformazioni
- materiali
- parti sostituite

Il sistema deve distinguere:

**età dell'oggetto**

da

**condizione attuale**.

---

## 21. Functional State

Un oggetto può avere uno stato funzionale.

Esempi:

- active
- inactive
- powered
- unpowered
- open
- closed
- deployed
- folded
- broken
- charging
- operating

Lo stato funzionale deve essere separato dalla condizione fisica.

---

## 22. Transformable Objects

Alcuni oggetti possiedono configurazioni multiple.

Esempi:

- coltello aperto / chiuso
- laptop aperto / chiuso
- veicolo con porte aperte
- robot trasformabile
- dispositivo ripiegato
- arma con configurazioni differenti
- macchina in modalità operativa

Il sistema deve poter definire:

```
Object
├── base_state
├── state_A
├── state_B
└── state_C
```

Le configurazioni devono mantenere lo stesso identity_id quando rappresentano lo stesso asset.

---

## 23. Vehicle System

I veicoli costituiscono una specializzazione importante.

Parametri possibili:

- chassis
- propulsion
- wheels
- tracks
- wings
- hull
- cockpit
- cabin
- windows
- lights
- doors
- cargo areas
- interior
- exterior

Il Vehicle System deve supportare:

- veicoli terrestri
- navali
- aerei
- spaziali
- fantastici
- fantascientifici

---

## 24. Robot System

I robot devono poter condividere principi con:

- Object Engine
- Creature Engine
- Human Engine

Un robot può essere modellato come:

```
Robot
├── mechanical_body
├── humanoid_components
├── sensors
├── actuators
├── power_system
└── equipment
```

Questo consente di rappresentare robot umanoidi e non umanoidi.

---

## 25. Technology Identity

Gli oggetti tecnologici devono mantenere caratteristiche distintive.

Esempi:

- disposizione dei pannelli
- forma del case
- numero di sensori
- configurazione delle luci
- logo
- porte
- antenna
- struttura meccanica

Questi elementi possono diventare **identity anchors**.

---

## 26. Distinctive Traits

I tratti distintivi sono caratteristiche che contribuiscono fortemente al riconoscimento.

Esempi:

- ammaccatura sul parafango
- graffio specifico
- faro rotto
- logo particolare
- pannello di colore differente
- antenna piegata
- ruota diversa
- componente sostituito

Devono poter essere marcati come persistenti.

---

## 27. Identity Anchors

Un oggetto complesso può possedere più identity anchors.

Esempio:

```
identity_anchors:
  - front_grille
  - left_headlight
  - roof_antenna
  - serial_marking
```

Gli anchor rappresentano elementi che devono essere preservati nelle varianti.

---

## 28. Controlled Variation

Le variazioni devono essere controllabili.

Esempio:

```
variation:
  geometry: 0.05
  materials: 0.1
  coloration: 0.2
  damage: 0.8
  accessories: 0.7
```

Un asset può quindi essere variato senza perdere la propria identità.

---

## 29. Object Variants

Una variante può rappresentare:

- nuova livrea
- colore differente
- equipaggiamento differente
- usura differente
- configurazione differente
- accessori differenti
- aggiornamento tecnologico

Le varianti devono mantenere un riferimento all'asset originale.

Concettualmente:

```
source_identity
      ↓
variant
      ↓
derived_identity
```

---

## 30. Transformation Compatibility

L'Object & Technology Engine deve essere compatibile con il Transformation Engine.

Esempi:

- auto → veicolo futuristico
- smartphone → dispositivo sci-fi
- macchina → robot
- oggetto moderno → artefatto fantasy
- veicolo terrestre → veicolo spaziale

La trasformazione deve essere tracciabile.

---

## 31. Human / Creature Integration

Oggetti, creature e umani possono interagire.

Esempi:

- personaggio che indossa un oggetto
- creatura che utilizza un dispositivo
- personaggio dentro un veicolo
- robot accanto a un personaggio
- animale trasportato da un veicolo

L'Object Engine deve esporre metadata utili all'integrazione, senza diventare responsabile della scena completa.

---

## 32. Style Separation

Il principio è:

> Object & Technology Engine definisce cosa è l'oggetto. Style Engine definisce come viene rappresentato.

Esempio:

```
Object:
  vintage motorcycle
  chrome frame
  black leather seat
  round headlight
  visible wear

Style:
  1970s cinematic photography
  35mm film
  natural light
```

Lo stesso asset deve poter essere rappresentato in altri stili.

---

## 33. Prompt Representation

Il modello strutturato deve poter essere trasformato in una descrizione semantica.

Esempio:

```
vintage motorcycle,
chrome frame,
black leather seat,
round headlight,
aged paint,
minor scratches,
distinctive front badge
```

Il prompt è una rappresentazione derivata.

Non costituisce la fonte primaria dell'identità.

---

## 34. Conditioning Representation

Pipeline concettuale:

```
Object Model
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

Il motore non deve dipendere da un singolo modello generativo.

---

## 35. Reference Sheet Integration

Gli oggetti devono poter generare Reference Sheet coerenti.

Per un oggetto:

- front
- back
- left
- right
- top
- bottom
- three-quarter
- detail views

Per un veicolo:

- exterior front
- exterior rear
- side
- top
- interior
- dashboard
- mechanical details

Per un dispositivo:

- front
- rear
- ports
- controls
- display
- component details

Il Reference Sheet System decide la composizione finale.

---

## 36. Technical Sheet

Per oggetti tecnici può essere utile una modalità aggiuntiva:

**Technical Reference Sheet**

che può includere:

- dimensioni
- componenti
- pannelli
- porte
- connettori
- parti mobili
- materiali
- numerazione
- annotazioni

Questa modalità deve essere distinta dalla Reference Sheet artistica.

---

## 37. Camera Independence

Il Object Engine non deve contenere la logica della fotocamera.

Può però fornire:

- dimensioni
- punti di riferimento
- orientamento
- bounding characteristics
- componenti da mantenere visibili

La composizione fotografica appartiene al Camera Engine.

---

## 38. Environment Compatibility

Gli oggetti possono essere associati a:

- luogo
- epoca
- tecnologia
- clima
- terreno
- atmosfera
- contesto industriale
- contesto urbano
- contesto naturale

L'Environment / World Engine gestirà la scena.

Il Object Engine deve fornire solo le caratteristiche dell'asset necessarie per la compatibilità.

---

## 39. Serialization

Il modello deve essere serializzabile.

Possibili formati:

- JSON
- YAML
- metadata ComfyUI
- formato CharacterForge

La serializzazione deve supportare:

- salvataggio
- caricamento
- duplicazione
- modifica
- confronto
- versionamento
- derivazione

---

## 40. Schema Versioning

Ogni asset salvato dovrebbe contenere:

```
schema_version: "1.0"
identity_id: "object_001"
```

Questo permette migrazioni future.

---

## 41. Determinism

Il sistema deve garantire determinismo principalmente strutturale.

Devono poter essere ricostruiti:

- componenti
- materiali
- marcature
- identity anchors
- stato
- varianti
- metadata
- preset

Il risultato visivo identico non può essere garantito indipendentemente dal modello generativo.

---

## 42. Validation Rules

Il motore deve validare:

- componenti validi
- gerarchie valide
- materiali validi
- categorie valide
- identity_id
- schema version
- stati compatibili
- trasformazioni valide
- preset esistenti

Esempi di errori:

- component_missing
- invalid_material
- invalid_state
- invalid_component_parent
- unknown_preset
- schema_mismatch
- invalid_transformation

---

## 43. Error Handling

Gli errori devono essere espliciti.

Un errore di validazione non deve produrre silenziosamente un oggetto differente.

I fallback devono essere controllati e tracciabili.

---

## 44. Preset Architecture

I preset non devono essere hard-coded nel core.

Struttura concettuale:

```
ObjectPreset
├── metadata
├── category
├── morphology
├── geometry
├── components
├── materials
├── coloration
├── functionality
├── technology
└── traits
```

Devono essere supportati:

- preset ufficiali
- preset personalizzati
- preset importati
- preset derivati

---

## 45. Test Strategy

Il motore dovrà essere verificato con:

### Unit Test

- identity
- morphology
- geometry
- components
- materials
- coloration
- condition
- damage
- serialization

### Integration Test

- Style Engine
- Human Engine
- Creature Engine
- Reference Sheet System
- Transformation Engine
- Environment Engine

### Regression Test

Gli asset salvati nelle versioni precedenti devono rimanere leggibili dopo gli aggiornamenti dello schema.

---

## 46. Migration Strategy

La migrazione dovrà essere incrementale.

### Fase 1

Definire il modello Object.

### Fase 2

Definire componenti e gerarchie.

### Fase 3

Definire materiali e superfici.

### Fase 4

Definire stati, usura e danni.

### Fase 5

Creare validator e serializer.

### Fase 6

Integrare Style Engine.

### Fase 7

Integrare Reference Sheet System.

### Fase 8

Integrare Transformation Engine.

Nessun componente esistente dovrà essere eliminato senza copertura di test.

---

## 47. Stato attuale

CharacterForge possiede già un'infrastruttura significativa per:

- stili
- conditioning
- style transfer
- gestione di soggetti
- preset

Non è stata verificata l'esistenza di un Object & Technology Engine centralizzato con il modello definito in questo documento.

Questo documento definisce quindi la **destinazione architetturale** e non dichiara implementate funzionalità non verificate.

---

## 48. Debito architetturale previsto

La futura implementazione deve evitare:

- oggetti rappresentati esclusivamente come prompt
- preset hard-coded
- duplicazione delle strutture
- dipendenza diretta dai nodi UI
- dipendenza da un singolo modello generativo
- perdita degli identity anchors
- confusione tra materiale e stile
- confusione tra condizione e identità

---

## 49. Relazione con gli altri Engine

La pipeline concettuale è:

```
Object & Technology Engine
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

L'ordine può variare nel workflow reale.

I confini logici devono rimanere separati.

---

## 50. Shared Entity Architecture

Object, Human e Creature possono condividere un livello comune:

```
Entity
├── Identity
├── Morphology
├── Materials
├── Traits
├── Variation
├── State
├── Style Binding
├── Transformation State
└── Metadata
```

Specializzazioni:

```
Entity
├── Human
├── Creature
└── Object
```

Questo shared core non deve essere implementato prematuramente.

Prima devono essere stabilizzati i singoli modelli.

---

## 51. Extensibility

Il motore deve poter essere esteso con:

- nuovi materiali
- nuovi componenti
- nuovi veicoli
- nuovi dispositivi
- nuovi sistemi tecnologici
- nuove categorie fantasy
- nuove categorie sci-fi
- nuovi stati
- nuove modalità di trasformazione

L'aggiunta di una categoria non deve richiedere modifiche invasive al core.

---

## 52. Principio architetturale finale

L'Object & Technology Engine deve garantire una separazione netta tra:

**CHE COSA È L'OGGETTO**

e

**COME VIENE RAPPRESENTATO**.

Il primo appartiene all'Object & Technology Engine.

Il secondo appartiene agli engine di stile, camera, cinematografia, ambiente e trasformazione.

Il risultato desiderato è un asset:

- identificabile
- persistente
- serializzabile
- modificabile
- componibile
- trasformabile
- riutilizzabile
- compatibile con Reference Sheet
- indipendente dallo stile
- indipendente dal modello generativo

---

# Fine Documento 05
