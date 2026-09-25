# CharacterForge — Visione, architettura di generazione, origine e stato tecnico (H4.15)

> Documento di riferimento del progetto: visione globale, architettura di generazione, origine e stato tecnico. Aggiornato a **H4.15 — Lower Body Anatomy** (chiusa, sottosezioni A→B).

---

# PARTE I — La visione globale: oltre il personaggio

La visione globale di CharacterForge è molto più grande della sola creazione di personaggi.

> **CharacterForge non deve modellare "un personaggio". Deve modellare una cosa qualsiasi come entità coerente, contestualizzata, parametrica e trasformabile.**

Il personaggio umano è semplicemente **il primo dominio complesso** con cui si sta costruendo e verificando l'architettura.

## Dal Character Engine all'Entity Engine

Se si elimina dal concetto la parola *character*, resta: **Forge = costruire un'entità.**

L'idea è creare un sistema nel quale non si dice semplicemente "genera un'immagine di X", ma:

> **"Costruisci X, definisci cosa è, di cosa è composto, quali proprietà possiede, in quale stato si trova, in quale contesto esiste e come deve essere rappresentato."**

Questa filosofia può essere applicata a praticamente qualsiasi elemento visivo.

Oggi si sta costruendo:

```text
CharacterForge
└── Human Engine
    └── Anatomy
```

Ma concettualmente la direzione è:

```text
CharacterForge
│
└── Entity Engine
    │
    ├── Human
    ├── Creature
    ├── Animal
    ├── Object
    ├── Vehicle
    ├── Building
    ├── Environment
    └── ...
```

E tutti questi domini condividono una filosofia comune.

## Un essere umano, una macchina e una casa diventano lo stesso problema astratto

**Persona:** identità, struttura, anatomia, materiali biologici, abbigliamento, stato, posizione, comportamento, contesto.

**Automobile:** identità, struttura, carrozzeria, materiali, componenti, stato, posizione, usura, contesto.

**Edificio:** identità, struttura, piani, stanze, materiali, stato, posizione, epoca, contesto.

**Albero:** specie, struttura, tronco, rami, foglie, materiali, stato, stagione, età, ambiente.

La **natura dell'oggetto** cambia, ma il problema informatico di fondo è sorprendentemente simile:

> **come rappresentare un'entità composta da parti, proprietà, relazioni, stato e contesto?**

## Il concetto fondamentale: Context

La parola chiave della visione globale è probabilmente **CONTEXT**.

Non basta sapere "che cos'è questa cosa?". Serve sapere: **"che cos'è questa cosa, in quale situazione si trova e come deve essere rappresentata in quella situazione?"**

Esempio — un'automobile non è completa con soli `modello`, `colore`, `dimensioni`, `materiali`, `stato`. Va aggiunto un `Context` con `luogo`, `terreno`, `ora`, `stagione`, `meteo`, `illuminazione`, `camera`, `evento`. La stessa automobile può così comparire in un garage, su una strada bagnata, nel deserto, o davanti a un edificio medievale — senza diventare quattro automobili diverse.

Il salto concettuale è passare da:

```text
IMAGE = OBJECT
```

a:

```text
OBJECT + STATE + CONTEXT + VIEW → REPRESENTATION
```

## Esempio: una spada

```text
Sword
├── Identity
├── Structure (blade, guard, handle)
├── Materials (steel, leather)
├── Dimensions (length, width, thickness)
├── State (pristine, worn, damaged)
├── History
├── Context (owner, location, era, environment)
└── View
```

Si può chiedere "mostramela integra", "mostramela dopo 20 anni di utilizzo", "mostramela appesa nella sala del castello" — è sempre **la stessa entità**.

## Esempio: un edificio

```text
Building
├── Identity
├── Architecture (foundation, walls, floors, roof, openings)
├── Materials
├── Interior (rooms, furniture, lighting)
├── State (new, inhabited, abandoned, ruined)
├── Time
├── Environment
└── View
```

Stesso edificio → nuovo / abitato / abbandonato / in rovina: non quattro asset scollegati.

## Identity ≠ State

Un personaggio ferito è sempre quel personaggio. Una macchina ammaccata è sempre quella macchina. Una casa abbandonata è sempre quella casa. Una spada arrugginita è sempre quella spada. Un albero in autunno è sempre quello stesso albero.

```text
ENTITY
├── Identity
├── State
├── Variant
└── Transformation
```

diventa una struttura universale.

## Il tempo come proprietà dell'entità

Un'entità può essere osservata in momenti diversi:

```text
ENTITY
├── t0
├── t1
├── t2
└── t3
```

Un castello nel 1200 → 1500 → 1800 → 2026 non è necessariamente quattro oggetti: può essere **quattro stati temporali della stessa entità**.

## Relazioni tra entità

Gli oggetti non devono essere isolati:

```text
Personaggio
├── owns → Sword
├── rides → Horse
├── lives_in → House
├── stands_in → Room
└── interacts_with → Person

Car
├── parked_at → Building
├── driven_by → Person
└── located_in → Street

Room
├── contains → Table
├── contains → Chair
├── contains → Lamp
└── belongs_to → Building
```

CharacterForge potrebbe progressivamente passare da **asset generator** a **entity + relationship system**.

## Il concetto di scena

Una scena non è più semplicemente "un'immagine con questi elementi", ma:

```text
SCENE
├── Environment
├── Entities
│   ├── Character A
│   ├── Character B
│   ├── Vehicle
│   ├── Building
│   └── Objects
├── Relationships
├── Time
├── Weather
├── Lighting
├── Camera
└── Composition
```

Da questa struttura si potrebbe produrre un'immagine, una reference sheet, una vista multi-angolo o, in fase avanzata, geometria 3D.

## Come si sposa con ComfyUI

ComfyUI è naturalmente adatto a workflow modulari e componibili. CharacterForge potrebbe occupare uno strato precedente:

```text
             CHARACTERFORGE
                    │
                    ↓
             ENTITY MODEL
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    STRUCTURE     CONTEXT      STATE
       │            │            │
       └────────────┼────────────┘
                    ↓
              REPRESENTATION
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
     IMAGE       MULTIVIEW    REFERENCE
       │
       ↓
    COMFYUI
```

CharacterForge non sostituisce ComfyUI: **lo rende più consapevole di ciò che sta generando.**

## La visione finale, oltre la milestone attuale

Oggi: **H4.15 — Lower Body** ✅ (chiusa, H4.15-A/B). Poi, progressivamente:

```text
Morphology → Geometry → Transformations → Identity → State
→ Context → Relationships → Multi-entity scenes → Reference Sheets → Generation
```

Ma sotto tutto questo esiste una singola idea:

> **CharacterForge vuole costruire un linguaggio strutturato per descrivere e trasformare entità visive.**

Il "character" è soltanto il primo caso d'uso perché è uno dei casi più complessi: contiene anatomia, aspetto, abbigliamento, stato, comportamento, relazioni, viewpoint e identità. Se l'astrazione sottostante viene costruita correttamente, la stessa architettura può essere applicata a:

**persone → animali → creature → oggetti → armi → veicoli → edifici → stanze → ambienti → scene → mondi.**

