"""
Stili Anime/Manga Completi - v7.0
===================================

128 stili totali divisi per:
- 7 Epoche (70s, 80s, 90s, 2000s, moderno, ecc.)
- 30 Generi (shonen, seinen, mecha, moe, shojo, cyberpunk, chibi, super robot,
  space opera, arti marziali, ecchi, kaiju, storico, hentai, harem, yaoi, yuri,
  commedia, cyberpunk classico, mecha organico, post-apocalittico, vampiri, ecc.)
- 23 Studi specifici (Ghibli, Trigger, MAPPA, WIT, Bones, KyoAni, Ufotable,
  Sunrise, Gainax, Toei, Madhouse, Production I.G, Pierrot, Shaft, A-1,
  Deen, Gonzo, J.C.Staff, Xebec, 8bit, P.A. Works, Zero-G)
- 54 Artisti leggendari (Toriyama, Tezuka, Otomo, Araki, Togashi, Inoue, Urasawa,
  Miyazaki, Shinkai, Fujimoto, Ito, Kim Jung Gi, ecc.)
- 11 Serie specifiche + 3 Varianti specifiche (Galaxy Express, Transformers G1,
  Lupin III, City Hunter, Dragon Ball, Dragon Ball Z, Saint Seiya, One Piece,
  Ranma 1/2, Yu Yu Hakusho + AKIRA specific, Inuyasha specific, Berserk 1997)

CHANGELOG v7.0:
- FIX critico: import "dragon_ball_z" corretto -> akira_toriyama_dragon_ball_z.py
- Aggiunti 20 stili nuovi:
    Generi: comedy_pure, cyberpunk_classic, harem, mecha_organic,
            post_apocalyptic, vampire_supernatural, yaoi, yuri
    Studi:  deen, gonzo, jc_staff, xebec, eight_bit, pa_works, zero_g
    Serie:  toriyama_dragon_ball, oda_one_piece, takahashi_ranma,
            togashi_yuyu, city_hunter
- Loader sicuro (_load): un file mancante o una variabile con nome diverso
  non blocca mai il caricamento di ComfyUI (fallback automatico o skip + warning)
"""

import importlib


# ============================================
# LOADER SICURO
# ============================================

_STYLE_HINT_KEYS = (
    "name", "style_name", "prompt", "negative_prompt",
    "description", "era", "artist", "studio", "genre",
)


def _load(module_name, *var_names):
    """Importa uno stile in modo sicuro.

    - Prova in ordine i nomi di variabile indicati.
    - Se nessuno corrisponde, cerca nel modulo il primo dict pubblico
      che sembra una config di stile (fallback automatico).
    - Se il modulo manca o non contiene stili, restituisce None
      e stampa un warning, senza far crashare il pacchetto.
    """
    try:
        module = importlib.import_module("." + module_name, __package__)
    except Exception as e:
        print(f"[CharacterForge-Anime] WARNING: modulo '{module_name}' non importabile: {e}")
        return None

    for var_name in var_names:
        value = getattr(module, var_name, None)
        if isinstance(value, dict):
            return value

    # Fallback: primo attributo pubblico che sembra una config di stile
    for attr_name in sorted(vars(module)):
        if attr_name.startswith("_"):
            continue
        value = getattr(module, attr_name)
        if isinstance(value, dict) and any(k in value for k in _STYLE_HINT_KEYS):
            print(f"[CharacterForge-Anime] INFO: fallback usato per '{module_name}' -> {attr_name}")
            return value

    print(f"[CharacterForge-Anime] WARNING: nessuno stile trovato in '{module_name}'")
    return None


# ============================================
# EPOCHE (7)
# ============================================

