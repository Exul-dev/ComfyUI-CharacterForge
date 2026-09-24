# 10 — Reference Sheet System

## 1. Scopo

Il **Reference Sheet System** definisce il sistema con cui CharacterForge rappresenta visivamente e strutturalmente un'entità in più viste coerenti.

Il Reference Sheet non deve essere considerato una semplice griglia di immagini.

È una rappresentazione strutturata dell'identità, della forma, delle caratteristiche, dei materiali, delle proporzioni, degli elementi distintivi e degli stati dell'asset.

Il sistema deve supportare:

- personaggi;
- creature;
- animali;
- oggetti;
- veicoli;
- edifici;
- ambienti;
- materiali;
- elementi naturali;
- entità fantasy;
- entità sci-fi;
- varianti;
- stati trasformati.

L'obiettivo fondamentale è ottenere **continuità visiva e semantica** tra viste differenti dello stesso asset.

---

## 2. Principio fondamentale

Il Reference Sheet deve rispondere alla domanda:

**"Come posso rappresentare la stessa entità da più punti di vista mantenendo riconoscibile la sua identità?"**

Non deve essere un semplice collage di immagini indipendenti.

Ogni vista deve appartenere allo stesso asset logico.

Il sistema deve quindi separare:

- Identity;
- State;
- Variant;
- View;
- Camera;
- Style;
- Transformation.

---

## 3. Reference Sheet come Asset Identity Surface

Il Reference Sheet rappresenta una superficie di controllo dell'identità dell'asset.

Deve permettere di verificare:

- silhouette;
- proporzioni;
- volto;
- anatomia;
- materiali;
- colori;
- dettagli;
- accessori;
- componenti;
- marcature;
- relazioni spaziali;
- continuità tra viste.

Il Reference Sheet deve quindi essere utilizzabile sia come output visivo sia come riferimento per generazioni successive.

---

## 4. Entity Coverage

Il sistema deve essere generalizzato.

### Human

Deve poter mostrare:

- volto;
- corpo;
- abbigliamento;
- accessori;
- caratteristiche distintive;
- proporzioni.

### Creature

Deve poter mostrare:

- anatomia;
- appendici;
- dentatura;
- occhi;
- superfici;
- pattern;
- silhouette.

### Animal

Deve poter mostrare:

- morfologia;
- postura;
- pelo;
- piume;
- scaglie;
- pattern;
- anatomia.

### Object

Deve poter mostrare:

- forma;
- dimensioni relative;
- componenti;
- materiali;
- dettagli funzionali.

### Vehicle

Deve poter mostrare:

- frontale;
- posteriore;
- laterale;
- superiore;
- componenti;
- ruote;
- interni quando richiesti.

### Building

Deve poter mostrare:

- facciate;
- struttura;
- proporzioni;
- aperture;
- materiali;
- elementi architettonici.

### Environment

Deve poter mostrare:

- panoramica;
- zone;
- distribuzione;
- terreno;
- vegetazione;
- strutture;
- atmosfera;
- scala.

---

## 5. Default Output

Il Reference Sheet deve essere il **default output concettuale** di CharacterForge quando l'obiettivo è definire una nuova entità.

La generazione di una singola immagine può rimanere disponibile.

Tuttavia, il sistema deve essere progettato assumendo che un'entità completa richieda più informazioni di una singola vista.

Il default deve quindi favorire:

**Identity → Reference Sheet → Variants → Transformations → Final Shots**

anziché:

**Prompt → Singola immagine**

---

## 6. Tipi di Reference Sheet

Il sistema deve supportare più formati.

### Character Sheet

Per personaggi umani e umanoidi.

### Creature Sheet

Per creature e animali.

### Object Sheet

Per oggetti.

### Vehicle Sheet

Per veicoli.

### Architecture Sheet

Per edifici e strutture.

### Environment Sheet

Per ambienti e mondi.

### Material Sheet

Per materiali e superfici.

### Transformation Sheet

Per confrontare stati differenti della stessa entità.

### Technical Sheet

Per rappresentazioni orientate alla struttura e alla progettazione.

### Custom Sheet

Per entità specializzate.

---

## 7. View System

Ogni Reference Sheet deve essere composto da viste semanticamente definite.

Le viste possono includere:

- front;
- back;
- left;
- right;
- three-quarter front;
- three-quarter back;
- profile;
- top;
- bottom;
- close-up;
- detail;
- expression;
- pose;
- interior;
- exploded view;
- technical view.

Non tutte le entità richiedono tutte le viste.

Il sistema deve permettere di scegliere le viste necessarie.

---

## 8. Canonical Views

Alcune viste devono essere considerate canoniche.

Per un personaggio:

- front;
- back;
- left;
- right;
- three-quarter.

Per un oggetto:

- front;
- back;
- left;
- right;
- top;
- bottom.

Per un veicolo:

- front;
- rear;
- left;
- right;
- top.

Per un ambiente:

- overview;
- primary zone;
- secondary zone;
- contextual view.

La configurazione canonica deve essere modificabile.

---

## 9. View Identity

Ogni vista deve avere un'identità propria all'interno dello sheet.

Una vista deve poter dichiarare:

- view id;
- semantic role;
- camera configuration;
- framing;
- target;
- crop;
- scale;
- orientation;
- state;
- visibility rules.

Questo permette di distinguere:

"vista laterale"

da:

"immagine casualmente laterale".

---

## 10. Camera Independence

Il Reference Sheet deve utilizzare il Camera & Cinematography Engine.

La camera non deve essere incorporata nell'identità dell'entità.

La stessa entità può essere osservata con:

- lente diversa;
- distanza diversa;
- altezza diversa;
- prospettiva diversa;
- profondità di campo diversa.

La Reference Sheet deve tuttavia poter definire **canonical camera configurations** per garantire coerenza tra viste.

---

## 11. Canonical Camera

Per ogni categoria possono essere definiti parametri standard.

Esempio concettuale:

Character:

- camera height;
- focal length;
- distance;
- neutral perspective;
- neutral lighting.

Object:

- orthographic-like presentation;
- controlled focal length;
- centered framing.

Environment:

- wider lens;
- contextual framing;
- controlled horizon.

La camera canonica serve alla comparabilità, non alla definizione dell'identità.

---

## 12. Identity Lock

Il Reference Sheet deve poter utilizzare un **Identity Lock**.

Identity Lock significa che le caratteristiche identitarie dichiarate devono essere mantenute attraverso le viste.

Possibili livelli:

- weak;
- standard;
- strong;
- strict.

Gli Identity Anchors definiti dal Transformation Engine devono essere disponibili al Reference Sheet.

---

## 13. Identity Anchors

Il sistema deve poter visualizzare o validare:

- volto;
- occhi;
- capelli;
- cicatrici;
- pattern;
- tatuaggi;
- corna;
- appendici;
- silhouette;
- componenti;
- marcature;
- elementi strutturali.

Gli anchor possono essere:

- visibili;
- parzialmente visibili;
- nascosti;
- trasformati;
- danneggiati.

---

## 14. Proportions Lock

La coerenza geometrica richiede un sistema di proporzioni.

Devono poter essere definiti:

- altezza;
- larghezza;
- profondità;
- rapporti anatomici;
- rapporti tra componenti;
- scala relativa;
- dimensioni comparative.

Per un personaggio:

- head-to-body ratio;
- shoulder width;
- limb proportions;
- torso ratio;
- hand size;
- foot size.

Per un oggetto:

- width;
- height;
- depth;
- component ratios.

---

## 15. Scale Reference

Il Reference Sheet deve poter includere riferimenti di scala.

Esempi:

- personaggio accanto a una persona standard;
- veicolo accanto a un essere umano;
- edificio con riferimento umano;
- creatura accanto a un oggetto noto.

La scala deve essere distinta dalla prospettiva.

---

## 16. Pose System

Per personaggi e creature deve essere possibile definire una posa di riferimento.

Possibili modalità:

- neutral;
- anatomical neutral;
- A-pose;
- T-pose;
- standing;
- sitting;
- custom pose.

La posa deve essere separata dall'identità.

Una modifica della posa non deve generare automaticamente una nuova entità.

---

## 17. Expression System

Per personaggi e creature il Reference Sheet può includere espressioni.

Esempi:

- neutral;
- happy;
- sad;
- angry;
- surprised;
- fearful;
- focused;
- custom.

Le espressioni devono essere trattate come stato o configurazione di rappresentazione, non come identità.

---

## 18. Clothing and Equipment

Il sistema deve poter rappresentare:

- abiti;
- armature;
- strumenti;
- armi quando semanticamente pertinenti;
- zaini;
- gioielli;
- accessori;
- equipaggiamento tecnico.

Ogni elemento deve poter essere classificato come:

- identity anchor;
- persistent equipment;
- optional equipment;
- state-dependent equipment.

---

## 19. Material Representation

Il Reference Sheet deve rappresentare i materiali quando questi sono importanti per l'identità o la progettazione.

Esempi:

- pelle;
- metallo;
- legno;
- plastica;
- vetro;
- tessuto;
- pietra;
- ceramica;
- gomma;
- materiali fantasy;
- materiali sci-fi.

Devono poter essere mostrati:

- colore;
- roughness;
- texture;
- riflessione;
- trasparenza;
- usura;
- pattern.

---

## 20. Surface Detail

Il sistema deve poter documentare dettagli superficiali.

Esempi:

- pori;
- rughe;
- cicatrici;
- graffi;
- ammaccature;
- cuciture;
- texture;
- incisioni;
- decorazioni;
- pattern.

I dettagli devono essere associabili all'entità o a specifici componenti.

---

## 21. Component System

Un'entità complessa deve poter essere suddivisa in componenti.

Esempio veicolo:

- chassis;
- wheels;
- windows;
- lights;
- doors;
- interior.

Esempio personaggio:

- head;
- torso;
- arms;
- hands;
- legs;
- footwear;
- accessories.

Esempio edificio:

- foundation;
- walls;
- roof;
- windows;
- doors;
- structural elements.

Ogni componente può avere proprie proprietà e Identity Anchors.

---

## 22. Component Visibility

Ogni componente deve poter avere regole di visibilità.

Possibili stati:

- visible;
- hidden;
- transparent;
- cutaway;
- exploded;
- detail-only.

Questo permette di produrre Technical Sheet e Reference Sheet differenti dalla semplice vista finale.

---

## 23. Detail Views

Il sistema deve poter generare viste ravvicinate.

Esempi:

- volto;
- occhi;
- mani;
- logo;
- ruota;
- materiale;
- componente tecnologico;
- dettaglio architettonico.

Ogni detail view deve mantenere il riferimento all'entità e al componente di origine.

---

## 24. Technical Sheet

Il Technical Sheet è una specializzazione del Reference Sheet.

Può includere:

- quote;
- proporzioni;
- componenti;
- nomenclatura;
- assi;
- simmetrie;
- punti di connessione;
- sezioni;
- viste esplose.

Il Technical Sheet deve essere distinto dalla semplice immagine artistica.

---

## 25. Environment Reference Sheet

Gli ambienti richiedono una struttura differente.

Il sistema deve poter rappresentare:

- overview;
- zone;
- foreground;
- midground;
- background;
- punti di interesse;
- terreno;
- architettura;
- vegetazione;
- acqua;
- atmosfera;
- scala.

La continuità dell'ambiente deve essere verificabile tra viste diverse.

---

## 26. Spatial Continuity

Un Reference Sheet ambientale deve preservare:

- posizione relativa;
- orientamento;
- scala;
- distribuzione;
- connessioni;
- topografia;
- architettura.

Una vista diversa non deve reinventare arbitrariamente la posizione degli elementi.

---

## 27. Transformation Sheet

Il Transformation Sheet deve mostrare l'evoluzione di un'entità.

Esempio:

Character A

Child → Adult → Elder

oppure:

Vehicle A

New → Used → Damaged → Restored

oppure:

Forest A

Summer → Autumn → Winter

Ogni stato deve mantenere il riferimento all'identità comune quando previsto.

---

## 28. Variant Sheet

Il Variant Sheet mostra configurazioni alternative della stessa entità.

Esempi:

- outfit A/B/C;
- materiali alternativi;
- color variants;
- equipment variants;
- body variants.

Le varianti devono essere distinguibili dalle trasformazioni.

Una variante può derivare da uno stesso stato senza rappresentare una sequenza temporale.

---

## 29. State vs Variant

Il sistema deve mantenere la distinzione:

**State**

rappresenta una condizione dell'entità.

**Variant**

rappresenta una configurazione alternativa.

**Transformation**

rappresenta il passaggio tra stati.

**Style**

rappresenta il linguaggio visivo.

Questi quattro concetti non devono essere fusi.

---

## 30. Style Independence

Il Reference Sheet deve essere compatibile con qualunque Style Profile.

