# ComfyUI-CharacterForge

Set professionale di nodi per il controllo granulare dei Character Sheet con supporto ibrido Text-to-Sheet e Image-to-Sheet.

Versione: 2.0.0
Licenza: MIT
Compatibilità: ComfyUI 0.34+, Flux.1, Krea2, SDXL

## Caratteristiche

- Controllo Genere: maschile, femminile, androgino o custom con pesi configurabili
- Controllo Etnia: multi-etnia con mix di caratteristiche
- Controllo Corporatura: altezza, tipo fisico, definizione muscolare
- Sistema Weighted Conditioning: combina conditioning multipli con pesi specifici
- Modalità Ibrida: Text-to-Sheet e Image-to-Sheet con switch automatico
- Supporto LoRA: applica stili personalizzati
- Preservazione Struttura: mantiene automaticamente il layout 4-colonne

## Requisiti

### Hardware Minimo

- VRAM: 16 GB
- RAM: 32 GB
- GPU: RTX 3060 12GB

### Hardware Consigliato

- VRAM: 24 GB
- RAM: 64 GB
- GPU: RTX 4090 24GB

### Software

- Python 3.11.x
- PyTorch 2.14.0+
- ComfyUI 0.34.0 o superiore

## Installazione

### Metodo 1: Git Clone (Consigliato)

1. Naviga nella directory custom_nodes di ComfyUI:

cd ComfyUI/custom_nodes

2. Clona la repository:

git clone https://github.com/tuousername/ComfyUI-CharacterForge.git

3. Riavvia ComfyUI

I nodi appariranno nella categoria "CharacterForge"

### Metodo 2: ComfyUI Manager

1. Apri ComfyUI
2. Vai su Manager > Custom Nodes Manager
3. Cerca "CharacterForge"
4. Clicca Install
5. Riavvia ComfyUI

### Metodo 3: Download Manuale

1. Scarica l'ultima versione da Releases
2. Estrai l'archivio ZIP
3. Copia la cartella in ComfyUI/custom_nodes/
4. Rinomina in ComfyUI-CharacterForge
5. Riavvia ComfyUI

### Verifica Installazione

Dopo il riavvio, dovresti vedere in console:

[CharacterForge] Inizializzazione v2.0.0...
[CharacterForge] Nodi registrati: 5
[CharacterForge] Nodi caricati: gender_controller, ethnicity_controller, body_controller, weighted_conditioning, hybrid_switch

## Nodi Disponibili

### CharacterForgeGenderController

Categoria: CharacterForge/Basic

Controlla il genere del soggetto nel character sheet.

Input:
- conditioning: Conditioning base da modificare
- gender: masculine / feminine / androgynous / custom
- weight: 0.0 - 1.5 (default 0.8)
- preserve_structure: true / false
- custom_prompt: testo per genere personalizzato

Output:
- conditioning: Conditioning modificato
- applied_features: descrizione features applicate

### CharacterForgeEthnicityController

Categoria: CharacterForge/Advanced

Controlla l'etnia del soggetto con supporto multi-etnia.

Input:
- conditioning: Conditioning base
- primary_ethnicity: caucasian / african / asian / latin / mixed
- secondary_ethnicity: none / caucasian / african / asian / latin
- weight: 0.0 - 1.5 (default 0.6)
- skin_tone_override: override specifico tono pelle

Output:
- conditioning: Conditioning con etnia applicata
- ethnicity_details: dettagli etnia applicata

### CharacterForgeBodyController

Categoria: CharacterForge/Basic

Controlla corporatura, altezza e definizione muscolare.

Input:
- conditioning: Conditioning base
- body_type: athletic / slim / curvy / muscular / average
- height: 150.0 - 200.0 cm (default 175.0)
- weight: 0.0 - 1.5 (default 0.7)
- muscle_definition: low / medium / high
- body_fat: low / medium / high

Output:
- conditioning: Conditioning con corporatura
- body_details: dettagli corporatura applicata

### CharacterForgeWeightedConditioning

Categoria: CharacterForge/Advanced

Combina conditioning multipli con pesi specifici.

Input:
- base_conditioning: Conditioning base (schema layout)
- conditioning_1: Primo conditioning aggiuntivo
- weight_1: peso primo conditioning (default 1.0)
- conditioning_2: Secondo conditioning
- weight_2: peso secondo conditioning (default 0.8)
- conditioning_3: Terzo conditioning
- weight_3: peso terzo conditioning (default 0.6)
- combination_method: weighted_sum / average / concat / max
- preserve_structure: true / false

