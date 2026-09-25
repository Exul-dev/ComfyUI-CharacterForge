# CharacterForge — Visione, architettura di generazione, origine e stato tecnico (H5-D)

> Documento di riferimento del progetto: visione globale, architettura di generazione, origine e stato tecnico. Aggiornato a **H5-D — The Complete Hair System** (chiusa, D-1/D-2/D-3). Il sistema-peli è completo: H4, H5 e H5-D chiuse.

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

Oggi: **H5-D — pieno controllo su calvizie, acconciature e peli** ✅ (scalpo, barba, corpo). Poi, progressivamente:

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

# PARTE V — Stato tecnico attuale (H5-D)

Siamo arrivati alla **H5-D** del ramo Human Engine. Il repository è **sincronizzato con origin/main**: i capitoli da H4.12 a H5, i completamenti anatomici post-H5 e il sistema-peli completo H5-D sono stati pushati.

```text
main
└── sincronizzato con origin/main
    └── working tree CLEAN
```

L'ultima milestone chiusa è: **H5-D — The Complete Hair System** ✅

I capitoli da H4.12 a H5, i completamenti anatomici post-H5 e H5-D (sistema-peli), chiusi in sottosezioni:

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
H4.16-A  Ear/Ears bilaterali + Nose + Mouth/Philtrum            92752e8
H4.16-B  Waist + Abdomen + fix Torso a cm reali                6c745d8
H4.16-C  Rimozione backup tracciati + .gitignore                604d16e
H4.17   Arm/Arms dual-mode (bilateralità totale)            31a4ed7
H5-A    Skin (SemanticComponent, standard stretto)          0aafb31
H5-B    Hair (bald ortogonale, graded strict)                a12c135
H5-C    Eyes bilaterali (eterocromia emergente)              ba2b284
H4.18-A  Hip/Hips + Glutei + pelvis composito                5abd50f
H4.18-B  Fianchi + cosce/gambe arricchite (4→8)              58e244b
H4.18-C  Ginocchia dettagliate + tallone strutturale         65dc7f2
H4.18-D  Head + MammaryRegion cablati (la testa!)            35e95c9
H4.19-A  Bocca interna + palpebre + sopracciglia             92a8ebc
H4.19-B  Tronco anteriore completo                           4da60fd
H4.19-C  Schiena dettagliata + pomo d'Adamo                 149915c
H4.19-D  Parità arti + malleoli + nocche + vascularity       bc78c84
H4.20   Sistema riproduttivo componibile (bias corretto)     b043086
H5-D-1  Scalpo: calvizie mediche + stili + fatture        87429ae
H5-D-2  Barba per regioni con preset-factory              8b68950
H5-D-3  Corpo per regioni + parita arti 9x4               6820c60
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
│   │   ├── Anatomy (dettaglio estremo: censimento 31/31)
│   │   └── Appearance (skin, hair, eyes)
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
│       ├── Trunk completo (waist, abdomen, torso a cm reali)
│       ├── Volto completo (nose, mouth, ears bilaterali)
│       ├── Arti superiori bilaterali (Arm/Arms dual-mode)
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

## 32. H4.16 — Anatomy Completion (A→C)

```text
H4.16-A — Volto completo
├── Ear: side OBBLIGATORIO, length/width, protrusion, lobe (size/attachment),
│   shape, prominence — aggancio landmark: porion
├── Ears: bilaterale forte (pattern Legs, non Arms), asimmetria rappresentabile
├── Nose: height/width/projection, bridge (flat/straight/convex/concave),
│   tip (upturned/straight/dropped), nostril_shape, nostril_visibility
│   — agganci landmark: nasion, pronasale, subnasale
└── Mouth: width, lip thickness, corner_position, opening, shape +
    Philtrum sotto-componente (length/width/depth/shape)
    — agganci landmark: stomion, labiale superius/inferius, cheilion L/R

H4.16-B — Trunk completo
├── Waist: circumference 80, width, depth, shape (tapered/straight/full)
├── Abdomen: length/width/depth, muscularity, fat_distribution, shape
└── FIX Torso: default adimensionali 1.0 → cm reali (52/36/24) —
    nessun test esistente asseriva i vecchi default (verificato in
    diagnostica), regressione H4.2 sopravvissuta intatta

H4.16-C — Igiene repository
├── rimossi 5 file backup tracciati (git rm, −1861 righe): la storia
│   li conserva; un backup dentro git e ridondante per definizione
└── .gitignore blindato: *.bak, *.bak_*, nodes/_backup_*/
```

