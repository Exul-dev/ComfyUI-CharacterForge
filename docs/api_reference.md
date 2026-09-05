
# API Reference - ComfyUI-CharacterForge

## Panoramica

Questo documento descrive le API di tutti i nodi CharacterForge con specifiche tecniche complete per sviluppatori.

## CharacterForgeGenderController

### Informazioni Base

- Categoria: CharacterForge/Basic
- Funzione: apply_gender_control
- Return Types: CONDITIONING, STRING

### INPUT_TYPES

{
    "required": {
        "conditioning": ("CONDITIONING",),
        "gender": (["masculine", "feminine", "androgynous", "custom"],),
        "weight": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 1.5})
    },
    "optional": {
        "custom_prompt": ("STRING", {"default": "", "multiline": True})
    }
}

### Parametri

#### conditioning (CONDITIONING, richiesto)

Conditioning base da modificare. Deve provenire da un nodo CLIPTextEncode valido.

#### gender (COMBO, richiesto)

Valori disponibili:

- masculine: Soggetto maschile con caratteristiche mascoline
- feminine: Soggetto femminile con caratteristiche femminili
- androgynous: Soggetto androgino con caratteristiche neutre
- custom: Genere personalizzato tramite custom_prompt

#### weight (FLOAT, richiesto)

Range: 0.0 - 1.5

- 0.0: Nessun effetto sul conditioning
- 0.5: Effetto moderato
- 0.8: Effetto forte (consigliato)
- 1.0: Effetto massimo standard
- 1.5: Effetto amplificato

#### custom_prompt (STRING, opzionale)

Prompt personalizzato per genere custom. Richiesto quando gender="custom".

### Output

#### conditioning (CONDITIONING)

Conditioning modificato con caratteristiche di genere applicate.

#### applied_features (STRING)

Stringa JSON con dettagli delle features applicate.

### Esempio Utilizzo

from nodes.gender_controller import CharacterForgeGenderController

controller = CharacterForgeGenderController()
result = controller.apply_gender_control(
    conditioning=base_conditioning,
    gender="masculine",
    weight=0.8,
    custom_prompt=""
)

conditioning, features = result

### Esempio con Custom Gender

result = controller.apply_gender_control(
    conditioning=base_conditioning,
    gender="custom",
    weight=0.9,
    custom_prompt="Adult male, age 30-35, Italian features, dark wavy hair, olive skin"
)

conditioning, features = result

### Errori

#### ValueError: Conditioning non valido o vuoto

Causa: Il conditioning input è None o vuoto.

Soluzione: Verificare che il CLIPTextEncode upstream produca output valido.

#### ValueError: Prompt custom richiesto

Causa: gender="custom" ma custom_prompt vuoto.

Soluzione: Fornire un custom_prompt non vuoto quando gender="custom".

## CharacterForgeEthnicityController

### Informazioni Base

- Categoria: CharacterForge/Advanced
- Funzione: apply_ethnicity_control
- Return Types: CONDITIONING, STRING

### INPUT_TYPES

{
    "required": {
        "conditioning": ("CONDITIONING",),
        "primary_ethnicity": (["caucasian", "african", "asian", "latin", "mixed"],),
        "weight": ("FLOAT", {"default": 0.6, "min": 0.0, "max": 1.5})
    },
    "optional": {
        "secondary_ethnicity": (["none", "caucasian", "african", "asian", "latin"],),
        "skin_tone_override": ("STRING", {"default": ""}),
        "custom_details": ("STRING", {"default": "", "multiline": True})
    }
}

### Parametri

#### conditioning (CONDITIONING, richiesto)

Conditioning base da modificare.

#### primary_ethnicity (COMBO, richiesto)

Valori disponibili:

- caucasian: Etnia caucasica con pelle chiara
- african: Etnia africana con pelle scura
- asian: Etnia asiatica con pelle olivastra
- latin: Etnia latina con pelle ambrata
- mixed: Heritage misto non specifico

