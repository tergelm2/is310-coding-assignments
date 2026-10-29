import csv
import time

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://bulbapedia.bulbagarden.net"
LIST_URL = f"{BASE_URL}/wiki/List_of_moves"
HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; tergelm2@illinois.edu)"
}

MOVE_NAMES = [
    "Thunder Punch", "Vise Grip", "Double Kick", "Fury Attack", "Pin Missile",
    "Water Gun", "Hydro Pump", "Psybeam", "Bubble Beam", "Hyper Beam",
    "Submission", "Mega Drain", "Fire Spin", "Psychic", "Sludge",
    "Dream Eater", "Barrage", "Sky Attack", "Explosion", "Rock Slide",
]


def fetch_soup(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    time.sleep(5)

    if response.status_code != 200:
        print(f"Could not download {url}: HTTP {response.status_code}")
        return None

    if "Just a moment" in response.text or "Enable JavaScript and cookies" in response.text:
        print("The site is blocking requests. Stop and choose another wiki.")
        return None

    return BeautifulSoup(response.text, "html.parser")


def scrape_move_links(soup):
    moves = []
    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        return moves

    table = content.find("table", class_="sortable")
    if table is None:
        return moves

    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) != 8:
            continue

        link = cells[1].find("a", href=True)
        if link is None:
            continue

        name = link.get_text(" ", strip=True)
        if name in MOVE_NAMES:
            moves.append({
                "move": name,
                "list_url": LIST_URL,
                "move_url": f"{BASE_URL}{link['href']}",
            })

    return moves


def analyze_move(move):
    soup = fetch_soup(move["move_url"])
    if soup is None:
        return None

    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        return None

    details = {}
    for title in ["Type", "Move category", "Power", "Accuracy", "PP"]:
        label = content.find("a", title=title)
        if label is None:
            return None
        value = label.find_next("td")
        if value is None:
            return None
        details[title] = value.get_text(" ", strip=True)
        if not details[title]:
            return None

    record = move.copy()
    record["type"] = details["Type"]
    record["category"] = details["Move category"]
    record["listed_power"] = details["Power"]
    accuracy = details["Accuracy"].split("%")[0]
    record["listed_accuracy_percent"] = accuracy.split()[0]
    record["base_pp"] = details["PP"].split()[0]
    return record


def save_csv(records):
    with open("move_stats.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def main():
    if "YOUR_NETID" in HEADERS["User-Agent"]:
        print("Replace YOUR_NETID in HEADERS with your Illinois NetID first.")
        return

    soup = fetch_soup(LIST_URL)
    if soup is None:
        return

    moves = scrape_move_links(soup)
    if len(moves) != len(MOVE_NAMES):
        print("Could not find all 20 move links. Check the list page.")
        return

    results = []
    for number, move in enumerate(moves, start=1):
        print(f"Processing {number}/{len(moves)}: {move['move']}")
        record = analyze_move(move)
        if record is None:
            print("Stopped because a move page could not be read. No new CSV was saved.")
            return
        results.append(record)

    save_csv(results)
    print(f"Saved {len(results)} moves to move_stats.csv")


if __name__ == "__main__":
    main()
