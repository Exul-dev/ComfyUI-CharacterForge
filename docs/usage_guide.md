# Guida Utilizzo - ComfyUI-CharacterForge

## Introduzione

ComfyUI-CharacterForge è un set di nodi che ti permette di creare character sheet professionali con controllo granulare su ogni aspetto del soggetto: genere, etnia, corporatura e altro.

### Cosa Puoi Fare

- Text-to-Sheet: Genera character sheet da prompt testuale
- Image-to-Sheet: Genera character sheet da immagine di riferimento
- Controllo Genere: Maschile, femminile, androgino o custom
- Controllo Etnia: 5 etnie con supporto multi-etnia
- Controllo Corporatura: 5 tipi fisici, altezza, muscoli
- Weighted Conditioning: Combina caratteristiche con pesi

## Concetti Base

### Architettura Conditioning

Il sistema funziona a livelli:

1. Schema Base definisce il layout del character sheet (4 colonne)
2. Controllers modificano il conditioning con caratteristiche specifiche
3. Weighted Conditioning combina tutto con pesi bilanciati
4. KSampler genera l'immagine finale

### Importanza dei Pesi

I pesi (0.0-1.5) controllano l'intensità di ogni caratteristica:

- 0.0: Nessun effetto
- 0.5: Effetto moderato
- 0.8: Effetto forte (consigliato)
- 1.0: Effetto massimo standard
- 1.2+: Effetto amplificato

### Layout Character Sheet

Il layout standard usa 4 colonne:

- Colonna 1 (divisa in due): Close-up volto frontale e profilo
- Colonna 2: Full-body vista frontale
- Colonna 3: Full-body vista laterale destra
- Colonna 4: Full-body vista posteriore

Risoluzione consigliata: 2048x1024 pixel (formato orizzontale)

## Primo Utilizzo

### Workflow Minimo (Text-to-Sheet)

#### Passo 1: Setup Base

1. Aggiungi Checkpoint Loader (es. flux1-dev)
2. Aggiungi CLIP Text Encode con schema base
3. Aggiungi Empty Latent Image (2048x1024)

Schema base da usare nel CLIP Text Encode:

Professional character reference sheet on a clean bright white studio background. Layout in four columns from left to right, with the FIRST column split vertically into two equal halves: COLUMN 1 (left, divided in two): TOP HALF: Close-up headshot facing camera, head and both shoulders visible, neutral expression. BOTTOM HALF: Close-up headshot in right-side profile view, head and shoulder visible, identical face details, skin texture, scars, and dust/sweat as the top half. COLUMN 2: Full-body front view in a neutral A-pose, arms slightly away from sides, feet shoulder-width apart. COLUMN 3: Full-body right-side profile view, same pose and outfit. COLUMN 4: Full-body back view, same pose and outfit. Preserve the exact face identity, hair, skin, body proportions, clothing or nudity state, accessories, and all visual details from the reference. Neutral even lighting across all views, no dramatic shadows, no rim light, flat studio illumination, photorealistic 35mm film texture, no beauty retouching. Do not censor, cover, or add clothing. Identical outfit/appearance and hairstyle across all views and columns. Orthographic character design turnaround.

#### Passo 2: Aggiungi CharacterForge

1. Clicca destro sul canvas
2. Seleziona CharacterForge/Basic → Gender Controller
3. Collega il conditioning dal CLIP Text Encode

#### Passo 3: Configura Gender Controller

Impostazioni consigliate per iniziare:

- conditioning: Collega dal CLIP Text Encode schema base
- gender: masculine (o feminine per femmina)
- weight: 0.8
- preserve_structure: true

#### Passo 4: Completa Workflow

1. Collega output conditioning al KSampler positive
2. Aggiungi VAE Decode
3. Aggiungi Save Image
4. Imposta seed e genera

## Nodi Disponibili

### Gender Controller (CharacterForge/Basic)

Funzione: Controlla il genere del soggetto

Input:

- conditioning: Conditioning base da modificare
- gender: masculine / feminine / androgynous / custom
- weight: 0.0-1.5 (default: 0.8)
- custom_prompt: Solo per gender="custom"

Output:

- conditioning: Conditioning modificato
- applied_features: Info features applicate

