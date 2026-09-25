# 09 — Transformation Engine

## 1. Scopo

Il **Transformation Engine** definisce il sistema con cui CharacterForge modifica in modo controllato un'entità, una materia, un ambiente, uno stato o una variante mantenendo una relazione esplicita con la configurazione di origine.

La trasformazione non deve essere interpretata come semplice variazione casuale.

Una trasformazione è una modifica intenzionale e descrivibile dello stato o della forma di un'entità.

Il sistema deve permettere di rappresentare trasformazioni come:

- crescita;
- invecchiamento;
- cambiamenti anatomici;
- cambiamenti morfologici;
- mutazioni;
- cambiamenti di materiali;
- cambiamenti di stato fisico;
- danno;
- usura;
- riparazione;
- deterioramento;
- ricostruzione;
- cambiamenti ambientali;
- cambiamenti stagionali;
- cambiamenti temporali;
- cambiamenti di scala;
- evoluzione di oggetti tecnologici;
- trasformazioni di creature;
- trasformazioni di veicoli;
- trasformazioni di ambienti;
- trasformazioni fantasy o sci-fi;
- trasformazioni composte da più fasi.

Il Transformation Engine deve inoltre stabilire quando una trasformazione conserva l'identità dell'asset originale e quando produce una nuova identità.

---

## 2. Principio fondamentale

CharacterForge deve distinguere chiaramente:

**Entity Identity**

da:

**Entity State**

e da:

**Entity Variation**

e da:

**Entity Transformation**

Una stessa entità può attraversare molti stati differenti senza perdere necessariamente la propria identità.

Esempio:

Un personaggio può essere:

- bambino;
- adolescente;
- adulto;
- anziano;
- ferito;
- guarito;
- bagnato;
- sporco;
- vestito diversamente;
- invecchiato;
- trasformato temporaneamente.

Se gli elementi identificativi fondamentali rimangono coerenti, queste configurazioni possono rappresentare stati differenti della stessa entità.

Al contrario, una trasformazione può modificare così profondamente la struttura dell'entità da produrre una nuova identità semantica.

Il sistema deve quindi poter rappresentare entrambe le situazioni.

---

## 3. Trasformazione vs variazione

La **variazione** rappresenta una differenza controllata rispetto a una configurazione.

La **trasformazione** rappresenta un cambiamento esplicito tra due stati.

### Variazione

Esempi:

- leggermente diversa acconciatura;
- colore degli occhi variato;
- piccola variazione della corporatura;
- differente posizione;
- differente illuminazione.

La variazione può non richiedere una relazione storica esplicita.

### Trasformazione

Esempi:

- giovane → adulto;
- umano → cyborg;
- auto integra → auto danneggiata;
- estate → inverno;
- roccia solida → roccia frantumata;
- acqua liquida → ghiaccio;
- edificio integro → edificio abbandonato;
- foresta estiva → foresta autunnale.

La trasformazione deve invece mantenere:

- origine;
- destinazione;
- proprietà modificate;
- proprietà mantenute;
- tipo di trasformazione;
- intensità;
- eventuali fasi intermedie;
- relazione con l'identità originale.

---

## 4. Identità e Identity Anchors

Ogni trasformazione deve dichiarare quali elementi dell'entità rappresentano la sua identità.

Gli **Identity Anchors** sono caratteristiche che permettono di riconoscere l'entità attraverso le trasformazioni.

Esempi umani:

- struttura facciale;
- proporzioni fondamentali;
- cicatrici distintive;
- forma degli occhi;
- caratteristiche del volto;
- elementi cromatici persistenti;
- accessori identitari;
- caratteristiche anatomiche uniche.

Esempi per creature:

- pattern della pelle;
- corna;
- forma del cranio;
- appendici caratteristiche;
- marcature;
- dentatura particolare.

Esempi per oggetti:

- geometria fondamentale;
- design;
- numero di componenti;
- disposizione dei componenti;
- serializzazione interna;
- elementi distintivi.

Esempi per veicoli:

- silhouette;
- configurazione del telaio;
- disposizione delle ruote;
- caratteristiche della carrozzeria;
- elementi identificativi.

Gli Identity Anchors devono poter essere:

- persistenti;
- trasformabili;
- sostituibili;
- temporaneamente nascosti;
- danneggiabili;
- recuperabili;
- dichiarati come non più validi.

---

## 5. Transformation Identity Policy

Ogni trasformazione deve poter specificare una policy di identità.

Valori concettuali:

- PRESERVE_IDENTITY
- PRESERVE_PARTIAL_IDENTITY
- CREATE_NEW_IDENTITY
- AUTO_RESOLVE

### Preserve Identity

La trasformazione rappresenta un nuovo stato della stessa entità.

Esempio:

persona adulta → persona anziana.

### Preserve Partial Identity

Una parte dell'identità viene mantenuta mentre un'altra viene modificata.

Esempio:

umano → creatura antropomorfa mantenendo volto, pattern e caratteristiche distintive.

### Create New Identity

La trasformazione produce un nuovo asset semanticamente distinto.

Esempio:

un'auto viene completamente ricostruita come veicolo differente.

### Auto Resolve

Il sistema valuta le modifiche e determina se l'identità può essere mantenuta sulla base delle regole dichiarate.

Questa modalità deve essere deterministica.

---

## 6. Transformation Graph

Le trasformazioni devono essere rappresentabili come un grafo.

Una trasformazione può essere descritta come:

Source State

↓

Transformation

↓

Target State

Esempio:

Character_A
→ AGE_PROGRESSION
→ Character_A_Adult

Un grafo può contenere più trasformazioni:

Character_A
→ AGE_PROGRESSION
→ Adult
→ INJURY
→ Injured_Adult
→ REPAIR
→ Adult_Recovered

Il sistema deve poter conservare:

- nodo sorgente;
- nodo destinazione;
- trasformazione applicata;
- timestamp logico;
- parametri;
- proprietà modificate;
- proprietà ereditate;
- origine;
- eventuali trasformazioni precedenti.

---

## 7. Categorie di trasformazione

Il Transformation Engine deve prevedere categorie modulari.

### 7.1 Temporal Transformation

Modifica legata al tempo.

Esempi:

- crescita;
- invecchiamento;
- evoluzione;
- deterioramento temporale;
- cambiamento storico;
- avanzamento tecnologico.

### 7.2 Anatomical Transformation

Modifica anatomica.

Esempi:

- altezza;
- massa;
- proporzioni;
- muscolatura;
- struttura facciale;
- crescita degli arti;
- sviluppo;
- deformazione.

### 7.3 Morphological Transformation

Modifica della forma.

Esempi:

- mutazione;
- metamorfosi;
- evoluzione;
- cambio di silhouette;
- sviluppo di appendici;
- perdita di appendici.

### 7.4 Material Transformation

Modifica della materia o del materiale.

Esempi:

- metallo → ossidato;
- legno → bruciato;
- tessuto → bagnato;
- superficie → ghiacciata;
- materia liquida → solida.

### 7.5 State Transformation

Modifica dello stato operativo o fisico.

Esempi:

- acceso → spento;
- integro → danneggiato;
- aperto → chiuso;
- attivo → inattivo;
- caldo → freddo;
- liquido → solido.

### 7.6 Environmental Transformation

Modifica dell'ambiente.

Esempi:

- giorno → notte;
- estate → inverno;
- asciutto → piovoso;
- foresta integra → foresta bruciata;
- città moderna → città abbandonata.

### 7.7 Scale Transformation

Modifica della scala.

Esempi:

- oggetto normale → miniatura;
- creatura → gigante;
- edificio → modello;
- ambiente → macrocosmo.

La scala deve essere distinta dalla semplice modifica della distanza della camera.

