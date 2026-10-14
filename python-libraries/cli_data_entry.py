import json
from pathlib import Path
from rich.console import Console
from rich.table import Table


console = Console()
file = Path("entries.json")

table = Table(title="Gaming vs. Academic Performance")
table.add_column("Student")
table.add_column("Game")
table.add_column("Hours/wk", justify="right")
table.add_column("GPA", justify="right")
table.add_row("Example A", "Valorant", "10", "3.6")
table.add_row("Example B", "Minecraft", "2", "3.9")
console.print(table)
console.print("\n[bold cyan]Now I want you to enter your name/GPA and the video games you play per week:[/bold cyan]")


while True:
    name = input("Student name: ")
    gpa = input("GPA: ")
    num_games = int(input("How many different video games do you play per week? "))
    
    games = []

    for i in range(num_games):
        title = input(f"Game {i + 1} title: ")
        hours = input(f"Hours per week on {title}: ")
        games.append({"title": title, "hours_per_week": hours})

    entry = {"student": name, "gpa" : gpa, "games" : games}
    console.print(entry)

    if input("Is this correct? (type y if yes, type n if not): ").lower() == "y":
        break

file.write_text(json.dumps(entry, indent=2))
console.print(f"Saved to {file.resolve()}", style="bold green")