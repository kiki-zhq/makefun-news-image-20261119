# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kiki-zhq/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kiki-zhq/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

"The World in One Day" — one newspaper page holding Thursday 19 November 2026. Entry for make.fun `news-image-20261119`.

`entry.png` is a 1024×1024 front page, dated 19 November 2026, carrying seven stories from that day:

- **Top story — Three leaders gather in China.** Donald Trump lands in Shenzhen for a regional summit, greeted on the tarmac by Xi Jinping; a first three-way meeting with Vladimir Putin is expected on Thursday.
- **Bridge to Crimea hit again.** Russian officials report another attack on the crossing, a day after part of the span gave way.
- **Van Gogh sells for a record $190.4m.** The canvas fetches the highest auction price ever, despite a dispute over its Nazi-era past.
- **Anthropic raises $81.3bn in the biggest IPO ever.** The maker of Claude heads for a stock-market debut valued above $1.4 trillion.
- **World Court rules on the Myanmar genocide case.** The UN's highest court delivers its landmark verdict on the massacres of the Rohingya.
- **Israeli tanks push past the Gaza ceasefire line.** A rare ground operation advances beyond the Yellow Line.
- **GTA VI opens its doors worldwide.** Players return to Vice City after a thirteen-year wait.

An "In brief" strip adds four more items from the day: Voyager 1 reaching a light-day from Earth fifty years after launch, Cyclone Akvan gathering over the Bay of Bengal, Hakeem Jeffries poised to become the first African-American Speaker of the US House, and the EU's proposed €45 billion loan for Ukraine.

The page was drawn as a single HTML file (`frontpage.html`) and rendered to PNG with headless Chromium at exactly 1024×1024.

`main.py` (Python 3.13, standard library only) reads the repository-held `entry.png` and writes its bytes to `/output/entry.png`. No network. Run it twice and both runs write the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t49c36pe&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