Con H4.16 la copertura anatomica del Human Engine è COMPLETA: ogni regione del corpo, dalla testa ai piedi, ha struttura semantica. I landmark framework (H4.12) forniscono i punti di collegamento geometrici documentati nei docstring dei nuovi componenti.

## 33. H4.17 — Bilateral Upper Limbs

```text
arm.py — NUOVO (pattern Leg, H4.15-B)
└── Arm: side OBBLIGATORIO + upper_arm/elbow/forearm/wrist/hand
    per-braccio; elbow/wrist/hand side-MATCHED

arms.py — dual-mode (pattern Shoulders, H4.5)
├── legacy: API H4.2/H4.3 intatta (segmenti condivisi) —
│   i test storici h43/h44 girano intatti: la regressione
│   come prova vivente della backward compatibility
└── bilaterale: left/right Arm side-matched, asimmetria
    rappresentabile, indipendente dal modello legacy
```

Con H4.17 ogni struttura bilaterale del corpo segue lo standard forte: spalle, orecchie, mani, regione mammaria, gambe, braccia. **L'anatomia H4 è bilateralmente completa.**

## 34. H5 — Appearance (A→C)

```text
Architettura del layer: l'appearance vive ACCANTO all'anatomia —
SemanticComponent puri (pattern Coordinate), agganciati a Human
tramite register_component. Nessuna dipendenza da AnatomyComponent
(verificata da test dedicati); unico contatto: BodySide, il
vocabolario condiviso della bilateralità.

H5-A — Skin (human/skin)                          0aafb31
├── tone (7 nominali) + tone_hex opzionale
├── skin_type: Fitzpatrick I..VI — scala INDIPENDENTE dal tono
│   (reattività UV ≠ colore percepito: nessuna mappa forzata)
├── undertone, texture, oiliness/hydration/sensitivity 0..1
└── freckle_density, mole_count (≥ 0, strict int)

H5-B — Hair (human/hair)                          a12c135
├── color (12 nominali) + hex, texture (Andre Walker semplificato)
├── length ORTOGONALE: bald descrive la copertura, gli attributi
│   della fibra restano significativi (stubble, regrowth)
├── density/volume/gloss 0..1
└── STANDARD STRETTO: niente cast nel costruttore, bool rifiutati,
    ValueError per input non numerici (mai TypeError)

H5-C — Eye/Eyes (human/eyes)                      ba2b284
├── Eye side-required (pattern Ear/Leg/Arm): iris (9 colori +
│   pattern), sclera_tint, lashes
└── Eyes bilaterale forte — ETEROCROMIA emergente: nessun campo
    esplicito, è semplicemente left.iris_color ≠ right.iris_color
```

Due lezioni di processo codificate in H5: (1) mai `int()` prima di un check `isinstance(int)` — il cast maschera l'input sporco (scoperto da test_skin_rejects_invalid_mole_count, fixato in 0aafb31); (2) le attese dei test si contano dal file (`def test_`), non a occhio — il conteggio automatico è parte del protocollo da H5-B.

Con H5 il registro componenti di Human ospita il layer appearance completo: skin + hair + eyes convivono sullo stesso personaggio (test_full_appearance_layer_coexists).

## 35. H4.18 — Lower Body Extreme Detail & Anatomical Integrity (A→D)

```text
Nato dalla segnalazione: pelvica, glutei, fianchi, anche, cosce,
ginocchia, gambe, talloni, piedi e dita — dettaglio estremo.

H4.18-A  Hip/Hips bilaterali (trochanter + iliac crest per lato)
          + Glute/GlutealRegion bilaterali (asimmetria glutea)
          + Pelvis composito                                      5abd50f
H4.18-B  Flank/Flanks bilaterali (love-handle per lato) in
          Abdomen + Thigh/LowerLeg arricchiti 4→8 (quad/hamstring,
          calf/shin definition)                                   58e244b
H4.18-C  Knee 5→10 (rotula, allineamento genu valgum/varum,
          popliteo) + Heel strutturale (Achille, fat pad, calcagno
          — heel_width plantare resta indipendente) + Toe
          certificata per parità di firma con Finger             65dc7f2
H4.18-D  INTEGRITÀ ANATOMICA: Head (Face→Nose/Mouth, Ears) e
          MammaryRegion CABLATI in HumanAnatomy — il personaggio
          ottiene la testa (18 componenti cablati)               35e95c9
```

