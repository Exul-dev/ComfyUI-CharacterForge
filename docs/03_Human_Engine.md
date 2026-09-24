# CharacterForge — Human Engine

**Documento:** 03 — Human Engine  
**Versione architetturale:** 1.0  
**Stato:** Baseline progettuale  
**Data:** 2026-09-24  

---

## 1. Scopo

Il **Human Engine** è il sottosistema responsabile della costruzione parametrica di entità umanoidi realistiche, stilizzate o cinematiche all'interno di CharacterForge.

Il suo compito non è generare direttamente l'immagine.

Il suo compito è definire in modo strutturato **chi è il soggetto umano**, quali caratteristiche possiede, come tali caratteristiche sono correlate e quali variazioni possono essere applicate senza perdere la sua identità.

Il risultato del motore deve poter essere utilizzato da:

- Style Engine
- Camera Engine
- Cinematography Engine
- Transformation Engine
- Reference Sheet System
- Environment / World Engine
- ComfyUI implementation layer

Il principio fondamentale è:

> **l'identità del soggetto deve essere separata dallo stile con cui il soggetto viene rappresentato.**

---

## 2. Principi fondamentali

### 2.1 Identity First

Un soggetto umano deve possedere una rappresentazione interna stabile.

Lo stile non deve diventare parte dell'identità.

Esempio concettuale:

```
HumanIdentity
  ├── anatomy
  ├── face
  ├── skin
  ├── hair
  ├── eyes
  ├── body
  ├── age
  ├── clothing
  └── persistent traits
```

Lo stesso soggetto deve poter essere rappresentato come:

- fotografia
- anime
- illustrazione
- fumetto
- cinematografia
- pixel art
- concept art
- altro stile compatibile

senza creare un nuovo soggetto.

---

## 3. Modello concettuale

Il Human Engine opera su una struttura gerarchica.

```
Human
├── identity
├── demographics
├── anatomy
├── face
├── hair
├── eyes
├── skin
├── body
├── clothing
├── accessories
├── pose_constraints
├── distinctive_traits
└── variation_rules
```

Ogni livello deve poter essere modificato indipendentemente quando possibile.

Le dipendenze devono essere esplicite.

---

## 4. Identity Layer

L'Identity Layer rappresenta gli attributi che definiscono la continuità del soggetto.

Può comprendere:

- identificatore univoco
- nome interno
- seed di identità
- tratti distintivi
- struttura facciale
- proporzioni corporee
- caratteristiche cromatiche
- caratteristiche persistenti
- vincoli di variazione

Esempio concettuale:

```
identity_id = "human_001"
identity_seed = 481927
```

L'identificatore non deve essere confuso con il seed di generazione.

Il seed può cambiare.

L'identità deve rimanere riconoscibile.

---

## 5. Demographics Layer

Il livello demografico descrive attributi generali del soggetto.

Possibili categorie:

- fascia d'età
- sesso biologico quando utilizzato dal modello
- caratteristiche fenotipiche
- origine geografica o culturale quando pertinente
- altezza
- peso relativo
- corporatura

Questi parametri devono essere trattati come **descrittori generativi**, non come classificazioni assolute.

Le categorie devono poter essere estese senza modificare il core.

---

## 6. Age System

L'età deve essere rappresentata come parametro controllabile.

Possibili modalità:

- valore numerico
- fascia d'età
- descrizione qualitativa

Esempio:

```
age:
  mode: range
  value: adult
```

L'età deve influenzare coerentemente:

- struttura del volto
- pelle
- capelli
- massa muscolare
- proporzioni
- postura
- dettagli anatomici

Il sistema non deve limitarsi ad aggiungere parole come "young" o "old" al prompt.

---

## 7. Anatomy System

L'Anatomy System descrive la struttura fisica del soggetto.

Categorie principali:

### 7.1 Proporzioni

- altezza relativa
- rapporto testa/corpo
- lunghezza degli arti
- ampiezza delle spalle
- ampiezza del bacino
- lunghezza del torso
- lunghezza delle gambe
- dimensione delle mani
- dimensione dei piedi

### 7.2 Corporatura

- esile
- magra
- atletica
- media
- robusta
- muscolosa
- corpulenta

Queste categorie sono preset descrittivi.

Il sistema deve inoltre permettere valori continui o combinazioni personalizzate.

### 7.3 Postura

La postura deve essere separata dalla struttura anatomica.

Possibili parametri:

- eretta
- rilassata
- incurvata
- asimmetrica
- atletica
- dinamica

La postura appartiene alla rappresentazione della posa, non all'identità anatomica permanente, salvo quando esistano caratteristiche persistenti.

