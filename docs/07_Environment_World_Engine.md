# CharacterForge — Environment & World Engine

**Documento:** 07 — Environment & World Engine  
**Versione architetturale:** 1.0  
**Stato:** Architecture Baseline  
**Progetto:** ComfyUI-CharacterForge

---

## 1. Scopo

L'**Environment & World Engine** definisce il sistema con cui CharacterForge rappresenta ambienti, luoghi, mondi e contesti spaziali complessi.

Il motore deve permettere di descrivere in modo strutturato:

- ambienti naturali;
- ambienti urbani;
- ambienti architettonici;
- interni;
- esterni;
- biomi;
- paesaggi;
- strutture;
- insediamenti;
- mondi fantasy;
- mondi fantascientifici;
- condizioni atmosferiche;
- stagioni;
- ora del giorno;
- scala;
- profondità;
- composizione spaziale;
- elementi presenti nell'ambiente.

L'obiettivo è separare il concetto di **mondo/ambiente** dalla sua rappresentazione visiva.

Un ambiente deve poter essere descritto indipendentemente dallo stile artistico, dal modello generativo e dalla tecnica di rendering.

---

## 2. Principi fondamentali

### 2.1 Ambiente come struttura

Un ambiente non deve essere rappresentato esclusivamente tramite una stringa di prompt.

Deve essere un insieme strutturato di:

- identità;
- tipo;
- spazio;
- elementi;
- materiali;
- atmosfera;
- illuminazione;
- tempo;
- condizioni;
- relazioni spaziali;
- variazioni.

### 2.2 Separazione tra ambiente e contenuto

L'ambiente definisce il contesto.

Gli altri engine definiscono gli elementi contenuti nel contesto.

Esempio:

- Environment Engine → foresta;
- Nature & Matter Engine → alberi, erba, foglie, nebbia;
- Human Engine → personaggio;
- Creature Engine → animale;
- Object Engine → veicolo;
- Camera Engine → punto di vista.

### 2.3 Separazione tra mondo e stile

Una città non deve diventare automaticamente:

- fotorealistica;
- anime;
- cinematografica;
- pittorica;
- pixel art.

Lo stile viene applicato separatamente.

### 2.4 Coerenza spaziale

La posizione relativa degli elementi deve poter essere mantenuta.

Il sistema deve poter distinguere:

- foreground;
- midground;
- background;
- elemento principale;
- elemento secondario;
- elemento distante.

---

## 3. Gerarchia ambientale

L'ambiente deve poter essere rappresentato attraverso una gerarchia.

Schema concettuale:

```
World
 └── Region
      └── Environment
           ├── Zone
           │    ├── Area
           │    └── Area
           └── Elements
```

La gerarchia deve essere flessibile.

Non tutti gli ambienti devono richiedere tutti i livelli.

---

## 4. Tipologie di ambiente

Categorie iniziali:

- Natural;
- Urban;
- Rural;
- Architectural;
- Interior;
- Exterior;
- Industrial;
- Coastal;
- Mountain;
- Desert;
- Forest;
- Jungle;
- Arctic;
- Swamp;
- Cave;
- Underground;
- Underwater;
- Space;
- Alien;
- Fantasy;
- Sci-Fi;
- Post-Apocalyptic;
- Historical.

La tassonomia deve essere estensibile.

---

## 5. Identità dell'ambiente

Un ambiente persistente può possedere una propria identità.

Esempi:

- una città specifica;
- un castello specifico;
- una casa specifica;
- una foresta specifica;
- una stanza specifica;
- una valle specifica.

L'identità può comprendere:

- nome;
- ID;
- categoria;
- descrizione;
- tags;
- metadata;
- seed;
- caratteristiche persistenti.

---

## 6. Coordinate e spazio

Il modello ambientale deve poter supportare una rappresentazione spaziale astratta.

Possibili proprietà:

- posizione;
- scala;
- orientamento;
- dimensione;
- altezza;
- profondità;
- distanza;
- direzione.

Non è necessario imporre inizialmente un sistema 3D completo.

Il modello deve però essere progettato in modo compatibile con future rappresentazioni:

- 2D;
- 2.5D;
- 3D;
- prospettive cinematografiche.

---

## 7. Zone e aree

Un ambiente complesso può essere suddiviso in zone.

Esempio:

**Castello**

- ingresso;
- cortile;
- sala principale;
- corridoio;
- torre;
- sotterraneo.

Ogni zona può possedere:

- identità;
- proprietà;
- elementi;
- atmosfera;
- illuminazione;
- accessi;
- relazioni con altre zone.

