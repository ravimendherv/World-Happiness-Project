from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Task - 1
@api_view(['GET'])
def getDetailsByCountryName(request, country_name):
    with open("world-happiness-report-2021-country.json") as jsonFile:         # world-happiness-report-2021-country.json is the custom json file
        jsonData = json.load(jsonFile)
    try:
        return Response({"data": [jsonData[country_name]]})
    except:
        return Response({"Note": "Enter Valid Country Name"})                  # For Wrong data 

# Task - 2
@api_view(['GET'])
def getDetailsByLadderScore(request):
    data = []
    ladderScorefrom = (request.query_params["from"])
    ladderScoreto = request.query_params["to"]

    with open("world-happiness-report-2021-score.json") as jsonFile:            # world-happiness-report-2021-score.json is the custom json file
        jsonData = json.load(jsonFile)
        try:
            for i in jsonData:
                if float("{:.1f}".format(float(jsonData[i]["ladderScore"]))) > float(ladderScorefrom) and float("{:.1f}".format(float(jsonData[i]["ladderScore"]))) <= float(ladderScoreto):
                    data.append(jsonData[i])
        except:
            return Response({"Note": "Enter Correct float data"})               # For Wrong data
    if not data:
        return Response({"Note": "No Data as Found"})                           # For Wrong value
    return Response({"data": data})