_EPOCHE_RAW = {
    "vintage_70s_anime": _load("vintage_70s", "VINTAGE_70S_ANIME"),
    "retro_80s_anime": _load("retro_80s_anime", "RETRO_80S_ANIME"),
    "ova_80s_style": _load("ova_80s", "OVA_80S_STYLE"),
    "anime_90s_classic": _load("anime_90s_classic", "ANIME_90S_CLASSIC"),
    "anime_2000s_digital": _load("anime_2000s", "ANIME_2000S_DIGITAL"),
    "anime_modern": _load("anime_modern", "ANIME_MODERN"),
    "anime_cinematic": _load("anime_cinematic", "ANIME_CINEMATIC"),
}


# ============================================
# GENERI (30)
# ============================================

_GENERI_RAW = {
    # Originali (22)
    "shonen_90s_style": _load("shonen_90s", "SHONEN_90S_STYLE"),
    "seinen_90s_style": _load("seinen_90s", "SEINEN_90S_STYLE"),
    "mecha_90s_style": _load("mecha_90s", "MECHA_90S_STYLE"),
    "moe_2000s_style": _load("moe_2000s", "MOE_2000S_STYLE"),
    "shonen_battle": _load("shonen_battle", "SHONEN_BATTLE"),
    "isekai_fantasy": _load("isekai_fantasy", "ISEKAI_FANTASY"),
    "slice_of_life": _load("slice_of_life", "SLICE_OF_LIFE"),
    "horror_anime": _load("horror_anime", "HORROR_ANIME"),
    "shojo_modern": _load("shojo_modern", "SHOJO_MODERN"),
    "mecha_military": _load("mecha_military", "MECHA_MILITARY"),
    "psychological_thriller": _load("psychological_thriller", "PSYCHOLOGICAL_THRILLER"),
    "sports_modern": _load("sports_modern", "SPORTS_MODERN"),
    "musical_idol": _load("musical_idol", "MUSICAL_IDOL"),
    "cyberpunk_modern": _load("cyberpunk_modern", "CYBERPUNK_MODERN"),
    "chibi_style": _load("chibi_style", "CHIBI_STYLE"),
    "super_robot": _load("super_robot", "SUPER_ROBOT"),
    "space_opera": _load("space_opera", "SPACE_OPERA"),
    "martial_arts": _load("martial_arts", "MARTIAL_ARTS"),
    "ecchi_modern": _load("ecchi_modern", "ECCHI_MODERN"),
    "kaiju_monster": _load("kaiju_monster", "KAIJU_MONSTER"),
    "historical": _load("historical", "HISTORICAL"),
    "hentai_artistic": _load("hentai", "HENTAI_ARTISTIC", "HENTAI"),
    # Nuovi (8)
    "comedy_pure": _load("comedy_pure", "COMEDY_PURE", "COMEDY_PURE_STYLE"),
    "cyberpunk_classic": _load("cyberpunk_classic", "CYBERPUNK_CLASSIC", "CYBERPUNK_CLASSIC_STYLE"),
    "harem": _load("harem", "HAREM", "HAREM_STYLE"),
    "mecha_organic": _load("mecha_organic", "MECHA_ORGANIC", "MECHA_ORGANIC_STYLE"),
    "post_apocalyptic": _load("post_apocalyptic", "POST_APOCALYPTIC", "POST_APOCALYPTIC_STYLE"),
    "vampire_supernatural": _load("vampire_supernatural", "VAMPIRE_SUPERNATURAL", "VAMPIRE_SUPERNATURAL_STYLE"),
    "yaoi": _load("yaoi", "YAOI", "YAOI_STYLE"),
    "yuri": _load("yuri", "YURI", "YURI_STYLE"),
}


# ============================================
# STUDIO SPECIFICI (23)
# ============================================

