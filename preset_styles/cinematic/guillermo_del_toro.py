"""
CharacterForge Cinematic - Guillermo del Toro
=============================================

Cinematic presets inspired by the visual language of Guillermo del Toro:
gothic fairy-tale production design, tactile creature effects, saturated
color contrasts, expressive practical textures, chiaroscuro, ornate spaces,
and poetic horror/fantasy imagery.
"""

DEL_TORO_STYLES = {

    "del_toro_gothic_fantasy": {
        "name": "Guillermo del Toro — Gothic Fantasy",
        "category": "cinematic",
        "era": "2000s–2020s",
        "prompt": (
            "gothic fairy-tale cinematography, richly tactile production design, "
            "ornate decaying architecture, practical creature textures, carved wood, "
            "aged stone, brass, leather, dust and damp surfaces, expressive chiaroscuro, "
            "deep pools of shadow, warm amber practical lights against cool blue-green "
            "ambient light, saturated but slightly weathered colors, atmospheric haze, "
            "subtle volumetric light, 35mm cinematic photography, medium-wide spherical "
            "lenses, controlled depth of field, carefully layered foreground and "
            "background elements, deliberate symmetrical and storybook compositions, "
            "slow expressive camera movement, painterly framing, tactile film grain, "
            "organic photographic texture, melancholic fairy-tale atmosphere, "
            "dark beauty rather than glossy fantasy"
        ),
        "negative_prompt": (
            "plastic CGI surfaces, generic fantasy concept art, sterile environments, "
            "clean modern interiors, excessive bloom, glossy digital rendering, "
            "flat lighting, weightless objects, videogame look, oversharpening, "
            "extreme depth of field, empty backgrounds, modern fashion photography"
        ),
        "denoise": 0.78,
        "structure_weight": 0.84,
        "color_boost": 1.12,
        "keywords": [
            "gothic fairy tale",
            "tactile production design",
            "amber and blue-green lighting",
            "practical textures",
            "chiaroscuro",
            "35mm",
            "ornate decay",
            "poetic horror"
        ],
    },

    "del_toro_pans_labyrinth": {
        "name": "Guillermo del Toro — Dark Fairy Tale",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "dark European fairy-tale cinematography, postwar rural Spain atmosphere, "
            "old stone interiors, damp forests, moss, roots, candles, worn wood and "
            "handcrafted objects, muted earth tones interrupted by deep ochre, blood red "
            "and sickly green accents, cool natural daylight contrasting with warm "
            "candlelight, soft overcast skies, volumetric forest haze, shallow but "
            "purposeful depth of field, 35mm spherical lenses, gentle focus transitions, "
            "low and intimate camera placement, carefully composed doorways and corridors, "
            "storybook framing with unsettling negative space, practical creature makeup, "
            "handmade prosthetics, subtle film grain, slightly desaturated photochemical "
            "texture, dreamlike realism, innocent beauty surrounded by menace"
        ),
        "negative_prompt": (
            "bright whimsical fantasy, glossy fairy tale, clean CGI creatures, "
            "plastic textures, neon fantasy colors, modern architecture, excessive "
            "sharpness, digital game rendering, cheerful atmosphere, superhero lighting, "
            "perfectly clean costumes, artificial studio backgrounds"
        ),
        "denoise": 0.8,
        "structure_weight": 0.86,
        "color_boost": 1.08,
        "keywords": [
            "dark fairy tale",
            "Spanish rural atmosphere",
            "forest haze",
            "candlelight",
            "ochre",
            "blood red",
            "sickly green",
            "35mm film",
            "practical creatures"
        ],
    },

    "del_toro_creature": {
        "name": "Guillermo del Toro — Creature Cinema",
        "category": "cinematic",
        "era": "2000s–2010s",
        "prompt": (
            "cinematic creature portrait, handcrafted practical creature design, "
            "extremely tactile skin and biological surface detail, pores, wrinkles, "
            "wet textures, translucent membranes, sculpted prosthetics, expressive eyes, "
            "organic asymmetry, macro cinematography combined with environmental wide shots, "
            "soft directional key light, deep shadow shaping, cool cyan ambient light with "
            "warm amber highlights, controlled specular reflections, humid atmospheric haze, "
            "35mm and macro lens character, shallow depth of field for intimate creature "
            "details, layered foreground elements, slow deliberate dolly perspective, "
            "physical production design surrounding the creature, subtle anamorphic character, "
            "fine film grain, rich blacks, tactile photochemical texture, creature treated "
            "as a tragic living presence rather than a digital effect"
        ),
        "negative_prompt": (
            "generic monster CGI, videogame creature, smooth plastic skin, rubber toy look, "
            "overly sharp digital textures, sterile laboratory rendering, excessive metallic "
            "surfaces, superhero spectacle, flat studio lighting, cartoon proportions, "
            "weightless creature, synthetic fur, artificial glossy eyes"
        ),
        "denoise": 0.82,
        "structure_weight": 0.8,
        "color_boost": 1.15,
        "keywords": [
            "practical creature",
            "prosthetic makeup",
            "macro detail",
            "wet organic textures",
            "cyan amber contrast",
            "creature portrait",
            "tactile skin",
            "35mm"
        ],
    },

    "del_toro_hellboy": {
        "name": "Guillermo del Toro — Occult Action",
        "category": "cinematic",
        "era": "2000s",
        "prompt": (
            "dark occult action cinematography, industrial gothic environments, ancient "
            "stone mixed with rusted metal and decaying machinery, practical prosthetics, "
            "large physical creature silhouettes, dramatic backlighting, hard warm sources "
            "cutting through cool blue-green darkness, smoky interiors, shafts of light, "
            "deep chiaroscuro, strong rim lighting around silhouettes, 35mm anamorphic "
            "cinematic photography, moderate depth of field, dynamic low-angle compositions, "
            "wide lenses close to subjects, expressive tracking shots, physical debris and "
            "weathered surfaces, saturated crimson accents against teal-black shadows, "
            "subtle anamorphic flare, organic film grain, tactile action staging, "
            "mythological horror grounded in physical environments"
        ),
        "negative_prompt": (
            "clean superhero blockbuster, glossy CGI, weightless action, generic comic-book "
            "rendering, excessive lens flare, plastic armor, sterile environments, flat "
            "lighting, overexposed highlights, videogame screenshot, futuristic clean design"
        ),
        "denoise": 0.79,
        "structure_weight": 0.83,
        "color_boost": 1.18,
        "keywords": [
            "occult action",
            "industrial gothic",
            "35mm anamorphic",
            "crimson accents",
            "teal-black shadows",
            "practical prosthetics",
            "dynamic low angle",
            "physical debris"
        ],
    },

    "del_toro_crimson_peak": {
        "name": "Guillermo del Toro — Crimson Gothic",
        "category": "cinematic",
        "era": "2010s",
        "prompt": (
            "luxurious gothic romantic horror cinematography, enormous decaying Victorian "
            "mansion, peeling wallpaper, carved wood, dark velvet, tarnished brass, "
            "snow blowing through broken architecture, crimson stains and blood-red "
            "visual motifs, deep burgundy, antique gold, cold blue-gray daylight, "
            "warm candlelight inside vast rooms, strong color symbolism, expressive "
            "production design, wide 35mm anamorphic compositions, controlled shallow "
            "depth of field, elegant foreground framing, long corridors and vertical "
            "architectural lines, slow camera movement, soft diffusion around practical "
            "lights, atmospheric dust and snow, subtle lens breathing, rich film grain, "
            "dense blacks, painterly highlights, romantic decay, beauty and horror sharing "
            "the same frame"
        ),
        "negative_prompt": (
            "generic haunted house, cheap horror lighting, modern interior, clean surfaces, "
            "flat production design, excessive digital effects, neon colors, glossy CGI, "
            "jump-scare aesthetic, harsh television lighting, empty composition, "
            "overly sharp digital photography"
        ),
        "denoise": 0.81,
        "structure_weight": 0.87,
        "color_boost": 1.2,
        "keywords": [
            "Victorian gothic",
            "crimson symbolism",
            "burgundy",
            "antique gold",
            "cold blue-gray",
            "candlelight",
            "35mm anamorphic",
            "romantic decay"
        ],
    },
}

__all__ = ["DEL_TORO_STYLES"]
