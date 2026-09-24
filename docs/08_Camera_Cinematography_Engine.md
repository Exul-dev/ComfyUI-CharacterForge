# CharacterForge — Camera & Cinematography Engine

**Documento:** 08 — Camera & Cinematography Engine  
**Versione architetturale:** 1.0  
**Stato:** Architecture Baseline  
**Progetto:** ComfyUI-CharacterForge

---

## 1. Scopo

Il **Camera & Cinematography Engine** definisce il sistema con cui CharacterForge controlla il modo in cui un mondo, un ambiente, un'entità o una scena vengono osservati e rappresentati dal punto di vista della camera.

Il motore deve poter descrivere:

- posizione della camera;
- orientamento;
- altezza;
- distanza;
- angolo;
- tipo di inquadratura;
- lente;
- focale;
- campo visivo;
- prospettiva;
- profondità di campo;
- apertura;
- fuoco;
- bokeh;
- esposizione;
- movimento;
- composizione;
- punto di osservazione;
- rapporto tra soggetto e camera;
- linguaggio cinematografico.

Il motore deve inoltre poter interagire con la libreria cinematografica di CharacterForge senza fondere:

- camera;
- illuminazione;
- stile;
- colore;
- regia;
- identità del soggetto.

---

## 2. Principi fondamentali

### 2.1 Camera come sistema indipendente

La camera deve essere indipendente dall'identità dell'elemento osservato.

Lo stesso personaggio deve poter essere osservato:

- frontalmente;
- lateralmente;
- posteriormente;
- dall'alto;
- dal basso;
- da vicino;
- da lontano.

L'identità deve rimanere invariata.

### 2.2 Separazione tra soggetto e osservazione

Il soggetto definisce:

- chi o cosa è;
- aspetto;
- identità;
- struttura;
- proprietà.

La Camera Engine definisce:

- da dove viene osservato;
- con quale lente;
- a quale distanza;
- con quale composizione.

### 2.3 Separazione tra camera e stile

Una camera grandangolare non deve diventare automaticamente cinematografica.

Una lente lunga non deve implicare automaticamente uno specifico regista.

La cinematografia può utilizzare preset, ma la camera deve rimanere parametrica.

### 2.4 Separazione tra camera e illuminazione

La camera può descrivere l'esposizione e alcuni parametri ottici.

La definizione completa dell'illuminazione rimane separata.

---

## 3. Modello concettuale

La camera può essere rappresentata come:

```
Camera
 ├── Transform
 │    ├── Position
 │    ├── Rotation
 │    └── Target
 │
 ├── Optics
 │    ├── Lens
 │    ├── Focal Length
 │    ├── Aperture
 │    └── Focus
 │
 ├── Framing
 │    ├── Shot Size
 │    ├── Angle
 │    ├── Composition
 │    └── Subject Relation
 │
 ├── Exposure
 │
 └── Motion
```

Questa struttura è concettuale e potrà essere estesa.

---

## 4. Posizione della camera

La camera deve poter definire:

- posizione assoluta;
- posizione relativa al soggetto;
- altezza;
- distanza;
- offset;
- orientamento.

La posizione relativa è particolarmente importante per mantenere la coerenza tra varianti.

Esempio:

**camera 2 metri davanti al soggetto**

deve poter essere mantenuta anche quando cambia il soggetto.

---

## 5. Target e punto di interesse

La camera deve poter utilizzare un target.

Esempi:

- volto;
- torso;
- corpo intero;
- oggetto;
- veicolo;
- edificio;
- punto ambientale.

Questo consente di separare:

**dove si trova la camera**

da

**verso cosa guarda la camera**.

---

## 6. Angoli di ripresa

Il sistema deve supportare almeno:

- eye level;
- low angle;
- high angle;
- bird's-eye;
- worm's-eye;
- overhead;
- dutch angle;
- front;
- rear;
- side;
- three-quarter;
- profile.

Gli angoli devono essere parametrizzabili e non soltanto preset fissi.

---

## 7. Altezza della camera

L'altezza può essere:

- assoluta;
- relativa al soggetto;
- relativa al terreno.

Esempi:

- ground level;
- knee level;
- waist level;
- chest level;
- eye level;
- above head;
- aerial.

---

## 8. Distanza

Il sistema deve distinguere tra distanza camera-soggetto e scala dell'inquadratura.

Possibili categorie:

- extreme close;
- close;
- medium;
- medium long;
- long;
- extreme long.

La categoria deve poter essere accompagnata da un valore continuo.

---

## 9. Shot Size

Il sistema deve supportare almeno:

- Extreme Close-Up;
- Close-Up;
- Medium Close-Up;
- Medium Shot;
- Medium Long Shot;
- Full Shot;
- Long Shot;
- Extreme Long Shot.

Lo shot size deve essere indipendente dal tipo di lente.

---

## 10. Lenti

Il motore deve supportare modelli di lente.

Categorie concettuali:

- ultra-wide;
- wide;
- normal;
- short telephoto;
- telephoto;
- super telephoto;
- macro;
- fisheye.

La classificazione non deve essere rigida.

---

## 11. Focale

La focale deve essere rappresentata come valore continuo.

Esempi:

- 14 mm;
- 18 mm;
- 24 mm;
- 35 mm;
- 50 mm;
- 85 mm;
- 135 mm;
- 200 mm.

Il sistema deve poter usare valori intermedi.

---

## 12. Campo visivo

Il campo visivo può essere derivato dalla combinazione di:

- focale;
- sensore astratto;
- formato;
- crop factor.

Il modello deve consentire di aggiungere in futuro differenti formati di sensore.

---

## 13. Prospettiva

La prospettiva deve essere distinta dalla focale.

La percezione prospettica dipende principalmente dalla posizione relativa della camera rispetto al soggetto.

Il sistema deve quindi evitare di rappresentare la focale come sinonimo di prospettiva.

Questa distinzione è fondamentale per mantenere un comportamento cinematografico coerente.

---

## 14. Formato e sensore

Il sistema deve poter rappresentare:

- full frame;
- APS-C;
- medium format;
- large format;
- formato cinematografico astratto;
- formati personalizzati.

Parametri possibili:

- width;
- height;
- aspect ratio;
- crop factor;
- sensor characteristics.

---

## 15. Aspect Ratio

Il motore deve supportare rapporti quali:

- 1:1;
- 4:3;
- 3:2;
- 16:9;
- 16:10;
- 2.35:1;
- 2.39:1;
- 2.76:1;
- formati personalizzati.

L'aspect ratio non deve essere confuso con la risoluzione.

---

## 16. Apertura

L'apertura deve essere rappresentabile tramite:

- f-stop;
- valore continuo;
- profondità di campo risultante.

Esempi:

- f/1.2;
- f/1.4;
- f/2;
- f/2.8;
- f/4;
- f/5.6;
- f/8;
- f/11;
- f/16.

---

## 17. Profondità di campo

La profondità di campo deve poter essere controllata.

Parametri:

- focus distance;
- aperture;
- focal length;
- sensor format;
- subject distance.

Preset semantici:

- shallow;
- moderate;
- deep;
- infinite.

Il sistema deve mantenere la possibilità di utilizzare valori numerici.

---

## 18. Focus

Il focus deve poter essere definito come:

- manuale;
- automatico;
- subject-based;
- point-based;
- rack focus.

Il target di messa a fuoco può essere:

- volto;
- occhio;
- soggetto;
- oggetto;
- punto nello spazio.

---

## 19. Rack Focus

Il sistema deve supportare transizioni di fuoco.

Esempio:

**foreground → background**

oppure:

**character → object**.

Questo sarà particolarmente utile per scene narrative e cinematiche.

---

## 20. Bokeh

Il sistema può rappresentare:

- intensità;
- forma;
- morbidezza;
- qualità ottica;
- highlight behavior.

Il bokeh non deve essere trattato come semplice "blur".

---

## 21. Distorsione ottica

Devono poter essere rappresentati:

- barrel distortion;
- pincushion distortion;
- chromatic aberration;
- vignetting;
- lens flare;
- bloom ottico;
- edge distortion.

Questi effetti devono essere parametrici.

---

## 22. Motion Blur

Il sistema deve supportare:

