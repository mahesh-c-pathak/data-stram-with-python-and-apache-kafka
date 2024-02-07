# data-stram-with-python-and-apache-kafka

#### Get data from a youtube plyalist, see which videos are in playlist, check their statistics

url = "GET https://www.googleapis.com/youtube/v3/playlists"

* To get data we need youtube data api key
    * create google project => enable api => credentials => create api key

* youtube playlist id

- we get paged results, 5 results per page, Hence we need to use python generator