---

## 8. Elementi ambientali

Un ambiente può contenere:

- personaggi;
- creature;
- oggetti;
- edifici;
- vegetazione;
- rocce;
- acqua;
- neve;
- veicoli;
- strutture;
- particelle;
- fenomeni atmosferici.

Gli elementi non devono essere duplicati nell'Environment Engine.

Il motore deve referenziare o contenere composizioni di elementi provenienti dagli altri engine.

---

## 9. Biomi

Il sistema deve supportare il concetto di biome.

Esempi:

- foresta temperata;
- foresta tropicale;
- deserto;
- tundra;
- palude;
- savana;
- montagna;
- costa;
- ambiente oceanico.

Un biome può definire:

- vegetazione dominante;
- terreno;
- umidità;
- temperatura;
- fauna;
- atmosfera;
- palette naturale;
- condizioni meteorologiche prevalenti.

Il biome non deve essere confuso con uno stile visivo.

---

## 10. Terreno

Il terreno deve poter essere descritto tramite proprietà quali:

- tipo;
- pendenza;
- altitudine;
- composizione;
- umidità;
- erosione;
- vegetazione;
- copertura;
- irregolarità.

Esempi:

- roccioso;
- sabbioso;
- fangoso;
- erboso;
- innevato;
- vulcanico.

La materia specifica appartiene al Nature & Matter Engine.

L'Environment Engine definisce come tale materia costituisce il terreno dell'ambiente.

---

## 11. Architettura e strutture

Il motore deve poter contenere strutture architettoniche.

Esempi:

- casa;
- palazzo;
- castello;
- tempio;
- ponte;
- strada;
- fabbrica;
- stazione;
- rovina.

La geometria e l'identità della struttura possono essere gestite dall'Object & Technology Engine.

L'Environment Engine definisce invece:

- posizione;
- relazione con il territorio;
- organizzazione;
- contesto;
- accessibilità;
- ruolo nello spazio.

---

## 12. Interni

Gli ambienti interni devono essere trattati come spazi strutturati.

Parametri:

- dimensioni;
- pareti;
- pavimento;
- soffitto;
- aperture;
- porte;
- finestre;
- arredamento;
- fonti luminose;
- materiali;
- atmosfera.

Esempio:

**Camera da letto**

può contenere:

- letto;
- comodino;
- armadio;
- finestra;
- lampada;
- tappeto;
- oggetti personali.

Gli oggetti rimangono entità separate.

---

## 13. Esterni

Gli ambienti esterni devono poter descrivere:

- terreno;
- orizzonte;
- vegetazione;
- strutture;
- acqua;
- cielo;
- atmosfera;
- condizioni meteorologiche;
- distanza.

Devono essere supportati sia ambienti aperti sia ambienti parzialmente confinati.

---

## 14. Cielo e atmosfera

Il cielo deve poter essere descritto separatamente dall'ambiente terrestre.

Parametri:

- stato del cielo;
- copertura nuvolosa;
- colore;
- visibilità;
- foschia;
- umidità;
- particolato;
- fenomeni atmosferici.

Il sistema deve permettere di rappresentare:

- cielo sereno;
- nuvoloso;
- coperto;
- temporalesco;
- alba;
- tramonto;
- notte;
- cielo fantastico;
- cielo alieno.

---

## 15. Meteo

Il meteo deve essere rappresentato come stato ambientale.

Parametri:

- temperatura;
- umidità;
- vento;
- precipitazioni;
- pressione astratta;
- visibilità;
- nuvolosità;
- intensità.

Fenomeni:

- sole;
- pioggia;
- neve;
- grandine;
- nebbia;
- temporale;
- vento;
- polvere;
- fulmini.

Il Nature & Matter Engine definisce il fenomeno.

L'Environment Engine definisce le condizioni in cui il fenomeno avviene.

---

## 16. Tempo

L'ambiente deve supportare una dimensione temporale.

Livelli:

- epoca;
- anno;
- stagione;
- giorno;
- ora;
- momento della giornata.

Esempi:

- estate;
- inverno;
- alba;
- mattina;
- mezzogiorno;
- pomeriggio;
- tramonto;
- crepuscolo;
- notte.

Il tempo può modificare:

- illuminazione;
- vegetazione;
- meteo;
- attività;
- colori naturali;
- presenza di elementi.

---

## 17. Stagioni

Le stagioni devono poter modificare l'ambiente.

Esempio:

**Foresta**

Estate:
- fogliame pieno;
- vegetazione intensa;
- luce calda.

Autunno:
- foglie colorate;
- caduta delle foglie;
- maggiore umidità.

