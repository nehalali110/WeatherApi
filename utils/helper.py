import urllib.parse

def get_path_query(url):
	parsed_url = urllib.parse.urlparse(url)
	path_query_params = parsed_url.path + '?' + parsed_url.query
	return path_query_params