#### weight (FLOAT, richiesto)

Range: 0.0 - 1.5. Controlla l'intensità delle caratteristiche etniche.

#### secondary_ethnicity (COMBO, opzionale)

Etnia secondaria per creare mix. Default: "none".

Quando specificata, crea un heritage misto con influenza massima del 40% (basata sul weight).

#### skin_tone_override (STRING, opzionale)

Override specifico per il tono della pelle. Esempi:

- "deep bronze"
- "pale ivory"
- "golden olive"
- "warm tan"

#### custom_details (STRING, opzionale)

Dettagli etnici personalizzati aggiuntivi.

### Etnie Disponibili e Caratteristiche

#### caucasian

- skin: fair to light skin with neutral undertones
- facial: European facial features, high cheekbones, relatively narrow nose bridge
- hair: straight to wavy hair texture, color range from blonde to dark brown to red
- eyes: light colored eyes common (blue, green, hazel, gray), also brown

#### african

- skin: dark to deep brown skin with warm undertones
- facial: African facial features, full lips, wider nose bridge, prominent cheekbones
- hair: curly to coily afro-textured hair, black color
- eyes: dark brown eyes, almond-shaped

#### asian

- skin: light to olive skin with neutral undertones
- facial: East Asian facial features, almond-shaped eyes, flatter facial profile
- hair: straight black hair, thick texture
- eyes: dark brown almond-shaped eyes

#### latin

- skin: olive to tan skin with warm golden undertones
- facial: Latin American facial features, warm expressive features
- hair: dark wavy to curly hair, brown to black
- eyes: brown to dark brown eyes, expressive

### Output

#### conditioning (CONDITIONING)

Conditioning con caratteristiche etniche applicate.

#### ethnicity_details (STRING)

Stringa JSON con dettagli delle features etniche applicate.

### Esempio Utilizzo Base

from nodes.ethnicity_controller import CharacterForgeEthnicityController

controller = CharacterForgeEthnicityController()
result = controller.apply_ethnicity_control(
    conditioning=base_conditioning,
    primary_ethnicity="caucasian",
    weight=0.6
)

conditioning, details = result

### Esempio Multi-Etnia

result = controller.apply_ethnicity_control(
    conditioning=base_conditioning,
    primary_ethnicity="caucasian",
    secondary_ethnicity="asian",
    weight=0.7,
    skin_tone_override="light olive",
    custom_details="Mediterranean features with subtle Asian influence"
)

conditioning, details = result

### Esempio con Override

result = controller.apply_ethnicity_control(
    conditioning=base_conditioning,
    primary_ethnicity="african",
    weight=0.8,
    skin_tone_override="deep bronze"
)

conditioning, details = result

## CharacterForgeBodyController

### Informazioni Base

- Categoria: CharacterForge/Basic
- Funzione: apply_body_control
- Return Types: CONDITIONING, STRING

### INPUT_TYPES

{
    "required": {
        "conditioning": ("CONDITIONING",),
        "body_type": (["athletic", "slim", "curvy", "muscular", "average"],),
        "height": ("FLOAT", {"default": 175.0, "min": 150.0, "max": 200.0}),
        "weight": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 1.5}),
        "muscle_definition": (["low", "medium", "high"],),
        "body_fat": (["low", "medium", "high"],)
    },
    "optional": {
        "custom_proportions": ("STRING", {"default": "", "multiline": True}),
        "target_gender": (["unspecified", "male", "female"],)
    }
}

### Parametri

#### conditioning (CONDITIONING, richiesto)

Conditioning base da modificare.

#### body_type (COMBO, richiesto)

Valori disponibili:

- athletic: Fisico atletico tonico
- slim: Fisico snello esile
- curvy: Fisico curvilineo con curve pronunciate
- muscular: Fisico muscoloso massiccio
- average: Fisico normale proporzionato

#### height (FLOAT, richiesto)

Range: 150.0 - 200.0 cm. Default: 175.0.

Categorie automatiche:

