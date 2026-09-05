# Modalità Ibrida - ComfyUI-CharacterForge

## Panoramica

La modalità ibrida permette di commutare dinamicamente tra Text-to-Sheet e Image-to-Sheet senza ricostruire il workflow. Il nodo CharacterForgeHybridLatentSwitch gestisce automaticamente il routing del latent in base alla modalità selezionata.

## Modalità Disponibili

### Text-to-Sheet

Generazione character sheet da prompt testuale.

Quando usarla:

- Vuoi generare un character sheet da zero
- Hai specifiche precise ma nessuna immagine riferimento
- Crei concetti originali

Configurazione:

- mode: text_to_sheet
- latent: EmptyLatentImage 2048x1024
- denoise: 1.0
- steps: 25-30

### Image-to-Sheet

Generazione character sheet da immagine di riferimento mantenendo l'identità.

Quando usarla:

- Hai un'immagine del soggetto
- Vuoi mantenere identità di un personaggio esistente
- Converti un ritratto in character sheet completo

Configurazione:

- mode: image_to_sheet
- latent: VAEEncode da immagine riferimento
- IPAdapter: weight 0.7
- denoise: 0.6
- steps: 30-35

## Setup Workflow Ibrido

### Struttura Nodi

1. EmptyLatentImage 2048x1024
2. LoadImage (immagine riferimento)
3. VAEEncode (converte immagine in latent)
4. CharacterForgeHybridLatentSwitch
5. IPAdapter (solo per Image mode)
6. CLIP Text Encode (schema base)
7. CharacterForge Controllers
8. KSampler
9. VAEDecode
10. SaveImage

### Collegamenti

EmptyLatentImage → text_latent (Hybrid Switch)

LoadImage → VAEEncode → image_latent (Hybrid Switch)

LoadImage → IPAdapter → KSampler model

LoadImage → image_reference (Hybrid Switch, opzionale)

Hybrid Switch selected_latent → KSampler latent_image

CLIP Text Encode → Controllers → KSampler positive

## Configurazione IPAdapter

### Parametri Consigliati

weight: 0.7
strength: 0.8
noise: 0.0

### Quando Aumentare Weight

- 0.8-0.9: Se l'identità non si mantiene sufficientemente
- 1.0+: Per identità molto forte (rischio sovrascritture)

### Quando Diminuire Weight

- 0.5-0.6: Se vuoi più variazione dal riferimento
- 0.3-0.4: Solo ispirazione leggera senza identità forte

## Parametri KSampler

### Text Mode (denoise 1.0)

steps: 25-30
cfg: 4.5-5.5
sampler: dpmpp_2m
scheduler: karras

### Image Mode (denoise 0.6)

steps: 30-35
cfg: 5.0-6.0
sampler: dpmpp_2m
scheduler: karras

## Preparazione Immagine Riferimento

### Formato Ideale

- Risoluzione: 512x512 o 768x768
- Contenuto: Ritratto o full-body chiaro
- Illuminazione: Uniforme senza ombre dure
- Sfondo: Neutro (bianco o grigio)

### Consigli

- Immagini con volto ben visibile funzionano meglio
- Evitare immagini con occlusioni parziali del volto
- Illuminazione frontale produce risultati più coerenti
- Immagini ad alta risoluzione non necessariamente migliori

## Switch Durante il Lavoro

Puoi cambiare modalità durante il lavoro:

1. Genera prima in Text mode per test layout
2. Cambia in Image mode per affinare identità
3. Usa stesso seed per confronto diretto

### Workflow Completo Esempio

Fase 1: Test Layout

- mode: text_to_sheet
- Genera e verifica layout 4 colonne
- Se layout corretto, passa a fase 2

Fase 2: Applica Identità

- mode: image_to_sheet
- Carica immagine riferimento
- IPAdapter weight: 0.7
- Genera e verifica identità mantenuta

Fase 3: Affina Parametri

- Se identità debole: IPAdapter weight 0.8, denoise 0.55
- Se troppo simile: IPAdapter weight 0.5, denoise 0.75
- Se layout rotto: Aumenta structure_strength

## Troubleshooting

### Identità Non Mantenuta

Causa: IPAdapter weight troppo basso o denoise troppo alto.

Soluzioni:

1. Aumenta IPAdapter weight a 0.8-0.9
2. Riduci denoise a 0.5-0.55
3. Aumenta steps a 35-40