Non si sta cercando soltanto di rendere la generazione più bella. Si sta cercando di renderla: **più descrivibile → più controllabile → più coerente → più modificabile → più riproducibile → più contestuale.**

---
---

# PARTE II — Architettura di generazione: CharacterForge come progettista, il modello generativo come pittore

> **CharacterForge è il progettista. Krea 2 è il pittore.**

CharacterForge non deve cercare di fare il lavoro del modello generativo. Deve costruire **il progetto completo dell'immagine** e poi tradurlo nel linguaggio che il modello destinatario comprende meglio.

## La divisione dei ruoli

```text
                    CHARACTERFORGE
                    ──────────────
                         │
                  PROGETTAZIONE
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     ENTITY          CONTEXT          INTENT
        │                │                │
     struttura        ambiente        immagine
     anatomia         tempo           desiderata
     materiali        luce
     identità         camera
     stato            viewpoint
        │                │                │
        └────────────────┼────────────────┘
                         ↓
                 PROMPT COMPILER
                         ↓
              PROMPT SPECIFICO PER MODELLO
                         ↓
                    KREA 2
                         │
                    "IL PITTORE"
                         ↓
                     IMMAGINE
```

## CharacterForge non deve essere "un altro generatore"

Se domani Krea 2 venisse sostituito da un altro modello, **CharacterForge dovrebbe continuare a esistere**:

```text
CharacterForge
      ├── Krea 2 Adapter
      ├── Modello B Adapter
      ├── Modello C Adapter
      └── Modello D Adapter
```

L'entità rimane la stessa. Quello che cambia è **il modo in cui CharacterForge comunica il progetto al pittore**.

## Il Prompt Compiler

Una delle componenti più importanti da costruire. L'utente non dovrebbe scrivere manualmente "uomo alto, atletico, volto ovale, mandibola pronunciata, capelli…". CharacterForge parte dalla struttura:

```text
Character
├── Height
├── BodyType
├── Musculature
├── BodyFat
├── HeadDimensions
├── HeadProportions
├── FaceDimensions
├── FacialProportions
├── FacialLandmarks
├── Hair
├── Clothing
├── Pose
├── Expression
├── Environment
├── Lighting
└── Camera
```

e la trasforma in:

```text
CHARACTER SPECIFICATION
          ↓
SEMANTIC INTERPRETATION
          ↓
MORPHOLOGICAL DESCRIPTION
          ↓
VISUAL DESCRIPTION
          ↓
MODEL-SPECIFIC PROMPT
```

Il prompt finale non è il **database** del personaggio: è una **compilazione temporanea** della sua descrizione.

## Stessa entità, viste diverse

`CHARACTER_001` può essere mandato a Krea 2 con `VIEW = FRONT`, poi `PROFILE`, poi `THREE_QUARTER`, poi `BACK`. CharacterForge genera ogni volta il prompt appropriato, ma il progetto sottostante rimane sempre `CHARACTER_001` — molto diverso dal salvare quattro prompt diversi.

## Il ruolo di Krea 2

Krea 2, nel paradigma attuale, assume il ruolo del **pittore**: CharacterForge dice "questo è ciò che devi rappresentare", Krea 2 decide "come trasformare questa descrizione in un'immagine visivamente convincente". Questo separa **progettazione** da **esecuzione artistica**.

## Esempio con un'automobile

```text
Car
ID: CAR_017

Model:      coupe
Dimensions: length / width / height
Materials:  aluminum, glass, leather
Color:      dark red
State:      lightly damaged
Environment: rainy urban street
Time:       night
Camera:     35mm, low angle
Lighting:   wet street reflections
```

CharacterForge costruisce il progetto; il **Krea Adapter** lo trasforma in un prompt orientato a ciò che Krea 2 interpreta meglio. Domani, un `Krea2Adapter` e poi un `OtherModelAdapter` potranno coesistere senza dover ricostruire l'automobile.

## L'architettura globale che ne deriva

```text
                    CHARACTERFORGE
                          │
                    ENTITY ENGINE
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    STRUCTURE          CONTEXT           STATE
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                   VISUAL DESIGN
                          │
                   VIEW / CAMERA
                          │
                  REFERENCE SHEET
                          │
                    PROMPT ENGINE
                          │
                 ┌────────┴────────┐
                 │                 │
            KREA 2 ADAPTER     OTHER ADAPTERS
                 │
                 ↓
              KREA 2
             "PAINTER"
                 │
                 ↓
               IMAGE
```

Questo spiega anche perché non c'è fretta di collegare Krea 2 al codice anatomico attuale: prima si costruisce il progettista, il generatore verrà collegato sopra una struttura che abbia già senso.

## Non tutto ciò che CharacterForge sa deve arrivare al modello

CharacterForge potrebbe conoscere internamente decine di proprietà anatomiche, morfometriche, relazionali, ambientali, fotografiche — ma il modello generativo potrebbe non averne bisogno di tutte. Il compilatore decide:

```text
CharacterForge Knowledge
          ↓
      relevance
          ↓
      prioritization
          ↓
   model vocabulary
          ↓
     final prompt
```

CharacterForge può quindi essere **molto più preciso internamente di quanto sia il prompt finale**: il prompt è la traduzione.

## Il futuro non è necessariamente solo testo

L'obiettivo finale potrebbe essere un output multi-canale, a seconda di ciò che il modello supporta:

```text
CharacterForge
      ├── Prompt
      ├── Image reference
      ├── Control parameters
      ├── Pose information
      ├── Depth information
      ├── Composition
      └── Model-specific conditioning
```

Il **Prompt Compiler** evolve quindi più correttamente in un **Model Adapter / Generation Compiler**, di cui il testo è soltanto uno dei possibili output.

## Il ruolo del Custom Node

Il custom node `ComfyUI-CharacterForge` è la porta attraverso cui tutto questo entra nel mondo ComfyUI. Non semplicemente `CharacterForge → Prompt`, ma progressivamente:

```text
CharacterForge Entity
        ↓
CharacterForge Builder
        ↓
Entity Specification
        ↓
Context
        ↓
Reference / View
        ↓
Generation Compiler
        ↓
Krea2 Prompt / Conditioning
        ↓
ComfyUI
        ↓
Krea 2
```

In questo modo ComfyUI diventa **l'ambiente di orchestrazione**, CharacterForge il **progettista**, Krea 2 il **pittore**.

## La frase che riassume tutto

**CharacterForge pensa e progetta ciò che deve esistere. Il Model Adapter traduce quel progetto nel linguaggio del generatore. Krea 2 lo dipinge.**

Se domani Krea 2 non fosse più il pittore, il progetto costruito da CharacterForge non dovrebbe andare perso. Questa è probabilmente la separazione architetturale più importante da fissare adesso: costruire CharacterForge come **motore indipendente dal modello generativo**, pur utilizzando Krea 2 come primo banco di prova concreto.

---
---

# PARTE III — Pipeline inversa: da immagine a entità (Image-to-Entity Reconstruction)

Una delle evoluzioni più importanti della visione: la direzione inversa rispetto alla pipeline standard.

```text
                 OGGI (forward)
Entity strutturata
       ↓
CharacterForge
       ↓
Model Adapter
       ↓
Krea 2
       ↓
       IMAGE
```

A cui si aggiunge:

