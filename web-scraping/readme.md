# Bulbapedia Web Scraping

## Research Question

Do physical or special Pokémon moves have more power?

## Why I Chose This Wiki

I chose Bulbapedia because it contains information about many Pokémon moves. I wanted to compare physical and special moves to see how their listed power differs. This data could help researchers study how video games organize different types of attacks.

## Website and Rules

- **Wiki:** [Bulbapedia](https://bulbapedia.bulbagarden.net/)
- **robots.txt:** [Bulbapedia robots.txt](https://bulbapedia.bulbagarden.net/robots.txt)

Before collecting data, I checked the website's robots.txt file. I also reviewed Bulbapedia's copyright policy and general disclaimer. The crawler rules allow ordinary wiki pages but restrict search pages, random-page links, Shipping pages, and history or old-revision URLs. They request a five-second delay between requests.

My script uses Python's requests and BeautifulSoup libraries. It identifies the scraper with a User-Agent, checks response status codes, and pauses five seconds between requests. Reused content is credited to Bulbapedia contributors through page links and shared under [CC BY-NC-SA 2.5](https://creativecommons.org/licenses/by-nc-sa/2.5/), where applicable.

## Data Collection

My scraper starts at the [List of moves](https://bulbapedia.bulbagarden.net/wiki/List_of_moves) page and follows links to individual move pages. It uses a fixed list of 20 moves introduced in Generation I: 10 physical and 10 special moves.

For each move, I collected its name, type, category, listed power, accuracy, PP (base number of uses), and page URL. I saved the results in move_stats.csv so they can be analyzed in Excel. The statistics are the wiki's latest listed values for each move, rather than their original Generation I values. The included data were collected with Codex assistance.


## Reflection

The scraper collected data for 10 physical and 10 special moves. Both groups had an average listed power of 76, so neither group had higher average power in this sample. However, listed power does not directly measure how much damage a move causes. Damage also depends on the Pokémon's stats, the opponent, and effects such as hitting multiple times. Since I only compared 20 moves, I cannot conclude that all physical and special moves are equally strong. The listed statistics can also come from different games, which limits the comparison.