- shutter speed;
- direzione;
- intensità;
- movimento della camera;
- movimento del soggetto.

Il motion blur deve essere distinto dal blur ottico derivante dalla profondità di campo.

---

## 23. Shutter

Il modello deve poter rappresentare:

- shutter speed;
- shutter angle;
- motion rendering.

Per un futuro sistema cinematografico può essere utile supportare sia:

- fotografia;
- cinema.

---

## 24. Esposizione

Parametri:

- ISO;
- shutter;
- aperture;
- exposure compensation.

L'esposizione deve essere rappresentata come proprietà della camera, senza obbligare il sistema a simulare fisicamente una macchina fotografica reale.

---

## 25. White Balance

Il sistema deve poter rappresentare:

- temperatura;
- tint;
- white balance;
- neutral;
- warm;
- cool.

La gestione cromatica avanzata rimane integrabile con i profili cinematografici.

---

## 26. Inquadratura

Il sistema deve poter definire la relazione tra camera e soggetti.

Esempi:

- centered;
- off-center;
- symmetrical;
- asymmetrical;
- leading lines;
- negative space;
- rule of thirds;
- golden ratio;
- balanced;
- intentionally unbalanced.

La composizione deve essere parametrica.

---

## 27. Composizione semantica

La camera può utilizzare obiettivi compositivi.

Esempi:

- enfatizzare il soggetto;
- isolare il soggetto;
- mostrare la scala;
- mostrare l'ambiente;
- creare tensione;
- creare simmetria;
- enfatizzare profondità;
- creare distanza.

Questi obiettivi non devono diventare automaticamente valutazioni estetiche.

Sono parametri di intenzione compositiva.

---

## 28. Linee e geometria

La composizione può considerare:

- linee guida;
- diagonali;
- simmetrie;
- archi;
- cornici naturali;
- prospettive convergenti;
- pattern.

Il sistema deve poter registrare queste intenzioni come metadati.

---

## 29. Negative Space

Il negative space deve essere rappresentabile.

Parametri:

- direzione;
- quantità;
- area;
- relazione con il soggetto.

Esempio:

**soggetto a sinistra + spazio vuoto a destra**

può essere rappresentato semanticamente senza fissare una particolare immagine.

---

## 30. Subject Framing

Il sistema deve poter specificare come il soggetto occupa il frame.

Parametri:

- percentuale del frame;
- posizione;
- margine superiore;
- margine laterale;
- spazio sopra la testa;
- spazio davanti al soggetto;
- crop.

Questo è importante per Reference Sheet e continuità visiva.

---

## 31. Multi-Subject Composition

Una scena può contenere più soggetti.

La camera deve poter definire:

- soggetto principale;
- soggetti secondari;
- priorità;
- distanza;
- relazione;
- disposizione.

Esempio:

**character A foreground + character B midground + environment background**.

---

## 32. Camera Movement

Per scene dinamiche devono essere supportati:

- pan;
- tilt;
- dolly;
- truck;
- pedestal;
- crane;
- orbit;
- tracking;
- handheld;
- static.

Il sistema deve poter descrivere sia lo stato iniziale sia quello finale.

---

## 33. Camera Path

Una traiettoria può essere descritta tramite:

- punti;
- curve;
- durata;
- velocità;
- accelerazione;
- easing.

La camera path deve essere serializzabile.

---

## 34. Cinematic Language

Il motore deve poter rappresentare concetti cinematografici come:

- establishing shot;
- master shot;
- close-up;
- insert;
- over-the-shoulder;
- two-shot;
- POV;
- tracking shot;
- dolly shot;
- static composition.

Questi concetti sono semanticamente distinti dai parametri fisici della camera.

---

## 35. POV

Il sistema deve supportare una camera associata al punto di vista di un'entità.

Esempi:

- human POV;
- creature POV;
- vehicle POV;
- first-person;
- observer POV.

La camera deve poter ereditare:

- posizione;
- altezza;
- orientamento;

dall'entità osservatrice.

---

## 36. Camera relativa al soggetto

Per mantenere la coerenza tra varianti, la camera deve poter essere definita relativamente al soggetto.

Esempio:

```
subject = character_A
position = front
height = eye_level
distance = 2m
target = face
```