---

## 8. Body Controller Integration

Il Human Engine deve poter utilizzare l'attuale Body Controller come livello di compatibilità durante la migrazione.

Il controller esistente non deve essere considerato automaticamente l'architettura definitiva.

La direzione futura è:

```
Human Engine
      ↓
Body Model
      ↓
Prompt / Conditioning Adapter
      ↓
ComfyUI
```

In questo modo il modello anatomico rimane indipendente dal particolare nodo ComfyUI.

---

## 9. Face System

Il volto costituisce uno dei principali identificatori dell'entità.

Deve essere scomposto in componenti.

### 9.1 Struttura

- forma generale del volto
- fronte
- zigomi
- mascella
- mento
- mascella inferiore
- larghezza facciale

### 9.2 Occhi

- forma
- dimensione
- distanza
- inclinazione
- colore
- sclera
- iride
- pupilla

### 9.3 Sopracciglia

- forma
- spessore
- densità
- arco
- colore

### 9.4 Naso

- lunghezza
- larghezza
- ponte
- punta
- narici

### 9.5 Bocca

- larghezza
- forma delle labbra
- spessore
- arco di Cupido
- posizione

### 9.6 Orecchie

- dimensione
- forma
- posizione
- caratteristiche distintive

---

## 10. Facial Identity

La Facial Identity Layer deve distinguere:

**struttura permanente**

da

**stato temporaneo**.

Esempio:

Struttura:

- forma degli occhi
- distanza interpupillare
- forma del naso
- struttura mandibolare

Stato:

- sorriso
- tristezza
- rabbia
- sorpresa
- occhi socchiusi

Un'espressione non deve modificare permanentemente l'identità facciale.

---

## 11. Skin System

La pelle deve essere modellata come materiale e come caratteristica anatomica.

Parametri possibili:

- tonalità
- sottotono
- saturazione
- luminosità
- texture
- porosità
- lentiggini
- nei
- cicatrici
- rughe
- imperfezioni
- abbronzatura
- distribuzione del colore

Il sistema deve evitare descrizioni eccessivamente rigide.

Il risultato deve poter essere tradotto in:

- prompt
- conditioning
- metadata
- reference constraints

---

## 12. Hair System

Il sistema dei capelli deve essere indipendente dal volto.

Parametri:

- lunghezza
- densità
- volume
- texture
- tipo
- colore
- radice
- sfumature
- pettinatura
- frangia
- attaccatura
- barba
- baffi
- basette

Una modifica dello stile dei capelli non deve generare automaticamente una nuova identità.

---

## 13. Eye System

Gli occhi devono avere una rappresentazione indipendente.

Parametri:

- colore
- tonalità
- saturazione
- forma
- dimensione
- apertura
- posizione
- distanza
- direzione dello sguardo

Devono inoltre essere compatibili con:

- età
- anatomia
- espressione
- illuminazione
- stile

---

## 14. Clothing System

L'abbigliamento deve essere separato dal corpo.

Categorie:

- headwear
- upper body
- lower body
- footwear
- outerwear
- underwear quando pertinente
- gloves
- accessories
- uniforms
- costumes

Ogni elemento dovrebbe poter possedere:

- materiale
- colore
- pattern
- usura
- stato
- epoca
- stile
- fit
- variazioni

Il cambio di abbigliamento non deve modificare l'identità del soggetto.

---

## 15. Accessories

Gli accessori possono diventare elementi persistenti dell'identità.

Esempi:

- occhiali
- gioielli
- orologi
- piercing
- tatuaggi
- cicatrici
- oggetti personali

Ogni elemento deve poter essere classificato come:

- permanente
- opzionale
- temporaneo

Questo consente di generare varianti dello stesso personaggio mantenendo un insieme controllato di caratteristiche.

---

## 16. Distinctive Traits

I tratti distintivi costituiscono un livello speciale.

Esempi:

- cicatrice sul sopracciglio
- neo specifico
- eterocromia
- ciocca di capelli caratteristica
- forma particolare del naso
- tatuaggio
- asimmetria facciale

Questi tratti devono avere una priorità superiore rispetto ai dettagli puramente estetici quando l'obiettivo è mantenere l'identità.

---

## 17. Identity Persistence

La persistenza dell'identità è uno degli obiettivi principali del Human Engine.

Una modifica a:

- stile
- luce
- fotocamera
- ambiente
- abbigliamento
- posa

non dovrebbe trasformare automaticamente il soggetto in un nuovo asset.

Concettualmente:

```
HumanIdentity
        │
        ├── Style
        ├── Camera
        ├── Lighting
        ├── Environment
        ├── Pose
        └── Clothing
```