```text
                 INVERSE PIPELINE

                    IMAGE
                      ↓
              Vision Analyzer
                      ↓
          ┌───────────┴───────────┐
          │                       │
     Visual Features        Scene / Relations
          │                       │
          └───────────┬───────────┘
                      ↓
              Entity Reconstruction
                      ↓
              CharacterForge Entity
                      ↓
              Context / State
                      ↓
             Entity Specification
                      ↓
             Generation Compiler
                      ↓
              Model Adapter
                 ┌────┴────┐
               Krea2     altro
```

Non è fantascienza: esistono già tecniche di computer vision che estraggono da immagini oggetti, attributi, relazioni spaziali e strutture tipo scene graph, oltre a sistemi che ricostruiscono forma/posa umana 3D da una singola immagine.

## Una distinzione fondamentale: osservato vs stimato vs sconosciuto

Non si tratta di "ricavare l'entità esatta" in senso matematico assoluto. Da una singola immagine 2D non si può sapere con certezza ciò che non è osservabile.

Si può stimare da un'immagine frontale: altezza relativa, proporzioni visibili, forma del volto, larghezza spalle, lunghezza arti, abbigliamento, colore capelli, colore occhi, posa, illuminazione, camera, ambiente.

Non si può sapere con certezza: profondità reale del cranio, circonferenza reale della testa, forma della schiena, proporzioni nascoste, altezza reale in centimetri.

CharacterForge dovrebbe quindi distinguere:

```text
OBSERVED → ESTIMATED → INFERRED → UNKNOWN
```

Questa distinzione è **importantissima**.

## Ricostruzione con livello di confidenza per parametro

Da un'immagine, il sistema non dovrebbe produrre semplicemente un testo tipo "a woman with long brown hair...", ma costruire un'entità completa:

```text
ENTITY
└── Human
    ├── Identity (entity_id: reconstructed_001)
    ├── Anatomy
    │   ├── Height
    │   ├── BodyType
    │   ├── Proportions
    │   ├── Shoulders
    │   ├── Torso
    │   ├── Arms
    │   ├── Neck
    │   └── Head
    │       ├── Dimensions
    │       ├── Proportions
    │       └── Face (Dimensions, Proportions, Forehead, Cheeks, Jaw, Chin, Landmarks)
    ├── Appearance (Hair, Eyes, Skin, ...)
    ├── Clothing
    ├── Pose
    ├── Environment
    ├── Camera
    └── Confidence
```

Ogni parametro porta con sé `value`, `confidence`, `source`, `status`, ad esempio:

```text
shoulder_width:
    value: 0.42
    confidence: 0.91
    source: visual_estimation
    status: estimated

cranial_depth:
    value: null
    confidence: 0.00
    source: none
    status: unknown
```

## La parte davvero potente: l'immagine come sorgente di dati

Se l'immagine originale è "Persona A, vista frontale", CharacterForge la ricostruisce come entità. A quel punto, chiedere "fammi la stessa persona di profilo" non significa più chiedere a Krea "crea una donna simile...", ma comporre:

```text
ENTITY A + VIEWPOINT = PROFILE + POSE = NEUTRAL + STYLE = ORIGINAL
```

che CharacterForge compila per il Model Adapter:

```text
CharacterForge Entity → View = PROFILE → Krea2Adapter → Prompt
```

**L'immagine iniziale diventa una sorgente di dati, non semplicemente una reference image.**

## Il percorso completo: Image → Entity → Modifica → Image

```text
IMAGE → analisi → ricostruzione → CharacterForge Entity   (IMAGE → ENTITY)
Entity → modifica → Model Adapter → immagine               (ENTITY → IMAGE)

             ┌─────────────────────┐
             │                     ↓
          IMAGE ──→ ENTITY ──→ MODIFIED ENTITY
             ↑                       │
             │                       ↓
             └──── MODEL ADAPTER ←──┘
```

Molto più potente di un semplice prompt generator.

## Confronto esplicito tra versioni dell'entità

```text
ORIGINAL IMAGE → ENTITY A
CharacterForge modifica: height +5%, shoulder_width -3%, hair = blonde
                       → ENTITY B → Krea2 → GENERATED IMAGE
```

CharacterForge saprebbe **esattamente quali proprietà sono cambiate**:

```text
ENTITY A                          ENTITY B
├── height        1.72    →       ├── height        1.81   ← changed
├── shoulders     0.42    →       ├── shoulders     0.40   ← changed
├── hair          brown   →       ├── hair          blonde ← changed
└── face_shape    oval    →       └── face_shape    oval   ← preserved
```

Questo risolve uno dei problemi fondamentali della generazione AI: **modificare una cosa senza perdere le altre.**

## H4.12 è ora realtà

La milestone **H4.12 — Anatomical Coordinate & Landmark Framework** è stata completata (H4.12-A…E): il percorso `pixel → landmark → coordinate normalizzate → anatomical structure → CharacterForge parameter` ha ora la sua infrastruttura. L'analizzatore d'immagine futuro dovrà percorrere, ad esempio:

```text
IMAGE
├── left_eye, right_eye, nose_tip, mouth_center, chin
├── left_cheek, right_cheek
├── left_shoulder, right_shoulder
└── ...
          ↓
FacialLandmarks → FacialProportions → FaceDimensions
```

La ricerca attuale va anche verso rappresentazioni strutturate di questo tipo: scene graph, relazioni spaziali e rappresentazioni multimodali strutturate per la comprensione composizionale delle immagini.

## L'architettura corretta: Krea2 fuori dal cuore del sistema

Non semplicemente `ImageAnalyzer → Prompt`, ma:

```text
ImageAnalyzer
      ↓
Observation Layer
      ↓
Reconstruction Layer
      ↓
CharacterForge Entity
      ↓
Entity Validation
      ↓
Context
      ↓
Generation Compiler
      ↓
Model Adapter
```

Così Krea2 non entra nel cuore di CharacterForge: resta un semplice `Krea2Adapter`, affiancabile domani da `FLUXAdapter`, `SDXLAdapter`, `WanAdapter`, ecc.

Allo stesso modo l'analisi può essere modulare per dominio:

```text
CharacterForge Vision
├── HumanAnalyzer
├── CreatureAnalyzer
├── ObjectAnalyzer
├── VehicleAnalyzer
├── EnvironmentAnalyzer
└── SceneAnalyzer
```

Una fotografia di una Ferrari diventa un'entità `Vehicle`; una fotografia di una casa → `Building`; un'immagine di un cavallo → `Animal`; un'immagine di una spada → `Object`; un'immagine di una stanza → `Environment`. Lo stesso ciclo `IMAGE → ENTITY → MODIFY → MODEL ADAPTER → IMAGE` funzionerebbe per tutti.

## Conclusione: un sistema bidirezionale

L'ingegneria inversa dovrebbe entrare nella visione architetturale di CharacterForge non come semplice "image-to-prompt", ma come **Image-to-Entity Reconstruction**. Questo cambia il significato stesso di CharacterForge: non più soltanto un *builder* di entità, ma un sistema **bidirezionale**:

> **progetta entità → genera rappresentazioni**
> **analizza rappresentazioni → ricostruisce entità**

Direzione coerente con quanto già costruito — `Landmarks`, `Proportions`, `Dimensions` — e con il sistema di coordinate ora costruito (H4.12-A…E).
---
---