Output:
- conditioning: Conditioning combinato
- combination_info: informazioni sulla combinazione

### CharacterForgeHybridLatentSwitch

Categoria: CharacterForge/Hybrid

Commuta automaticamente tra modalità Text-to-Sheet e Image-to-Sheet.

Input:
- mode: text_to_sheet / image_to_sheet
- text_latent: Latent da EmptyLatentImage
- image_latent: Latent da VAEEncode
- image_reference: Immagine riferimento (opzionale)

Output:
- selected_latent: Latent selezionato in base alla modalità
- active_mode: descrizione modalità attiva

## Utilizzo

### Quick Start: Text-to-Sheet

1. Aggiungi nodo Checkpoint Loader (es. flux1-dev)
2. Aggiungi nodo CLIP Text Encode con schema base
3. Aggiungi nodo CharacterForgeGenderController:
   - Collega il conditioning
   - Seleziona genere
   - Imposta peso 0.8
4. Aggiungi nodo KSampler:
   - Collega il conditioning modificato
   - Risoluzione: 2048x1024
5. Genera

### Quick Start: Image-to-Sheet

1. Aggiungi nodo LoadImage e carica immagine riferimento
2. Aggiungi nodo VAEEncode e collega l'immagine
3. Aggiungi nodo EmptyLatentImage 2048x1024
4. Aggiungi nodo CharacterForgeHybridLatentSwitch:
   - Collega entrambi i latent
   - Seleziona image_to_sheet
5. Aggiungi IPAdapter con immagine riferimento (peso 0.7)
6. Aggiungi KSampler con denoise 0.6-0.7
7. Genera

### Esempio: Character Sheet Maschile Caucasico

Configurazione nodi:
- GenderController: ["masculine", 0.8, true, ""]
- EthnicityController: ["caucasian", "none", 0.6, ""]
- BodyController: ["athletic", 180.0, 0.7, "medium", "low"]

### Esempio: Character Sheet Multi-Etnico Femminile

Configurazione nodi:
- GenderController: ["feminine", 0.8, true, ""]
- EthnicityController: ["caucasian", "asian", 0.5, "olive skin"]
- BodyController: ["slim", 165.0, 0.6, "low", "medium"]

## Modelli Compatibili

### Consigliati

- Flux.1 Dev: migliore qualità complessiva
- Flux.1 Schnell: più veloce
- Krea2: ottimizzato per character sheet

### Compatibili

- SDXL Base 1.0
- SD3 Large 1.0

## LoRA Consigliati

- character_sheet_v2.safetensors: layout base (peso 0.7-0.9)
- cinematic_realistic.safetensors: stile realistico (peso 0.4-0.6)
- anime_style_v3.safetensors: stile anime (peso 0.5-0.7)

## Configurazione

Il pacchetto include configurazione in config/default_config.json.

Variabili ambiente disponibili:
- CHARACTERFORGE_SILENT=1: disattiva output console
- CHARACTERFORGE_VERBOSE=1: attiva report dettagliato
- CHARACTERFORGE_DEBUG=1: attiva debug completo

## Troubleshooting

### Nodi non visibili in ComfyUI

Verifica che la cartella sia in custom_nodes/ e riavvia ComfyUI.

### Layout character sheet distrutto

Usa ConditioningConcat invece di ConditioningCombine per lo schema.
Verifica che preserve_structure sia true.

### VRAM insufficiente

Riduci risoluzione a 1536x768 temporaneamente.
Usa --lowvram flag all'avvio.

### Identità non mantenuta in Image mode

Aumenta IPAdapter weight a 0.8-0.9.
Verifica che denoise sia 0.6-0.7.

## Contribuire

1. Fork del progetto
2. Crea branch feature (git checkout -b feature/AmazingFeature)
3. Commit modifiche (git commit -m 'Add some AmazingFeature')
4. Push al branch (git push origin feature/AmazingFeature)
5. Apri Pull Request

## Licenza

MIT License

Copyright (c) 2026 [Il Tuo Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Ringraziamenti

- ComfyUI Team per l'eccellente piattaforma
- ComfyUI Community per il supporto