### 7.8 Damage Transformation

Rappresenta danno e deterioramento.

Esempi:

- graffi;
- ammaccature;
- fratture;
- bruciature;
- corrosione;
- usura;
- decadimento.

### 7.9 Repair Transformation

Rappresenta ripristino o ricostruzione.

Esempi:

- riparazione;
- sostituzione;
- ricostruzione;
- restauro;
- pulizia;
- rigenerazione.

### 7.10 Context Transformation

Modifica il contesto senza necessariamente modificare l'entità.

Esempi:

- stesso personaggio in un altro ambiente;
- stesso veicolo in un'altra epoca;
- stesso edificio in un'altra stagione;
- stessa creatura in un altro habitat.

Il Context Transformation deve rimanere distinto dalla modifica dell'identità dell'entità.

---

## 8. Lo Style Engine non appartiene al Transformation Engine

Lo stile visivo deve rimanere separato.

Il Transformation Engine può modificare:

- forma;
- stato;
- materia;
- ambiente;
- tempo;
- anatomia;
- morfologia.

Non deve diventare proprietario della rappresentazione stilistica.

Esempio:

Character A

può essere trasformato da:

- adulto → anziano;

e successivamente rappresentato tramite:

- anime;
- cinematic;
- western;
- photorealistic;
- painterly.

La trasformazione dell'entità e lo stile con cui viene rappresentata devono rimanere due dimensioni indipendenti.

---

## 9. Trasformazioni reversibili e irreversibili

Ogni trasformazione deve dichiarare la propria reversibilità.

### Reversibile

La trasformazione può essere annullata mantenendo informazioni sufficienti.

Esempi:

- giorno → notte;
- vestito → altro vestito;
- camera → altra camera;
- temperatura controllata.

### Reversibile con perdita

Il ritorno è possibile ma può richiedere informazioni aggiuntive.

Esempio:

- oggetto danneggiato → riparato.

### Irreversibile

La trasformazione modifica permanentemente l'asset o la sua struttura.

Esempi:

- distruzione;
- mutazione irreversibile;
- fusione;
- perdita definitiva di una componente.

Il sistema deve evitare di dichiarare reversibile una trasformazione per la quale non esiste una rappresentazione sufficiente dello stato precedente.

---

## 10. Trasformazioni locali e globali

Una trasformazione può interessare:

### Local Scope

Una singola parte.

Esempi:

- un occhio;
- un braccio;
- una ruota;
- una parete;
- una foglia;
- una superficie.

### Regional Scope

Una parte strutturale.

Esempi:

- volto;
- torso;
- carrozzeria;
- edificio;
- area ambientale.

### Global Scope

L'intera entità.

Esempi:

- metamorfosi completa;
- cambio di scala globale;
- trasformazione dell'intero ambiente.

Lo scope deve essere esplicito.

---

## 11. Ereditarietà delle proprietà

Una trasformazione non deve ricostruire inutilmente l'intera entità.

Il modello deve distinguere:

- proprietà ereditate;
- proprietà modificate;
- proprietà rimosse;
- proprietà aggiunte;
- proprietà sostituite;
- proprietà derivate.

Esempio:

Character_A

Identità:
- invariata

Volto:
- invariato

Capelli:
- invariati

Età:
- modificata

Altezza:
- modificata

Abbigliamento:
- invariato

Cicatrice:
- invariata

Questo permette di mantenere la continuità dell'asset.

---

## 12. Determinismo

Le trasformazioni devono poter essere eseguite in modo deterministico.

Una trasformazione deve poter essere descritta attraverso:

- tipo;
- parametri;
- seed;
- origine;
- versione del Transformation Engine;
- regole applicate.

Dato lo stesso stato sorgente e gli stessi parametri, il sistema deve produrre la stessa configurazione logica.

Le variazioni casuali devono essere controllabili attraverso seed espliciti.

---

## 13. Constraint System