Se cambia il personaggio, la relazione può essere mantenuta.

---

## 37. Camera e Reference Sheet

La Reference Sheet deve poter utilizzare configurazioni camera standardizzate.

Esempi:

- front;
- rear;
- left;
- right;
- three-quarter front;
- three-quarter rear;
- profile;
- full body;
- close-up.

Queste configurazioni devono essere riproducibili.

---

## 38. Camera e Environment Engine

L'Environment Engine fornisce:

- spazio;
- zone;
- elementi;
- condizioni.

La Camera Engine determina:

- punto di osservazione;
- framing;
- prospettiva;
- profondità;
- ottica.

La camera non deve modificare l'identità dell'ambiente.

---

## 39. Camera e Human Engine

La camera deve poter utilizzare punti di riferimento anatomici:

- occhi;
- volto;
- testa;
- torso;
- corpo intero.

Questo consente di costruire inquadrature coerenti.

---

## 40. Camera e Creature Engine

La stessa logica deve essere applicabile a creature.

Il target può essere:

- occhi;
- testa;
- corpo;
- elemento anatomico specifico.

L'altezza della camera può essere relativa alla creatura.

---

## 41. Camera e Object & Technology Engine

La camera deve supportare:

- prodotti;
- veicoli;
- edifici;
- oggetti tecnici;
- macchinari.

Possibili preset:

- product shot;
- technical shot;
- hero shot;
- architectural shot.

---

## 42. Camera e Nature & Matter Engine

La camera deve poter enfatizzare:

- texture;
- materiali;
- particelle;
- acqua;
- ghiaccio;
- vegetazione;
- fenomeni atmosferici.

La camera non modifica la materia.

---

## 43. Cinematography Profiles

Il sistema deve poter utilizzare profili cinematografici.

Un profilo può combinare:

- lente;
- framing;
- camera height;
- movement;
- focus;
- aspect ratio;
- exposure;
- lighting relationship;
- composition.

Questi profili possono essere utilizzati dai preset dei registi.

---

## 44. Director Presets

La libreria cinematografica esistente deve essere integrabile con questo motore.

Un preset cinematografico può definire preferenze relative a:

- ottiche;
- inquadrature;
- altezza camera;
- movimento;
- contrasto;
- profondità;
- composizione;
- atmosfera.

Il preset non deve sovrascrivere arbitrariamente i parametri esplicitamente impostati dall'utente.

---

## 45. Override e priorità

Il sistema deve definire una gerarchia di precedenza.

Ordine concettuale:

1. User Explicit Override
2. Scene Configuration
3. Cinematography Profile
4. Camera Preset
5. Engine Default

Un parametro esplicitamente impostato dall'utente deve avere precedenza su un preset.

---

## 46. Camera Preset Architecture

I preset devono essere modulari.

Esempi:

```
portrait_85mm
wide_establishing
macro_detail
architectural_24mm
cinematic_closeup
hero_product
overhead_scene
```

Un preset può definire soltanto alcuni parametri.

Gli altri devono essere ereditati.

---

## 47. Serializzazione

La camera deve poter essere serializzata.

Lo schema deve poter contenere:

- transform;
- target;
- optics;
- lens;
- focal length;
- sensor;
- aperture;
- focus;
- exposure;
- white balance;
- framing;
- composition;
- movement;
- profile;
- overrides;
- metadata.

---

## 48. Determinismo

A parità di:

- scena;
- camera definition;
- preset;
- seed;
- configurazione;

la descrizione della camera deve essere riproducibile.

Questo è essenziale per:

- Reference Sheet;
- test;
- workflow;
- variazioni;
- confronto tra versioni.

---

## 49. Validazione

Il sistema deve verificare:

- focal length valida;
- apertura valida;
- distanza valida;
- target esistente;
- aspect ratio valido;
- preset valido;
- valori compatibili;
- camera path valido.

Gli errori devono essere espliciti.

---

## 50. Gestione degli errori

Categorie minime:

- invalid camera;
- invalid lens;
- invalid target;
- invalid transform;
- invalid composition;
- invalid profile;
- invalid camera path;
- schema error.