# PARTE IV — Origine e scopo (il caso d'uso "Human")

## Da dove nasce CharacterForge

CharacterForge nasce da un problema concreto incontrato lavorando con la generazione d'immagini e con ComfyUI:

**i modelli generativi sono bravissimi a produrre immagini, ma non possiedono necessariamente una rappresentazione strutturata dell'entità che stanno rappresentando.**

Si può dire a un modello "crea questo personaggio, con questa corporatura, questo volto, queste mani, questa età apparente, questa posizione…" e ottenere una bella immagine. Ma quando si vuole poi:

- cambiare soltanto la larghezza delle spalle;
- mantenere identico il volto;
- modificare il peso senza alterare l'identità;
- cambiare la prospettiva;
- generare fronte, profilo e tre quarti;
- mantenere le proporzioni;
- cambiare un elemento anatomico preciso;
- trasformare il personaggio;
- produrre una reference sheet coerente;
- riutilizzare quello stesso asset mesi dopo;

il semplice prompt diventa una rappresentazione troppo debole.

Da qui l'idea fondamentale: **prima costruire l'entità in modo strutturato, poi generare le immagini che la rappresentano.** Non partire dall'immagine. Partire dal **modello dell'oggetto/personaggio**.

## Che cos'è veramente CharacterForge

Un **motore semantico, parametrico e morfologico per la costruzione di entità visive**:

```text
ENTITY
│
├── Identity
├── State
├── Variant
├── Transformation
│
├── Structure
│   ├── Anatomy
│   ├── Morphology
│   ├── Dimensions
│   └── Proportions
│
├── Appearance
│   ├── Skin
│   ├── Hair
│   ├── Eyes
│   ├── Clothing
│   └── Materials
│
├── Geometry
│   ├── Coordinates
│   ├── Landmarks
│   ├── Measurements
│   ├── Angles
│   ├── Planes
│   └── Deformations
│
├── Environment
├── Time
├── Weather
├── Viewpoint
│
└── Reference Sheet
```

Non semplicemente **"un generatore di personaggi"**, ma un tentativo di costruire una **rappresentazione digitale strutturata dell'entità**.

## Il problema fondamentale che vuole risolvere

Il problema più grande è la **perdita di identità e coerenza**. Oggi, in un workflow generativo: prompt → immagine, poi prompt modificato → nuova immagine, e la seconda può differire dalla prima in modi non richiesti.

CharacterForge introduce: entità strutturata → parametri → stato → vista → generazione. **L'immagine non è più l'entità**: è una **rappresentazione dell'entità**. Questa distinzione è probabilmente la parte più importante dell'intero progetto.

## Quali problemi vuole risolvere definitivamente

### 1. Incoerenza anatomica

Un generatore può produrre braccia di lunghezza diversa, mani incoerenti, proporzioni che cambiano, volto differente, spalle diverse, corporatura instabile. Da qui la struttura anatomica esplicita `HumanAnatomy` e poi `Head → Face` morfometrico (dettagli in Parte V).

### 2. Perdere l'identità del personaggio

Come dire che un volto appartiene allo stesso asset della generazione precedente? Da qui la distinzione tra `Identity`, `State`, `Variant`, `Transformation`:

```text
Personaggio A
├── Identity: A
├── Variant: casual
├── State: sorridente
├── Transformation: ferito
└── View: profile
```

L'identità rimane la stessa; cambiano stato, variante, trasformazione o vista.

### 3. Il problema delle Reference Sheet

Le viste devono derivare dallo stesso modello parametrico: non quattro personaggi simili, ma un personaggio visto da quattro direzioni.

### 4. Il problema delle proporzioni

Molte proporzioni oggi rimangono implicite: il progetto le rende dati espliciti (`HeadDimensions`, `HeadProportions`) — descrizione quantitativa, non solo linguistica.

### 5. Il problema della bilateralità

`left_cheek`/`right_cheek`, `left_jaw`/`right_jaw` con `BodySide.LEFT`/`BodySide.RIGHT` esplicito — permette di rappresentare anche l'**asimmetria**, invece di un volto matematicamente perfetto.

### 6. Il problema della morfometria

Progressione concettuale: descrizione → componente semantico → misura → proporzione → landmark → coordinate → relazione geometrica → trasformazione → geometria. Con H4.12 questa progressione ha la sua infrastruttura completa (coordinate, relazioni, grafo, misure, piani); con H4.13 la derivazione morfometrica chiude il cerchio (misure → dimensioni → proporzioni derivate).

### 7. Il problema delle modifiche indipendenti

"Aumenta altezza" senza modificare casualmente identità, volto, mani, colore occhi, abbigliamento; "riduci body fat" mantenendo struttura scheletrica, altezza, identità, proporzioni fondamentali — realizzato in **H4.14**: contratto changed/preserved, operatori top-down e bottom-up con equivalenza provata.

### 8. Il problema della dipendenza dai prompt

Il prompting va spostato al livello giusto: struttura esplicita (`height`, `body_type`, `musculature`, `body_fat`, `head_dimensions`, `face_dimensions`...) tradotta poi nella rappresentazione per il modello generativo. Il prompt diventa **un output della descrizione strutturata**, non l'unica fonte di verità (vedi anche il Prompt Compiler in Parte II).

## Il Custom Node per ComfyUI

Nato anche come **custom node pack per ComfyUI** (`ComfyUI/custom_nodes/ComfyUI-CharacterForge`), coerente con l'estensibilità di ComfyUI tramite custom node (schema input, funzione di esecuzione, output, registrazione del nodo).

Non un semplice nodo `CharacterForge → IMAGE` (troppo limitante). Direzione:

```text
                    ┌─────────────────────┐
                    │  CharacterForge     │
                    │      Builder        │
                    └──────────┬──────────┘
                               │
                     ENTITY / CHARACTER
                               │
          ┌────────────────────┼────────────────────┐
          ↓                    ↓                    ↓
       Anatomy             Appearance          Environment
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ↓
                         TRANSFORM
                               ↓
                         VIEWPOINT
                               ↓
                       REFERENCE SHEET
                               ↓
                    ComfyUI generation nodes
```

CharacterForge diventerebbe **lo strato strutturale che precede la generazione**. ComfyUI è già costruito attorno a una logica a grafo, adatta a: Builder → Semantic Entity → Anatomy → Morphology → Appearance → Camera/View → Conditioning → Generation, inseribile dentro workflow più grandi.

## La vera idea, in sintesi

> **CharacterForge nasce dalla necessità di trasformare il personaggio generato da un'immagine fragile e dipendente dal prompt in un'entità digitale strutturata, parametrica, modificabile e riutilizzabile.**

Il **Custom Node è l'interfaccia di CharacterForge dentro ComfyUI**. Ma **CharacterForge non è il nodo** — il nodo è il punto d'ingresso. Il vero progetto è il **motore di rappresentazione e costruzione dell'entità** costruito dietro quel nodo: da qui il percorso dall'anatomia (`HeadDimensions`, `HeadProportions`, `FacialLandmarks`) verso la struttura di coordinate — il fondamento che permette al sistema di sapere **che cosa sta costruendo, quali proprietà possiede, quali relazioni le legano e come una trasformazione dovrebbe propagarsi senza distruggere il resto dell'asset**.