Nota storica: la diagnostica rivelò che Head e MammaryRegion esistevano, erano testati ed esportati, ma NON erano mai stati cablati nel composito — il buco d'integrità più grande del progetto. Chiuso con `test_complete_human_head_to_toe`, la traversata certificata dalla trichion all'alluce.

## 36. H4.19 — Anatomy Completion: "voglio tutto" (A→D)

```text
Nato dalla direttiva: "verifica se mancano sezioni facciali e
anatomiche non considerate o trattate con superficialità. voglio
tutto." Il censimento (pattern NON-ambigui: i falsi positivi
'lid '→'valid ' e 'brow'→docstring insegnarono la lezione)
certificò 24 strutture assenti + l'asimmetria di trattamento
upper/lower (3 vs 8 parametri). H4.19 ha chiuso tutto.

H4.19-A  Bocca interna: Teeth (allineamenti gapped/crowded),
          Tongue — Mouth composito + Eyelid/Eyelids bilaterali
          (hooded/monolid, piega palpebrale, PTOSI monolaterale)
          + Brow/Brows bilaterali                                 92a8ebc
H4.19-B  Tronco anteriore: Clavicles (visibilità per lato),
          Sternum (xifoide), Navel, Axillae, PubicRegion +
          pettorali/addominali espliciti (rectus, linea alba,
          obliqui)                                                4da60fd
H4.19-C  Schiena: Scapulae bilaterali (WINGING monolaterale —
          caso clinico), solco vertebrale, fosse lombari, trapezio
          + Neck: pomo d'Adamo (dimorfismo sessuale)             149915c
H4.19-D  PARITÀ ARTI: UpperArm/Forearm 3→8 (bicipite/tricipite,
          vascularity — dove le vene leggono davvero), malleoli
          in Ankle, nocche in Hand. Parità CERTIFICATA per
          introspezione: firma UpperArm == Thigh == 8,
          Forearm == LowerLeg == 8                                bc78c84

CENSIMENTO FINALE: 31/31 strutture presenti, zero mancanti.
```

Tre lezioni di processo codificate in H4.19: (1) i messaggi d'errore SONO contratto — il rosso di "fat distribution" (spazio, H4.16-B) contro il mio loop con underscore; (2) export senza import è invisibile finché il nome non viene importato — il probe deve importare ogni nuovo nome (Navel/PubicRegion); (3) le guardie di idempotenza testano il pattern specifico (l'import), mai la mera presenza del nome.

## 37. H4.20 — Composable Reproductive System

```text
Nato dalla domanda: "organi riproduttivi? sia maschili che
femminili? e loro sezioni da personalizzare?" — che smascherò
l'ultimo bias del censimento "voglio tutto" (H4.19), che aveva
escluso implicitamente la regione genitale mentre il progetto
trattava la MammaryRegion (H4.8) al massimo dettaglio da sempre.

DECISIONE ARCHITETTURALE — COMPOSIZIONE, mai hardcoding:
il sistema NON deduce l'anatomia dai Demographics (il progetto
separa Sex da Gender by design). MaleGenitalia e FemaleGenitalia
sono opzionali, indipendenti e possono COESISTERE.

male_genitalia.py (pattern mouth.py: 4 classi, 1 file)
├── Testicle(side): size, hang — ASIMMETRIA testicolare
│   (la norma anatomica, rappresentabile per lato)
├── Scrotum: width, tightness, rugae, texture + testicoli L/R
├── Penis: length_flaccid/erect, girth_erect, glans_shape
│   (tapered/round/mushroom), circumcision, curvature
│   (direction + degree), veination — dimensioni STRUTTURALI,
│   lo stato dinamico appartiene ai layer pose/state futuri
└── MaleGenitalia: composito

female_genitalia.py (5 classi, 1 file)
├── LabiumMajus(side): length/width/thickness, prominence,
│   pigmentation, shape (flat/full/drooping)
├── LabiumMinus(side): length, width,
│   protrusion_beyond_majora 0..1 (tratto reale e variabile)
├── ClitoralStructure: glans_size, hood_coverage, prominence
├── Vulva: composito (majora L/R + minora L/R + clitoral) —
│   asimmetria labiale = norma anatomica
└── FemaleGenitalia = Vulva (il mons resta in PubicRegion,
    non duplicato)

reproductive_system.py
└── ReproductiveSystem: male|None, female|None — default VUOTO:
    nessuna anatomia hardcodata, la configurazione è sempre
    esplicita e componibile

Integrazione: HumanAnatomy.reproductive_system (opzionale).
```

