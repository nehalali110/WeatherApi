import json
import re
import redis
import RedisCache.cache
import json

# date_pattern = r"^\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])$"
# temp = "1999-01-31"
# match = re.search(date_pattern, temp)
# pattern2=r"^\d+|(?:\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1]))$"
# temp2 = "222222"
# match2 = re.fullmatch(pattern2, temp2)

user_data = json.dumps({"id": 1, "name": "demo_user"})
path = "user/data"
r = redis.Redis(host='localhost', port=6379, db=0)
RedisCache.cache.set_cache(r, path, user_data)
result = RedisCache.cache.get_cache(r, path)
print(result)