_STUDI_RAW = {
    # Originali (16)
    "ghibli": _load("ghibli", "GHIBLI"),
    "trigger_style": _load("trigger", "TRIGGER_STYLE"),
    "trigger_detailed_style": _load("trigger_studio_detailed", "TRIGGER_DETAILED_STYLE", "TRIGGER_STUDIO_DETAILED_STYLE"),
    "ufotable_style": _load("ufotable", "UFOTABLE_STYLE"),
    "mappa_style": _load("mappa", "MAPPA_STYLE"),
    "wit_studio_style": _load("wit_studio", "WIT_STUDIO_STYLE"),
    "bones_studio_style": _load("bones", "BONES_STUDIO_STYLE"),
    "kyoto_animation_style": _load("kyoto_animation", "KYOTO_ANIMATION_STYLE"),
    "sunrise_style": _load("sunrise", "SUNRISE_STYLE"),
    "gainax_style": _load("gainax", "GAINAX_STYLE"),
    "toei_style": _load("toei", "TOEI_STYLE"),
    "madhouse_style": _load("madhouse", "MADHOUSE_STYLE"),
    "production_ig_style": _load("production_ig", "PRODUCTION_IG_STYLE"),
    "pierrot_style": _load("pierrot", "PIERROT_STYLE"),
    "shaft_style": _load("shaft", "SHAFT_STYLE"),
    "a1_pictures_style": _load("a1_pictures", "A1_PICTURES_STYLE"),
    # Nuovi (7)
    "deen_style": _load("deen", "DEEN_STYLE"),
    "gonzo_style": _load("gonzo", "GONZO_STYLE"),
    "jc_staff_style": _load("jc_staff", "JC_STAFF_STYLE", "JC_STAFF"),
    "xebec_style": _load("xebec", "XEBEC_STYLE"),
    "eight_bit_style": _load("eight_bit", "EIGHT_BIT_STYLE", "EIGHTBIT_STYLE"),
    "pa_works_style": _load("pa_works", "PA_WORKS_STYLE", "PAWORKS_STYLE"),
    "zero_g_style": _load("zero_g", "ZERO_G_STYLE", "ZEROG_STYLE"),
}


# ============================================
# ARTISTI LEGGENDARI (54)
# ============================================

