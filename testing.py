import re

date_pattern = r"^\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])$"
temp = "1999-01-31"
match = re.search(date_pattern, temp)
print(match)