Commit: b043086 (feat) + 1fc3f16 (fix: la classe `Testicle` inizia per "Test" = prefisso di raccolta pytest → `__test__ = False`, meccanismo documentato — il nome anatomico corretto vince sul tooling).

Nota di processo: l'anchor fallito del primo tentativo (`from .pelvis import Pelvis, PubicRegion` — esiste in `__init__.py` ma NON in `human_anatomy.py`) insegnò la regola: *verificare l'anchor nel FILE TARGET, mai nella memoria della sessione*.

## 38. H5-D — The Complete Hair System (D-1/D-2/D-3)

```text
Nato dalla direttiva: "pieno controllo sulle acconciature e
tipologie di capigliatura, ivi comprese le calvizie e l'essere
glabri." — che trasformò H5-D da "body hair" a sistema-peli
COMPLETO.

H5-D-1  ScalpoHair                                        87429ae
├── Calvizie MEDICHE, non inventate: Norwood II-VII
│   (progressione maschile standard; Norwood I = NONE),
│   Ludwig I-III (diffusa femminile), areata (a chiazze),
│   totalis (cuoio capelluto nudo) — 12 pattern
├── SHAVED ≠ BALD: rasato = scelta con ombra di ricrescita;
│   calvo = assenza. Prima erano la stessa parola.
├── ACONCIATURE su due assi indipendenti: style (il TAGLIO:
│   21 vocaboli da buzz_cut a wolf_cut) × arrangement (COME È
│   PORTATO: 9 vocaboli da loose a space_buns) = 189 combinazioni
├── thinning per density 0..1 (già H5-B, ora documentato)
└── soft constraints documentati MAI imposti (bun su buzz cut
    = valido per parrucca)

H5-D-2  FacialHair                                        8b68950
├── 6 REGIONI anatomiche: MOUSTACHE, CHIN, JAWLINE,
│   SIDEBURNS, NECK, CHEEKS — la barba cresce a zone
├── 11 PRESET-FACTORY (clean_shaven, stubble, goatee, van_dyke,
│   full_beard, mutton_chops...) — from_style() configura le
│   coverage, tutto resta tunabile: IL PRESET È UN PUNTO DI
│   PARTENZA, MAI UNA GABBIA
├── COLORE indipendente dai capelli (grigio anticipato, rosso
│   su castano: tratto reale)
└── neckline = coverage NECK (la beard line È dove la coverage
    del collo si ferma)

H5-D-3  BodyHair + parità arti                            6820c60
├── 11 REGIONI Ferriman-Gallwey (lo standard medico dei peli
│   androgenici): CHEST, ABDOMEN, BACK, SHOULDERS, ARMS,
│   FOREARMS, HANDS, BUTTOCKS, THIGHS, LEGS, FEET
├── GLABRO = coverage 0 ovunque: STATO EMERGENTE dal dato,
│   mai una flag — il personaggio liscio e quello peloso sono
│   lo stesso componente con numeri diversi
├── PARITÀ ARTI 9×4: vascularity su UpperArm/Forearm/Thigh/
│   LowerLeg + flexor_definition su Forearm (completa il trio
│   di tessuti molli che gli altri tre segmenti portano:
│   il "Popeye forearm" è esattamente quello)
└── nessun preset-factory per il corpo: i peli corporei non
    hanno una tradizione di stili con nome — coerenza: i preset
    esistono dove esiste una tradizione

INCIDENTE E RIPRISTINO: durante H5-D-3, un editing esterno
(out-of-protocol) corromise lower_leg.py rimuovendo
calf_prominence dalla firma ma lasciando i riferimenti nel
corpo — 80 test in cascata. Il ripristino avvenne per
RISCRITTURA CANONICA dei 4 segmenti (possessone il contenuto
integrale dalla sessione) + il mio errore gemello: annunciai
"parità 9×4" contando Forearm a 8 dalla memoria (Forearm aveva
GIÀ vascularity nel suo 8; il 9° di Forearm è flexor_definition,
aggiunto nel fix). Lezioni: (1) evolvere un contratto di parità
richiede il riconteggio dai SORGENTI di TUTTI i membri; (2) le
guardie di evoluzione verificano assenza del vecchio, non solo
presenza del nuovo.
```

## 39. Sistema di validazione

```text
AnatomyComponent → SemanticComponent → CharacterForgeObject
```

