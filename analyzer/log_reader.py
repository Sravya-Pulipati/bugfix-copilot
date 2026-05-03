def read_latest_logs():
    try:
        with open("app.log", "r") as f:
            logs = f.readlines()
            return logs[-5:]
    except FileNotFoundError:
        return []