La stessa identità può essere rappresentata in:

- anime;
- cinematic;
- realistic;
- painterly;
- western;
- retro;
- sci-fi;
- fantasy.

Il Reference Sheet non deve diventare proprietario dello Style Engine.

---

## 31. Style Consistency

Quando più viste appartengono allo stesso sheet, devono condividere il medesimo profilo stilistico quando richiesto.

Devono essere controllabili:

- palette;
- rendering;
- linework;
- contrasto;
- materiali;
- illuminazione;
- grain;
- atmosfera.

Lo stile è però applicato sopra la struttura dell'asset.

---

## 32. Prompt Assembly

Il sistema deve poter costruire prompt specifici per ogni vista.

Struttura concettuale:

Entity Identity

+

Entity State

+

View Definition

+

Camera

+

Environment

+

Style

+

Quality Controls

La composizione deve evitare duplicazioni incoerenti.

---

## 33. Conditioning Assembly

Il Reference Sheet deve poter produrre conditioning coerente con la struttura definita.

Le informazioni devono poter essere pesate secondo priorità.

Esempio concettuale:

Identity

>

Structural Features

>

View

>

State

>

Environment

>

Style

>

Secondary Details

La gerarchia concreta deve rimanere configurabile.

---

## 34. View-to-View Consistency

La coerenza deve essere controllabile tra viste.

Devono essere confrontabili:

- silhouette;
- proporzioni;
- colori;
- materiali;
- componenti;
- Identity Anchors;
- dettagli;
- posizione relativa.

Il sistema futuro potrà utilizzare:

- image embeddings;
- feature matching;
- segmentation;
- pose comparison;
- structural analysis.

Queste tecnologie devono rimanere implementazioni sostituibili.

---

## 35. Reference Sheet Layout

Il layout deve essere configurabile.

Possibili configurazioni:

- grid;
- horizontal strip;
- vertical strip;
- central hero;
- technical board;
- cinematic board;
- custom layout.

Il layout non deve modificare l'identità dell'asset.

---

## 36. Metadata

Ogni sheet deve poter contenere metadata.

Esempi:

- entity_id;
- entity_type;
- state_id;
- variant_id;
- transformation_id;
- style_id;
- camera_profile;
- seed;
- engine_version;
- generation_date;
- source;
- notes.

I metadata devono poter essere serializzati.

---

## 37. Reproducibility

Un Reference Sheet deve poter essere rigenerato.

La configurazione deve conservare:

- prompt;
- conditioning;
- seed;
- modelli;
- LoRA;
- style profile;
- camera profile;
- view configuration;
- entity configuration;
- transformation state.

L'obiettivo è poter ricostruire lo sheet senza dipendere esclusivamente dall'immagine precedente.

---

## 38. Asset Identity Persistence

Il Reference Sheet deve essere uno dei principali strumenti di persistenza dell'identità.

Un asset creato oggi deve poter essere richiamato successivamente.

Esempio:

Character_001

può essere usato in:

- scena A;
- scena B;
- scena C;
- stagione differente;
- outfit differente;
- età differente;
- ambiente differente.

Il sistema deve mantenere un riferimento comune all'identità.

---

## 39. Reference Sheet come Source of Truth

Quando esiste un Reference Sheet canonico, questo deve poter essere dichiarato come:

**Canonical Reference**

La Canonical Reference rappresenta la configurazione di riferimento dell'entità.

Altre configurazioni possono essere derivate da essa attraverso:

- Variant;
- Transformation;
- Context;
- Style;
- Camera.

Questo crea una gerarchia controllabile.

---

## 40. Reference Hierarchy

La gerarchia concettuale deve essere:

Canonical Identity

↓

Canonical State

↓

Variants / Transformations

↓

Views

↓

Camera

↓

Environment Context

↓

Style

↓

Final Image

L'ordine può essere adattato dall'implementazione, ma la separazione semantica deve essere preservata.

---

## 41. Multi-Reference Support

Un'entità può avere più riferimenti.

Esempio:

- reference front;
- reference profile;
- reference face;
- reference outfit;
- reference material;
- reference technical.

Il sistema deve poter associare ogni riferimento alla funzione che svolge.

Non tutte le immagini devono avere lo stesso peso.

---

## 42. Reference Priority

Le reference possono avere priorità differenti.

Esempio:

1. Canonical Identity Reference
2. Structural Reference
3. Component Reference
4. State Reference
5. Style Reference
6. Context Reference

La priorità deve essere configurabile.

---

## 43. Conflict Resolution

Se due reference sono incompatibili, il sistema deve rilevare il conflitto.

Esempi:

- due forme del volto differenti;
- due colori incompatibili;
- due configurazioni di componenti;
- due scale differenti;
- due stati temporali incompatibili.

Il sistema non deve risolvere silenziosamente il conflitto.

Deve poter:

- segnalare;
- chiedere una priorità;
- applicare una policy esplicita;
- creare una variante separata.

---

## 44. Identity Drift Detection

Il sistema deve prevedere in futuro strumenti per rilevare l'**identity drift**.

Identity drift significa che l'asset generato si allontana progressivamente dall'identità canonica.

Possibili segnali:

- variazione del volto;
- variazione della silhouette;
- perdita di marcature;
- cambiamento di proporzioni;
- sostituzione di componenti;
- cambiamento cromatico non richiesto.

La rilevazione può essere:

- visiva;
- strutturale;
- semantica;
- embedding-based.

Il metodo concreto deve rimanere sostituibile.

---

## 45. Versioning

I Reference Sheet devono essere versionabili.

Esempio:

Character_001

- v1.0 canonical;
- v1.1 corrected hair;
- v1.2 corrected scar;
- v2.0 transformed adult state.

Una modifica non deve cancellare necessariamente il riferimento precedente.

---

## 46. Provenance

Il sistema deve poter ricostruire l'origine dello sheet.

Deve essere possibile sapere:

- chi lo ha creato;
- quale configurazione lo ha prodotto;
- quale asset lo ha originato;
- quale trasformazione è stata applicata;
- quale stile era attivo;
- quale camera era attiva;
- quale workflow è stato utilizzato.

---

## 47. Serialization Schema

Il Reference Sheet deve essere serializzabile.

Struttura concettuale:

Entity Reference

- identity;
- state;
- variant;
- anchors;
- components;
- views;
- camera;
- style;
- environment;
- transformations;
- metadata;
- provenance.

Il formato deve essere versionato e validabile.

---

## 48. Determinism

La configurazione di un Reference Sheet deve essere deterministica.

Stessa configurazione:

- stesso asset;
- stesso stato;
- stessa vista;
- stessi parametri;
- stesso seed;

deve produrre lo stesso risultato logico.

L'immagine generata può comunque dipendere dalle caratteristiche del modello utilizzato.

---

## 49. Validation

Prima della generazione il sistema deve validare:

- entity id;
- entity type;
- state;
- variant;
- view;
- camera;
- style;
- references;
- components;
- metadata;
- transformation compatibility.

Gli errori devono essere espliciti.

---

## 50. Error Handling

Possibili errori:

- InvalidEntityReference
- MissingCanonicalReference
- InvalidView
- InvalidCamera
- ReferenceConflict
- IdentityAnchorConflict
- InvalidState
- InvalidVariant
- MissingComponent
- InvalidSheetLayout
- SerializationError
- ReferenceGenerationError

Gli errori non devono essere mascherati da fallback silenziosi.

---

## 51. Preset Architecture

I preset di Reference Sheet devono essere separati dal core.

Esempi:

- Character Standard;
- Character Cinematic;
- Character Technical;
- Creature Standard;
- Vehicle Technical;
- Object Product;
- Environment World;
- Material Study.

I preset devono definire configurazioni, non logica core.

---

## 52. ComfyUI Integration

Il Reference Sheet System deve essere progettato come sistema compatibile con ComfyUI.

La futura implementazione può prevedere nodi dedicati per:

- creare Reference Sheet;
- configurare viste;
- configurare Identity Lock;
- gestire references;
- gestire layout;
- creare transformation sheets;
- creare variant sheets;
- esportare metadata.

I nodi devono rimanere modulari.

---

## 53. Workflow Integration

Un workflow completo può essere:

Entity Builder

→ Canonical Reference

→ Reference Sheet

→ Identity Validation

→ Variant / Transformation

→ Scene

→ Camera

→ Style

→ Final Render

Il Reference Sheet deve poter essere inserito anche dopo la creazione iniziale dell'asset.

---

## 54. Relationship with Transformation Engine

Il Transformation Engine fornisce:

- stato sorgente;
- trasformazione;
- stato risultante;
- Identity Anchors;
- history.

Il Reference Sheet System visualizza e documenta questi elementi.

Esempio:

Character_A

Child

→ Transformation: AGE

→ Adult

Il Transformation Sheet deve poter mostrare entrambi gli stati mantenendo il riferimento all'identità comune.

---

## 55. Relationship with Camera Engine

Il Camera Engine definisce:

- posizione;
- orientamento;
- lente;
- FOV;
- profondità di campo;
- framing;
- esposizione;
- movimento.

Il Reference Sheet definisce quali configurazioni camera utilizzare per le viste canoniche.

Il Reference Sheet non deve duplicare la logica ottica.

---

## 56. Relationship with Style Engine

Lo Style Engine definisce il linguaggio visivo.

Il Reference Sheet definisce la struttura delle viste.

Quindi:

**Reference Sheet = cosa mostrare e come organizzarlo**

**Camera = come osservarlo**

**Style = come rappresentarlo visivamente**

Questa separazione deve essere mantenuta.

---

## 57. Relationship with Human, Creature and Object Engines

Gli Entity Engine definiscono la struttura dell'entità.

Il Reference Sheet deve poter interrogare tale struttura per creare viste coerenti.

Non deve duplicare:

- anatomia;
- morfologia;
- materiali;
- componenti.

Deve rappresentarli.

---

## 58. Testing Strategy

Il sistema deve essere testato a più livelli.

### Unit Tests

- view definitions;
- layout;
- metadata;
- serialization.

### Identity Tests

- anchor persistence;
- identity lock;
- canonical reference.

### Consistency Tests

- view-to-view;
- component consistency;
- proportions.

### Transformation Tests

- transformation sheet;
- state continuity;
- provenance.

### Variant Tests

- variant separation;
- inheritance.

### Integration Tests

- Human;
- Creature;
- Object;
- Nature;
- Environment;
- Camera;
- Style.

### Regression Tests

Ogni modifica deve evitare regressioni sulle configurazioni esistenti.

---

## 59. Migration Strategy

Il Reference Sheet System deve essere introdotto senza rompere gli output attuali.

Le funzionalità esistenti possono continuare a generare singole immagini.

Progressivamente potranno essere interpretate come viste di un asset.

Questo permette una migrazione incrementale:

Single Image

→ Named View

→ Multi-View Reference

→ Canonical Reference

→ Persistent Asset.

---

## 60. Stato attuale di CharacterForge

CharacterForge possiede già elementi utili:

- Human controllers;
- Creature architecture prevista;
- Object architecture prevista;
- Style Engine;
- Cinematic Engine;
- Conditioning;
- workflows;
- preset systems;
- Transformation architecture documentata.

Il Reference Sheet System deve diventare il livello di aggregazione visiva e strutturale di questi sistemi.

---

## 61. Debito architetturale

Il progetto deve ancora introdurre formalmente:

- Entity IDs;
- canonical references;
- view definitions;
- identity locks;
- anchor schemas;
- reference priorities;
- sheet layouts;
- identity drift detection;
- reference serialization.

Questi elementi devono essere implementati progressivamente.

Non devono essere simulati attraverso stringhe di prompt non strutturate.

---

## 62. Estensibilità futura

Il Reference Sheet System deve poter evolvere verso:

- storyboard;
- model sheets;
- character turnarounds;
- production design;
- concept art boards;
- technical documentation;
- game asset sheets;
- animation model sheets;
- continuity sheets;
- shot continuity;
- multi-character sheets;
- scene breakdown;
- asset libraries;
- asset matching;
- automatic identity verification.

---

## 63. Principio finale

Il Reference Sheet System non deve essere un semplice collage di immagini.

Deve essere una **rappresentazione strutturata dell'identità e delle viste di un asset**.

Ogni vista deve sapere:

- quale entità rappresenta;
- quale stato rappresenta;
- quale variante rappresenta;
- quale trasformazione l'ha prodotta;
- quale camera utilizza;
- quale ambiente utilizza;
- quale stile utilizza;
- quali Identity Anchors deve preservare.

Il principio fondamentale è:

**Una singola immagine mostra un'entità.**

**Un Reference Sheet definisce l'entità.**

La continuità tra viste, stati, varianti e trasformazioni deve essere una proprietà architetturale del sistema, non una conseguenza casuale della generazione.