_ARTISTI_RAW = {
    # Maestri Storici
    "toriyama_style": _load("toriyama", "TORIYAMA_STYLE"),
    "tezuka_style": _load("tezuka", "TEZUKA_STYLE"),
    "otomo_style": _load("otomo", "OTOMO_STYLE"),
    "kishimoto_style": _load("kishimoto", "KISHIMOTO_STYLE"),
    "oda_style": _load("oda", "ODA_STYLE"),
    "takahashi_rumiko_style": _load("takahashi_rumiko", "TAKAHASHI_RUMIKO_STYLE"),
    "clamp_style": _load("clamp", "CLAMP_STYLE"),
    "kubo_style": _load("kubo", "KUBO_STYLE"),
    "kubo_detailed_style": _load("kubo_tite_detailed", "KUBO_DETAILED_STYLE", "KUBO_TITE_DETAILED_STYLE"),
    "miura_style": _load("miura", "MIURA_STYLE"),
    "kon_satoshi_style": _load("kon_satoshi", "KON_SATOSHI_STYLE"),
    "shiro_masamune_style": _load("shiro_masamune", "SHIRO_MASAMUNE_STYLE"),
    "watanabe_style": _load("watanabe", "WATANABE_STYLE"),
    "go_nagai_style": _load("go_nagai", "GO_NAGAI_STYLE"),
    "tetsuo_hara_style": _load("tetsuo_hara", "TETSUO_HARA_STYLE"),
    "yoichi_takahashi_style": _load("yoichi_takahashi", "YOICHI_TAKAHASHI_STYLE"),
    "masami_kurumada_style": _load("masami_kurumada", "MASAMI_KURUMADA_STYLE"),
    "tsukasa_hojo_style": _load("city_hunter", "TSUKASA_HOJO_STYLE"),
    "yoshiyuki_tomino_style": _load("yoshiyuki_tomino", "YOSHIYUKI_TOMINO_STYLE"),
    "leiji_matsumoto_style": _load("leiji_matsumoto", "LEIJI_MATSUMOTO_STYLE"),
    "hideaki_anno_style": _load("hideaki_anno", "HIDEAKI_ANNO_STYLE"),
    # Maestri Moderni
    "miyazaki_solo_style": _load("miyazaki_solo", "MIYAZAKI_SOLO_STYLE"),
    "mamoru_hosoda_style": _load("mamoru_hosoda", "MAMORU_HOSODA_STYLE"),
    "makoto_shinkai_style": _load("makoto_shinkai", "MAKOTO_SHINKAI_STYLE"),
    "ryo_timo_style": _load("ryo_timo", "RYO_TIMO_STYLE"),
    "masaaki_yuasa_style": _load("masaaki_yuasa", "MASAAKI_YUASA_STYLE"),
    "ken_akamatsu_style": _load("ken_akamatsu", "KEN_AKAMATSU_STYLE"),
    "naoko_takeuchi_style": _load("naoko_takeuchi", "NAOKO_TAKEUCHI_STYLE"),
    "koyoharu_gotouge_style": _load("koyoharu_gotouge", "KOYOHARU_GOTOUGE_STYLE"),
    "gege_akutami_style": _load("gege_akutami", "GEGE_AKUTAMI_STYLE"),
    "one_murata_style": _load("one_murata", "ONE_MURATA_STYLE"),
    # Nuovi Maestri
    "ishida_sui_style": _load("ishida_sui", "ISHIDA_SUI_STYLE"),
    "arakawa_hiromu_style": _load("arakawa_hiromu", "ARAKAWA_HIROMU_STYLE"),
    "fujimoto_tatsuki_style": _load("fujimoto_tatsuki", "FUJIMOTO_TATSUKI_STYLE"),
    # CRITICI (JoJo, HxH, Vagabond, Monster, Lupin)
    "araki_style": _load("araki", "ARAKI_STYLE"),
    "togashi_style": _load("togashi", "TOGASHI_STYLE"),
    "inoue_style": _load("inoue", "INOUE_STYLE"),
    "urasawa_style": _load("urasawa", "URASAWA_STYLE"),
    "monkey_punch_style": _load("monkey_punch", "MONKEY_PUNCH_STYLE"),
    # ALTI (Cobra, Bastard, Asano)
    "terasawa_style": _load("terasawa", "TERASAWA_STYLE"),
    "hagiwara_style": _load("hagiwara", "HAGIWARA_STYLE"),
    "asano_style": _load("asano", "ASANO_STYLE"),
    # STILI UNICI / ESTREMI
    "yasuhiko_yoshikazu_style": _load("yasuhiko_yoshikazu", "YASUHIKO_YOSHIKAZU", "YASUHIKO_YOSHIKAZU_STYLE"),
    "sadamoto_yoshiyuki_style": _load("sadamoto_yoshiyuki", "SADAMOTO_YOSHIYUKI", "SADAMOTO_YOSHIYUKI_STYLE"),
    "nihei_tsutomu_style": _load("nihei_tsutomu", "NIHEI_TSUTOMU", "NIHEI_TSUTOMU_STYLE"),
    "murata_range_style": _load("murata_range", "MURATA_RANGE", "MURATA_RANGE_STYLE"),
    "shinkawa_yoji_style": _load("shinkawa_yoji", "SHINKAWA_YOJI", "SHINKAWA_YOJI_STYLE"),
    "kim_jung_gi_style": _load("kim_jung_gi", "KIM_JUNG_GI", "KIM_JUNG_GI_STYLE"),
    "maruo_suehiro_style": _load("maruo_suehiro", "MARUO_SUEHIRO", "MARUO_SUEHIRO_STYLE"),
    "ito_junji_style": _load("ito_junji", "ITO_JUNJI", "ITO_JUNJI_STYLE"),
    "hino_hideshi_style": _load("hino_hideshi", "HINO_HIDESHI", "HINO_HIDESHI_STYLE"),
    "hayashida_q_style": _load("hayashida_q", "HAYASHIDA_Q", "HAYASHIDA_Q_STYLE"),
    "ohkubo_atsushi_style": _load("ohkubo_atsushi", "OHKUBO_ATSUSHI", "OHKUBO_ATSUSHI_STYLE"),
    "toboso_yana_style": _load("toboso_yana", "TOBOSO_YANA", "TOBOSO_YANA_STYLE"),
}