L'identità rimane il livello superiore.

---

## 18. Controlled Variation

Il sistema deve consentire variazioni controllate.

Ogni parametro può avere un livello di stabilità.

Esempio concettuale:

```
identity_strength:
  face: 1.0
  body: 0.9
  hair: 0.8
  clothing: 0.2
```

Questi valori sono concettuali e non costituiscono ancora una API definitiva.

L'obiettivo è permettere:

- variazione minima
- variazione moderata
- variazione ampia
- rigenerazione controllata

senza perdere il riferimento all'identità originale.

---

## 19. Prompt Representation

Il Human Engine deve poter produrre una rappresentazione testuale strutturata.

Esempio:

```
adult human,
athletic build,
oval face,
dark brown eyes,
short wavy black hair,
medium warm skin tone,
distinctive eyebrow scar
```

Il prompt generato non deve essere l'unica rappresentazione dell'entità.

Il modello strutturato rimane la fonte primaria.

---

## 20. Conditioning Representation

Quando il backend lo permette, il Human Engine deve poter trasformare i parametri strutturati in conditioning.

Pipeline concettuale:

```
Human Model
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

Il Human Engine non deve assumere un particolare modello generativo.

---

## 21. Style Separation

Il seguente principio è vincolante:

> Human Engine definisce il soggetto. Style Engine definisce come il soggetto viene rappresentato.

Esempio:

```
Human:
  adult
  athletic
  brown eyes
  black hair
  facial scar

Style:
  cinematic
  35mm
  low key
  film grain
```

Lo stesso Human Model deve poter essere passato a uno stile anime senza ricostruire manualmente il soggetto.

---

## 22. Reference Sheet Integration

Il Human Engine deve essere progettato nativamente per il Reference Sheet System.

Una Reference Sheet umana potrà comprendere:

- front
- back
- left
- right
- three-quarter
- profile
- full body
- portrait
- facial close-up
- expression variants
- clothing variants

La selezione delle viste sarà gestita dal Reference Sheet System.

Il Human Engine fornisce la coerenza dell'entità.

---

## 23. Camera Independence

Il Human Engine non deve contenere la logica della fotocamera.

Può però esporre vincoli utili alla Camera Engine.

Esempio:

- altezza del soggetto
- dimensioni relative
- punti di riferimento anatomici
- bounding characteristics

La composizione fotografica appartiene al Camera Engine.

---

## 24. Transformation Compatibility

Il Human Engine deve essere compatibile con il Transformation Engine.

Possibili trasformazioni future:

- umano → anziano
- umano → giovane
- umano → cyborg
- umano → creatura
- umano → versione fantasy
- umano → versione stilizzata

La trasformazione deve poter preservare una parte dell'identità originale.

Concettualmente:

```
Source Identity
      ↓
Transformation
      ↓
Derived Identity
```

La derivazione deve essere tracciabile.

---

## 25. Preset Architecture

I preset umani non devono essere hard-coded nel core.

Struttura concettuale:

```
HumanPreset
├── metadata
├── demographics
├── anatomy
├── face
├── hair
├── eyes
├── skin
├── clothing
└── traits
```

Il sistema deve supportare:

- preset ufficiali
- preset personalizzati
- preset importati
- preset derivati

---

## 26. Compatibility With Existing Controllers

L'attuale CharacterForge contiene:

- Gender Controller
- Ethnicity Controller
- Body Controller

Questi componenti rappresentano funzionalità già esistenti, ma non devono essere considerati automaticamente la struttura definitiva del nuovo Human Engine.

La futura architettura dovrà progressivamente spostare la logica verso un modello umano centralizzato.

Direzione:

```
Legacy Controllers
       ↓
Compatibility Layer
       ↓
Human Model
       ↓