Contratto: `validate()` **solleva ValueError**, `is_valid()` la cattura e restituisce bool. Validazione eager in `__init__` + ri-validabile dopo mutazione. Esempi: `dimensione <= 0 → ValueError`; `BodySide.RIGHT assegnato a left_cheek → ValueError`; endpoint sconosciuto in una relazione → `ValueError`.

Nota di sviluppo: durante H4.12-B il primo abbozzo restituiva una lista di errori invece di sollevare `ValueError`, rompendo il contratto della gerarchia; corretto prima del commit. Lezione: il contratto di validazione del progetto è a eccezioni.

## 40. Test e procedura canonica

Python di riferimento per sviluppo e test: **il venv di ComfyUI** — `D:\AVVIO PULITO di ComfyUI\ComfyUI\venv\Scripts\python.exe` (Python 3.12.10, pytest 9.1.1). Il Python 3.14 globale non ha pytest e non deve essere usato.

```text
regressione unittest : python -m unittest discover -s tests -p "test_*.py"  → Ran 196 tests OK
suite pytest         : 5 suite storiche + H4.12-B/C/D/E + H4.13-A/B/C + H4.14-A/B/C/D + H4.15-A/B + H4.16-A/B + H4.17 + H5-A/B/C + H4.18-A/B/C/D + H4.19-A/B/C/D + H4.20 + H5-D-1/2/3 → 802 passed
TOTALE TEST UNICI   : 998 verdi
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
- H4.16-A: 42 test → OK (pytest)
- H4.16-B: 18 test → OK (pytest)
- H4.17: 24 test → OK (pytest)
- H5-A: 20 test → OK (pytest)
- H5-B: 17 test → OK (pytest)
- H5-C: 19 test → OK (pytest)
- H4.18-A: 24 test → OK (pytest)
- H4.18-B: 25 test → OK (pytest)
- H4.18-C: 17 test → OK (pytest)
- H4.18-D: 12 test → OK (pytest)
- H4.19-A: 31 test → OK (pytest)
- H4.19-B: 28 test → OK (pytest)
- H4.19-C: 19 test → OK (pytest)
- H4.19-D: 16 test → OK (pytest)
- H4.20: 30 test → OK (pytest)
- H5-D-1: 18 test → OK (pytest)
- H5-D-2: 19 test → OK (pytest)
- H5-D-3: 19 test → OK (pytest)

Totale capitolo H4.12: **92 test**. Totale capitolo H4.13: **54 test**. Totale capitolo H4.14: **97 test**. Totale capitolo H4.15: **62 test**. Totale capitolo H4.16: **60 test**. Totale capitolo H4.17: **24 test**. Totale capitolo H5: **56 test**. Totale capitolo H4.18: **78 test**. Totale capitolo H4.19: **94 test**. Totale capitolo H4.20: **30 test**. Totale capitolo H5-D: **56 test**.

Nota storica: i 5 errori di import `No module named 'pytest'` documentati fino a H4.11 nascevano dall'uso del Python 3.14 globale; con il venv di ComfyUI l'intera suite gira senza errori. Da H4.12 in poi la procedura canonica usa il venv.

## 41. Git

Ultimo checkpoint: **H5-D-3** — commit `feat(human): add H5-D-3 body hair per region and four-segment limb parity` (`6820c60`).

```text
main
↑ 0 commit locali rispetto a origin/main (sincronizzato)
working tree clean
```

Commit dei capitoli H4.12 … H5-D:

```text
6820c60 feat(human): add H5-D-3 body hair per region and four-segment limb parity
8b68950 feat(human): add H5-D-2 facial hair per region with style factories
87429ae feat(human): add H5-D-1 scalp hair control baldness patterns and styling
1fc3f16 fix(human): opt Testicle class out of pytest collection
b043086 feat(human): add H4.20 composable reproductive system
bc78c84 feat(human): add H4.19-D limb parity malleoli knuckles vascularity
149915c feat(human): add H4.19-C back detail scapulae and neck laryngeal prominence
4da60fd feat(human): add H4.19-B anterior trunk structures clavicles sternum navel axillae pubic
92a8ebc feat(human): add H4.19-A mouth interior eyelids and brows
35e95c9 feat(human): add H4.18-D wire head and mammary region into HumanAnatomy
65dc7f2 feat(human): add H4.18-C knee detail heel structure and composite foot
58e244b feat(human): add H4.18-B flanks and enriched thigh lower leg detail
5abd50f feat(human): add H4.18-A hip and gluteal region with composite pelvis
ba2b284 feat(human): add H5-C eyes appearance component
a12c135 feat(human): add H5-B hair appearance component
0aafb31 feat(human): add H5-A skin appearance component
31a4ed7 feat(human): add H4.17 bilateral arm model with legacy compatibility
604d16e chore: remove tracked backup files and ignore future ones
6c745d8 feat(human): add H4.16-B waist abdomen and real-unit torso defaults
92752e8 feat(human): add H4.16-A ears nose mouth components
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