---
---

# PARTE V — Stato tecnico attuale (H4.15)

Siamo arrivati alla **H4.15** del ramo Human Engine. Il repository è **sincronizzato con origin/main**: i capitoli da H4.12 a H4.15 sono stati pushati.

```text
main
└── sincronizzato con origin/main
    └── working tree CLEAN
```

L'ultima milestone chiusa è: **H4.15 — Lower Body** ✅

I capitoli H4.12, H4.13, H4.14 e H4.15, chiusi in sottosezioni:

```text
H4.12-A  CoordinateSpace / Coordinate / CoordinateSystem / Landmark   b3cf564
H4.12-B  LandmarkRelation                                             c5b560e
H4.12-C  LandmarkGraph                                                38a7828
H4.12-D  LandmarkGeometry (distanze / offset / angoli)                766a9f9
H4.12-E  AnatomicalPlane (semantica + geometria dei piani)            f5d48d3
H4.13-A  FacialMorphometry (misure → dimensioni → proporzioni)      be36725
H4.13-B  HeadMorphometry (FaceDimensions → HeadDimensions)          7bd554f
H4.13-C  CranialLandmarks / cranio interamente derivabile     8de9481
H4.14-A  ModifyOperation / ModifyResult (contratto)         67eb4f7
H4.14-B  Operatori facciali top-down                       426160d
H4.14-C  Operatori cranici + invarianza facciale           281592c
H4.14-D  Operatori landmark bottom-up                      a9b36a2
H4.15-A  Pelvis + segmenti (Thigh/Knee/LowerLeg/Ankle)     80debd5
H4.15-B  Toe/Foot/Leg/Legs bilaterali + integrazione       2250c39
```

## 1. Architettura generale raggiunta

```text
CharacterForge
│
├── Core / Domain
│   ├── Entity
│   ├── Identity
│   ├── State
│   ├── Variant
│   ├── Transformation
│   ├── Metadata
│   └── Registry / Contracts
│
├── Human Engine
│   │
│   ├── Human
│   │   ├── Identity
│   │   ├── Demographics
│   │   └── Anatomy
│   │
│   └── Anatomy
│       ├── Body structure
│       ├── Upper limbs
│       ├── Hands
│       ├── Shoulders
│       ├── Neck
│       ├── Thorax
│       ├── Mammary region
│       ├── Head / Face morphometrics
│       ├── Lower limbs (pelvis, gambe, piedi)
│       ├── Landmark framework (coordinate, relazioni, grafo, geometria, piani)
│       ├── Morphometric derivation (misure → dimensioni → proporzioni derivate, cranio compreso)
│       └── Parametric modification (contratto changed/preserved + operatori top-down/bottom-up)
│
├── Cinematic
├── Reference Sheets
├── Builders
├── Controllers
└── future generation / transformation systems
```

## 2. Core semantico

```text
Entity
├── Identity
├── State
├── Variant
├── Transformation
└── Metadata
```

- l'identità non venga confusa con lo stato;
- una variante non sia una nuova identità;
- una trasformazione possa modificare lo stato;
- gli oggetti siano rappresentati semanticamente;
- la serializzazione sia deterministica e verificabile;
- i contratti impediscano strutture incoerenti.

Registry e contract già presenti per gli entity type: base per gestire in futuro `Human`, `Creature`, `Animal`, `Object`, `Vehicle`, `Building`, `Environment` con lo stesso modello concettuale.

## 3. Human Engine

```text
Human
├── Identity
├── Demographics
│   ├── Age
│   ├── Sex
│   ├── Gender
│   ├── Ethnicity
│   ├── Ancestry
│   └── PopulationTraits
└── Anatomy
```

Classi semantiche vere, non dizionari di proprietà. Principio guida: se qualcosa rappresenta un concetto importante del dominio, deve essere un oggetto del dominio.

## 4. Human Anatomy — struttura corporea

```text
HumanAnatomy
├── BodyType
├── Height
├── Proportions
├── Musculature
├── BodyFat
├── Neck
├── Shoulders
├── Torso
├── Chest
├── RibCage
├── Back
└── Arms
```

## 5. Arti superiori

```text
Arms
├── UpperArm
├── Elbow
├── Forearm
├── Wrist
└── Hands
    ├── Left Hand (Palm, Fingers: Thumb, Index, Middle, Ring, Little)
    └── Right Hand (Palm, Fingers: Thumb, Index, Middle, Ring, Little)
```

Ogni dito possiede il proprio `Nail`. `BodySide.LEFT`/`BodySide.RIGHT` con struttura bilaterale verificata.

## 6. Spalle

```text
Shoulders
├── left: Shoulder
└── right: Shoulder
```

Parametri: width, height, depth, slope, muscularity, shape, side.

## 7. Collo

`Neck`: length, circumference, width, depth, shape.

## 8. Torace

`Torso`, `Chest`, `RibCage`, `Back` — scomposizione semantica del tronco.

## 9. Regione mammaria (H4.8)

```text
MammaryRegion
├── left: BreastUnit (Breast, Areola, Nipple)
└── right: BreastUnit (Breast, Areola, Nipple)
```

Con bilateralità, volume, dimensioni, proiezione, forma, posizione, orientamento, pienezza regionale, consistenza, asimmetria.

## 10. Head

H4.7/H4.9: `Head → Face`. H4.11: modello dimensionale e proporzionale. H4.12: framework di landmark.

```text
Head
├── HeadDimensions
├── HeadProportions
└── Face
```

## 11. Face

```text
Face
├── FaceDimensions
├── FacialProportions
├── Forehead
├── CheekStructure (left, right)
├── Jaw (left, right)
├── Chin
├── FacialSymmetry
└── FacialLandmarks
```

## 12. FaceDimensions

facial height/width/depth, upper/mid/lower face height, forehead width, bizygomatic width, bigonial width, jaw width, chin width, chin height. Distingue dimensione, forma, proporzione.

## 13. FacialProportions

`upper_to_mid_ratio`, `mid_to_lower_ratio`, `width_to_height_ratio`, `forehead_to_cheek_ratio`, `cheek_to_jaw_ratio`, `jaw_to_chin_ratio`. **Nota H4.10 — chiusa in H4.13-A:** le proporzioni sono ora derivabili dalle dimensioni tramite `facial_proportions_from_dimensions`.

## 14. Forehead

height, width, projection, slope, curvature, temporal width, shape (flat, average, rounded, sloped, prominent, receding), symmetry.

## 15. Guance / zigomi

`CheekStructure` bilaterale: width, projection, height, lateral projection, anterior projection, vertical position, prominence, shape.

## 16. Mandibola

`Jaw` bilaterale: width, height, depth, angle, projection, ramus height, ramus width, gonial angle, shape.

## 17. Mento

`Chin`: width, height, projection, depth, vertical position, shape (narrow, average, broad, round, square, pointed, prominent, receding), symmetry.

## 18. Simmetria facciale

`FacialSymmetry`: global_symmetry, upper_face, mid_face, lower_face, left_right_alignment — normalizzati a `0..1`.

## 19. Facial Landmarks

trichion, glabella, nasion, pronasale, subnasale, labiale_superius, stomion, labiale_inferius, gnathion, left/right zygion, left/right gonion, left/right endocanthion, left/right exocanthion, left/right cheilion — coordinate `(x, y, z)` normalizzate.

