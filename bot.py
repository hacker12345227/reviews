import requests
import random
import json

# ---- Webhook URL ----
WEBHOOK_URL = "https://discord.com/api/webhooks/1448748226206502993/f8IcbH3aLb5wqdAnAN36oXadMS5NXcqMXqwfaX01i3nI0iNqW0yu3zg6wIdDykUyBBKq"

# ---- Load usernames from file ----
with open("usernames_5000.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f]

# ---- Extra usernames you can add manually ----
extra_usernames = ["ExtraUser1", "ExtraUser2", "SuperNovaX"]
usernames.extend(extra_usernames)

# ---- Robux options ----
robux_options = [
    ("25,000 Robux", "€19.99"),
    ("50,000 Robux", "€34.99"),
    ("100,000 Robux", "€59.99"),
    ("150,000 Robux", "€79.99"),
    ("250,000 Robux", "€129.99")
]

payment_methods = ["💠 Litecoin","💳 PayPal","📱 Tikkie"]

time_formats = ["Just now","1 minute ago","5 minutes ago","12 minutes ago","27 minutes ago","1 hour ago","2 hours ago"]

# ---- Load webhook config ----
with open("webhook_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

WEBHOOK_USERNAME = config.get("username", "BloxxVault")
WEBHOOK_AVATAR = config.get("avatar_url", "")
GIF_BANNER = config.get("banner_url", "")
BIO_TEXT = config.get("bio_text", "")

# ---- Embed function ----
def send_embed():
    random_user = random.choice(usernames)
    random_robux, random_price = random.choice(robux_options)
    random_ticket = random.randint(100000000000000, 999999999999999)
    random_stars = random.randint(3, 5)
    random_payment = random.choice(payment_methods)
    random_time = random.choice(time_formats)
    verified = random.random() < 0.30

    stars_display = "⭐" * random_stars + "☆" * (5 - random_stars)
    verified_text = " | ⭐ **Verified Buyer**" if verified else ""

    embed = {
        "title": f"🟧 Order Confirmed — Thank You!{verified_text}",
        "description": BIO_TEXT,
        "color": 16744192,
        "fields": [
            {"name": "Stars", "value": f"{stars_display} ({random_stars}/5)", "inline": True},
            {"name": "User", "value": f"`{random_user}`", "inline": True},
            {"name": "Payment Method", "value": random_payment, "inline": True},
            {"name": "Robux Purchased", "value": f"🟧 **{random_robux}**\n💵 {random_price}", "inline": True},
            {"name": "Ticket ID", "value": f"🎫 `{random_ticket}`", "inline": True},
            {"name": "Time", "value": random_time, "inline": True}
        ],
        "image": {"url": GIF_BANNER},
        "footer": {"text": f"{WEBHOOK_USERNAME} | Trusted by the Community"}
    }

    data = {
        "username": WEBHOOK_USERNAME,
        "avatar_url": WEBHOOK_AVATAR,
        "embeds": [embed]
    }

    requests.post(WEBHOOK_URL, json=data)
    print(f"Embed verzonden voor {random_user} ({random_robux})!")

# ---- Main loop (testmodus: geen vertraging, 24/7) ----
if __name__ == "__main__":
    while True:
        send_embed()
        print("Volgende bericht wordt direct verzonden (geen slaapmodus)")