I capitoli da H4.12 a H5, i completamenti H4.18/H4.19/H4.20, il sistema-peli H5-D e il documento della visione sono stati pushati su `origin/main`.

## 42. Dove NON siamo ancora arrivati

Le fondamenta geometriche, la derivazione morfometrica, la modifica parametrica, l'anatomia a dettaglio estremo e TOTALE, l'appearance completa (pelle, capelli con pieno controllo su calvizie e acconciature, occhi, barba per regioni, peli corporei per regioni con glabro emergente) esistono ora. CharacterForge **non è ancora un generatore 3D anatomico**. **H4 (fino a H4.19) e H5 sono complete.** Mancano:

```text
3D representation
→ Reference Sheet generation
→ Consistent image generation
→ Vision analyzers (Image → Entity)
→ Generation Compiler
→ Model Adapters
```

## 43. Il salto concettuale successivo

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

La catena completa `FacialLandmarks → FacialMeasurements → FaceDimensions → HeadDimensions → HeadProportions` (più `FacialProportions` dal FaceDimensions) chiude il cerchio semantica ↔ geometria e realizza la nota della sezione 13. Con H4.14: **"COME SI PROPAGA una modifica?"** — e la risposta è codice con report a tre livelli. Con H5-D il sistema-peli è completo: calvizie mediche, acconciature su due assi, barba per regioni, corpo per regioni, glabro emergente. Prossimo: **H6 — Clothing**, il primo layer relazionale (copre ciò che abbiamo costruito).

## 44. In sintesi — percorso fatto

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
H4.16   Anatomy Completion (A→C)                           ← CHIUSA
H4.17   Bilateral Upper Limbs (dual-mode Arms)             ← CHIUSA
H5      Appearance (A→C: skin, hair, eyes)               ← CHIUSA
H4.18   Lower Body Extreme Detail + Integrità (A→D)       ← CHIUSA
H4.19   Anatomy Completion: voglio tutto (A→D)            ← CHIUSA
H4.20   Composable Reproductive System                   ← CHIUSA
H5-D    The Complete Hair System (D-1/2/3)              ← CHIUSA
```

H4.12 ha costruito il ponte tra **modello anatomico semantico** e **modello geometrico parametrico**: ora esiste. H4.13 lo ha reso percorribile in entrambe le direzioni: le proporzioni non si dichiarano più, si derivano — cranio compreso. H4.14 lo ha reso reversibile e verificabile: ogni modifica torna con il certificato di cosa è cambiato e cosa è sopravvissuto.

## 45. Roadmap estesa oltre H6

```text
H4  HUMAN ANATOMY
│
├── H4.13 Morphometric derivation (proporzioni/dimensioni derivate)   ✅
├── H4.14 Parametric builder / propagazione delle modifiche     ✅
├── H4.15 Lower body (pelvis, gambe, piedi)                  ✅
├── H4.16 Anatomy completion (viso, tronco, igiene)          ✅
├── H4.17 Bilateralità completa degli arti superiori (Arms)  ✅
├── H4.18 Lower body extreme detail + integrità (testa!)    ✅
├── H4.19 Censimento "voglio tutto" a zero (31/31)         ✅
├── H4.20 Sistema riproduttivo componibile                   ✅
├── H5-D  The Complete Hair System (calvizie/stili/peli)     ✅
└── H4+H5+H5-D CHIUSE: struttura + superficie + peli
        ↓
H5  APPEARANCE
│
├── H5-A Skin (SemanticComponent, standard stretto)          ✅
├── H5-B Hair (bald ortogonale, graded strict)               ✅
├── H5-C Eyes bilaterali (eterocromia emergente)             ✅
└── H5 CHIUSA: appearance base completa
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

## 46. Il punto fondamentale del progetto, in una frase

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

E con H4.20 chiusa, il censimento anatomico è TOTALE: ogni struttura del corpo umano ha componente semantica certificata — visibile o interna, bilateralmente asimmetrica dove l'anatomia lo è, componibile dove la configurazione deve restare esplicita. Il modello è pronto per H6.