## 20. HeadDimensions (H4.11)

cranial height/width/depth/length/breadth/circumference, neurocranial height, facial height, bizygomatic width, bigonial width.

## 21. HeadProportions (H4.11)

cephalic index, cranial height/width, cranial depth/width, face/head height, face/head width, neurocranium/face height, bizygomatic/bigonial.

```text
Head
├── dimensional model
├── proportional model
└── facial model
```

## 22. H4.12-A — Coordinate, spazi, sistemi e Landmark

```text
CoordinateSpace (Enum)
├── IMAGE_2D        → 2 dimensioni
├── NORMALIZED_3D   → 3 dimensioni
└── PHYSICAL_3D     → 3 dimensioni
    └── property dimensions

Coordinate
├── x, y, z (z vietata in 2D, obbligatoria in 3D)
├── space (CoordinateSpace)
├── system (CoordinateSystem | None)
└── valori finiti obbligatori

CoordinateSystem
├── spazio + origine + orientamento semantici
└── classmethod anatomical_normalized()

Landmark (AnatomyComponent)
├── name (identificatore testuale)
├── coordinate (Coordinate)
├── side (BodySide | None)
├── status: OBSERVED / ESTIMATED / INFERRED / UNKNOWN
├── confidence: 0..1
└── source: MANUAL / MODEL / VISION / CALCULATED / IMPORTED
```

Lo status epistemico realizza la distinzione OBSERVED → ESTIMATED → INFERRED → UNKNOWN della Parte III.

## 23. H4.12-B — LandmarkRelation

```text
LandmarkRelation (AnatomyComponent)
├── landmark_a, landmark_b (identificatori testuali, non oggetti)
├── relation_type: DISTANCE / ANGLE / HORIZONTAL_OFFSET / VERTICAL_OFFSET / DEPTH_OFFSET
├── value (numerica finita o None; DISTANCE >= 0)
├── unit (stringa non vuota o None)
└── directed (bool, default False)
```

Gli endpoint sono identificatori testuali: la relazione resta leggera, serializzabile e pronta per una futura rappresentazione a grafo.

## 24. H4.12-C — LandmarkGraph

```text
LandmarkGraph (AnatomyComponent)
├── landmarks: unici per nome (duplicato → ValueError)
├── relations: solo tra landmark presenti (endpoint sconosciuto → ValueError)
├── relazioni duplicate respinte (inclusi gli specchi non-diretti)
├── coordinate_system (opzionale): vincola lo spazio delle coordinate
└── to_dict(): landmark ordinati per nome → serializzazione deterministica
```

## 25. H4.12-D — LandmarkGeometry

```text
euclidean_distance(a, b)           → distanza euclidea 2D/3D
horizontal_offset(a, b)            → offset con segno (x)
vertical_offset(a, b)              → offset con segno (y)
depth_offset(a, b)                 → offset con segno (z), solo 3D
angle_at_vertex(a, vertex, b)      → angolo in gradi al vertice
computed_relation(lm_a, lm_b, t)   → LandmarkRelation con value calcolata
```

`computed_relation` è il ponte geometria → semantica: la misura non si dichiara a mano, si calcola. Le relazioni ANGLE a due endpoint sono respinte (richiedono il vertice: estensione futura del modello relazioni).

Esempi dimostrati nei test:

```text
left_zygion ↔ right_zygion → bizygomatic width = 0.28 (calcolata)
glabella → nasion          → vertical offset = +0.04 (calcolato)
endocanthion L / nasion / endocanthion R → angolo nasionale (calcolato)
```

## 26. H4.12-E — AnatomicalPlane e geometria dei piani

```text
AnatomicalPlaneType
├── MID_SAGITTAL / CORONAL / AXIAL   (piani standard: definiti dal sistema, nessun landmark)
└── FRANKFURT / LANDMARK_DEFINED     (piani di riferimento: esattamente 3 landmark distinti)

landmark_geometry
├── plane_normal(a, b, c)                → normale unitaria (right-hand rule); collineari → ValueError; solo 3D
├── signed_distance_to_plane(p, a, b, c) → distanza con segno dal piano
└── is_on_plane(p, a, b, c, tolerance)   → appartenenza con tolleranza
```

Applicazioni dimostrate nei test: simmetria bilaterale rispetto al mid-sagittal (`left_zygion` −0.14 / `right_zygion` +0.14), piano di Frankfurt end-to-end nel grafo.

## 27. H4.13-A — Facial Morphometric Derivation

```text
facial_morphometry.py
├── FacialMeasurements (AnatomyComponent)
│   └── 11 misure normalizzate: facial_height, terzi (upper/mid/lower),
│       chin_height, bizygomatic, bigonial, eye_inner/eye_outer,
│       mouth_width, facial_depth
├── facial_measurements(FacialLandmarks) → FacialMeasurements
│   └── 15 landmark richiesti; i mancanti sono elencati nel ValueError
├── facial_scale_factor(measurements, target_height) → scala normalizzato→fisico
├── face_dimensions_from_measurements(m, scale, *, forehead_width, chin_width)
│   └── forehead_width e chin_width: fallback fisici NON derivabili dai landmark
└── facial_proportions_from_dimensions(FaceDimensions) → FacialProportions
    └── le 6 proporzioni DERIVATE — chiude la nota H4.10 (sezione 13)
```

Convenzioni documentate nel modulo: misure verticali con |Δy| (terzi additivi: upper + mid + lower = facial_height), larghezze bilaterali con distanza euclidea 3D, profondità facciale come range z. `facial_width := bizygomatic`, `jaw_width := bigonial`. Le proporzioni puramente geometriche sono invarianti di scala; le due che coinvolgono i fallback fisici (forehead_to_cheek, jaw_to_chin) sono scale-dipendenti — proprietà di design documentata e testata esplicitamente.

## 28. H4.13-B — Head Morphometric Derivation

```text
head_morphometry.py
├── head_dimensions_from_face_dimensions(face_dimensions, *, fallback cranici)
│   ├── iniettati dal FaceDimensions: facial_height, bizygomatic, bigonial
│   ├── cranial_length := cranial_depth; cranial_breadth := cranial_width
│   └── fallback cranici: cranial_height/width/depth/circumference,
│       neurocranial_height (i landmark facciali NON coprono il neurocranio)
└── head_proportions_from_dimensions(HeadDimensions) → HeadProportions
    ├── cephalic_index = cranial_breadth / cranial_length × 100 (formula classica)
    └── cranial_height_to_width legge neurocranial_height (13/15 → 0.87, default H4.11)
```

Catena completa: `FacialLandmarks → FacialMeasurements → FaceDimensions → HeadDimensions → HeadProportions` (più `FacialProportions` dal FaceDimensions). Sei delle sette proporzioni dichiarate in H4.11 sono i rapporti dei default arrotondati a due decimali; il default `cephalic_index` 78.0 è la media tabellare mesocefalica (il valore derivato dai default dimensionali è 78.95).

Il percorso fallback è legacy: con landmark cranici disponibili, H4.13-C (sezione 29) deriva il cranio per intero.

## 29. H4.13-C — Cranial Landmark Coverage

