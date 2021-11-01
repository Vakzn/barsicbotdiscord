# create time converter
times = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400,
    "w": 604800,
    "y": 220752000
}

# create function get seconds
def get_seconds(string: str):
    string = string.lower()
    time = int(string[:-1])
    time_type = times[string[-1]]
    return time * time_type