# makefun-news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/kiki-zhq/makefun-news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/kiki-zhq/makefun-news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

"The World in One Day" — a newspaper front page summing up Thursday 19 November 2026 in one image. Entry for make.fun `news-image-20261119`.

`entry.png` is a 1024×1024 newspaper front page with the date line and seven real stories from 19 November 2026:

- **Lead — Trump, Xi and Putin meet in China.** Trump arrives in Shenzhen for a regional summit and is hugged by Xi on the tarmac; a first trilateral meeting of the three leaders is expected on Thursday.
- **Crimean Bridge attacked again.** Russian officials report another attack on the bridge linking Russia to Crimea, a day after part of the span collapsed.
- **Van Gogh sells for a record $190.4m after a Nazi-history row.** The painting fetches a record price at auction despite a dispute over its history during the Nazi era.
- **Anthropic raises $81.3bn in the biggest IPO ever.** The maker of Claude is set for a stock market debut valued at more than $1.4 trillion.
- **Myanmar faces a historic ICJ genocide verdict.** The U.N. court rules on the Rohingya massacres in a landmark case against Myanmar.
- **Israeli ground operation in Gaza crosses the ceasefire line.** Israeli tanks advance in a rare ground operation beyond the Yellow Line in Gaza.
- **GTA VI begins its global rollout.** Gamers return to Vice City after a 13-year wait as Grand Theft Auto VI launches worldwide.

Plus an "IN BRIEF" line: NASA's Voyager 1 reaches a light-day milestone 50 years after launch, Cyclone Akvan bears down on India's Andhra coast, Hakeem Jeffries is set to be the first African-American House Speaker, and the EU proposes a €45bn Ukraine loan.

Every headline was checked against news reported on 19 November 2026 (NYT, BBC, Al Jazeera, Times of India, NDTV, APSDMA). The page was built as a single HTML file (`frontpage.html`) and rendered to PNG with headless Chromium at exactly 1024×1024.

`main.py` (Python 3.13, standard library only) copies the repository-held `entry.png` to `/output/entry.png`. No network. Run it twice and both runs write the same bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t49c36pe&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