Human Engine
```

Questo permette di mantenere compatibilità senza bloccare l'evoluzione architetturale.

---

## 27. Validation Rules

Il Human Engine deve validare almeno:

- valori ammessi
- tipi dei parametri
- compatibilità tra parametri
- presenza di identificatore
- coerenza delle strutture
- valori numerici fuori intervallo
- riferimenti a preset inesistenti

La validazione deve avvenire prima della generazione del conditioning.

---

## 28. Determinism

Quando un'identità viene salvata, il sistema dovrebbe essere in grado di ricostruire la stessa configurazione.

Questo richiede:

- serializzazione
- identificatore stabile
- versione dello schema
- seed quando necessario
- metadata dei preset utilizzati

Una futura struttura potrebbe includere:

```
schema_version: "1.0"
identity_id: "human_001"
```

La struttura esatta sarà definita durante l'implementazione.

---

## 29. Serialization

Il modello umano deve essere serializzabile.

Formati candidati:

- JSON
- YAML
- metadata ComfyUI
- formato interno CharacterForge

Il formato canonico dovrà essere definito dall'implementazione.

La serializzazione deve consentire:

- salvataggio
- caricamento
- duplicazione
- modifica
- confronto
- versionamento

---

## 30. Error Handling

Gli errori del Human Engine devono essere espliciti.

Esempi:

- parametro sconosciuto
- preset mancante
- tipo errato
- valore fuori range
- conflitto tra attributi
- schema incompatibile

Gli errori non devono produrre silenziosamente un'identità differente.

---

## 31. Test Strategy

Il Human Engine dovrà essere testato a più livelli.

### Unit Test

Test dei singoli componenti:

- anatomy
- face
- skin
- hair
- eyes
- clothing
- identity

### Integration Test

Verifica della comunicazione con:

- Style Engine
- Camera Engine
- Reference Sheet System
- Transformation Engine

### Regression Test

Ogni modifica al modello deve verificare che le identità precedentemente supportate rimangano leggibili.

---

## 32. Migration Strategy

La migrazione deve essere incrementale.

### Fase 1

Definire il modello dati Human.

### Fase 2

Creare validator e serializer.

### Fase 3

Creare adapter per i controller esistenti.

### Fase 4

Integrare Style Engine.

### Fase 5

Integrare Reference Sheet System.

### Fase 6

Integrare Transformation Engine.

### Fase 7

Ridurre progressivamente la logica duplicata nei legacy controllers.

Nessun controller esistente deve essere eliminato prima che la sua funzionalità sia coperta dal nuovo sistema e dai test.

---

## 33. Stato attuale

Alla data di questo documento, CharacterForge possiede già componenti funzionanti relativi alla costruzione del soggetto umano:

- Gender Controller
- Ethnicity Controller
- Body Controller

Sono inoltre presenti sistemi di conditioning e style transfer.

Questi componenti costituiscono la base tecnica esistente, ma non rappresentano ancora un Human Engine centralizzato secondo questa architettura.

Il presente documento definisce quindi la **destinazione architetturale**, non dichiara implementate funzionalità che non sono state verificate.

---

## 34. Debito architetturale noto

Sono presenti differenze tra:

- controller legacy
- modello concettuale Human Engine
- rappresentazione prompt
- conditioning
- style system
- gestione dei preset

La migrazione deve evitare di creare ulteriori duplicazioni.

Particolare attenzione deve essere posta alla separazione tra:

- dati
- logica
- preset
- adapter ComfyUI
- nodi UI

---

## 35. Dipendenze

Il Human Engine dipende concettualmente da:

```
Human Engine
├── Core Data Model
├── Validation
├── Serialization
├── Style Engine
├── Reference Sheet System
└── ComfyUI Adapter
```

Non deve dipendere direttamente da implementazioni specifiche di singoli modelli generativi.

---

## 36. API futura

L'API definitiva non è ancora stabilita.

La direzione desiderata è un'interfaccia simile a:

```
human = HumanEngine.create(...)
human.validate()
human.to_prompt()
human.to_conditioning(...)
human.serialize()
human.derive(...)
```

Questa rappresentazione è architetturale e non costituisce ancora codice da implementare.

---

## 37. Principio di estensibilità

Il Human Engine deve poter essere esteso senza modificare il core per ogni nuovo attributo.

Nuove categorie future potrebbero includere:

- protesi
- modificazioni corporee
- cybernetics
- trucco
- effetti speciali
- abiti storici
- equipaggiamento
- caratteristiche fantasy
- caratteristiche fantascientifiche

L'architettura deve permettere l'aggiunta di nuovi componenti mantenendo compatibilità con le entità esistenti.

---

## 38. Relazione con gli altri Engine

Il Human Engine non è isolato.

La pipeline concettuale complessiva è:

```
Human Engine
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

La pipeline reale potrà variare in base al workflow, ma i confini logici devono rimanere separati.

---

## 39. Regola architetturale finale

Il Human Engine deve garantire una separazione netta tra:

**CHI È IL SOGGETTO**

e

**COME VIENE RAPPRESENTATO**.

Il primo appartiene al Human Engine.

Il secondo appartiene agli engine di stile, camera, cinematografia, ambiente e trasformazione.

Questa separazione è fondamentale per ottenere:

- identità persistente
- varianti controllate
- reference sheet coerenti
- riutilizzabilità
- modularità
- compatibilità con più modelli
- evoluzione futura del CharacterForge

---

# Fine Documento 03