```text
cranial_landmarks.py
└── CranialLandmarks — separato da FacialLandmarks: normalizzato al
    bounding box della TESTA (non del viso). 10 punti validi:
    vertex, euryon L/R, opisthocranion, porion L/R, orbitale L/R,
    glabella, nasion. 8 richiesti per la derivazione.

head_morphometry.py (estensione H4.13-C)
├── CranialMeasurements (AnatomyComponent)
├── cranial_measurements(CranialLandmarks)
│   ├── cranial_width  = euryon↔euryon (euclidea 3D)
│   ├── cranial_length = glabella→opisthocranion (depth := length)
│   ├── neurocranial_height = distanza perpendicolare del vertex
│   │   dal piano di FRANKFURT (porion L/R + orbitale): la
│   │   geometria dei piani H4.12-E diventa strumento di misura
│   └── cranial_circumference ≈ perimetro ellittico di Ramanujan
│       costruito su width e length
├── cranial_scale_factor(m, target_cranial_length)
└── head_dimensions_from_cranial_measurements(FaceDimensions, m, scale)
    ├── cranio interamente DERIVATO: width/depth/length/breadth/
    │   circumference/neurocranial_height dalle misure scalate
    ├── cranial_height (vertex→menton) non misurabile dal solo set
    │   cranico: approssimata come neurocranial + facial, o esplicita
    └── head_dimensions_from_face_dimensions resta come percorso
        LEGACY (fallback H4.13-B, nessun refactor distruttivo)
```

I due set di landmark vivono in normalizzazioni DIVERSE (bounding box del viso vs della testa): ciascuno viene scalato ai valori fisici col proprio fattore, e il modello combinato è coerente perché entrambi i lati convergono nelle stesse unità fisiche.

Con H4.13-C l'intera testa è derivabile dai punti anatomici: nel percorso landmark → misure → dimensioni → proporzioni non sopravvive alcun valore dichiarato a mano (restano come eccezioni documentate le larghezze frontale/mentale facciali e l'altezza totale del cranio, non misurabile senza il menton).

## 30. H4.14 — Parametric Builder (A→D)

```text
modify.py — il CONTRATTO
├── PropertyChange: una transizione (name, before, after, changed)
│   con tolleranza esplicita per i confronti float
├── ModifyResult: il report semantico — changes[] + preserved[]
│   └── contratto duro: change dichiarata = change reale;
│       nomi unici; changed ∩ preserved = ∅
└── diff_properties(before, after, names, *, operation)
    └── generatore automatico del diff tra componenti

facial_modify.py / head_modify.py — operatori TOP-DOWN
├── modify_face_dimensions / modify_head_dimensions (deltas espliciti)
├── wrapper con PROPAGAZIONE DICHIARATA:
│     widen_bizygomatic → bizygomatic + facial_width
│     widen_jaw → bigonial + jaw_width
│     widen_cranial → width + breadth + CIRCONFERENZA ricalcolata (Ramanujan)
│     lengthen_cranial → depth + length + circonferenza
│     adjust_neurocranial_height → solo la volta
├── proporzioni RIDERIVATE automaticamente (catena H4.13)
└── INVARIANZA INCROCIATA: gli operatori cranici non toccano mai
    il volto — e i report lo certificano

landmark_modify.py — operatori BOTTOM-UP
├── modify_facial_landmarks / modify_cranial_landmarks:
│     muovono punti (dx, dy, dz) → la catena H4.13 si ri-esegue
├── wrapper: widen_zygions, lower_gnathion, advance_pronasale,
│     widen_euryons
├── scala fisica ANCORATA al modello originale
└── report a TRE livelli: landmark / dimensioni / proporzioni
```

EQUIVALENZA PROVATA: top-down e bottom-up producono lo stesso modello — `widen_zygions` ≡ `widen_bizygomatic`, `widen_euryons` ≡ `widen_cranial` (circonferenza inclusa). La narrazione della Parte III — ENTITY A → ENTITY B sapendo esattamente cosa è cambiato e cosa è sopravvissuto — è ora codice eseguito e testato.

## 31. H4.15 — Lower Body Anatomy (A→B)

```text
H4.15-A — Pelvis e segmenti dell'arto inferiore
├── Pelvis: width/depth/circumference, tilt ±20°, shape, iliac_flare
├── Thigh: length 44 / circumference 56, shape
├── Knee: side, flexion 0-150°, rotation ±45°, width/circumference/prominence
├── LowerLeg: length 42 / circumference 36, calf_prominence
└── Ankle: side, flexion 0-60°, extension 0-30°, deviation ±30°

H4.15-B — Piedi, gambe bilaterali e integrazione
├── ToeType (HALLUX..FIFTH) + Toe (riusa Nail)
├── Foot: side, dimensioni, arch, heel/ball width, dict[ToeType, Toe] completo
├── Leg: side + thigh/knee/lower_leg/ankle/foot con SIDE-MATCHING
├── Legs: pattern bilaterale forte, validazione incrociata left/right
└── HumanAnatomy: + pelvis, + legs (opzionali, backward compatible)
```

Nota di design: a differenza del modello upper-limb (segmenti condivisi tra le due braccia), ogni gamba possiede i propri segmenti e le proprie articolazioni, col side verificato in cascata — la bilateralità è completa e l'asimmetria resta rappresentabile.

## 32. Sistema di validazione

```text
AnatomyComponent → SemanticComponent → CharacterForgeObject
```

Contratto: `validate()` **solleva ValueError**, `is_valid()` la cattura e restituisce bool. Validazione eager in `__init__` + ri-validabile dopo mutazione. Esempi: `dimensione <= 0 → ValueError`; `BodySide.RIGHT assegnato a left_cheek → ValueError`; endpoint sconosciuto in una relazione → `ValueError`.

Nota di sviluppo: durante H4.12-B il primo abbozzo restituiva una lista di errori invece di sollevare `ValueError`, rompendo il contratto della gerarchia; corretto prima del commit. Lezione: il contratto di validazione del progetto è a eccezioni.

## 33. Test e procedura canonica

Python di riferimento per sviluppo e test: **il venv di ComfyUI** — `D:\AVVIO PULITO di ComfyUI\ComfyUI\venv\Scripts\python.exe` (Python 3.12.10, pytest 9.1.1). Il Python 3.14 globale non ha pytest e non deve essere usato.

```text
regressione unittest : python -m unittest discover -s tests -p "test_*.py"  → Ran 196 tests OK
suite pytest         : 5 suite storiche + H4.12-B/C/D/E + H4.13-A/B/C + H4.14-A/B/C/D + H4.15-A/B → 404 passed
TOTALE TEST UNICI   : 600 verdi
```

- H4.10: 14 test → OK
- H4.11: 6 test → OK
- H4.12-A: 12 test → OK (unittest)
- H4.12-B: 14 test → OK (pytest)
- H4.12-C: 17 test → OK (pytest)
- H4.12-D: 26 test → OK (pytest)
- H4.12-E: 23 test → OK (pytest)
- H4.13-A: 21 test → OK (pytest)
- H4.13-B: 14 test → OK (pytest)
- H4.13-C: 19 test → OK (pytest)
- H4.14-A: 22 test → OK (pytest)
- H4.14-B: 25 test → OK (pytest)
- H4.14-C: 23 test → OK (pytest)
- H4.14-D: 27 test → OK (pytest)
- H4.15-A: 30 test → OK (pytest)
- H4.15-B: 32 test → OK (pytest)

