# Comedy Central sketch data

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

I queried the `PlaylistItems` of the [YouTube Data API](https://developers.google.com/youtube/v3/docs/playlistItems/list) with the [Requests](http://docs.python-requests.org/en/master/) library to get the titles, dates, and IDs of the videos from each playlist. Then I queried the [statistics](https://developers.google.com/youtube/v3/docs/videos/list) of each video, the most important of which was the `viewCount`. And then I made basic CSV files of each show to capture the raw data in a digestible format.

## Results

The resulting CSVs.

- [Inside Amy Schumer CSV](https://github.com/richardcornish/sketches/blob/master/csvs/amy.csv)
- [Key & Peele CSV](https://github.com/richardcornish/sketches/blob/master/csvs/kap.csv)

I imported the CSVs into Google Sheets

- [Inside Amy Schumer spreadsheet](https://docs.google.com/spreadsheets/d/1NR-f01QeMjcNyZ9Y39f4O4-RJUtlX_XfmYma8XWnrd0/edit?usp=sharing)
- [Key & Peele CSV spreadsheet](https://docs.google.com/spreadsheets/d/1l7lgAKJdepVZVFACqyAbeS3g9DShtYDHfBB3DalmGM8/edit?usp=sharing)

## Insights

