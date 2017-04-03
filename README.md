# Crunching sketch comedy data

I was curious about which sketches on Comedy Central were funniest, so I wrote a basic script to download data from the YouTube Data API.

![Inside Amy Schumer](https://raw.githubusercontent.com/richardcornish/sketches/master/charts/amy.png)

![Key & Peele](https://raw.githubusercontent.com/richardcornish/sketches/master/charts/kap.png)

## Do it yourself

1. [Install Requests](https://pypi.python.org/pypi/requests/)
2. [Get a YouTube Data API key](https://developers.google.com/youtube/v3/getting-started)
3. Run `$ python sketches.py`

## Why did you do this?

I write sketch comedy and I was curious about using a more data-driven approach in understanding which sketches people find funniest.

I decided to look at [Inside Amy Schumer](https://en.wikipedia.org/wiki/Inside_Amy_Schumer) and [Key & Peele](https://en.wikipedia.org/wiki/Key_%26_Peele) because they air traditional sketch comedy segments and because Comedy Central meticulously organizes each show's videos into a respective playlist. Without this manual curation, I would have had to download a whole channel's worth of data and sift through the titles in a likely error-prone process, or worse, search for illegally uploaded videos.

The YouTube playlists:

- [Inside Amy Schumer playlist](https://www.youtube.com/playlist?list=PLD7nPL1U-R5o_GHb3XEx8XKCjzgCFCTuF)
- [Key & Peele playlist](https://www.youtube.com/playlist?list=PL83DDC2327BEB616D)

I queried the `PlaylistItems` of the [YouTube Data API](https://developers.google.com/youtube/v3/docs/playlistItems/list) with the [Requests](http://docs.python-requests.org/en/master/) library to get the titles, dates, and IDs of the videos from each playlist. Then I queried the [statistics](https://developers.google.com/youtube/v3/docs/videos/list) of each video, the most important of which was the `viewCount`.

I made basic CSV files of each show to capture the raw data in a digestible format. The resulting CSVs:

- [Inside Amy Schumer CSV](https://github.com/richardcornish/sketches/blob/master/csvs/amy.csv)
- [Key & Peele CSV](https://github.com/richardcornish/sketches/blob/master/csvs/kap.csv)

I imported the CSVs into Google Sheets:

- [Inside Amy Schumer spreadsheet](https://docs.google.com/spreadsheets/d/1NR-f01QeMjcNyZ9Y39f4O4-RJUtlX_XfmYma8XWnrd0/edit?usp=sharing)
- [Key & Peele CSV spreadsheet](https://docs.google.com/spreadsheets/d/1l7lgAKJdepVZVFACqyAbeS3g9DShtYDHfBB3DalmGM8/edit?usp=sharing)

## Insights

Inside Amy Schumer:

- "[Milk Milk Lemonade](https://www.youtube.com/watch?v=HeiSx5MNDvg)" is Amy Schumer's most popular video with 8M views. Playground rhymes work.
- "[Last F**kable Day](https://www.youtube.com/watch?v=XPpsI8mWKmg)" is Amy's second most popular video, depsite it being not a traditional laugh-out-loud sketch. Satirizing a social trend is more important than fart jokes.
- Out of Amy's top three videos, two are songs. Songs are big. More sketches should aspire to be songs.
- When likes and dislikes were put against each other as a ratio, only one of Amy's videos, "[When Amy Happens to You](https://www.youtube.com/watch?v=vI6GzvhJqhg)," received more dislikes than likes. This was a season 4 promo and not a sketch, and aired around the time she was accused of plagiarism, so that had likely something to do with it.
- Sometimes Amy's videos can garner attention in some ways but not in others. "[Hello M'Lady](https://www.youtube.com/watch?v=e8teRxOSNHs)," a sketch about meeting creepy guys through an app, is her 48th video by view count, but *2nd* in comment count. A video about creepy guys bring out the comments.
- Likewise, "[The Universe - Uncensored](https://www.youtube.com/watch?v=6eqCaiwmr_M)," which earned a respectable 7th place by view count, is 2nd place in likes, which probably means nerds *love* it when Bill Nye swears.

Key & Peele:

- "[Subtitute Teacher](https://www.youtube.com/watch?v=Dd7FixvoKBw)" is Key & Peele's most popular video with 113M views. That's *14 times* more popular than "Milk Milk Lemonade." Despite Amy's fame and promotion the last few years, it takes the combined views of Amy's top *66 videos*, or her top 40% , to beat the single top Key & Peele video. That's incredible.
- Key & Peele's top 88 videos all beat Amy's top single video. It isn't until video 89 does the view count start dipping below what Amy's best does.
- "[Mr. Nostrand's Big Mistake](https://www.youtube.com/watch?v=18t5V3gvfa4)" is their fifth most popular. OK, so maybe fart jokes do work.

It's also worth stating that as episodes and seasons of each show progressed, the newer videos are obviously online for less time, making it more prone to have fewer views. However, Key & Peele ended at the end of 2015, and at the time of this writing the last season of Inside Amy Schumer was a year ago and is on indefinite hiatus.