Totale capitolo H4.12: **92 test**. Totale capitolo H4.13: **54 test**. Totale capitolo H4.14: **97 test**. Totale capitolo H4.15: **62 test**.

Nota storica: i 5 errori di import `No module named 'pytest'` documentati fino a H4.11 nascevano dall'uso del Python 3.14 globale; con il venv di ComfyUI l'intera suite gira senza errori. Da H4.12 in poi la procedura canonica usa il venv.

## 34. Git

Ultimo checkpoint: **H4.15-B** — commit `feat(human): add H4.15-B feet legs bilateral model and anatomy integration` (`2250c39`).

```text
main
↑ 0 commit locali rispetto a origin/main (sincronizzato)
working tree clean
```

Commit dei capitoli H4.12 / H4.13 / H4.14 / H4.15:

```text
2250c39 feat(human): add H4.15-B feet legs bilateral model and anatomy integration
80debd5 feat(human): add H4.15-A pelvis and lower limb segments
a9b36a2 feat(human): add H4.14-D landmark modification operators
281592c feat(human): add H4.14-C cranial modification operators with facial invariance
426160d feat(human): add H4.14-B facial modification operators
67eb4f7 feat(human): add H4.14-A modify operation contract
8de9481 feat(human): add H4.13-C cranial landmark coverage
7bd554f feat(human): add H4.13-B head morphometric derivation
be36725 feat(human): add H4.13-A facial morphometric derivation
f5d48d3 feat(human): add H4.12-E anatomical planes
766a9f9 feat(human): add H4.12-D landmark geometry measurements
38a7828 feat(human): add H4.12-C landmark graph container
c5b560e feat(human): add H4.12-B landmark relation component
b3cf564 feat(human): add H4.12-A coordinate and landmark foundation
```

I capitoli da H4.12 a H4.15 e il documento della visione sono stati pushati su `origin/main`.

## 35. Dove NON siamo ancora arrivati

Le fondamenta geometriche, la derivazione morfometrica, la modifica parametrica e il lower body esistono ora (coordinate, grafo, misure, piani, proporzioni derivate, operatori changed/preserved, corpo completo fino ai piedi), ma CharacterForge **non è ancora un generatore 3D anatomico** — e l'anatomia non è ancora totale (mancano orecchie, naso e bocca come componenti). Mancano:

```text
3D representation
→ Reference Sheet generation
→ Consistent image generation
→ Vision analyzers (Image → Entity)
→ Generation Compiler
→ Model Adapters
```

## 36. Il salto concettuale successivo

Fino a H4.11: **"CHE COS'È una parte anatomica?"** Con H4.12: **"DOVE SI TROVA e COME SI RELAZIONA alle altre parti?"** Con H4.13: **"COME SI DERIVA una misura da un'altra?"** — e la risposta è nel codice.

```text
left_zygion ↔ right_zygion → bizygomatic width (calcolata, H4.12-D)
→ FaceDimensions.bizygomatic_width (derivata, H4.13-A)
→ HeadDimensions.bizygomatic_width (derivata, H4.13-B)
→ FacialProportions / HeadProportions (derivate, H4.13-A/B)

vertex / euryon↔euryon / glabella→opisthocranion → misure craniche (H4.13-C)
→ HeadDimensions craniali complete (derivate, H4.13-C, piano Frankfurt reale)

move zygion ±δ (H4.14-D, bottom-up) ≡ widen_bizygomatic (H4.14-B, top-down)
→ stesso modello: equivalenza provata, report changed/preserved certificato
```

La catena completa `FacialLandmarks → FacialMeasurements → FaceDimensions → HeadDimensions → HeadProportions` (più `FacialProportions` dal FaceDimensions) chiude il cerchio semantica ↔ geometria e realizza la nota della sezione 13. Con H4.14: **"COME SI PROPAGA una modifica?"** — e la risposta è codice con report a tre livelli. Con H4.15 il corpo è completo dalla testa ai piedi. Prossimo: chiudere le componenti anatomiche residue (orecchie, naso, bocca) o il salto verso **H5 — Appearance**.

## 37. In sintesi — percorso fatto

```text
FASE 1  Core semantico
FASE 2  Human Entity
FASE 3  Demographics
FASE 4  Human Anatomy
H4.4    Hands / Fingers / Nails
H4.5    Shoulders
H4.6    Neck
H4.7    Head + Chest + RibCage + Back
H4.8    Mammary Region
H4.9    Head → Face
H4.10   Facial Morphometric Core
H4.11   Head Morphometric Core
H4.12   Anatomical Coordinate & Landmark Framework (A→E)   ← CHIUSA
H4.13   Morphometric Derivation (A→C)                      ← CHIUSA
H4.14   Parametric Builder (A→D)                          ← CHIUSA
H4.15   Lower Body (A→B)                                  ← CHIUSA
```

H4.12 ha costruito il ponte tra **modello anatomico semantico** e **modello geometrico parametrico**: ora esiste. H4.13 lo ha reso percorribile in entrambe le direzioni: le proporzioni non si dichiarano più, si derivano — cranio compreso. H4.14 lo ha reso reversibile e verificabile: ogni modifica torna con il certificato di cosa è cambiato e cosa è sopravvissuto.

## 38. Roadmap estesa oltre H4.15

```text
H4  HUMAN ANATOMY
│
├── H4.13 Morphometric derivation (proporzioni/dimensioni derivate)   ✅
├── H4.14 Parametric builder / propagazione delle modifiche     ✅
├── H4.15 Lower body (pelvis, gambe, piedi)                  ✅
└── completamento Human Anatomy (restano: orecchie, naso, bocca)
        ↓
H5  APPEARANCE
        ↓
H6  CLOTHING
        ↓
H7  IDENTITY / VARIANTS / STATES
        ↓
H8  ENVIRONMENT / CONTEXT
        ↓
H9  CAMERA / VIEW / REFERENCE SHEETS
        ↓
H10 GENERATION COMPILER
        ↓
H11 MODEL ADAPTERS
        ├── Krea2Adapter
        ├── ...
        ↓
H12 VISION / IMAGE-TO-ENTITY
        ↓
H13 SCENE / RELATIONSHIPS
```

## 39. Il punto fondamentale del progetto, in una frase

All'inizio si stava costruendo un **Character Generator**. Ora la visione è diventata:

> **CharacterForge = motore strutturato per progettare, rappresentare, modificare, ricostruire e infine generare entità visive.**

Con le due direzioni ormai chiarite (vedi Parte II e Parte III):

```text
              CHARACTERFORGE

       IMAGE ───────────────→ ENTITY
        ↑                       │
        │                       │
        │                       ↓
      IMAGE ←──── ADAPTER ←── ENTITY
```

E con H4.12, H4.13, H4.14 e H4.15 chiuse, l'infrastruttura geometrica, morfometrica e parametrica che serve a **entrambe** le direzioni — generazione controllata e futuro percorso Image → Entity — è al suo posto: il modello si descrive, si deriva, si modifica con verifica — e ora ha anche le gambe per stare in piedi.