- short: < 160 cm
- medium-short: 160-170 cm
- medium: 170-180 cm
- tall: 180-190 cm
- very tall: > 190 cm

#### weight (FLOAT, richiesto)

Range: 0.0 - 1.5. Peso dell'applicazione corporatura.

#### muscle_definition (COMBO, richiesto)

Valori disponibili:

- low: Minima definizione muscolare, fisico morbido
- medium: Definizione muscolare moderata, aspetto atletico
- high: Alta definizione muscolare, aspetto shredded/vascular

#### body_fat (COMBO, richiesto)

Valori disponibili:

- low: Basso grasso corporeo (8-12%), aspetto vascolare
- medium: Grasso corporeo normale (15-20%), aspetto sano
- high: Alto grasso corporeo (25-30%), aspetto morbido

#### custom_proportions (STRING, opzionale)

Proporzioni personalizzate aggiuntive. Esempi:

- "extra long legs"
- "broad back"
- "narrow waist"

#### target_gender (COMBO, opzionale)

Genere target per descrizioni specifiche:

- unspecified: Descrizioni neutre
- male: Descrizioni specifiche maschili
- female: Descrizioni specifiche femminili

### Database Corporatura

#### athletic

- description: athletic build, toned physique, visible muscle definition
- proportions: shoulders 1.2, waist 0.8, hips 0.9, muscle 0.7, fat 0.3
- height_range: 165-195 cm

#### slim

- description: slim build, slender physique, lean body
- proportions: shoulders 0.9, waist 0.7, hips 0.8, muscle 0.3, fat 0.2
- height_range: 160-185 cm

#### curvy

- description: curvy build, hourglass figure, pronounced curves
- proportions: shoulders 1.0, waist 0.6, hips 1.1, muscle 0.4, fat 0.5
- height_range: 155-180 cm

#### muscular

- description: muscular build, bodybuilder physique, massive muscle mass
- proportions: shoulders 1.4, waist 0.9, hips 0.9, muscle 0.9, fat 0.2
- height_range: 170-200 cm

#### average

- description: average build, normal proportions, healthy body type
- proportions: shoulders 1.0, waist 0.8, hips 0.9, muscle 0.5, fat 0.4
- height_range: 160-190 cm

### Output

#### conditioning (CONDITIONING)

Conditioning con corporatura applicata.

#### body_details (STRING)

Stringa JSON con dettagli corporatura applicata.

### Esempio Utilizzo

from nodes.body_controller import CharacterForgeBodyController

controller = CharacterForgeBodyController()
result = controller.apply_body_control(
    conditioning=base_conditioning,
    body_type="athletic",
    height=180.0,
    weight=0.8,
    muscle_definition="high",
    body_fat="low",
    target_gender="male"
)

conditioning, details = result

### Esempio Femminile Curvy

result = controller.apply_body_control(
    conditioning=base_conditioning,
    body_type="curvy",
    height=170.0,
    weight=0.7,
    muscle_definition="low",
    body_fat="high",
    custom_proportions="extra long legs, elegant posture",
    target_gender="female"
)

conditioning, details = result

## CharacterForgeWeightedConditioning

### Informazioni Base

- Categoria: CharacterForge/Advanced
- Funzione: combine_weighted
- Return Types: CONDITIONING, STRING

### INPUT_TYPES

{
    "required": {
        "base_conditioning": ("CONDITIONING",),
        "conditioning_1": ("CONDITIONING",),
        "weight_1": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.5}),
        "conditioning_2": ("CONDITIONING",),
        "weight_2": ("FLOAT", {"default": 0.8, "min": 0.0, "max": 1.5}),
        "conditioning_3": ("CONDITIONING",),
        "weight_3": ("FLOAT", {"default": 0.6, "min": 0.0, "max": 1.5}),
        "combination_method": (["weighted_sum", "average", "concat", "max", "blend"],),
        "preserve_structure": ("BOOLEAN", {"default": True})
    },
    "optional": {
        "structure_strength": ("FLOAT", {"default": 0.3, "min": 0.0, "max": 1.0})
    }
}