# ============================================
# SERIE SPECIFICHE (11) + VARIANTI (3)
# ============================================

_SERIE_RAW = {
    # Originali
    "galaxy_express_999": _load("galaxy_express_999", "GALAXY_EXPRESS_999"),
    "adieu_galaxy_express": _load("adieu_galaxy_express", "ADIEU_GALAXY_EXPRESS"),
    "transformers_g1": _load("transformers_g1", "TRANSFORMERS_G1"),
    # FIX: il file si chiama akira_toriyama_dragon_ball_z.py (non dragon_ball_z.py)
    "dragon_ball_z": _load("akira_toriyama_dragon_ball_z", "DRAGON_BALL_Z", "AKIRA_TORIYAMA_DRAGON_BALL_Z", "DRAGON_BALL_Z_STYLE"),
    "saint_seiya": _load("saint_seiya", "SAINT_SEIYA"),
    "lupin_iii": _load("lupin_iii", "LUPIN_III"),
    # Nuove serie
    "toriyama_dragon_ball": _load("toriyama_dragon_ball", "TORIYAMA_DRAGON_BALL", "DRAGON_BALL", "TORIYAMA_DRAGON_BALL_STYLE"),
    "oda_one_piece": _load("oda_one_piece", "ODA_ONE_PIECE", "ONE_PIECE", "ODA_ONE_PIECE_STYLE"),
    "takahashi_ranma": _load("takahashi_ranma", "TAKAHASHI_RANMA", "RANMA", "RANMA_ONE_HALF"),
    "togashi_yuyu": _load("togashi_yuyu", "TOGASHI_YUYU", "YUYU_HAKUSHO", "TOGASHI_YUYU_STYLE"),
    "city_hunter": _load("city_hunter", "CITY_HUNTER", "CITY_HUNTER_STYLE"),
}

_VARIANTI_RAW = {
    "otomo_akira_specific": _load("otomo_akira_specific", "OTOMO_AKIRA_SPECIFIC"),
    "takahashi_rumiko_inuyasha": _load("takahashi_rumiko_inuyasha", "TAKAHASHI_INUYASHA", "TAKAHASHI_RUMIKO_INUYASHA", "INUYASHA"),
    "miura_berserk_1997": _load("miura_berserk_1997", "MIURA_BERSERK_1997"),
}

_SERIE_KEYS = list(_SERIE_RAW)
_VARIANTI_KEYS = list(_VARIANTI_RAW)


# ============================================
# DATABASE COMPLETO
# ============================================

_ALL_RAW = {
    **_EPOCHE_RAW, **_GENERI_RAW, **_STUDI_RAW,
    **_ARTISTI_RAW, **_SERIE_RAW, **_VARIANTI_RAW,
}

# Solo gli stili effettivamente caricati (None = saltato con warning)
ANIME_STYLES = {k: v for k, v in _ALL_RAW.items() if v is not None}
_MISSING_STYLES = sorted(k for k, v in _ALL_RAW.items() if v is None)


# ============================================
# FUNZIONI UTILITY ANIME
# ============================================

def get_anime_style_by_name(style_name):
    """Ottiene uno stile anime per nome."""
    return ANIME_STYLES.get(style_name, None)


def get_anime_styles_by_era(era):
    """Ottiene stili anime per epoca."""
    return {
        name: config for name, config in ANIME_STYLES.items()
        if config.get("era", "").find(era) >= 0
    }


def get_anime_styles_by_artist(artist):
    """Ottiene stili anime per artista."""
    return {
        name: config for name, config in ANIME_STYLES.items()
        if config.get("artist", "") == artist
    }


