from time import time
from fastapi import HTTPException, Request

window_time = 0
window_IPs = {}


def ratelimit(request: Request, max_counter: int = 5, max_session_time: int = 20):
	global window_time, window_IPs
	current_ip = request.client.host
	check_current_window(max_session_time)
	if not current_ip in window_IPs:
		window_IPs[current_ip] = 1
		print(f"hit registered --> {window_IPs[current_ip]}  IP_Pool : {current_ip} Time_Window: {window_time} Current time: {time()}")
	else:
		hit_counter = window_IPs[current_ip]
		if hit_counter >= 5:
			time_remaining = str(int(window_time - time()))
			# print(f"Max HIT Reached --> {hit_counter} IP_Pool: {window_IPs} Time_Window: {window_time} Current_Time: {time()}")
			raise HTTPException(status_code=429, detail="Too many requests", headers={"IP": current_ip, "Retry-After": f"{time_remaining} seconds"})
		window_IPs[current_ip] += 1
		# print(f"hit registered --> {window_IPs[current_ip]}  IP_Pool: {window_IPs} Time_Window: {window_time} Current time: {time()}")


def check_current_window(max_session_time):
	global window_time, window_IPs
	current_time = time()
	print(current_time)
	if window_time == 0 or current_time > window_time:
		print("time resetted")
		window_time = current_time + max_session_time
		window_IPs = {}