Il sistema deve evitare configurazioni silenziosamente corrotte.

---

## 51. Test Strategy

Il motore dovrà includere test per:

### Ottica

- focale;
- sensore;
- campo visivo;
- apertura;
- focus.

### Framing

- shot size;
- posizione;
- crop;
- subject relation.

### Composizione

- symmetry;
- negative space;
- subject placement;
- multi-subject.

### Movimento

- pan;
- tilt;
- dolly;
- orbit;
- tracking;
- path.

### Integrazione

- Human;
- Creature;
- Object;
- Nature;
- Environment;
- Cinematic Profiles;
- Reference Sheet.

---

## 52. Migrazione

L'introduzione del Camera Engine deve seguire:

1. schema;
2. Camera Core;
3. optics;
4. framing;
5. composition;
6. focus;
7. movement;
8. cinematic profiles;
9. integrazione preset;
10. test;
11. integrazione ComfyUI.

Le funzionalità esistenti non devono essere sostituite senza test di compatibilità.

---

## 53. Stato attuale

Questo documento definisce l'architettura target.

CharacterForge possiede già una base cinematografica significativa, comprendente:

- profili skin;
- lighting profiles;
- lens profiles;
- film stocks;
- grain profiles;
- color profiles;
- atmosphere profiles;
- camera profiles;
- numerosi preset cinematografici associati a registi.

Questi elementi devono essere considerati patrimonio esistente e integrati progressivamente nel nuovo modello.

Il documento non implica che il nuovo Camera Engine sia già implementato.

---

## 54. Debito architetturale

Prima dell'implementazione sarà necessario:

- normalizzare i profili camera esistenti;
- definire uno schema comune;
- separare parametri camera da parametri stilistici;
- definire priorità e override;
- integrare i profili cinematografici;
- introdurre validazione;
- definire serializzazione;
- aggiungere test.

La normalizzazione deve evitare la perdita dei preset cinematografici già costruiti.

---

## 55. Relazioni con gli altri Engine

Il Camera & Cinematography Engine riceve informazioni da:

- Human Engine;
- Creature Engine;
- Object & Technology Engine;
- Nature & Matter Engine;
- Environment & World Engine.

Può inoltre interagire con:

- Style Engine;
- Transformation Engine;
- Reference Sheet System.

Il suo compito è trasformare la struttura della scena in una **configurazione osservativa coerente**.

---

## 56. Regola architetturale fondamentale

CharacterForge deve distinguere:

**WHAT**

da

**WHERE**

da

**HOW IT IS SEEN**

da

**HOW IT IS STYLED**.

Il Camera Engine controlla:

**HOW IT IS SEEN.**

Il World Engine controlla:

**WHERE.**

Gli entity engine controllano:

**WHAT.**

Lo Style Engine controlla:

**HOW IT IS STYLED.**

Questa separazione deve essere mantenuta anche nei workflow ComfyUI.

---

## 57. Estensibilità futura

Il motore deve poter evolvere verso:

- multi-camera;
- shot lists;
- storyboard;
- sequenze;
- continuità cinematografica;
- camera matching;
- virtual cinematography;
- tracking;
- previs;
- camera rigs;
- animazione della camera;
- simulazione ottica avanzata;
- analisi automatica dell'inquadratura.

Queste funzionalità devono poter essere aggiunte senza alterare il core.

---

## 58. Conclusione

Il **Camera & Cinematography Engine** rappresenta il sistema che stabilisce come CharacterForge osserva e inquadra il mondo.

La pipeline concettuale diventa:

**World → Scene → Subject → Camera → Optics → Framing → Composition → Cinematic Representation**

mantenendo separate:

- identità;
- ambiente;
- materia;
- camera;
- cinematografia;
- stile.

Il principio fondamentale è:

**la stessa scena deve poter essere osservata con camere differenti senza perdere la propria identità.**

Allo stesso modo, la stessa configurazione camera deve poter essere applicata a scene differenti mantenendo coerenti le proprie proprietà.

Questo costituisce la base per Reference Sheet, continuità tra varianti, preset cinematografici e futura generazione di sequenze narrative.

---

**Documento 08 completato — Camera & Cinematography Engine**
