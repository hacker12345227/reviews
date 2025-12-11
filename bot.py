import requests
import random
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1448748226206502993/f8IcbH3aLb5wqdAnAN36oXadMS5NXcqMXqwfaX01i3nI0iNqW0yu3zg6wIdDykUyBBKq"  # <-- PLAK HIER JOUW WEBHOOK
import requests
import random
import time

WEBHOOK_URL = "JOUW_WEBHOOK_HIER"  # <-- PLAK HIER JOUW WEBHOOK

# ---- 200+ ROBLOX-STYLE USERNAMES ----

usernames = [
    "NovaRBLX","PixelStorm","GalaxyStrike","FireNova","LunarEcho","ZenithRBLX","StormWizard",
    "ByteHunter","ShadowPulse","SolarFlame","NightRogue","CyberWolf","EchoBlade","RiftMaster",
    "AstroPlayer","NeonSpectre","MysticShadow","SilentNebula","FrostShift","VortexByte","OmegaShift",
    "DriftByte","HexRBLX","QuantumNova","NovaKnight","SilentNova","ShadeHunter","PrimeVortex",
    "LuxeByte","SolarX","VoidMaster","HyperRBLX","TwinPixel","ShadowBurst","LightSpectre","OrbitalFlash",
    "NovaRogue","NeoVoltage","ByteWizard","ZeroSpectre","KryoShift","IceNova","PulseRBLX","SolarByte",
    "RBLXLegend","DarkNebula","TitanByte","AstroShift","NebulaStorm","NightSpectre","GalacticByte",
    "DuskHunter","VeloNova","RazorPulse","SilentRift","MetaSpectre","NovaFlow","ShatterByte",
    "FlashRBLX","VyperByte","SkyNova","NightPulse","BladeSpectre","FangRBLX","StealthNova",
    "StormPulse","NebulaGhost","HoloRBLX","QuantumGhost","SolarKnight","ShadowNova","ArcticRBLX",
    "ZypherByte","ChronoNova","TerraRBLX","MysticNova","PulseKnight","ArcticSpectre","GhostRBLX",
    "MegaNova","PhantomByte","Roblite","PulseStorm","FireSpectre","GlitchByte","FrozenPulse",
    "CrystalNova","NexusRBLX","ZeroNova","StaticShift","GigaNova","DriftKnight","EchoStorm",
    "FlashSpectre","FrostByte","CyberNova","VoidPulse","HyperGhost","AstralKnight","SilentShade",
    "ShadowNovaX","NightWolfRBLX","GhostShift","PyroByte","StealthStorm","GalaxyKnight",
    "DreamRBLX","AlphaNova","RobluXY","StaticRogue","MegaSpectre","IonByte","BlitzVortex",
    "AeroNova","NeoPulse","CyberShade","DuskShift","NebulaSpirit","GlitchStorm","AstralViper",
    "ChromeRBLX","DeltaNova","FuryByte","PhantomRift","LunarKnight","SolarSpectre","RBLXSpirit",
    "SpikeNova","ThunderByte","NightGlitch","FrozenNebula","StarPulse","NovaSpark","ByteDragon",
    "MysticVortex","RBLXShift","PulseDrift","TurboNova","ViralByte","SteelSpectre","DarkViper",
    "SilentStormX","HackerNova","GhostKnight","StarSpectre","NebulaKnight","InfernoNova",
    "SkySpectre","ThunderNova","VortexKnight","CelestialByte","DarkEcho","SolarDrift",
    "QuantumPulse","LavaNova","ShockSpectre","ViperNova","DreadByte","HoloKnight","ZeroPulse",
    "BladeNova","PhantomStorm","VoidKnight","MegaPulse","TechSpectre","VortexShadow",
    "SilentWolf","PixelKnight","RobloxionX","HyperNebula","NightNovaX","AstroWolf",
    "NebulaBlade","NovaRift","CyberKnight","NeoVortex","FrozenKnight","StormDragon",
    "SpectralByte","DarkShift","StarVortex","IonSpectre","ArcticWolf","PixelNovaX",
    "GhostNova","NebulaByte","TitanStorm","RoblXeno","ZeroWolf","NightDragon",
    "QuantumWolf","SkyHunter","ShadowFang","NovaClaw","MegaHunter","GlitchFang",
    "StormWolf","IronSpectre","PlasmaNova","BladeWolf","DeltaSpectre"
]

# ---- OPTIONS ----

robux_options = [
    "25,000 Robux",
    "50,000 Robux",
    "100,000 Robux",
    "150,000 Robux",
    "250,000 Robux"
]

payment_methods = [
    "💠 Litecoin",
    "💳 PayPal",
    "📱 Tikkie"
]

review_sentences = [
    "Fast delivery! 🔥",
    "Super smooth transaction!",
    "Amazing service as always!",
    "Legit & trusted 💯",
    "Very fast, thank you!",
    "Perfect, will buy again!",
    "Outstanding service!",
    "Highly recommended!",
    "Fast and reliable!",
]

time_formats = [
    "Just now",
    "1 minute ago",
    "5 minutes ago",
    "12 minutes ago",
    "27 minutes ago",
    "1 hour ago",
    "2 hours ago"
]

GIF_BANNER = "https://i.imgur.com/abcd123.gif"   # <-- JOUW GIF

# ---- SEND WEBHOOK ----

def send_embed():
    random_user = random.choice(usernames)
    random_robux = random.choice(robux_options)
    random_ticket = random.randint(100000000000000, 999999999999999)
    random_stars = random.randint(3, 5)
    random_payment = random.choice(payment_methods)
    random_review = random.choice(review_sentences)
    random_time = random.choice(time_formats)
    verified = random.random() < 0.30

    stars_display = "⭐" * random_stars + "☆" * (5 - random_stars)
    verified_text = " | ⭐ **Verified Buyer**" if verified else ""

    embed = {
        "title": f"🟧 Order Confirmed — Thank You!{verified_text}",
        "color": 16744192,
        "fields": [
            {"name": "Stars", "value": f"{stars_display} ({random_stars}/5)", "inline": True},
            {"name": "User", "value": f"`{random_user}`", "inline": True},
            {"name": "Payment Method", "value": random_payment, "inline": True},
            {"name": "Robux Purchased", "value": f"🟧 **{random_robux}**", "inline": True},
            {"name": "Ticket ID", "value": f"🎫 `{random_ticket}`", "inline": True},
            {"name": "Review", "value": random_review, "inline": False},
            {"name": "Time", "value": random_time, "inline": True}
        ],
        "image": {"url": https://i.postimg.cc/K8vwGtN8/Schermafbeelding-2025-12-11-200714.png},
        "footer": {"text": "BloxxVault | Trusted by the Community"}
    }

    data = {"username": "BloxxVault", "embeds": [embed]}
    requests.post(WEBHOOK_URL, json=data)

send_embed()  # GitHub workflow roept dit script elke 5 minuten aan