### Parametri

#### base_conditioning (CONDITIONING, richiesto)

Conditioning base che rappresenta lo schema layout del character sheet.

#### conditioning_1, conditioning_2, conditioning_3 (CONDITIONING, richiesto)

Conditioning aggiuntivi da combinare con il base. Tipicamente provengono dai controllers.

#### weight_1, weight_2, weight_3 (FLOAT, richiesto)

Range: 0.0 - 1.5. Pesi rispettivi per ogni conditioning aggiuntivo.

#### combination_method (COMBO, richiesto)

Metodi di combinazione disponibili:

- weighted_sum: Somma pesata con base al 50%
- average: Media aritmetica di tutti
- concat: Concatenazione sequenziale
- max: Massimo valore per dimensione
- blend: Interpolazione lineare verso base

#### preserve_structure (BOOLEAN, richiesto)

Default: True. Se attivo, preserva la struttura del conditioning base.

#### structure_strength (FLOAT, opzionale)

Range: 0.0 - 1.0. Default: 0.3. Forza con cui preservare la struttura base.

### Metodi di Combinazione

#### weighted_sum (Consigliato)

Formula:

Risultato = Base × 0.5 + (Cond1 × w1 + Cond2 × w2 + Cond3 × w3) × 0.5

Caratteristiche:

- Base ha influenza fissa del 50%
- Pesi normalizzati automaticamente
- Layout stabile

#### average

Formula:

Risultato = (Base + Cond1 + Cond2 + Cond3) / 4

Caratteristiche:

- Tutti i conditioning hanno uguale peso
- Layout meno stabile

#### concat

Formula:

Risultato = Concat(Base, Cond1, Cond2, Cond3)

Caratteristiche:

- Massime informazioni disponibili
- Simile a ConditioningConcat nativo
- Layout variabile

#### max

Formula:

Risultato = max(Base, Cond1 × w1, Cond2 × w2, Cond3 × w3)

Caratteristiche:

- Valori dominanti vincono
- Per dimensione tensor

#### blend

Formula:

Risultato = Base × (1 - t) + Media(Cond) × t
dove t = 1.0 - structure_strength

Caratteristiche:

- Controllo preciso struttura
- Base influenza configurabile

### Output

#### conditioning (CONDITIONING)

Conditioning combinato secondo il metodo specificato.

#### combination_info (STRING)

Stringa JSON con dettagli della combinazione effettuata.

### Esempio Utilizzo

from nodes.weighted_conditioning import CharacterForgeWeightedConditioning

controller = CharacterForgeWeightedConditioning()
result = controller.combine_weighted(
    base_conditioning=schema_conditioning,
    conditioning_1=gender_result,
    weight_1=0.8,
    conditioning_2=ethnicity_result,
    weight_2=0.6,
    conditioning_3=body_result,
    weight_3=0.7,
    combination_method="weighted_sum",
    preserve_structure=True,
    structure_strength=0.3
)

conditioning, info = result

### Esempio con Blend

result = controller.combine_weighted(
    base_conditioning=schema_conditioning,
    conditioning_1=gender_result,
    weight_1=0.8,
    conditioning_2=ethnicity_result,
    weight_2=0.6,
    conditioning_3=body_result,
    weight_3=0.7,
    combination_method="blend",
    preserve_structure=True,
    structure_strength=0.5
)

conditioning, info = result

### Esempio con Concat

result = controller.combine_weighted(
    base_conditioning=schema_conditioning,
    conditioning_1=gender_result,
    weight_1=0.8,
    conditioning_2=ethnicity_result,
    weight_2=0.6,
    conditioning_3=body_result,
    weight_3=0.7,
    combination_method="concat",
    preserve_structure=False
)

conditioning, info = result

## CharacterForgeHybridLatentSwitch

### Informazioni Base

