def classify_severity(error_text):
    error = error_text.lower()

    if "outofmemory" in error or "database down" in error:
        return "HIGH"

    elif "exception" in error or "indexerror" in error or "nullpointer" in error:
        return "MEDIUM"

    else:
        return "LOW"