Ogni trasformazione deve poter dichiarare vincoli.

Esempi:

- altezza minima;
- altezza massima;
- età minima;
- età massima;
- compatibilità anatomica;
- compatibilità materiale;
- compatibilità strutturale;
- compatibilità ambientale;
- limiti fisici;
- limiti tecnologici;
- dipendenze tra componenti.

Il sistema deve impedire trasformazioni logicamente incompatibili quando queste violano vincoli espliciti.

Esempio:

un veicolo non può perdere una ruota senza che la configurazione risultante venga classificata come danneggiata o modificata.

---

## 14. Transformation Parameters

I parametri devono essere espliciti.

Esempio concettuale:

Transformation:

- 	ype
- scope
- identity_policy
- eversible
- intensity
- seed
- duration
- source
- 	arget
- constraints
- preserve
- modify
- emove
- dd

I parametri devono essere serializzabili.

---

## 15. Intensità

Le trasformazioni devono poter utilizzare un'intensità controllata.

Esempio:

 .0

nessuna trasformazione.

 .25

trasformazione lieve.

 .50

trasformazione intermedia.

 .75

trasformazione marcata.

1.0

trasformazione completa.

L'intensità non deve essere interpretata come valore universale quando la trasformazione richiede una scala semantica differente.

Il sistema deve permettere parametri specifici quando necessario.

---

## 16. Trasformazioni temporali

Il sistema deve supportare trasformazioni temporali strutturate.

Esempio:

Age:

Child
→ Teen
→ Young Adult
→ Adult
→ Elder

Ogni fase può essere un nodo indipendente.

Devono poter essere definiti:

- età;
- durata;
- caratteristiche anatomiche;
- caratteristiche facciali;
- altezza;
- massa;
- capelli;
- pelle;
- abbigliamento;
- accessori;
- caratteristiche identitarie.

Gli Identity Anchors devono essere mantenuti quando semanticamente appropriato.

---

## 17. Crescita delle creature

Creature e animali devono poter attraversare stadi di crescita.

Esempio:

Egg
→ Hatchling
→ Juvenile
→ Adult
→ Elder

La trasformazione può modificare:

- dimensione;
- proporzioni;
- appendici;
- colorazione;
- dentatura;
- corna;
- piumaggio;
- pelliccia;
- comportamento rappresentato;
- caratteristiche sessuali secondarie.

Il Creature Engine rimane proprietario della struttura della creatura.

Il Transformation Engine orchestra il cambiamento tra stati.

---

## 18. Trasformazioni di oggetti e tecnologia

Gli oggetti devono poter attraversare stati funzionali e fisici.

Esempio:

New Vehicle
→ Used Vehicle
→ Damaged Vehicle
→ Abandoned Vehicle
→ Restored Vehicle

Devono essere rappresentabili:

- usura;
- corrosione;
- sporco;
- graffi;
- ammaccature;
- componenti mancanti;
- componenti sostituiti;
- modifiche;
- upgrade;
- downgrade;
- riconfigurazioni.

L'Object & Technology Engine definisce cosa costituisce l'oggetto.

Il Transformation Engine definisce come cambia nel tempo.

---

## 19. Material Transformations

La materia deve poter cambiare stato o proprietà.

Esempi:

Water
→ Ice

Water
→ Steam

Metal
→ Heated Metal

Metal
→ Oxidized Metal

Wood
→ Burned Wood

Snow
→ Melted Snow

La trasformazione deve mantenere la relazione con il materiale sorgente.

Le proprietà fisiche risultanti devono essere derivate quando possibile invece di essere duplicate manualmente.

---

## 20. Environmental Transformations

Gli ambienti possono cambiare senza diventare ambienti completamente nuovi.

Esempi:

Forest — Summer
→ Forest — Autumn

City — Day
→ City — Night

Street — Dry
→ Street — Wet

Building — Intact
→ Building — Abandoned