- Categoria: CharacterForge/Hybrid
- Funzione: switch_latent
- Return Types: LATENT, STRING, IMAGE

### INPUT_TYPES

{
    "required": {
        "mode": (["text_to_sheet", "image_to_sheet"],),
        "text_latent": ("LATENT",),
        "image_latent": ("LATENT",)
    },
    "optional": {
        "image_reference": ("IMAGE",),
        "auto_validate": ("BOOLEAN", {"default": True}),
        "debug_mode": ("BOOLEAN", {"default": False})
    }
}

### Parametri

#### mode (COMBO, richiesto)

Modalità del workflow:

- text_to_sheet: Generazione da prompt testuale
- image_to_sheet: Generazione da immagine riferimento

#### text_latent (LATENT, richiesto)

Latent da EmptyLatentImage. Usato quando mode="text_to_sheet".

#### image_latent (LATENT, richiesto)

Latent da VAEEncode. Usato quando mode="image_to_sheet".

#### image_reference (IMAGE, opzionale)

Immagine di riferimento per debug e visualizzazione.

#### auto_validate (BOOLEAN, opzionale)

Default: True. Valida automaticamente i latent input.

#### debug_mode (BOOLEAN, opzionale)

Default: False. Attiva logging dettagliato.

### Configurazione Modalità

#### text_to_sheet

- description: Generazione character sheet da prompt testuale
- uses: EmptyLatentImage (2048x1024 consigliato)
- denoise_suggestion: 1.0
- k_sampler_notes: Generazione completa, nessuna identità di partenza

#### image_to_sheet

- description: Generazione character sheet da immagine riferimento
- uses: VAEEncode + IPAdapter per identità
- denoise_suggestion: 0.6
- k_sampler_notes: Mantiene 30-40% identità originale

### Validazione Latent

Il nodo valida automaticamente:

1. Latent non è None
2. Formato ComfyUI latent (dict con "samples" o tensor)
3. Tensor non vuoto (numel > 0)
4. Dimensioni sufficienti (min 3D)

### Output

#### selected_latent (LATENT)

Latent selezionato in base alla modalità.

#### active_mode_info (STRING)

Stringa JSON con informazioni sulla modalità attiva, incluso:

- active_mode: Modalità corrente
- mode_description: Descrizione modalità
- denoise_suggestion: Denoise consigliato
- k_sampler_notes: Note per KSampler
- routing: Quale latent è stato usato

#### reference_preview (IMAGE)

Immagine riferimento passata per visualizzazione.

### Esempio Utilizzo Text Mode

from nodes.hybrid_switch import CharacterForgeHybridLatentSwitch

switch = CharacterForgeHybridLatentSwitch()
result = switch.switch_latent(
    mode="text_to_sheet",
    text_latent=empty_latent,
    image_latent=vae_encoded_latent,
    auto_validate=True
)

selected_latent, mode_info, reference_preview = result

### Esempio Utilizzo Image Mode

result = switch.switch_latent(
    mode="image_to_sheet",
    text_latent=empty_latent,
    image_latent=vae_encoded_latent,
    image_reference=reference_image,
    auto_validate=True,
    debug_mode=True
)

selected_latent, mode_info, reference_preview = result

### Esempio Debug Mode

Quando debug_mode=True, il nodo produce output console dettagliato:

[HybridLatentSwitch] Modalità selezionata: image_to_sheet
[HybridLatentSwitch] Descrizione: Generazione character sheet da immagine riferimento
[HybridLatentSwitch] Debug - Validazione:
  text_latent: VALID
  image_latent: VALID
[HybridLatentSwitch] Preparazione IMAGE latent:
  image_latent (dict): keys=['samples', 'characterforge_mode', 'characterforge_timestamp']
    samples shape: torch.Size([1, 4, 128, 256])
    samples dtype: torch.float32

## Integrazione con Altri Nodi

### Con CLIPTextEncode

# Codifica testo schema
schema_conditioning = clip_text_encode(schema_text)

