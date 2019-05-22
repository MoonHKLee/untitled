import redis

r = redis.StrictRedis(host='15.164.32.115', port=6379, db=0,password='since2012!')
print(str(r.get("1")))