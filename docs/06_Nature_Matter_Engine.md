# CharacterForge — Nature & Matter Engine

**Documento:** 06 — Nature & Matter Engine  
**Versione architetturale:** 1.0  
**Stato:** Architecture Baseline  
**Progetto:** ComfyUI-CharacterForge

---

## 1. Scopo

Il **Nature & Matter Engine** definisce il modello architetturale con cui CharacterForge rappresenta:

- materia naturale;
- sostanze;
- materiali;
- elementi naturali;
- vegetazione;
- fenomeni atmosferici;
- fenomeni fisici;
- particolato;
- stati della materia;
- trasformazioni naturali;
- variazioni procedurali;
- condizioni ambientali;
- fenomeni fantasy o elementali.

Il motore deve consentire di descrivere in modo strutturato **che cosa è presente nella scena**, quali proprietà possiede e come tali proprietà cambiano in funzione di ambiente, stato fisico, tempo e trasformazione.

Il motore non deve confondere:

1. **entità persistenti**;
2. **materiali o sostanze**;
3. **fenomeni dinamici**;
4. **rappresentazione visiva**.

La separazione tra contenuto e rappresentazione costituisce un principio fondamentale dell'architettura CharacterForge.

---

## 2. Principi fondamentali

### 2.1 Natura e materia come sistemi strutturati

Una sostanza naturale non deve essere rappresentata esclusivamente tramite testo descrittivo.

Il sistema deve poter rappresentare strutturalmente proprietà quali:

- tipo;
- categoria;
- stato fisico;
- composizione;
- colore;
- texture;
- densità;
- temperatura;
- umidità;
- rugosità;
- riflettività;
- traslucenza;
- viscosità;
- fluidità;
- granulometria;
- comportamento;
- interazione ambientale.

La descrizione testuale deve essere una rappresentazione derivata dal modello strutturato.

### 2.2 Distinzione tra materia e fenomeno

Il sistema deve distinguere tra:

- acqua;
- roccia;
- sabbia;
- neve;
- legno;
- metallo naturale;
- terreno;

e fenomeni quali:

- pioggia;
- nebbia;
- fumo;
- vapore;
- vento;
- temporale;
- incendio;
- polvere sospesa.

La materia può avere una persistenza relativamente stabile.

Il fenomeno può essere invece:

- temporaneo;
- dinamico;
- dipendente dal tempo;
- dipendente dall'ambiente;
- procedurale.

### 2.3 Separazione tra contenuto e stile

Il Nature & Matter Engine definisce **che cosa è la materia o il fenomeno**.

Lo Style Engine definisce invece:

- come viene illustrato;
- come viene illuminato;
- come viene colorato;
- come viene renderizzato;
- quale linguaggio artistico viene utilizzato.

Un lago realistico e un lago in stile anime devono condividere lo stesso modello concettuale dell'elemento naturale.

### 2.4 Variazione controllata

La natura deve poter variare senza perdere coerenza.

Il sistema deve distinguere tra:

- variazione casuale;
- variazione controllata;
- variazione ambientale;
- variazione temporale;
- trasformazione intenzionale.

---

## 3. Tassonomia

Il motore deve prevedere una tassonomia estensibile.

Categorie iniziali:

- Water
- Ice
- Fire
- Rock
- Soil
- Sand
- Mud
- Snow
- Wood
- Leaves
- Flowers
- Grass
- Trees
- Fungi
- Moss
- Minerals
- Clouds
- Fog
- Smoke
- Steam
- Dust
- Rain
- Wind
- Lightning
- Atmospheric Phenomena
- Organic Matter
- Fantasy Matter
- Elemental Matter

La tassonomia non deve essere hard-coded in modo da impedire l'aggiunta di nuove categorie.

---

## 4. Modello della materia

Ogni elemento materiale deve poter essere rappresentato tramite un modello strutturato.

Esempio concettuale:

```
{
  "type": "material",
  "category": "water",
  "state": "liquid",
  "properties": {
    "color": "...",
    "roughness": 0.05,
    "reflectivity": 0.8,
    "translucency": 0.4,
    "density": 1.0,
    "temperature": 20.0,
    "wetness": 1.0
  }
}
```

Il formato definitivo sarà definito dallo schema condiviso del progetto.

---

## 5. Proprietà fisiche e visive

### 5.1 Colore

Il sistema deve poter controllare:

- colore base;
- variazioni cromatiche;
- saturazione;
- luminosità;
- gradienti;
- variazioni naturali;
- colorazione dipendente dall'ambiente.