Inverno:
- vegetazione ridotta;
- neve;
- alberi spogli.

Primavera:
- germogli;
- fioritura;
- vegetazione crescente.

La stagione deve essere un parametro ambientale e non un preset visivo obbligatorio.

---

## 18. Illuminazione ambientale

L'Environment Engine deve descrivere le condizioni luminose globali.

Parametri:

- direzione principale;
- intensità;
- temperatura cromatica;
- luce ambientale;
- luce diffusa;
- ombre;
- contrasto;
- condizioni atmosferiche.

La cinematografia dettagliata appartiene al Camera & Cinematography Engine.

---

## 19. Scala

Il sistema deve mantenere una nozione coerente della scala.

Esempi:

- stanza;
- edificio;
- quartiere;
- città;
- regione;
- pianeta;
- mondo.

La scala influenza:

- profondità;
- densità;
- distanza;
- dimensione percepita;
- composizione.

---

## 20. Densità ambientale

Un ambiente può avere diversa densità di elementi.

Esempi:

- foresta rada;
- foresta densa;
- città poco popolata;
- città affollata;
- interno minimalista;
- mercato caotico.

La densità deve essere parametrica.

---

## 21. Distribuzione degli elementi

Il sistema deve poter definire come gli elementi vengono distribuiti.

Parametri:

- uniforme;
- casuale;
- cluster;
- lineare;
- radiale;
- gerarchica;
- procedurale.

Esempio:

gli alberi di una foresta non devono essere necessariamente distribuiti uniformemente.

---

## 22. Relazioni spaziali

Gli elementi devono poter avere relazioni semantiche.

Esempi:

- vicino a;
- lontano da;
- davanti a;
- dietro;
- sopra;
- sotto;
- dentro;
- fuori;
- accanto;
- al centro;
- ai margini.

Questo sistema sarà importante per la generazione di scene coerenti.

---

## 23. Foreground, Midground e Background

Il sistema deve supportare una suddivisione compositiva astratta.

### Foreground

Elementi vicini alla camera.

### Midground

Area principale della scena.

### Background

Elementi distanti.

Questa suddivisione non sostituisce la Camera Engine.

Serve a fornire informazioni spaziali preliminari.

---

## 24. Profondità

La profondità ambientale può essere rappresentata tramite:

- distanza;
- stratificazione;
- prospettiva;
- atmosfera;
- scala;
- occlusione;
- densità.

La profondità deve poter essere modificata senza alterare necessariamente l'identità degli elementi.

---

## 25. Ambiente dinamico

Alcuni ambienti devono poter essere dinamici.

Esempi:

- mare;
- foresta al vento;
- città trafficata;
- temporale;
- incendio;
- mercato;
- stazione.

Il sistema deve distinguere:

- stato statico;
- stato dinamico;
- fenomeni temporanei.

---

## 26. Ambiente procedurale

Il motore deve supportare ambienti generabili proceduralmente.

Esempi:

- foresta;
- deserto;
- montagna;
- città;
- dungeon;
- pianeta alieno.

Parametri:

- seed;
- dimensione;
- densità;
- distribuzione;
- clima;
- biome;
- topologia astratta;
- regole di generazione.

Il seed deve consentire la riproducibilità.

---

## 27. Persistenza

Un ambiente persistente deve poter mantenere:

- identità;
- struttura;
- elementi;
- modifiche;
- stato;
- varianti.

Esempio:

Una casa specifica può essere:

**giorno 1 → integra**

**giorno 2 → danneggiata**

**giorno 3 → abbandonata**

La persistenza non deve essere obbligatoria per ogni ambiente generato.

---

## 28. Variazione controllata

Il sistema deve distinguere tra:

- variazione dell'ambiente;
- variazione degli elementi;
- variazione atmosferica;
- variazione temporale;
- trasformazione permanente.

Questo permette di generare più versioni dello stesso luogo senza perdere la sua identità.

---

## 29. Fantasy e fantascienza

Il motore deve supportare mondi non realistici.

Esempi:

- foreste magiche;
- città volanti;
- pianeti alieni;
- castelli impossibili;
- deserti extraterrestri;
- città cyberpunk;
- ambienti dimensionali.

La logica deve rimanere compatibile con il modello generale:

**World → Environment → Zone → Elements → Conditions**

---

## 30. Integrazione con Nature & Matter Engine

Il Nature & Matter Engine fornisce:

- acqua;
- neve;
- roccia;
- terreno;
- vegetazione;
- nebbia;
- fumo;
- polvere;
- fenomeni naturali.

