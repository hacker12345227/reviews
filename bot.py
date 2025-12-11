import requests
import random
import time
import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1448748226206502993/f8IcbH3aLb5wqdAnAN36oXadMS5NXcqMXqwfaX01i3nI0iNqW0yu3zg6wIdDykUyBBKq"

# ---- usernames uit file inladen ----
with open("usernames.txt", "r", encoding="utf-8") as f:
    usernames = [line.strip() for line in f]

# ---- Extra usernames handmatig toevoegen ----
extra_usernames = ["ExtraUser1", "ExtraUser2", "SuperNovaX"]
usernames.extend(extra_usernames)

# ---- Robux opties ----
robux_options = [
    ("25,000 Robux", "€19.99"),
    ("50,000 Robux", "€34.99"),
    ("100,000 Robux", "€59.99"),
    ("150,000 Robux", "€79.99"),
    ("250,000 Robux", "€129.99")
]

payment_methods = ["💠 Litecoin","💳 PayPal","📱 Tikkie"]

time_formats = ["Just now","1 minute ago","5 minutes ago","12 minutes ago","27 minutes ago","1 hour ago","2 hours ago"]

GIF_BANNER = "https://i.postimg.cc/K8vwGtN8/Schermafbeelding-2025-12-11-200714.png"

# ---- Embed functie (zonder review) ----
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
        "footer": {"text": "BloxxVault | Trusted by the Community"}
    }

    data = {"username": "BloxxVault", "embeds": [embed]}
    requests.post(WEBHOOK_URL, json=data)
    print(f"Embed verzonden voor {random_user} ({random_robux})!")

# ---- Loop met nachtmodus en random delay 10-25 min ----
def is_allowed_time():
    now = datetime.datetime.now().time()
    start = datetime.time(8, 0)   # 08:00
    end = datetime.time(22, 0)    # 22:00
    return start <= now <= end

if __name__ == "__main__":
    while True:
        if is_allowed_time():
            send_embed()
            delay = random.randint(600, 1500)  # 10–25 minuten
            print(f"Wachten: {delay/60:.1f} minuten")
            time.sleep(delay)
        else:
            print("Nachtmodus actief (22:00–08:00) — geen berichten.")
            time.sleep(600)  # elke 10 min controleren