### 5.2 Texture

La texture può includere:

- liscia;
- ruvida;
- granulosa;
- fibrosa;
- porosa;
- cristallina;
- organica;
- irregolare;
- stratificata.

### 5.3 Rugosità

La rugosità deve essere rappresentabile come proprietà continua e non soltanto come categoria discreta.

### 5.4 Riflettività

Il sistema deve distinguere tra:

- opaco;
- semi-riflettente;
- riflettente;
- altamente riflettente.

### 5.5 Traslucenza

La traslucenza deve poter rappresentare materiali quali:

- ghiaccio;
- acqua;
- foglie;
- petali;
- membrane;
- materiali fantasy.

### 5.6 Umidità

L'umidità deve poter modificare dinamicamente:

- colore;
- riflettività;
- texture;
- brillantezza;
- aggregazione;
- comportamento superficiale.

Esempio:

**terra asciutta → terra umida → fango**

deve poter essere rappresentato come trasformazione controllata dello stesso materiale.

---

## 6. Stati della materia

Il sistema deve supportare almeno:

- solido;
- liquido;
- gas;
- plasma o stato energetico astratto, quando richiesto dal dominio fantasy.

Devono inoltre essere rappresentabili stati intermedi o compositi quando necessari.

Esempi:

- ghiaccio;
- acqua;
- vapore;
- neve;
- neve sciolta;
- fango;
- lava;
- cristalli;
- fumo.

---

## 7. Transizioni di fase

Le transizioni devono essere modellabili.

Esempi:

- acqua → ghiaccio;
- ghiaccio → acqua;
- acqua → vapore;
- neve → acqua;
- acqua + terreno → fango;
- roccia → materiale fratturato;
- vegetazione → materia organica.

Una trasformazione non deve necessariamente creare una nuova identità.

Quando semanticamente appropriato, deve essere possibile rappresentarla come:

**stessa materia + nuovo stato**.

---

## 8. Fluidi

I fluidi richiedono proprietà specifiche:

- viscosità;
- densità;
- temperatura;
- velocità;
- direzione;
- turbolenza;
- superficie;
- profondità;
- rifrazione;
- trasparenza;
- interazione con contenitori e superfici.

Esempi:

- acqua;
- fango;
- lava;
- sangue sintetico o fantasy;
- resina;
- sostanze magiche.

Il motore non deve simulare necessariamente la fisica reale.

Deve invece fornire una rappresentazione parametrica utilizzabile dalla pipeline generativa.

---

## 9. Particolato

Il sistema deve supportare materiali composti da particelle o elementi dispersi.

Esempi:

- sabbia;
- polvere;
- cenere;
- neve;
- foglie;
- petali;
- scintille;
- detriti.

Parametri possibili:

- dimensione;
- densità;
- distribuzione;
- quantità;
- velocità;
- direzione;
- aggregazione;
- dispersione;
- sospensione;
- deposizione.

---

## 10. Fuoco, fumo, vapore e nebbia

Questi elementi devono essere trattati come fenomeni dinamici.

### 10.1 Fuoco

Parametri:

- intensità;
- temperatura percepita;
- altezza;
- forma;
- colore;
- luminosità;
- distribuzione;
- direzione;
- turbolenza;
- produzione di fumo.

### 10.2 Fumo

Parametri:

- densità;
- colore;
- trasparenza;
- direzione;
- dispersione;
- turbolenza;
- origine;
- persistenza.

### 10.3 Vapore

Parametri:

- temperatura;
- densità;
- quantità;
- dispersione;
- condensazione;
- interazione con l'ambiente.

### 10.4 Nebbia

Parametri:

- densità;
- altezza;
- profondità;
- temperatura;
- umidità;
- visibilità;
- distribuzione;
- movimento.

---

## 11. Vegetazione

La vegetazione deve essere rappresentata come sistema strutturato.

Categorie iniziali:

- alberi;
- arbusti;
- erba;
- fiori;
- piante;
- muschio;
- funghi;
- radici;
- foglie;
- rami;
- frutti.

### 11.1 Struttura

Un elemento vegetale può includere:

- specie;
- dimensione;
- età;
- crescita;
- struttura;
- fogliame;
- colore;
- densità;
- stato di salute;
- stagione;
- fioritura;
- fruttificazione.

### 11.2 Crescita

Il sistema deve poter rappresentare:

- giovane;
- adulto;
- maturo;
- vecchio;
- danneggiato;
- morente;
- morto.

La crescita deve essere compatibile con variazioni controllate e trasformazioni temporali.

---

## 12. Materia geologica

Devono poter essere rappresentati:

- roccia;
- pietra;
- ghiaia;
- sabbia;
- terreno;
- argilla;
- minerali;
- cristalli;
- lava;
- materiale vulcanico.

Parametri importanti:

- stratificazione;
- fratture;
- erosione;
- granulometria;
- inclusioni;
- composizione visiva;
- umidità;
- sedimentazione.

---

## 13. Pattern naturali

Il motore deve supportare pattern procedurali e naturali.

Esempi:

- venature;
- marmorizzazione;
- strati geologici;
- crepe;
- corteccia;
- crescita muschiosa;
- distribuzione fogliare;
- cristallizzazione;
- increspature dell'acqua;
- dune;
- erosione.

I pattern devono poter essere parametrizzati e riprodotti con seed deterministico.

---

## 14. Danno, erosione e invecchiamento

La materia naturale deve poter cambiare nel tempo.

Parametri possibili:

- usura;
- erosione;
- fratturazione;
- corrosione;
- essiccazione;
- decomposizione;
- congelamento;
- scioglimento;
- sedimentazione;
- accumulo;
- crescita biologica.

Questi parametri devono poter interagire con l'ambiente.

---

## 15. Meteo e fenomeni atmosferici

Il motore deve fornire una rappresentazione parametrica dei fenomeni atmosferici.

Esempi:

- sole;
- pioggia;
- neve;
- grandine;
- nebbia;
- vento;
- nuvole;
- temporali;
- fulmini;
- foschia;
- polvere atmosferica.

Il fenomeno deve poter essere collegato a:

- temperatura;
- umidità;
- vento;
- visibilità;
- ora del giorno;
- stagione;
- ambiente.

---

## 16. Fantasy ed elementi non realistici

Il sistema deve poter rappresentare materia immaginaria senza modificare il core.

Esempi:

- fuoco magico;
- ghiaccio magico;
- cristalli energetici;
- nebbia soprannaturale;
- materia oscura;
- energia elementale;
- sostanze alchemiche.

Il principio architetturale è:

**il core rappresenta proprietà e comportamento; il preset definisce la semantica specifica.**

---

## 17. Persistenza e identità

Non tutti gli elementi naturali devono possedere una vera identità persistente.

### Elementi che possono avere identità

- albero specifico;
- roccia specifica;
- cristallo specifico;
- pianta specifica;
- elemento naturale utilizzato come asset.

### Elementi normalmente privi di identità individuale

- pioggia;
- nebbia;
- vento;
- fumo;
- polvere atmosferica;
- nuvole generiche.

Il sistema deve quindi distinguere:

**Persistent Natural Asset**

da

**Transient Natural Phenomenon**.

---

## 18. Variazione procedurale

La natura richiede variazione.

Il sistema deve supportare:

- seed;
- range;
- distribuzioni;
- variazioni locali;
- variazioni globali;
- pattern ripetibili;
- variazioni dipendenti dall'ambiente.

Esempio:

Un bosco può utilizzare la stessa definizione di specie ma generare alberi differenti mantenendo:

- struttura coerente;
- palette coerente;
- dimensioni plausibili;
- distribuzione controllata.

---

## 19. Integrazione con Environment & World Engine

Il Nature & Matter Engine deve poter ricevere informazioni dall'ambiente.

Esempi:

**Temperatura**

può modificare:

- ghiaccio;
- neve;
- acqua;
- vegetazione;
- nebbia.

**Umidità**

può modificare:

- terreno;
- vegetazione;
- superfici;
- nebbia.

**Vento**

può modificare:

- fumo;
- nuvole;
- foglie;
- erba;
- pioggia;
- polvere.

L'Environment Engine non deve duplicare queste proprietà.

Deve fornire il contesto.

---

## 20. Integrazione con Entity Core

Quando sarà introdotto un Entity Core condiviso, il Nature & Matter Engine potrà utilizzare componenti comuni quali:

- identity;
- metadata;
- tags;
- variation;
- serialization;
- transformation;
- validation.

Tuttavia, materia e fenomeni devono mantenere i propri modelli specialistici.

---

## 21. Integrazione con Human Engine

Gli elementi naturali possono interagire con gli esseri umani.

Esempi:

- pioggia sui vestiti;
- fango sulle scarpe;
- neve sui capelli;
- polvere sulla pelle;
- acqua bagnata sulla superficie;
- vegetazione che circonda il soggetto.

L'interazione deve essere rappresentabile senza incorporare la logica umana nel Nature & Matter Engine.

---

## 22. Integrazione con Creature Engine

Analogamente devono essere supportate interazioni quali:

- pelo bagnato;
- fango;
- neve;
- polline;
- polvere;
- vegetazione;
- acqua;
- ghiaccio.

Il Nature Engine fornisce la materia.

Il Creature Engine mantiene l'identità della creatura.

---

## 23. Integrazione con Object & Technology Engine

Gli oggetti possono essere:

- coperti di neve;
- bagnati;
- ricoperti di polvere;
- immersi nell'acqua;
- ricoperti di muschio;
- danneggiati dall'erosione;
- incendiati;
- congelati.

La materia deve rimanere un componente indipendente.

---

## 24. Prompt e Conditioning

Il motore deve poter convertire il modello strutturato in rappresentazioni utilizzabili dal sistema generativo.

Pipeline concettuale:

```
Natural Matter Definition
        ↓
Semantic Representation
        ↓
Material / Phenomenon Description
        ↓
Prompt Components
        ↓
Conditioning
        ↓
Generation
```

La rappresentazione testuale deve essere derivata dal modello strutturato.

---

## 25. Separazione dallo Style Engine

Il Nature & Matter Engine non deve contenere direttamente:

- stile anime;
- stile cinematografico;
- stile pittorico;
- pixel art;
- fumetto;
- fotorealismo.

Può invece fornire proprietà semantiche come:

- wet surface;
- crystalline ice;
- dense fog;
- rough bark;
- volcanic rock.

Lo Style Engine determina come queste proprietà vengono rappresentate visivamente.

---

## 26. Reference Sheet

Gli elementi naturali persistenti possono utilizzare Reference Sheet specializzate.

Tipologie:

- Material Sheet;
- Vegetation Sheet;
- Natural Asset Sheet;
- Phenomenon Sheet;
- Geological Sheet.

Non tutti i fenomeni transitori richiedono una Reference Sheet tradizionale.

Per fenomeni dinamici può essere più appropriata una rappresentazione comprendente:

- stato;
- comportamento;
- distribuzione;
- variazioni;
- condizioni ambientali.

---

## 27. Transformation Engine

Il motore deve essere compatibile con trasformazioni quali:

- acqua → ghiaccio;
- ghiaccio → acqua;
- neve → acqua;
- terreno → fango;
- pianta giovane → pianta adulta;
- pianta → pianta danneggiata;
- roccia → roccia erosa;
- materiale asciutto → materiale bagnato.

La trasformazione deve preservare le proprietà non interessate dal cambiamento.

---

## 28. Preset Architecture

I preset devono essere modulari.

Esempio concettuale:

```
water_clear
water_murky
water_ocean
water_river
water_frozen
```

Un preset può definire:

- categoria;
- proprietà;
- valori predefiniti;
- range;
- compatibilità;
- tags;
- trasformazioni disponibili;
- interazioni ambientali.

Il core non deve essere modificato per aggiungere nuovi preset.

---

## 29. Schema e serializzazione

Ogni definizione deve poter essere serializzata.

Lo schema deve essere:

- leggibile;
- versionabile;
- estensibile;
- validabile;
- compatibile con migrazioni future.

La serializzazione deve preservare almeno:

- tipo;
- categoria;
- stato;
- proprietà;
- seed;
- variazioni;
- trasformazioni;
- metadata.

---

## 30. Determinismo

Quando viene specificato un seed, la generazione procedurale deve essere riproducibile.

Lo stesso:

- input;
- seed;
- preset;
- configurazione;

deve produrre la stessa descrizione procedurale.

Il determinismo è importante per:

- test;
- debugging;
- Reference Sheet;
- variazioni controllate;
- workflow riproducibili.

---

## 31. Validazione

Il sistema deve verificare:

- categorie valide;
- stati compatibili;
- range numerici;
- proprietà coerenti;
- transizioni valide;
- parametri obbligatori;
- valori incompatibili.

Esempio:

un materiale definito come ghiaccio non dovrebbe avere automaticamente proprietà incoerenti con lo stato dichiarato, salvo override esplicito.

---

## 32. Gestione degli errori

Gli errori devono essere:

- espliciti;
- leggibili;
- localizzabili;
- non distruttivi.

