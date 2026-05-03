from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BugLog
from .parser import extract_error
from .ai_analyzer import analyze_error_with_ai
from .log_reader import read_latest_logs
import logging

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
    
    
@api_view(['GET'])
def auto_analyze(request):
    logs = read_latest_logs()

    if not logs:
        return Response({"message": "No logs found"})

    latest_log = logs[-1]

    parsed_error = extract_error(latest_log)
    ai_result = analyze_error_with_ai(parsed_error)

    return Response({
        "log": latest_log,
        "parsed_error": parsed_error,
        "ai_analysis": ai_result
    })
    

logger = logging.getLogger(__name__)

@api_view(['GET'])
def generate_error(request):
    try:
        x = [1, 2]
        print(x[5])  # This will cause IndexError
    except Exception as e:
        logger.error(str(e))
        return Response({"message": "Error generated and logged"})
    

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')