def get_anime_styles_by_genre(genre):
    """Ottiene stili anime per genere."""
    return {
        name: config for name, config in ANIME_STYLES.items()
        if config.get("genre", "") == genre
    }


def get_anime_styles_by_studio(studio):
    """Ottiene stili anime per studio."""
    return {
        name: config for name, config in ANIME_STYLES.items()
        if config.get("studio", "") == studio
    }


def get_matsumoto_universe():
    """Ottiene tutti gli stili dell'universo Matsumoto."""
    matsumoto_styles = []
    for name, config in ANIME_STYLES.items():
        if config.get("artist") == "Leiji Matsumoto":
            matsumoto_styles.append(name)
        elif "matsumoto" in name.lower():
            matsumoto_styles.append(name)
        elif "galaxy_express" in name.lower():
            matsumoto_styles.append(name)
    return matsumoto_styles


def get_80s_legends():
    """Ottiene tutti gli stili degli artisti anni '80."""
    legends_80s = [
        "retro_80s_anime",
        "toriyama_style",
        "tetsuo_hara_style",
        "leiji_matsumoto_style",
        "yoshiyuki_tomino_style",
        "masami_kurumada_style",
        "tsukasa_hojo_style",
        "yoichi_takahashi_style",
        "go_nagai_style",
        "galaxy_express_999",
        "transformers_g1",
        "toriyama_dragon_ball",
        "dragon_ball_z",
        "saint_seiya",
        "city_hunter",
        "takahashi_ranma",
        "otomo_style",
        "otomo_akira_specific",
        "araki_style",
        "hagiwara_style",
        "lupin_iii",
        "monkey_punch_style"
    ]
    return {name: ANIME_STYLES[name] for name in legends_80s if name in ANIME_STYLES}


def get_modern_masters():
    """Ottiene gli stili dei maestri moderni (2010+)."""
    modern_masters = [
        "makoto_shinkai_style",
        "mamoru_hosoda_style",
        "koyoharu_gotouge_style",
        "gege_akutami_style",
        "one_murata_style",
        "ryo_timo_style",
        "masaaki_yuasa_style",
        "fujimoto_tatsuki_style",
        "ishida_sui_style",
        "asano_style"
    ]
    return {name: ANIME_STYLES[name] for name in modern_masters if name in ANIME_STYLES}


def get_shojo_styles():
    """Ottiene tutti gli stili shojo (femminili)."""
    shojo_list = [
        "shojo_modern",
        "naoko_takeuchi_style",
        "clamp_style",
        "moe_2000s_style",
        "toboso_yana_style",
        "yaoi",
        "yuri"
    ]
    return {name: ANIME_STYLES[name] for name in shojo_list if name in ANIME_STYLES}


def get_modern_studios():
    """Ottiene gli stili degli studi moderni."""
    modern_studios_list = [
        "mappa_style",
        "wit_studio_style",
        "bones_studio_style",
        "kyoto_animation_style",
        "trigger_detailed_style",
        "ufotable_style",
        "shaft_style",
        "a1_pictures_style",
        "eight_bit_style",
        "pa_works_style",
        "zero_g_style"
    ]
    return {name: ANIME_STYLES[name] for name in modern_studios_list if name in ANIME_STYLES}


def get_classic_studios():
    """Ottiene gli stili degli studi classici/storici."""
    classic_studios_list = [
        "sunrise_style",
        "gainax_style",
        "toei_style",
        "madhouse_style",
        "production_ig_style",
        "pierrot_style",
        "ghibli",
        "deen_style",
        "gonzo_style",
        "jc_staff_style",
        "xebec_style"
    ]
    return {name: ANIME_STYLES[name] for name in classic_studios_list if name in ANIME_STYLES}


def get_dark_anime_styles():
    """Ottiene stili anime dark/horror."""
    dark_styles = [
        "horror_anime",
        "psychological_thriller",
        "vampire_supernatural",
        "ishida_sui_style",
        "miura_style",
        "miura_berserk_1997",
        "kon_satoshi_style",
        "urasawa_style",
        "hagiwara_style",
        "ito_junji_style",
        "maruo_suehiro_style",
        "hino_hideshi_style"
    ]
    return {name: ANIME_STYLES[name] for name in dark_styles if name in ANIME_STYLES}


