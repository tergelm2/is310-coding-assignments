# Assignment 1 - The Programming Historian

For this assignment I chose this website:

https://programminghistorian.org/


It is a peer-reviewed open-access resource teaching digital research methods/tools to people who are interested.

I found the github repo for this website as well:

https://github.com/programminghistorian/jekyll

From this repo I learned that it is built with Jekyll, which is a static site generator. Jekyll takes text plus templates and compiles it into static .html, .css, and .js files ahead of time.

According to the GitHub language breakdown for the repo:

- *HTML*: 92.8%
- *CSS*: 2.7%
- *Ruby*: 1.4%
- *Jupyter Notebook*: 1.4%
- *JavaScript*: 1.2%
- *Python*: 0.3%

The Ruby is mostly Jekyll's own build tooling rather than content and the Jupyter and Python percentages come from the tutorials that embed code examples.

I didn't recognize these files in the repo at first:

- the _layouts/ and _includes/ folders - I learned that these are Jekyll's templating system and they hold the reusable page structure/head/footer that is replicated onto every page
- .yml files - these are Jekyll configuration files

## Who built it?

The Programming Historian is not a project made by a single person or a single organization. It is a large and volunteer-run editorial community.

In the repo I found this information:

- The README lists a named technical manager (Matthew Lincoln) and there are links to contribution guides for authors, reviewers, and editors.
- The release changelogs on GitHub credit dozens of named contributors across English, Spanish, French, and Portuguese language teams.
- The commit history has thousands of commits from many different Github usernames and the repo has 227 forks and 550 stars, which shows sustained contribution over a long period of time.