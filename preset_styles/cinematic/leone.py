"""
CharacterForge Cinematic - Sergio Leone
========================================

Cinematic presets inspired by Sergio Leone:
operatic widescreen composition, extreme close-ups, monumental landscapes,
dust, weathered textures, deliberate pacing, expressive faces, anamorphic
optics, long lenses, strong contrast, earthy palettes and rhythmic visual
tension between vast spaces and intimate details.
"""

LEONE_STYLES = {

    "leone_spaghetti_western": {
        "name": "Sergio Leone — Spaghetti Western",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "1960s Italian spaghetti western cinematography, anamorphic 2.35:1 "
            "widescreen composition, sun-blasted desert landscapes, ochre dust, "
            "weathered wood, faded leather, tobacco brown, muted blue sky, "
            "strong Mediterranean sunlight, hard directional shadows, "
            "35mm anamorphic lenses, long-lens compression for distant figures, "
            "extreme close-ups of eyes and faces, wide establishing shots with "
            "tiny human figures against monumental landscapes, deliberate visual "
            "symmetry, low camera angles, dry atmospheric haze, subtle optical "
            "distortion, photochemical film grain, slightly faded Eastmancolor "
            "texture, dusty production design, tactile costumes and aged surfaces, "
            "operatic stillness before sudden action"
        ),
        "negative_prompt": (
            "modern western cinematography, digital sharpness, teal and orange, "
            "clean pristine costumes, glossy CGI landscapes, handheld documentary, "
            "soft commercial lighting, excessive bokeh, modern action editing"
        ),
        "denoise": 0.81,
        "structure_weight": 0.94,
        "color_boost": 1.08,
        "keywords": [
            "spaghetti western",
            "anamorphic",
            "extreme close-up",
            "desert",
            "ochre dust",
            "Eastmancolor",
            "operatic widescreen"
        ],
    },

    "leone_good_bad_ugly": {
        "name": "Sergio Leone — The Good, the Bad and the Ugly",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "epic 1960s spaghetti western photography, anamorphic widescreen, "
            "enormous Civil War era landscapes, dry yellow earth, dusty gray-green "
            "vegetation, weathered uniforms, sun-bleached architecture, "
            "hard overhead sunlight, long shadows near sunset, telephoto compression "
            "across open terrain, extreme facial close-ups, intense eyes filling the "
            "frame, wide compositions contrasting tiny figures with immense terrain, "
            "slow deliberate camera movement, circular spatial staging, dusty "
            "atmospheric perspective, period Eastmancolor, fine organic grain, "
            "slightly imperfect optical rendering, tactile dirt and sweat, "
            "monumental production design and operatic scale"
        ),
        "negative_prompt": (
            "modern digital western, clean military uniforms, glossy Hollywood "
            "photography, teal-orange grading, drone footage, excessive HDR, "
            "plastic skin, videogame environment, modern props"
        ),
        "denoise": 0.82,
        "structure_weight": 0.95,
        "color_boost": 1.1,
        "keywords": [
            "Civil War landscape",
            "extreme close-up",
            "telephoto",
            "anamorphic",
            "dust",
            "operatic scale",
            "1960s western"
        ],
    },

    "leone_once_upon_a_time": {
        "name": "Sergio Leone — Once Upon a Time",
        "category": "cinematic",
        "era": "1960s–1970s",
        "prompt": (
            "grand 1960s-1970s anamorphic epic cinematography, warm amber and "
            "sepia-inflected palette, monumental American landscapes and railway "
            "architecture, weathered wood, brass, leather and rust textures, "
            "soft golden-hour sunlight, strong backlight through dust and smoke, "
            "anamorphic 35mm lenses, slow tracking shots, elegant lateral camera "
            "movement, deep layered compositions, long dissolving perspective, "
            "expressive faces framed against large environments, controlled shallow "
            "depth of field for intimate moments, fine film grain, subtle halation, "
            "period optical softness, elaborate production design, nostalgic "
            "mythological atmosphere, melancholy grandeur"
        ),
        "negative_prompt": (
            "modern digital cinema, hyper-clean detail, neon palette, fast handheld "
            "camera, generic western photography, CGI spectacle, excessive contrast, "
            "modern architecture, sterile environments"
        ),
        "denoise": 0.8,
        "structure_weight": 0.92,
        "color_boost": 1.12,
        "keywords": [
            "anamorphic epic",
            "railway",
            "golden hour",
            "dust and smoke",
            "nostalgia",
            "American landscape",
            "melancholy grandeur"
        ],
    },

    "leone_extreme_closeup": {
        "name": "Sergio Leone — Extreme Close-Up",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "iconic spaghetti western extreme close-up cinematography, anamorphic "
            "35mm lens, face occupying most of the frame, eyes sharply isolated, "
            "skin texture, sweat, dust and wrinkles rendered with tactile realism, "
            "very controlled depth of field, strong directional sunlight, hard "
            "facial shadows, catchlights in the eyes, tiny background fragments "
            "compressed by long lenses, muted earth tones, tobacco brown, dusty "
            "gold and faded blue, subtle lens breathing, organic film grain, "
            "period optical softness, deliberate static framing, psychological "
            "tension created through facial micro-expression and silence"
        ),
        "negative_prompt": (
            "beauty portrait, modern fashion photography, softbox glamour lighting, "
            "perfect skin, excessive retouching, digital sharpness, beauty bokeh, "
            "modern color grading, plastic textures, exaggerated facial distortion"
        ),
        "denoise": 0.78,
        "structure_weight": 0.93,
        "color_boost": 1.06,
        "keywords": [
            "extreme close-up",
            "eyes",
            "anamorphic lens",
            "dust",
            "sweat",
            "facial texture",
            "psychological tension"
        ],
    },

    "leone_duel": {
        "name": "Sergio Leone — The Final Duel",
        "category": "cinematic",
        "era": "1960s",
        "prompt": (
            "operatic western duel cinematography, anamorphic 2.35:1 frame, "
            "large circular or architectural staging, three-dimensional spatial "
            "relationships between opposing figures, alternating extreme close-ups "
            "and monumental wide shots, 35mm anamorphic lenses, long-lens facial "
            "compression, hard desert sunlight, deep eye sockets, dust suspended "
            "in the air, earth brown and sun-bleached yellow palette, restrained "
            "blue accents, very slow camera movement, deliberate push-ins, "
            "precise eyeline matching, strong negative space, long pauses, "
            "photochemical grain, subtle halation and period optical imperfections, "
            "mythic tension and ritualistic composition"
        ),
        "negative_prompt": (
            "fast action editing, shaky camera, modern tactical cinematography, "
            "digital clarity, excessive muzzle flashes, videogame action, neon "
            "colors, glossy surfaces, generic Hollywood western"
        ),
        "denoise": 0.83,
        "structure_weight": 0.96,
        "color_boost": 1.07,
        "keywords": [
            "duel",
            "anamorphic",
            "extreme close-up",
            "negative space",
            "eyeline",
            "dust",
            "ritualistic composition"
        ],
    },

    "leone_monument_valley": {
        "name": "Sergio Leone — Mythic Landscape",
        "category": "cinematic",
        "era": "1960s–1970s",
        "prompt": (
            "mythic western landscape cinematography, ultra-wide anamorphic "
            "composition, enormous desert formations, isolated human figures, "
            "dry mesas, rocky plains, distant mountains, dusty atmosphere, "
            "sun-bleached ochre, burnt sienna, faded turquoise sky and muted "
            "olive vegetation, hard Mediterranean-style sunlight, long shadows, "
            "atmospheric perspective, 35mm anamorphic optics, subtle edge softness, "
            "deep focus across large environments, tiny silhouettes against "
            "monumental terrain, slow lateral tracking, static tableaux, "
            "organic 1960s film grain, restrained halation, weathered production "
            "design and a sense of historical myth rather than photographic realism"
        ),
        "negative_prompt": (
            "modern landscape photography, drone perspective, HDR, ultra-clean "
            "digital image, lush tropical vegetation, fantasy CGI landscape, "
            "neon colors, oversaturated skies, modern western styling"
        ),
        "denoise": 0.8,
        "structure_weight": 0.94,
        "color_boost": 1.1,
        "keywords": [
            "mythic landscape",
            "anamorphic widescreen",
            "desert",
            "monumental scale",
            "deep focus",
            "atmospheric perspective",
            "1960s film grain"
        ],
    },
}

__all__ = ["LEONE_STYLES"]