### Immagine Troppo Simile

Causa: IPAdapter weight troppo alto o denoise troppo basso.

Soluzioni:

1. Riduci IPAdapter weight a 0.4-0.6
2. Aumenta denoise a 0.7-0.8
3. Verifica che schema base sia collegato

### Latent Non Valido

Causa: VAEEncode non collegato correttamente o immagine corrotta.

Soluzioni:

1. Verifica collegamento VAEEncode
2. Attiva auto_validate nel Hybrid Switch
3. Attiva debug_mode per log dettagliato
4. Verifica formato immagine (JPG, PNG supportati)

### Layout Rotto in Image Mode

Causa: Conflitto tra conditioning schema e IPAdapter.

Soluzioni:

1. Aumenta structure_strength a 0.5
2. Usa combination_method: blend
3. Riduci IPAdapter weight leggermente
4. Verifica risoluzione 2048x1024

## Best Practices

### 1. Verifica Latent Prima di Generare

Controlla sempre:

- text_latent abbia shape 2048x1024
- image_latent abbia dimensioni compatibili
- auto_validate sia attivo

### 2. Ottimizzazione Identità Progressiva

Approccio incrementale:

1. Inizia con IPAdapter weight 0.7
2. Se identità insufficiente, aumenta a 0.8
3. Solo se necessario, arriva a 0.9
4. Oltre 0.9 rischi sovrascritture del layout

### 3. Documenta Configurazioni

Mantieni un log delle configurazioni che funzionano:

- IPAdapter weight usato
- denoise applicato
- steps e cfg
- seed utilizzato
- Risultato ottenuto

### 4. Seed Management

- Fissa seed dopo aver trovato configurazione ottimale
- Stesso seed per confronti Text vs Image mode
- Seed diversi per variazioni

## Limitazioni Note

### VRAM Usage

Image mode consuma più VRAM:

- Text mode: 10-12 GB
- Image mode: 13-15 GB (con IPAdapter)

Su sistemi con 16GB VRAM, considera:

- Risoluzione ridotta temporanea (1536x768)
- Flag --lowvram in ComfyUI
- Cache meno aggressiva

### Compatibilità Immagini

Formati testati:

- JPG: Supportato completamente
- PNG: Supportato completamente
- WEBP: Supportato con possibile perdita qualità

Formati non testati:

- TIFF: Non garantito
- BMP: Non garantito
- Immagini con alpha channel: Possibili problemi

## Esempi Pratici

### Esempio 1: Ritratto to Character Sheet

Scenario: Hai un ritratto di un personaggio e vuoi il character sheet completo.

Setup:

1. LoadImage: ritratto.jpg
2. mode: image_to_sheet
3. IPAdapter weight: 0.7
4. denoise: 0.6

Risultato atteso: Character sheet 4 colonne con identità mantenuta al 70-80%.

### Esempio 2: Concept Art to Sheet

Scenario: Hai concept art di un personaggio e vuoi un reference tecnico.

Setup:

1. LoadImage: concept_art.png
2. mode: image_to_sheet
3. IPAdapter weight: 0.6 (concept art ha già stile)
4. denoise: 0.7 (più libertà interpretativa)

Risultato atteso: Character sheet con caratteristiche del concept ma più standardizzato.

### Esempio 3: Testing Layout

Scenario: Vuoi testare il layout senza immagine riferimento.

Setup:

1. mode: text_to_sheet
2. IPAdapter: non collegato
3. denoise: 1.0

Risultato atteso: Character sheet standard con soggetto generico.

## Configurazione Avanzata

### Combining Multiple References

Workflow avanzato con multiple immagini:

1. LoadImage 1 (volto)
2. LoadImage 2 (corpo)
3. IPAdapter separati per volto e corpo
4. Hybrid Switch per latent routing

Nota: Richiede IPAdapter Plus custom nodes.

### Custom Denoise Curves

Per workflow avanzati, puoi implementare denoise variabile:

- Inizia con denoise 0.5
- Incrementa progressivamente durante sampling
- Richiede KSampler Advanced

## Supporto

Per problemi specifici della modalità ibrida:

1. Controlla la sezione Troubleshooting sopra
2. Verifica la documentazione completa in docs/
3. Apri issue su GitHub con dettagli:
   - Configurazione utilizzata
   - Log della console
   - Immagini di esempio (input e output)

Autore: Massimo Bivona
Versione: 2.0.0
Licenza: MIT