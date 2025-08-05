from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from os import getenv
from datetime import date

def get_jackpots():
    url = "https://www.national-lottery.co.uk/games"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jackpots = {}

    for meta in soup.find_all('meta'):
        name = meta.get('name')
        content = meta.get('content')
        if name and content and 'jackpot-short' in name:
            game = name.replace('-jackpot-short', '').replace('-', ' ').title()
            jackpots[game] = content

    jackpot_items = list(jackpots.items())
    selected = {
        jackpot_items[0][0]: jackpot_items[0][1],
        jackpot_items[2][0]: jackpot_items[2][1]
    }

    return selected

def format_for_notification(jackpots):
    today = date.today()
    format_today = today.strftime("%d/%m/%Y")
    lines = [f"🎰 **National Lottery Daily Update {format_today}**"]
    for game, amount in jackpots.items():
        game = game.replace('Next Draw', '').strip().title()
        lines.append(f"- {game}: {amount}")
    return "\n".join(lines)

def send_to_discord(message):
    load_dotenv()
    webhook_url = getenv("WEBHOOK_URL")
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send: {response.status_code}")

if __name__ == '__main__':
    jackpots = get_jackpots()
    message = format_for_notification(jackpots)
    print("Sending to Discord:\n", message)
    send_to_discord(message)