Il sistema deve distinguere:

- trasformazione dell'ambiente;
- cambio della camera;
- cambio dello stile;
- cambio della rappresentazione.

---

## 21. Transformation Sequences

Le trasformazioni possono essere concatenate.

Esempio:

Source

→ Growth

→ Injury

→ Recovery

→ Aging

Ogni fase deve essere identificabile.

Il sistema deve supportare:

- sequenze lineari;
- rami;
- stati alternativi;
- checkpoint;
- rollback quando possibile;
- versionamento.

---

## 22. Branching e Variants

Una trasformazione può produrre più rami.

Esempio:

Character_A

→ Adult_A

→ Adult_A_Injured

→ Adult_A_Armored

oppure:

Character_A

→ Adult_A

→ Adult_A_Cinematic

→ Adult_A_Anime

La seconda famiglia rappresenta però una separazione tra trasformazione e stile.

Il Transformation Engine deve evitare di trasformare automaticamente una differenza puramente stilistica in una nuova identità.

---

## 23. Provenance e History

Ogni trasformazione deve poter conservare la propria provenienza.

La history deve permettere di sapere:

- da quale entità deriva lo stato;
- quali trasformazioni sono state applicate;
- in quale ordine;
- con quali parametri;
- quali proprietà sono cambiate;
- quali proprietà sono state ereditate;
- quale versione del sistema ha prodotto il risultato.

Questo permette:

- debugging;
- riproducibilità;
- rollback;
- confronto;
- versionamento;
- continuità narrativa;
- continuità visiva.

---

## 24. Integration con Human Engine

Il Transformation Engine deve poter utilizzare l'Human Engine per:

- crescita;
- invecchiamento;
- cambi anatomici;
- variazioni corporee;
- cambiamenti facciali;
- trasformazioni controllate;
- danni;
- recupero.

L'Human Engine rimane proprietario della rappresentazione umana.

---

## 25. Integration con Creature Engine

Il Creature Engine deve fornire:

- struttura anatomica;
- tassonomia;
- morfologia;
- appendici;
- superfici;
- pattern;
- caratteristiche distintive.

Il Transformation Engine gestisce la transizione tra stati.

---

## 26. Integration con Object & Technology Engine

Il sistema deve supportare:

- danno;
- riparazione;
- upgrade;
- downgrade;
- usura;
- riconfigurazione;
- trasformazione tecnologica;
- evoluzione del design.

---

## 27. Integration con Nature & Matter Engine

Il sistema deve orchestrare:

- cambi di fase;
- crescita;
- decadimento;
- combustione;
- erosione;
- congelamento;
- fusione;
- evaporazione;
- sedimentazione;
- trasformazioni naturali.

---

## 28. Integration con Environment & World Engine

Il sistema deve supportare:

- giorno/notte;
- stagioni;
- condizioni meteorologiche;
- deterioramento;
- cambiamenti storici;
- crescita della vegetazione;
- distruzione;
- ricostruzione;
- evoluzione urbana;
- modifiche del territorio.

---

## 29. Integration con Camera & Cinematography Engine

La camera deve poter osservare qualsiasi stato risultante dalla trasformazione.

Una trasformazione non deve modificare automaticamente:

- lente;
- posizione camera;
- framing;
- profondità di campo;
- composizione.

Questi parametri appartengono al Camera & Cinematography Engine.

Il sistema può tuttavia permettere trasformazioni che richiedano una nuova configurazione camera quando la scena risultante lo rende necessario.

La decisione deve essere esplicita.

---

## 30. Prompt e Conditioning

Il Transformation Engine deve produrre una rappresentazione semantica della trasformazione.

Esempio:

Base:

dult male character

Transformation:

ged by 40 years

Result:

elderly male character with preserved identity anchors

Il sistema non deve confondere:

- stato sorgente;
- trasformazione;
- stato risultante;
- stile.

La derivazione del prompt deve mantenere questa separazione.

