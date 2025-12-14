import requests
from dotenv import load_dotenv
import os
from RedisCache.cache import set_cache, get_cache
import redis
import json
import lz4.frame

r = redis.Redis(host="localhost", port=6379, db=0)

load_dotenv()

def fetch_weather(url):
	print(url.path)
	cache_result = get_cache(r, url.path)
	if cache_result:
		print(f"Fetched from cache ->>")
		return json.loads(lz4.frame.decompress(cache_result))

	localBaseUrl = "http://localhost:8000/"
	remoteBaseUrl = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
	query_url = str(url).replace(localBaseUrl, remoteBaseUrl)

	api_key = os.getenv("API_KEY")
	api_key_param = {"key": api_key}

	result = requests.get(query_url, params=api_key_param).json()
	set_cache(r, url.path, lz4.frame.compress(json.dumps(result).encode()))
	print(f"Data saved into cache ->")
	return result