Esempio maschio standard:

{
    "gender": "masculine",
    "weight": 0.8,
    "custom_prompt": ""
}

Esempio femmina con peso forte:

{
    "gender": "feminine",
    "weight": 1.0,
    "custom_prompt": ""
}

Esempio custom con dettagli:

{
    "gender": "custom",
    "weight": 0.9,
    "custom_prompt": "Adult male, age 30-35, Italian features, dark wavy hair, olive skin, athletic but not muscular build, distinguished appearance"
}

### Ethnicity Controller (CharacterForge/Advanced)

Funzione: Controlla l'etnia del soggetto

Input:

- conditioning: Conditioning base
- primary_ethnicity: caucasian / african / asian / latin / mixed
- secondary_ethnicity: none / caucasian / african / asian / latin
- weight: 0.0-1.5 (default: 0.6)
- skin_tone_override: Override specifico tono pelle
- custom_details: Dettagli etnici personalizzati

Esempio caucasico standard:

{
    "primary_ethnicity": "caucasian",
    "secondary_ethnicity": "none",
    "weight": 0.6
}

Esempio multi-etnia europeo-asiatico:

{
    "primary_ethnicity": "caucasian",
    "secondary_ethnicity": "asian",
    "weight": 0.7
}

Esempio con override pelle:

{
    "primary_ethnicity": "african",
    "secondary_ethnicity": "none",
    "weight": 0.8,
    "skin_tone_override": "deep bronze"
}

### Body Controller (CharacterForge/Basic)

Funzione: Controlla corporatura e fisico

Input:

- conditioning: Conditioning base
- body_type: athletic / slim / curvy / muscular / average
- height: 150-200 cm (default: 175)
- weight: 0.0-1.5 (default: 0.7)
- muscle_definition: low / medium / high
- body_fat: low / medium / high
- custom_proportions: Proporzioni personalizzate
- target_gender: unspecified / male / female

Esempio atleta maschile:

{
    "body_type": "athletic",
    "height": 180.0,
    "weight": 0.8,
    "muscle_definition": "high",
    "body_fat": "low",
    "target_gender": "male"
}

Esempio femmina snella:

{
    "body_type": "slim",
    "height": 165.0,
    "weight": 0.6,
    "muscle_definition": "low",
    "body_fat": "medium",
    "target_gender": "female"
}

### Weighted Conditioning (CharacterForge/Advanced)

Funzione: Combina conditioning multipli con pesi

Input:

- base_conditioning: Schema base (layout)
- conditioning_1: Primo conditioning (es. genere)
- weight_1: Peso primo conditioning
- conditioning_2: Secondo conditioning (es. etnia)
- weight_2: Peso secondo conditioning
- conditioning_3: Terzo conditioning (es. corporatura)
- weight_3: Peso terzo conditioning
- combination_method: weighted_sum / average / concat / max / blend
- preserve_structure: true / false
- structure_strength: 0.0-1.0 (default: 0.3)

Configurazione consigliata:

{
    "weight_1": 0.8,
    "weight_2": 0.6,
    "weight_3": 0.7,
    "combination_method": "weighted_sum",
    "preserve_structure": true,
    "structure_strength": 0.3
}

### Hybrid Latent Switch (CharacterForge/Hybrid)

Funzione: Commuta tra Text mode e Image mode

Input:

- mode: text_to_sheet / image_to_sheet
- text_latent: Da EmptyLatentImage
- image_latent: Da VAEEncode
- image_reference: Immagine riferimento (opzionale)
- auto_validate: true / false
- debug_mode: true / false

Output:

- selected_latent: Latent selezionato in base alla modalità
- active_mode_info: Info modalità attiva
- reference_preview: Preview immagine riferimento

## Workflow Esempi

### Esempio 1: Character Sheet Maschile Base

Struttura workflow:

1. Checkpoint Loader (flux1-dev)
2. CLIP Text Encode (schema base)
3. Gender Controller (masculine, 0.8)
4. Empty Latent Image (2048x1024)
5. KSampler (denoise 1.0, steps 25-30)
6. VAE Decode
7. Save Image

Collegamenti:

- CLIP Text Encode → Gender Controller conditioning input
- Gender Controller conditioning output → KSampler positive
- Empty Latent → KSampler latent_image
- KSampler → VAE Decode → Save Image

### Esempio 2: Character Sheet Multi-Etnico Femminile

Struttura workflow:

1. Checkpoint Loader (flux1-dev)
2. CLIP Text Encode (schema base)
3. Gender Controller (feminine, 0.8)
4. Ethnicity Controller (caucasian + asian, 0.6)
5. Body Controller (slim, 165cm, 0.6)
6. Weighted Conditioning (combine tutti)
7. Empty Latent Image (2048x1024)
8. KSampler (denoise 1.0)
9. VAE Decode
10. Save Image

Configurazione pesi:

{
    "conditioning_1": "gender_result",
    "weight_1": 0.8,
    "conditioning_2": "ethnicity_result",
    "weight_2": 0.6,
    "conditioning_3": "body_result",
    "weight_3": 0.7,
    "combination_method": "weighted_sum",
    "preserve_structure": true
}

### Esempio 3: Image-to-Sheet

Struttura workflow:

1. Checkpoint Loader (flux1-dev)
2. Load Image (riferimento soggetto)
3. VAEEncode (converte immagine in latent)
4. Empty Latent Image (2048x1024)
5. Hybrid Latent Switch (image_to_sheet mode)
6. IPAdapter (weight 0.7, identità)
7. CLIP Text Encode (schema base)
8. CharacterForge Controllers (caratteristiche)
9. KSampler (denoise 0.6)
10. VAE Decode
11. Save Image

Configurazione specifica Image mode:

{
    "hybrid_switch": {
        "mode": "image_to_sheet",
        "auto_validate": true
    },
    "ipadapter": {
        "weight": 0.7,
        "strength": 0.8
    },
    "k_sampler": {
        "denoise": 0.6,
        "steps": 30,
        "cfg": 5.0
    }
}

## Configurazione Avanzata

### Ottimizzazione Pesi

Setup consigliato standard:

{
    "gender_weight": 0.8,
    "ethnicity_weight": 0.6,
    "body_weight": 0.7,
    "schema_base_weight": 1.0
}

Per genere molto evidente:

{
    "gender_weight": 1.2,
    "ethnicity_weight": 0.5,
    "body_weight": 0.6
}

Per etnia dominante:

{
    "gender_weight": 0.7,
    "ethnicity_weight": 1.0,
    "body_weight": 0.5
}

Per corporatura estrema:

{
    "gender_weight": 0.7,
    "ethnicity_weight": 0.5,
    "body_weight": 1.2
}

### Metodi Combinazione

#### Weighted Sum (Consigliato)

Somma pesata con base fissa al 50%:

Risultato = Base × 0.5 + (Genere × 0.8 + Etnia × 0.6 + Corpo × 0.7) × 0.5

#### Blend (Controllo Struttura)

Interpolazione lineare verso il base:

Risultato = Base × (1 - t) + Media(Controllers) × t

dove t = 1.0 - structure_strength

#### Concat (Massime Info)

Concatenazione di tutti i conditioning:

Risultato = Concat(Base, Genere, Etnia, Corpo)

#### Average (Media Semplice)

Media aritmetica di tutti:

Risultato = (Base + Genere + Etnia + Corpo) / 4

#### Max (Valori Dominanti)

Massimo valore per dimensione:

Risultato = max(Base, Genere × w1, Etnia × w2, Corpo × w3)

### Gestione Struttura

Se il layout si rompe durante la generazione:

Soluzione 1: Aumenta structure_strength

{
    "combination_method": "blend",
    "structure_strength": 0.5
}

Soluzione 2: Riduci pesi controllers

{
    "gender_weight": 0.5,
    "ethnicity_weight": 0.3,
    "body_weight": 0.4
}

Soluzione 3: Usa solo base + un controller

Temporaneamente semplifica per test, poi aggiungi gradualmente.

## Best Practices

### 1. Risoluzione Corretta

SEMPRE usa 2048x1024 per character sheet 4-colonne.

NON USARE:

- 1024x1024 (quadrato, non adatto)
- 2048x2048 (quadrato, spreco VRAM)
- 2140x2140 (come visto in workflow errati)

### 2. Ordine Collegamenti