Il sistema dovrebbe distinguere tra:

- errore di schema;
- parametro mancante;
- valore fuori range;
- categoria inesistente;
- trasformazione non supportata;
- incompatibilità ambientale;
- preset inesistente.

---

## 33. Test Strategy

Il motore dovrà essere coperto da test per:

### Tassonomia

- categorie;
- registrazione;
- ricerca.

### Proprietà

- validazione;
- range;
- conversione.

### Stati

- solidi;
- liquidi;
- gas;
- transizioni.

### Proceduralità

- seed;
- determinismo;
- variazioni.

### Fenomeni

- nebbia;
- fumo;
- pioggia;
- vento;
- fuoco.

### Vegetazione

- crescita;
- variazioni;
- stagioni.

### Integrazione

- Environment Engine;
- Human Engine;
- Creature Engine;
- Object Engine;
- Transformation Engine;
- Reference Sheet System.

---

## 34. Migrazione

Il nuovo motore deve poter essere introdotto senza rompere le funzionalità esistenti.

La strategia prevista è:

1. definizione dello schema;
2. implementazione del core;
3. test isolati;
4. preset iniziali;
5. adapter per dati esistenti;
6. integrazione con gli altri engine;
7. test ComfyUI;
8. migrazione progressiva.

Nessuna sostituzione massiva deve essere eseguita prima della validazione.

---

## 35. Stato attuale

Questo documento definisce l'architettura target.

Non implica che tutte le funzionalità descritte siano già implementate.

Lo stato attuale di CharacterForge contiene:

- preset di stile;
- Style Transfer;
- controlli di genere;
- controlli etnici;
- controllo del corpo;
- conditioning;
- sistema LoRA;
- sistemi cinematici;
- infrastruttura di preset.

Il Nature & Matter Engine costituisce un'estensione architetturale futura.

---

## 36. Debito architetturale previsto

Prima dell'implementazione saranno probabilmente necessari:

- schema condiviso;
- Entity Core;
- sistema di registrazione;
- sistema di validazione;
- sistema di serializzazione;
- registry dei preset;
- sistema di trasformazioni;
- interfaccia comune con Environment Engine.

Questi elementi devono essere progettati evitando duplicazioni tra engine.

---

## 37. Relazioni con gli altri Engine

Il Nature & Matter Engine si collega direttamente a:

- Style Engine;
- Human Engine;
- Creature Engine;
- Object & Technology Engine;
- Environment & World Engine;
- Camera & Cinematography Engine;
- Transformation Engine;
- Reference Sheet System.

La relazione principale è:

**Nature & Matter definisce cosa è la materia o il fenomeno.**

Gli altri engine definiscono:

- dove si trova;
- come interagisce;
- come viene trasformato;
- come viene osservato;
- come viene rappresentato.

---

## 38. Regola architetturale fondamentale

CharacterForge deve distinguere sempre:

**WHAT**

da

**HOW**.

Il Nature & Matter Engine descrive:

- che materia esiste;
- quali proprietà possiede;
- quale stato ha;
- come si comporta;
- come varia;
- come interagisce.

Non decide autonomamente:

- stile artistico;
- linguaggio cinematografico;
- composizione finale;
- modello generativo;
- estetica finale.

La materia deve rimanere indipendente dalla sua rappresentazione.

---

## 39. Estensibilità futura

Il sistema dovrà poter essere esteso verso:

- sistemi biologici;
- ecosistemi;
- simulazione ambientale semplificata;
- materiali fantasy;
- alchimia;
- magia elementale;
- fenomeni extraterrestri;
- ambienti alieni;
- sistemi climatici;
- particellari avanzati;
- interazioni fisiche più sofisticate.

L'architettura deve consentire queste estensioni senza modificare il nucleo fondamentale.

---

## 40. Conclusione

Il **Nature & Matter Engine** costituisce il livello semantico dedicato alla natura, alla materia e ai fenomeni dinamici.

Il suo compito è trasformare concetti naturali complessi in strutture:

- coerenti;
- parametrizzabili;
- serializzabili;
- trasformabili;
- riproducibili;
- integrabili;
- indipendenti dallo stile.

La progettazione deve mantenere una separazione rigorosa tra:

**materia → proprietà → comportamento → ambiente → rappresentazione.**

Questo principio permetterà a CharacterForge di trattare la natura non come semplice testo aggiuntivo nel prompt, ma come una componente strutturata del mondo generato.

---

**Documento 06 completato — Nature & Matter Engine**