L'Environment Engine stabilisce:

- dove;
- quanto;
- in quale condizione;
- in quale stagione;
- con quale distribuzione.

---

## 31. Integrazione con Human Engine

L'ambiente può contenere esseri umani.

Il sistema deve poter definire:

- posizione;
- zona;
- relazione con l'ambiente;
- attività;
- distanza;
- visibilità.

L'identità e l'anatomia rimangono responsabilità dell'Human Engine.

---

## 32. Integrazione con Creature Engine

Le creature possono essere associate a:

- habitat;
- biome;
- territorio;
- posizione;
- gruppo;
- distanza;
- ambiente preferito.

Il Creature Engine mantiene l'identità della creatura.

---

## 33. Integrazione con Object & Technology Engine

Gli oggetti possono essere collocati nell'ambiente.

Esempi:

- automobili su una strada;
- mobili in una stanza;
- armi in una sala;
- macchinari in una fabbrica;
- veicoli in un parcheggio.

L'Environment Engine gestisce il contesto spaziale.

---

## 34. Prompt e Conditioning

Il modello ambientale deve essere convertibile in componenti semantiche.

Pipeline:

```
World Definition
      ↓
Environment Structure
      ↓
Semantic Scene Description
      ↓
Prompt Components
      ↓
Conditioning
      ↓
Generation
```

La descrizione deve essere derivata dalla struttura.

---

## 35. Separazione dallo Style Engine

Il World Engine non deve contenere direttamente:

- anime;
- manga;
- fotorealismo;
- pittura;
- pixel art;
- cinematografia specifica.

Può invece descrivere:

- città medievale;
- foresta umida;
- appartamento moderno;
- deserto roccioso;
- stazione ferroviaria.

Lo Style Engine determina la rappresentazione estetica.

---

## 36. Reference Sheet

Gli ambienti persistenti devono poter utilizzare Reference Sheet dedicate.

Tipologie:

- Environment Sheet;
- Location Sheet;
- Architecture Sheet;
- World Sheet;
- Biome Sheet;
- Interior Sheet.

Una Environment Sheet può includere:

- vista generale;
- vista frontale;
- vista laterale;
- vista dall'alto;
- elementi principali;
- palette;
- materiali;
- condizioni atmosferiche.

La struttura finale sarà definita dal Reference Sheet System.

---

## 37. Camera Independence

L'ambiente deve essere indipendente dalla camera.

Una location deve poter essere osservata da:

- fronte;
- retro;
- lato;
- alto;
- basso;
- distanza ravvicinata;
- distanza panoramica.

La Camera & Cinematography Engine definisce successivamente:

- lente;
- inquadratura;
- prospettiva;
- movimento;
- profondità di campo;
- linguaggio cinematografico.

---

## 38. Transformation Engine

Gli ambienti devono poter essere trasformati.

Esempi:

- giorno → notte;
- estate → inverno;
- città integra → città distrutta;
- foresta → foresta bruciata;
- casa abitata → casa abbandonata;
- terreno asciutto → terreno allagato;
- ambiente pulito → ambiente degradato.

La trasformazione deve preservare, quando possibile, l'identità della location.

---

## 39. Preset Architecture

I preset ambientali devono essere modulari.

Esempi:

```
temperate_forest
desert_canyon
medieval_castle
modern_apartment
industrial_factory
alien_planet
fantasy_village
```

Un preset può definire:

- categoria;
- biome;
- condizioni;
- elementi suggeriti;
- materiali;
- densità;
- atmosfera;
- tags;
- compatibilità.

Il core non deve essere modificato per aggiungere preset.

---

## 40. Schema e serializzazione

La definizione ambientale deve essere serializzabile.

Lo schema deve poter contenere:

- identity;
- type;
- hierarchy;
- zones;
- elements;
- spatial relations;
- climate;
- time;
- season;
- lighting;
- atmosphere;
- seed;
- variations;
- transformations;
- metadata.

Lo schema deve essere versionabile e migrabile.

---

## 41. Determinismo

Gli ambienti procedurali devono supportare seed deterministici.

Lo stesso:

- world definition;
- environment definition;
- seed;
- preset;
- configuration;

deve produrre una struttura equivalente.

Questo è necessario per:

- test;
- debugging;
- Reference Sheet;
- workflow riproducibili;
- varianti controllate.

---

## 42. Validazione

Il sistema deve verificare:

- categorie valide;
- gerarchie valide;
- riferimenti corretti;
- zone valide;
- relazioni spaziali valide;
- range;
- condizioni compatibili;
- preset esistenti;
- trasformazioni supportate.