---

## 31. Reference Sheet Integration

Il Reference Sheet System deve poter rappresentare gli stati trasformati.

Esempio:

### Identity Sheet

Character A

### Transformation Sheet

Child → Adult → Elder

### State Sheet

Adult → Injured → Recovered

### Material Sheet

Object → Worn → Damaged → Restored

### Environment Sheet

Summer → Autumn → Winter

La Reference Sheet deve poter mostrare la relazione tra gli stati senza perdere l'identità comune.

---

## 32. Transformation Recipes

Le trasformazioni ricorrenti devono poter essere definite come recipe.

Esempio concettuale:

Age_Progression

con parametri:

- source_age;
- target_age;
- intensity;
- preserve_identity;
- preserve_anchors;
- seed.

Altre recipe:

- Damage_Light
- Damage_Heavy
- Repair
- Season_Change
- Day_To_Night
- Material_Oxidation
- Creature_Growth
- Vehicle_Aging

Le recipe devono essere modulari e versionabili.

---

## 33. Preset Architecture

I preset di trasformazione devono essere separati dal core.

Struttura concettuale:

Transformation Core

↓

Transformation Types

↓

Transformation Recipes

↓

Transformation Presets

Il core non deve contenere una lunga lista di casi speciali.

Nuove trasformazioni devono poter essere aggiunte senza modificare il motore principale quando la loro struttura è compatibile con il sistema esistente.

---

## 34. Serialization

Ogni trasformazione deve poter essere serializzata.

La serializzazione deve includere almeno:

- source entity;
- source state;
- transformation type;
- parameters;
- identity policy;
- scope;
- intensity;
- target state;
- changed properties;
- inherited properties;
- provenance;
- version;
- seed quando applicabile.

Il formato deve essere stabile e validabile.

---

## 35. Schema

Lo schema concettuale deve distinguere:

### Entity

Identità persistente.

### State

Configurazione corrente.

### Transformation

Operazione che collega due stati.

### Variant

Configurazione derivata.

### History

Sequenza delle trasformazioni.

### Identity Anchor

Elemento che contribuisce alla continuità dell'identità.

Questi concetti non devono essere collassati in un'unica struttura ambigua.

---

## 36. Validation

Ogni trasformazione deve poter essere validata prima dell'applicazione.

Controlli possibili:

- tipo valido;
- source esistente;
- parametri validi;
- scope valido;
- identity policy valida;
- compatibilità;
- constraint;
- valori numerici;
- dipendenze;
- stato risultante coerente.

Una trasformazione non valida deve produrre un errore esplicito.

---

## 37. Error Handling

Gli errori devono essere distinguibili.

Esempi:

- InvalidTransformationType
- InvalidSourceState
- InvalidTargetState
- ConstraintViolation
- IdentityConflict
- IncompatibleTransformation
- MissingParameter
- InvalidParameter
- SerializationError
- TransformationHistoryError

Gli errori non devono essere nascosti attraverso fallback silenziosi.

---

## 38. Testing Strategy

Il Transformation Engine deve essere testato a più livelli.

### Unit Tests

Test dei singoli tipi di trasformazione.

### Identity Tests

Verifica della persistenza degli Identity Anchors.

### Constraint Tests

Verifica dei vincoli.

### Serialization Tests

Serializzazione e deserializzazione.

### Determinism Tests

Stesso input + stessi parametri + stesso seed = stesso risultato logico.

### Integration Tests

Human Engine.

Creature Engine.

Object & Technology Engine.

Nature & Matter Engine.

Environment & World Engine.

Camera & Cinematography Engine.

### History Tests

Verifica della corretta sequenza delle trasformazioni.

### Regression Tests

Prevenzione delle regressioni durante l'evoluzione del progetto.

---

## 39. Migration Strategy

Il Transformation Engine deve essere introdotto senza rompere i sistemi esistenti.

I controller attuali devono continuare a funzionare.