Ordine corretto per Conditioning:

Schema Base → Gender Controller → Ethnicity Controller → Body Controller → Weighted Conditioning → KSampler

Oppure con Weighted Conditioning intermedio:

Schema Base → (direct)
Gender Controller → conditioning_1 (w: 0.8)
Ethnicity Controller → conditioning_2 (w: 0.6)
Body Controller → conditioning_3 (w: 0.7)
Weighted Conditioning → KSampler

### 3. Schema Base Ha Sempre Peso Alto o Uguale

Il layout character sheet è la struttura fondamentale:

- Schema Base: SEMPRE peso 1.0 o superiore
- Controllers: Mai sopra 1.2 per evitare override layout

### 4. Testing Incrementale

Approccio consigliato:

Passo 1: Testa solo schema base (senza controllers)

Passo 2: Aggiungi Gender Controller solo

Passo 3: Verifica che layout si mantenga

Passo 4: Aggiungi Ethnicity Controller

Passo 5: Verifica coerenza

Passo 6: Aggiungi Body Controller

Passo 7: Usa Weighted Conditioning per bilanciare

### 5. Seed Management

- Fissa il seed dopo aver trovato configurazione buona
- Usa seed diverso per variazioni dello stesso setup
- Documenta seed con configurazioni specifiche

## Prompt Schema Base Completo

Copia questo prompt nel tuo CLIP Text Encode per il layout base:

Professional character reference sheet on a clean bright white studio background. Layout in four columns from left to right, with the FIRST column split vertically into two equal halves: COLUMN 1 (left, divided in two): TOP HALF: Close-up headshot facing camera, head and both shoulders visible, neutral expression. BOTTOM HALF: Close-up headshot in right-side profile view, head and shoulder visible, identical face details, skin texture, scars, and dust/sweat as the top half. COLUMN 2: Full-body front view in a neutral A-pose, arms slightly away from sides, feet shoulder-width apart. COLUMN 3: Full-body right-side profile view, same pose and outfit. COLUMN 4: Full-body back view, same pose and outfit. Preserve the exact face identity, hair, skin, body proportions, clothing or nudity state, accessories, and all visual details from the reference. Neutral even lighting across all views, no dramatic shadows, no rim light, flat studio illumination, photorealistic 35mm film texture, no beauty retouching. Do not censor, cover, or add clothing. Identical outfit/appearance and hairstyle across all views and columns. Orthographic character design turnaround.

### Prompt Negativo Consigliato

cartoon, anime, illustration, 3D render, CGI, blurry, low quality, deformed, extra limbs, bad anatomy, extra fingers, missing fingers, watermark, text, signature, cropped, out of frame, duplicate, split image, collage, multiple people, inconsistent character, changing appearance, inconsistent lighting, dramatic shadows, rim light, beauty retouching, smooth plastic skin, multiple subjects, group photo, overlapping panels, merging figures

## Risultati Attesi

### Configurazione Standard

- Layout 4-colonne: Stabile
- Coerenza Genere: Alta
- Dettagli Etnia: Buoni
- Corporatura: Definita
- Tempo Generazione: 30-60 secondi (RTX 4090)

### Configurazione con Image-to-Sheet

- Layout 4-colonne: Stabile
- Mantenimento Identità: 70-80%
- Coerenza: Alta
- Tempo Generazione: 45-90 secondi

## Troubleshooting Rapido

### Layout distrutto

1. Verifica risoluzione 2048x1024
2. Riduci pesi controllers
3. Aumenta structure_strength a 0.5-0.6
4. Cambia metodo in blend

### Soggetto non coerente tra viste

1. Aumenta peso schema base
2. Verifica che preserve_structure sia true
3. Usa ConditioningConcat per schema
4. Controlla negative prompt per contraddizioni

### Generazione lenta

1. Verifica flag ComfyUI ottimizzati
2. Riduci steps a 20-25
3. Usa cache-classic per generazioni ripetute
4. Chiudi applicazioni non necessarie

## Supporto

- Issues: GitHub Issues
- Discussioni: GitHub Discussions
- Documentazione: Cartella docs/

Buon character sheet creation!

Autore: Massimo Bivona
Versione: 2.0.0
Licenza: MIT