
# Troubleshooting - ComfyUI-CharacterForge

## Panoramica

Questa guida risolve i problemi più comuni incontrati durante l'utilizzo di ComfyUI-CharacterForge. I problemi sono organizzati per categoria con diagnosi e soluzioni progressive.

## Problemi Installazione

### I Nodi Non Appaiono in ComfyUI

Sintomi: Dopo l'installazione, i nodi CharacterForge non sono visibili nel menu o nel canvas.

Diagnosi:

1. Verifica che la cartella sia nel percorso corretto:

Test-Path "ComfyUI\custom_nodes\ComfyUI-CharacterForge\__init__.py"

2. Verifica console ComfyUI per messaggi [CharacterForge]

3. Verifica importazioni Python:

python -c "from nodes import CharacterForgeGenderController; print('OK')"

Soluzioni:

1. Verifica percorso: La cartella deve essere esattamente in custom_nodes/
2. Riavvia ComfyUI completamente (non solo refresh browser)
3. Cancella cache browser (Ctrl+F5)
4. Verifica permessi cartella
5. Controlla errori Python nella console

### ModuleNotFoundError

Sintomi: ModuleNotFoundError: No module named 'torch' o simili

Diagnosi:

python -c "import torch; print(torch.__version__)"

Soluzioni:

1. Verifica ambiente virtuale attivo:

Get-Command python

2. Installa dipendenze:

pip install -r requirements.txt

3. Verifica versione PyTorch (deve essere >= 2.14.0):

pip install torch>=2.14.0

### Conflitti Versioni

Sintomi: Errori di compatibilità tra pacchetti

Diagnosi:

pip check

Soluzioni:

1. Aggiorna pip:

python -m pip install --upgrade pip

2. Reinstalla con force:

pip install -r requirements.txt --force-reinstall --no-cache-dir

3. Verifica conflitti specifici:

pip check

## Problemi Rendering

### Immagini Sfuocate o Artefatti

Causa probabile: Pesi troppo alti o risoluzione errata

Soluzioni:

1. Verifica risoluzione: DEVE essere 2048x1024

2. Riduci pesi:

{
    "gender_weight": 0.6,
    "ethnicity_weight": 0.4,
    "body_weight": 0.5
}

3. Aumenta steps da 25 a 30-35

4. Verifica negative prompt per contraddizioni

### Colori Innaturali

Causa probabile: Conflitto conditioning o CFG troppo alto

Soluzioni:

1. Riduci CFG da 5.0 a 4.0-4.5
2. Cambia metodo combinazione da weighted_sum a blend
3. Aumenta structure_strength a 0.5

### Qualità Inferiore alle Aspettative

Causa probabile: Configurazione non ottimizzata

Soluzioni:

1. Verifica modello base (Flux.1 Dev consigliato)
2. Aumenta steps a 30-35
3. Verifica LoRA character sheet attivo
4. Controlla pesi bilanciati

## Problemi Layout

### Layout Character Sheet Distrutto

Sintomi: Le 4 colonne non sono chiare, soggetti sovrapposti o confusi.

Diagnosi:

1. Verifica risoluzione latent: deve essere 2048x1024
2. Verifica schema base collegato correttamente
3. Controlla preserve_structure sia true

Soluzioni Progressive:

Livello 1: Riduci Pesi

{
    "gender_weight": 0.5,
    "ethnicity_weight": 0.3,
    "body_weight": 0.4,
    "combination_method": "blend",
    "structure_strength": 0.5
}

Livello 2: Usa Blend

{
    "combination_method": "blend",
    "structure_strength": 0.7
}

Livello 3: Semplifica Temporaneamente

Usa solo schema base + Gender Controller. Se funziona, aggiungi Ethnicity gradualmente.

Livello 4: Verifica ConditioningConcat

Assicurati di usare ConditioningConcat (non ConditioningCombine) per lo schema base.

### Colonne Disuguali

Causa probabile: Risoluzione errata o conditioning conflittuale

Soluzioni:

1. Verifica ESATTAMENTE 2048x1024 (non 2140x2140)
2. Rimuovi conditioning negativi complessi
3. Testa solo con schema base senza controllers

### Soggetto Non Coerente Tra Viste

Sintomi: Il soggetto appare diverso nelle varie colonne del character sheet.

Soluzioni:

1. Aumenta peso schema base a 1.0+
2. Verifica preserve_structure: true in tutti i controllers
3. Usa ConditioningConcat per schema
4. Controlla negative prompt per contraddizioni
5. Fissa seed per coerenza

## Problemi Performance

### Generazione Lenta

Causa probabile: Configurazione non ottimizzata

Soluzioni:

1. Verifica flag ComfyUI ottimizzati:

python main.py --lowvram --disable-smart-memory --async-offload 4 --cache-classic --use-sage-attention

2. Riduci steps a 20-25 (da 30)
3. Usa cache-classic per generazioni ripetute
4. Chiudi applicazioni non necessarie
5. Verifica SageAttention attivo

### VRAM Insufficiente

Sintomi: CUDA out of memory error

Soluzioni:

1. Flag gestione memoria:

python main.py --lowvram --reserve-vram 4096

2. Riduci risoluzione temporanea (1536x768)
3. Usa cache-none invece di cache-classic
4. Riduci batch size a 1
5. Come ultima risorsa: --novram

### RAM Usage Eccessivo

Sintomi: Sistema lento, swap attivo

Soluzioni:

1. Chiudi applicazioni non necessarie
2. Riduci cache ComfyUI: --cache-none
3. Verifica modelli non necessari non caricati
4. Usa --novram come ultima risorsa

### GPU Non Utilizzata Completamente

Sintomi: GPU usage basso durante generazione

Soluzioni:

1. Verifica CUDA disponibile:

python -c "import torch; print(torch.cuda.is_available())"

2. Verifica modello su GPU
3. Controlla data loading bottlenecks
4. Verifica batch size ottimale

## Problemi Modalità Ibrida

### Identità Non Mantenuta (Image Mode)

Sintomi: Il character sheet non assomiglia all'immagine riferimento.

Diagnosi:

1. Verifica IPAdapter configurato correttamente
2. Controlla IPAdapter weight
3. Verifica denoise KSampler

Soluzioni:

{
    "ipadapter": {
        "weight": 0.8,
        "strength": 0.9
    },
    "k_sampler": {
        "denoise": 0.5
    }
}

### Immagine Troppo Simile all'Originale

Sintomi: Il character sheet è troppo identico, nessuna variazione layout.

Soluzioni:

{
    "ipadapter": {
        "weight": 0.4
    },
    "k_sampler": {
        "denoise": 0.8
    }
}

### Latent Non Valido

Sintomi: ValueError: image_latent non valido

Diagnosi:

1. Verifica VAEEncode collegato correttamente
2. Controlla formato immagine
3. Attiva auto_validate nel Hybrid Switch

Soluzioni:

1. Verifica collegamento VAEEncode
2. Attiva auto_validate: true
3. Attiva debug_mode: true per log dettagliato
4. Verifica immagine non corrotta
5. Controlla risoluzione immagine compatibile

### Switch Non Funziona

Sintomi: Cambio modalità ma output rimane invariato

Diagnosi:

1. Verifica mode setting nel Hybrid Switch
2. Controlla collegamenti latent
3. Verifica auto_validate non stia bloccando

Soluzioni:

1. Verifica mode sia "text_to_sheet" o "image_to_sheet"
2. Controlla entrambi i latent collegati
3. Disattiva temporaneamente auto_validate
4. Attiva debug_mode per verificare routing

## Errori Specifici Nodi

### GenderController Errori

#### ValueError: Conditioning non valido o vuoto

Causa: Conditioning input è None o vuoto

Soluzione:

Verifica che CLIPTextEncode upstream produca output valido:

conditioning = clip_text_encode(text)
assert conditioning is not None
assert len(conditioning) > 0

#### ValueError: Prompt custom richiesto

Causa: gender="custom" ma custom_prompt vuoto

Soluzione:

{
    "gender": "custom",
    "custom_prompt": "Adult male, 30 years, Italian, dark hair"
}

### EthnicityController Errori

#### ValueError: Etnia non riconosciuta

Causa: Etnia specificata non nel database

Soluzione:

Verifica etnie disponibili: caucasian, african, asian, latin, mixed

#### ValueError: Etnia secondaria non riconosciuta

Causa: Secondary ethnicity non valida

Soluzione:

Verifica secondary etnie: none, caucasian, african, asian, latin

### BodyController Errori

#### Altezza Fuori Range

Sintomi: Warning in console ma non errore bloccante

Soluzione:

Altezza range supportato: 150-200 cm. Valori fuori range generano warning ma funzionano.

### WeightedConditioning Errori

#### ValueError: Somma pesi zero

Causa: Tutti i pesi sono 0.0

Soluzione:

Almeno un peso deve essere > 0.0

#### Shape Mismatch Warning

Sintomi: "[WeightedConditioning] Warning: Shape mismatch cond_1, skip"

Causa: Conditioning hanno shapes diverse

Soluzione:

Il nodo gestisce automaticamente saltando conditioning incompatibili. Verifica che tutti i conditioning provengano dallo stesso modello CLIP.

### HybridLatentSwitch Errori

#### ValueError: Modalità non riconosciuta

Causa: Mode specificato non valido

Soluzione:

Verifica mode sia "text_to_sheet" o "image_to_sheet"

#### ValueError: text_latent/image_latent non valido

Causa: Latent input non valido

Soluzione:

Verifica EmptyLatentImage e VAEEncode funzionino correttamente

## Strumenti Diagnostici

### Script Diagnostico Completo

# Salva come diagnose.ps1 ed esegui

Write-Host "=== DIAGNOSTI CHARACTERFORGE ===" -ForegroundColor Cyan

# 1. Verifica installazione
Write-Host "`n1. Verifica Installazione:" -ForegroundColor Yellow
$installPath = "ComfyUI\custom_nodes\ComfyUI-CharacterForge"

if (Test-Path "$installPath\__init__.py") {
    Write-Host "   OK Installazione presente" -ForegroundColor Green
} else {
    Write-Host "   MANCANTE Installazione" -ForegroundColor Red
}

