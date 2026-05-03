import re

def extract_error(log_text):
    patterns = [
        r'.*Exception.*',
        r'.*Error.*',
        r'Traceback.*'
    ]

    for p in patterns:
        match = re.search(p, log_text, re.IGNORECASE)
        if match:
            return match.group(0)

    return log_text  # fallback: return original log