Gli errori devono essere individuabili senza dover analizzare l'intero workflow.

---

## 43. Gestione degli errori

Il sistema deve distinguere almeno:

- invalid world;
- invalid environment;
- invalid zone;
- invalid element reference;
- invalid spatial relation;
- invalid condition;
- invalid transformation;
- invalid preset;
- schema error.

Gli errori devono essere leggibili e non distruttivi.

---

## 44. Test Strategy

Il motore dovrà essere coperto da test per:

### Gerarchia

- world;
- region;
- environment;
- zone;
- area.

### Spazio

- posizione;
- distanza;
- relazioni;
- profondità.

### Condizioni

- meteo;
- stagione;
- ora;
- temperatura;
- atmosfera.

### Proceduralità

- seed;
- distribuzione;
- densità;
- determinismo.

### Integrazione

- Nature & Matter;
- Human;
- Creature;
- Object;
- Camera;
- Transformation;
- Reference Sheet.

---

## 45. Migrazione

L'introduzione del World Engine deve avvenire progressivamente.

Ordine previsto:

1. definizione schema;
2. definizione Environment Core;
3. sistema di zone;
4. sistema di elementi;
5. relazioni spaziali;
6. condizioni ambientali;
7. preset;
8. integrazione con gli altri engine;
9. test;
10. integrazione ComfyUI.

Nessuna riscrittura globale deve essere eseguita prima della validazione.

---

## 46. Stato attuale

Questo documento rappresenta l'architettura target.

Non implica che il World Engine sia già implementato.

CharacterForge dispone attualmente di:

- Style Engine e preset;
- controlli Human;
- sistemi Creature in progettazione;
- Object Engine in progettazione;
- Nature & Matter in progettazione;
- sistemi cinematici;
- Style Transfer;
- conditioning;
- workflow ComfyUI.

Il World Engine costituisce il livello di orchestrazione spaziale e ambientale futuro.

---

## 47. Debito architetturale previsto

Prima dell'implementazione saranno necessari:

- Entity Core;
- schema comune;
- registry;
- sistema di riferimenti;
- sistema di coordinate astratte;
- validazione;
- serializzazione;
- trasformazioni;
- gestione dei seed;
- integrazione con Camera Engine.

Il design deve evitare duplicazioni tra engine.

---

## 48. Relazioni con gli altri Engine

Il World Engine si trova al centro della composizione ambientale.

Relazioni principali:

- Nature & Matter → materiali e fenomeni;
- Human → esseri umani;
- Creature → creature;
- Object & Technology → oggetti e strutture;
- Camera & Cinematography → osservazione;
- Transformation → cambiamenti;
- Reference Sheet → documentazione visiva;
- Style Engine → rappresentazione estetica.

Il World Engine organizza il contesto senza appropriarsi della responsabilità degli altri sistemi.

---

## 49. Regola architetturale fondamentale

CharacterForge deve distinguere:

**DOVE**

da

**CHE COSA**

e da

**COME VIENE RAPPRESENTATO**.

Il World Engine definisce:

- dove;
- quando;
- in quale ambiente;
- in quale zona;
- con quali relazioni spaziali;
- con quali condizioni.

Gli altri engine definiscono il contenuto.

Lo Style Engine definisce la rappresentazione.

La Camera Engine definisce il punto di osservazione.

---

## 50. Estensibilità futura

L'architettura deve poter evolvere verso:

- ecosistemi;
- città procedurali;
- continenti;
- pianeti;
- mondi persistenti;
- mappe;
- dungeon;
- sistemi di navigazione;
- simulazione ambientale;
- popolazioni;
- traffico;
- eventi;
- ambienti interattivi;
- world building avanzato.

Queste estensioni non devono richiedere la modifica del core fondamentale.

---

## 51. Conclusione

L'**Environment & World Engine** rappresenta il livello che organizza il mondo nel quale CharacterForge colloca entità, materia, strutture e fenomeni.

La pipeline concettuale diventa:

**World → Environment → Zone → Elements → Conditions → Observation**

con una separazione rigorosa tra:

- identità;
- spazio;
- contenuto;
- condizioni;
- trasformazione;
- rappresentazione.

Il principio fondamentale è:

**un luogo deve mantenere la propria identità anche quando cambiano camera, stile, stagione, condizioni atmosferiche o stato temporale.**

Questo permette a CharacterForge di evolvere da un sistema di preset visivi a un vero sistema strutturato di costruzione e mantenimento di mondi coerenti.

---

**Documento 07 completato — Environment & World Engine**