# 2. Verifica importazioni
Write-Host "`n2. Verifica Importazioni:" -ForegroundColor Yellow

$imports = @(
    "nodes.gender_controller",
    "nodes.ethnicity_controller",
    "nodes.body_controller",
    "nodes.weighted_conditioning",
    "nodes.hybrid_switch"
)

foreach ($import in $imports) {
    try {
        python -c "from $import import *; print('OK')"
        Write-Host "   OK $import" -ForegroundColor Green
    } catch {
        Write-Host "   ERRORE $import" -ForegroundColor Red
    }
}

# 3. Verifica PyTorch
Write-Host "`n3. Verifica PyTorch:" -ForegroundColor Yellow
python -c "import torch; print(f'   PyTorch: {torch.__version__}')"
python -c "import torch; print(f'   CUDA: {torch.cuda.is_available()}')"
python -c "import torch; print(f'   GPU: {torch.cuda.get_device_name(0)}')"

# 4. Verifica VRAM
Write-Host "`n4. Verifica VRAM:" -ForegroundColor Yellow
python -c "import torch; print(f'   VRAM Totale: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB')"
python -c "import torch; print(f'   VRAM Libera: {(torch.cuda.get_device_properties(0).total_memory - torch.cuda.memory_allocated()) / 1024**3:.2f} GB')"

### Debug Mode Attivo

# PowerShell
$env:CHARACTERFORGE_DEBUG = "1"
python main.py

# Output atteso:
# [CharacterForge] DEBUG MODE ATTIVO
# [HybridLatentSwitch] Modalità selezionata: text_to_sheet
# [GenderController] Applicando genere: masculine (peso: 0.8)
# [WeightedConditioning] Combinazione: weighted_sum
# [WeightedConditioning] Pesi: [0.267, 0.200, 0.233]

### Verifica Configurazione

# Verifica configurazione JSON valida
python -c "import json; config = json.load(open('config/default_config.json')); print('Config OK')"

# Verifica metadati conditioning
python -c "
from nodes.gender_controller import CharacterForgeGenderController
controller = CharacterForgeGenderController()
# Il controller aggiunge metadati characterforge_gender al conditioning
"

## Matrice Problemi-Soluzioni

| Problema | Categoria | Soluzione Rapida | Soluzione Completa |
|----------|-----------|------------------|-------------------|
| Nodi non visibili | Installazione | Riavvia ComfyUI | Verifica percorso + cache |
| ModuleNotFoundError | Installazione | pip install -r requirements.txt | Verifica venv attivo |
| Layout distrutto | Layout | Riduci pesi | Usa blend + structure_strength |
| Immagini sfocate | Rendering | Verifica 2048x1024 | Riduci pesi + aumenta steps |
| Generazione lenta | Performance | Flag ottimizzati | Verifica SageAttention |
| VRAM insufficiente | Performance | --lowvram | Riduci risoluzione |
| Identità persa | Ibrida | ↑ IPAdapter weight | ↓ denoise + ↑ weight |
| Troppo simile | Ibrida | ↓ IPAdapter weight | ↑ denoise |
| Latent non valido | Ibrida | Attiva auto_validate | Verifica VAEEncode |

## Quando Richiedere Aiuto

Prima di aprire un issue, verifica:

1. Hai letto questa guida troubleshooting
2. Hai provato le soluzioni suggerite
3. Hai attivato debug mode per log dettagliato

### Informazioni da Includere nell'Issue

1. Versione ComfyUI e CharacterForge
2. Sistema operativo e hardware
3. Log completo della console (con errori)
4. Workflow JSON (se possibile)
5. Configurazione nodi (pesi, metodi)
6. Immagini di esempio (input e output)
7. Passi per riprodurre il problema

### Template Issue

**Descrizione Problema:**
[Descrizione breve]

**Configurazione:**
- ComfyUI Version: [versione]
- CharacterForge Version: [versione]
- GPU: [modello]
- VRAM: [GB]
- RAM: [GB]

**Log Error:**
[Log completo console]

**Workflow:**
[JSON workflow se possibile]

**Steps to Reproduce:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

**Expected Result:**
[Cosa ti aspettavi]

**Actual Result:**
[Cosa hai ottenuto]

## Prevenzione Problemi

### Best Practices per Evitare Problemi

1. Usa sempre risoluzione 2048x1024
2. Mantieni preserve_structure: true
3. Testing incrementale (un controller alla volta)
4. Documenta configurazioni funzionanti
5. Backup workflow prima di modifiche major
6. Aggiorna ComfyUI e CharacterForge regolarmente

### Monitoraggio Regolare

1. Controlla VRAM usage durante generazioni
2. Verifica RAM non saturi
3. Monitora temperature GPU
4. Log errori ricorrenti

## Risorse Aggiuntive

- Installation Guide: docs/installation.md
- Usage Guide: docs/usage_guide.md
- API Reference: docs/api_reference.md
- Hybrid Mode Guide: docs/hybrid_mode.md

Autore: Massimo Bivona
Versione: 2.0.0
Licenza: MIT