def get_realism_masters():
    """Ottiene i maestri del realismo."""
    realism_masters = [
        "inoue_style",
        "urasawa_style",
        "asano_style",
        "kon_satoshi_style",
        "kim_jung_gi_style"
    ]
    return {name: ANIME_STYLES[name] for name in realism_masters if name in ANIME_STYLES}


def get_action_legends():
    """Ottiene le leggende dell'azione."""
    action_legends = [
        "araki_style",
        "togashi_style",
        "togashi_yuyu",
        "tetsuo_hara_style",
        "masami_kurumada_style",
        "one_murata_style",
        "martial_arts",
        "dragon_ball_z",
        "toriyama_dragon_ball"
    ]
    return {name: ANIME_STYLES[name] for name in action_legends if name in ANIME_STYLES}


def get_mecha_styles():
    """Ottiene tutti gli stili mecha."""
    mecha_styles = [
        "mecha_90s_style",
        "mecha_military",
        "mecha_organic",
        "super_robot",
        "shinkawa_yoji_style",
        "nihei_tsutomu_style",
        "yoshiyuki_tomino_style",
        "sunrise_style"
    ]
    return {name: ANIME_STYLES[name] for name in mecha_styles if name in ANIME_STYLES}


def get_unique_artists():
    """Ottiene artisti con stile veramente unico/riconoscibile."""
    unique_artists = [
        "masaaki_yuasa_style",
        "kim_jung_gi_style",
        "nihei_tsutomu_style",
        "maruo_suehiro_style",
        "ito_junji_style",
        "hayashida_q_style",
        "ohkubo_atsushi_style"
    ]
    return {name: ANIME_STYLES[name] for name in unique_artists if name in ANIME_STYLES}


def get_variant_specific_styles():
    """Ottiene le varianti specifiche di serie."""
    return {name: ANIME_STYLES[name] for name in _VARIANTI_KEYS if name in ANIME_STYLES}


def get_series_styles():
    """Ottiene tutti gli stili dedicati a serie specifiche."""
    return {name: ANIME_STYLES[name] for name in _SERIE_KEYS if name in ANIME_STYLES}


def get_romance_styles():
    """Ottiene gli stili romantici (harem, yaoi, yuri, shojo, ecc.)."""
    romance_list = [
        "harem",
        "yaoi",
        "yuri",
        "shojo_modern",
        "slice_of_life",
        "moe_2000s_style",
        "naoko_takeuchi_style",
        "clamp_style",
        "ken_akamatsu_style",
        "ecchi_modern"
    ]
    return {name: ANIME_STYLES[name] for name in romance_list if name in ANIME_STYLES}


def get_supernatural_styles():
    """Ottiene gli stili sovrannaturali (vampiri, mostri, occulto)."""
    supernatural_list = [
        "vampire_supernatural",
        "horror_anime",
        "kaiju_monster",
        "ito_junji_style",
        "hino_hideshi_style",
        "maruo_suehiro_style",
        "ishida_sui_style",
        "gege_akutami_style"
    ]
    return {name: ANIME_STYLES[name] for name in supernatural_list if name in ANIME_STYLES}


def get_dystopian_styles():
    """Ottiene gli stili distopici/post-apocalittici."""
    dystopian_list = [
        "post_apocalyptic",
        "cyberpunk_classic",
        "cyberpunk_modern",
        "nihei_tsutomu_style",
        "otomo_style",
        "otomo_akira_specific",
        "kaiju_monster"
    ]
    return {name: ANIME_STYLES[name] for name in dystopian_list if name in ANIME_STYLES}


# ============================================
# CONFIGURAZIONE EXPORT
# ============================================

