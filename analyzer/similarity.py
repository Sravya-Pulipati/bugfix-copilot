from difflib import SequenceMatcher
from .models import BugLog

def find_similar_error(new_error):
    logs = BugLog.objects.all()

    best_match = None
    highest_score = 0

    for log in logs:
        score = SequenceMatcher(None, new_error, log.parsed_error).ratio()

        if score > highest_score:
            highest_score = score
            best_match = log

    if highest_score > 0.6:  # threshold
        return best_match

    return None