Le funzionalità esistenti devono poter essere progressivamente reinterpretate come trasformazioni quando appropriato.

Esempi:

- Body Controller → modifica anatomica;
- Gender Controller → modifica di attributi identitari/anatomici;
- Ethnicity Controller → configurazione demografica e fenotipica;
- Style Transfer → rimane separato e appartiene allo Style Engine.

Non deve essere effettuata una migrazione distruttiva.

---

## 40. Stato attuale di CharacterForge

CharacterForge dispone già di componenti utili per il futuro Transformation Engine:

- Human controllers;
- Creature architecture prevista;
- Object architecture prevista;
- Nature & Matter architecture prevista;
- Environment architecture prevista;
- cinematic systems;
- style systems;
- preset systems;
- conditioning systems;
- workflow systems.

Il Transformation Engine deve diventare il livello di orchestrazione delle modifiche tra stati, senza sostituire i motori specialistici.

---

## 41. Debito architetturale

Il progetto deve ancora separare chiaramente:

- state;
- variant;
- transformation;
- style;
- conditioning;
- identity.

Le implementazioni esistenti possono contenere logiche di variazione direttamente nei nodi.

Queste logiche devono essere progressivamente ricondotte a un'architettura comune.

La migrazione deve essere incrementale.

---

## 42. Relazioni con gli altri Engine

Il Transformation Engine è trasversale.

Relazioni principali:

**Human Engine**
→ trasformazioni anatomiche e temporali.

**Creature Engine**
→ crescita, mutazione e metamorfosi.

**Object & Technology Engine**
→ danno, riparazione, evoluzione e riconfigurazione.

**Nature & Matter Engine**
→ cambi di stato e trasformazioni della materia.

**Environment & World Engine**
→ trasformazioni temporali, stagionali e ambientali.

**Camera & Cinematography Engine**
→ osservazione degli stati risultanti.

**Style Engine**
→ rappresentazione visiva indipendente dalla trasformazione.

**Reference Sheet System**
→ documentazione visiva e strutturale degli stati.

---

## 43. Evoluzione verso un Entity Core condiviso

Il Transformation Engine prepara l'introduzione futura di un **Shared Entity Core**.

Il modello futuro potrà essere:

Entity

├── Identity

├── Anchors

├── State

├── Components

├── Variants

├── Transformations

└── History

Questo permetterà di trattare in maniera coerente:

- persone;
- creature;
- animali;
- oggetti;
- veicoli;
- edifici;
- ambienti;
- materiali;
- fenomeni.

Il Transformation Engine non deve quindi essere progettato esclusivamente per personaggi.

---

## 44. Regola architetturale fondamentale

Il Transformation Engine deve rispondere alla domanda:

**"Come cambia questa entità, questa materia o questo ambiente nel tempo o tra due stati?"**

Non deve rispondere alle domande:

**"Che cos'è?"**

Questa è responsabilità degli Entity Engine.

**"Dove si trova?"**

Questa è responsabilità dell'Environment & World Engine.

**"Come viene visto?"**

Questa è responsabilità del Camera & Cinematography Engine.

**"Come viene rappresentato visivamente?"**

Questa è responsabilità dello Style Engine.

La trasformazione è il collegamento controllato tra stati.

---

## 45. Principio finale

Una trasformazione deve modificare **stato, forma, materia o contesto** mantenendo l'identità quando questa rimane semanticamente valida.

Quando la trasformazione supera il limite oltre il quale l'entità non può più essere considerata la stessa, il sistema deve poter creare una nuova identità mantenendo comunque la provenienza dall'entità originale.

Il sistema deve quindi preservare contemporaneamente:

- continuità;
- causalità;
- tracciabilità;
- determinismo;
- identità;
- possibilità di variazione;
- possibilità di evoluzione.

La trasformazione non è una semplice modifica del prompt.

È una relazione strutturata tra due stati di un'entità.
