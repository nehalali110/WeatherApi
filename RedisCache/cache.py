def get_cache(conn, path):
	return conn.get(path)

def set_cache(conn, path, value):
	return conn.set(path, value)