# Applica controller
gender_result = gender_controller.apply_gender_control(
    conditioning=schema_conditioning,
    gender="masculine",
    weight=0.8
)

### Con KSampler

# Combina conditioning
final_result = weighted_conditioning.combine_weighted(
    base_conditioning=schema_conditioning,
    conditioning_1=gender_result[0],
    weight_1=0.8,
    conditioning_2=ethnicity_result[0],
    weight_2=0.6,
    conditioning_3=body_result[0],
    weight_3=0.7,
    combination_method="weighted_sum",
    preserve_structure=True
)

# Campiona
sampled_latent = ksampler.sample(
    model=model,
    positive=final_result[0],
    negative=negative_conditioning,
    latent_image=latent_image
)

### Con IPAdapter (Image Mode)

# Carica immagine riferimento
reference_image = load_image("reference.jpg")

# Applica IPAdapter
ipadapter_model = ipadapter.apply(
    model=model,
    image=reference_image,
    weight=0.7
)

# Switch latent
switch_result = hybrid_switch.switch_latent(
    mode="image_to_sheet",
    text_latent=empty_latent,
    image_latent=vae_encoded_latent
)

# Campiona con denoise ridotto
sampled_latent = ksampler.sample(
    model=ipadapter_model,
    positive=conditioning,
    negative=negative_conditioning,
    latent_image=switch_result[0],
    denoise=0.6
)

## Gestione Errori

### Errori Comuni

#### ValueError: Conditioning non valido o vuoto

Tutti i controllers validano il conditioning input. Soluzione: verificare che CLIPTextEncode produca output valido.

#### ValueError: Prompt custom richiesto

GenderController richiede custom_prompt quando gender="custom".

#### ValueError: Etnia non riconosciuta

EthnicityController valida che le etnie specificate esistano nel database.

#### ValueError: Metodi combinazione non validi

WeightedConditioning valida il combination_method specificato.

#### ValueError: Modalità non riconosciuta

HybridLatentSwitch valida il mode specificato.

### Pattern di Gestione Errori

try:
    result = controller.apply_gender_control(
        conditioning=base_conditioning,
        gender="masculine",
        weight=0.8
    )
except ValueError as e:
    print(f"Errore: {e}")
    # Fallback o gestione specifica

## Costanti e Database

### GenderController.GENDER_PRESETS

Database dei preset di genere con prompt e pesi suggeriti.

### EthnicityController.ETHNICITY_DATABASE

Database delle caratteristiche etniche per ogni etnia supportata.

### BodyController.BODY_DATABASE

Database delle corporatura con proporzioni e range altezza.

### BodyController.MUSCLE_DEFINITIONS

Descrizioni per i livelli di definizione muscolare.

### BodyController.BODY_FAT_LEVELS

Descrizioni e percentuali per i livelli di grasso corporeo.

### WeightedConditioning.COMBINATION_METHODS

Configurazione dei metodi di combinazione disponibili.

### HybridLatentSwitch.MODE_CONFIGS

Configurazione delle modalità hybrid switch.

## Metadati Conditioning

Tutti i controllers aggiungono metadati al conditioning per tracciabilità:

- characterforge_gender: Dettagli genere applicato
- characterforge_ethnicity: Dettagli etnia applicata
- characterforge_body: Dettagli corporatura applicata
- characterforge_combined: Dettagli combinazione
- characterforge_mode: Modalità hybrid switch

## Performance

### Tempi di Elaborazione Attesi

- GenderController: < 1ms
- EthnicityController: < 1ms (senza secondary) / < 2ms (con secondary)
- BodyController: < 1ms
- WeightedConditioning: 2-5ms (dipende dal metodo)
- HybridLatentSwitch: < 1ms

### Ottimizzazione

- Usare preserve_structure=True per evitare ricalcoli layout
- Cache IS_CHANGED implementata per ricalcolo solo su cambiamenti
- Validazione input leggera ma completa

Autore: Massimo Bivona
Versione: 2.0.0
Licenza: MIT