from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BugLog
from .parser import extract_error
from .ai_analyzer import analyze_error_with_ai

@api_view(['POST'])
def analyze_bug(request):
    log_text = request.data.get("log")

    parsed_error = extract_error(log_text)

    BugLog.objects.create(
        raw_log=log_text,
        parsed_error=parsed_error
    )

    ai_result = analyze_error_with_ai(parsed_error)

    return Response({
        "parsed_error": parsed_error,
        "ai_analysis": ai_result
    })