__all__ = [
    'ANIME_STYLES',
    'get_anime_style_by_name',
    'get_anime_styles_by_era',
    'get_anime_styles_by_artist',
    'get_anime_styles_by_genre',
    'get_anime_styles_by_studio',
    'get_matsumoto_universe',
    'get_80s_legends',
    'get_modern_masters',
    'get_shojo_styles',
    'get_modern_studios',
    'get_classic_studios',
    'get_dark_anime_styles',
    'get_realism_masters',
    'get_action_legends',
    'get_mecha_styles',
    'get_unique_artists',
    'get_variant_specific_styles',
    'get_series_styles',
    'get_romance_styles',
    'get_supernatural_styles',
    'get_dystopian_styles',
]


# ============================================
# LOG DI CARICAMENTO
# ============================================

def _loaded_count(section):
    return sum(1 for v in section.values() if v is not None)

print(f"[CharacterForge-Anime] Stili anime caricati: {len(ANIME_STYLES)}/{len(_ALL_RAW)} attesi")
print(f"[CharacterForge-Anime] Epoche: {_loaded_count(_EPOCHE_RAW)}")
print(f"[CharacterForge-Anime] Generi: {_loaded_count(_GENERI_RAW)}")
print(f"[CharacterForge-Anime] Studios: {_loaded_count(_STUDI_RAW)}")
print(f"[CharacterForge-Anime] Artisti leggendari: {_loaded_count(_ARTISTI_RAW)}")
print(f"[CharacterForge-Anime] Serie specifiche: {_loaded_count(_SERIE_RAW)}")
print(f"[CharacterForge-Anime] Varianti specifiche: {_loaded_count(_VARIANTI_RAW)}")

if _MISSING_STYLES:
    print(f"[CharacterForge-Anime] WARNING: {len(_MISSING_STYLES)} stili non caricati:")
    for _name in _MISSING_STYLES:
        print(f"[CharacterForge-Anime]   - {_name}")
else:
    print(f"[CharacterForge-Anime] TUTTI i {len(ANIME_STYLES)} stili caricati correttamente!")

# Log dettagliato artisti
artists_present = set()
for style_config in ANIME_STYLES.values():
    if "artist" in style_config:
        artists_present.add(style_config["artist"])

print(f"[CharacterForge-Anime] Artisti unici nel database: {len(artists_present)}")

# Log collezioni
print(f"[CharacterForge-Anime] Universo Matsumoto: {len(get_matsumoto_universe())} stili")
print(f"[CharacterForge-Anime] Leggende anni '80: {len(get_80s_legends())} stili")
print(f"[CharacterForge-Anime] Maestri moderni: {len(get_modern_masters())} stili")
print(f"[CharacterForge-Anime] Stili shojo: {len(get_shojo_styles())} stili")
print(f"[CharacterForge-Anime] Studi moderni: {len(get_modern_studios())} stili")
print(f"[CharacterForge-Anime] Studi classici: {len(get_classic_studios())} stili")
print(f"[CharacterForge-Anime] Stili dark/horror: {len(get_dark_anime_styles())} stili")
print(f"[CharacterForge-Anime] Maestri realismo: {len(get_realism_masters())} stili")
print(f"[CharacterForge-Anime] Leggende azione: {len(get_action_legends())} stili")
print(f"[CharacterForge-Anime] Stili mecha: {len(get_mecha_styles())} stili")
print(f"[CharacterForge-Anime] Artisti unici: {len(get_unique_artists())} stili")
print(f"[CharacterForge-Anime] Varianti specifiche: {len(get_variant_specific_styles())} stili")
print(f"[CharacterForge-Anime] Serie specifiche: {len(get_series_styles())} stili")
print(f"[CharacterForge-Anime] Stili romantici: {len(get_romance_styles())} stili")
print(f"[CharacterForge-Anime] Stili sovrannaturali: {len(get_supernatural_styles())} stili")
print(f"[CharacterForge-Anime] Stili distopici: {len(get_dystopian_styles())} stili")