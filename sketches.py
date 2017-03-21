import csv
import os

try:
    import requests
except ImportError:
    raise ImportError("Please install Requests. https://pypi.python.org/pypi/requests/")


try:
    YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
except KeyError:
    raise KeyError("Please register a YouTube API Key. https://developers.google.com/youtube/v3/getting-started")


def get_video_items(playlist_id, page_token=None, video_items=[]):
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'playlistId': playlist_id,
        'maxResults': 50,
    }
    if page_token is not None:
        params['pageToken'] = page_token
    playlist_items = requests.get('https://www.googleapis.com/youtube/v3/playlistItems', params=params)
    for item in playlist_items.json()['items']:
        video_items.append({
            'title': item['snippet']['title'],
            'publishedAt': item['snippet']['publishedAt'],
            'id': item['snippet']['resourceId']['videoId'],
        })
    if 'nextPageToken' in playlist_items.json():
        video_items = get_video_items(playlist_id, page_token=playlist_items.json()['nextPageToken'], video_items=video_items)
    return video_items


def get_video_stats(video_items, iterator=0):
    start = iterator * 50
    end = start + 50
    ids = []
    for item in video_items[start:end]:
        ids.append(item['id'])
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'statistics',
        'id': ','.join(ids),
        'maxResults': 50,
    }
    videos = requests.get('https://www.googleapis.com/youtube/v3/videos', params=params)
    for video_item in video_items:
        for item in videos.json()['items']:
            if video_item['id'] == item['id']:
                video_item['viewCount'] = item['statistics']['viewCount']
                video_item['likeCount'] = item['statistics']['likeCount']
                video_item['commentCount'] = item['statistics']['commentCount']
                video_item['dislikeCount'] = item['statistics']['dislikeCount']
                video_item['url'] = 'https://www.youtube.com/watch?v=' + item['id']
    if len(ids) == 50:
        video_items = get_video_stats(video_items, iterator + 1)
    return video_items


def convert_to_csv(my_dict, filename):
    keys = my_dict[0].keys()
    with open('csvs/' + filename + '.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys, quoting=csv.QUOTE_ALL)
        dict_writer.writeheader()
        dict_writer.writerows(my_dict)


# Inside Amy Schumer
video_items = get_video_items('PLD7nPL1U-R5o_GHb3XEx8XKCjzgCFCTuF', video_items=[])
video_stats = get_video_stats(video_items)
convert_to_csv(video_stats, 'amy')

# Key & Peele
video_items = get_video_items('PL83DDC2327BEB616D', video_items=[])
video_stats = get_video_stats(video_items)
convert_to_csv(video_stats, 'kap')
