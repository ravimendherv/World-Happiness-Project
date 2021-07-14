# World-Happiness-Project
World-Happiness-Index-2021

# URL ENDPOINT STRUCTURE:  http://<your-url>/v1/country/<country-name>
# EXAMPLE: https://world-happiness-index-2021-api.herokuapp.com/v1/country/finland
# METHOD: USE SUITABLE HTTP METHOD

Response: 

{
  "data": [{
    "countryName": "Finland",
    "rank": "1",
    "ladderScore": "7.842",
    "healthyLifeExpectancy": "72",
    "generosity": "0.949",
    "gdp": "10.775"
  }]
}

# URL ENDPOINT STRUCTURE:  http://<your-url>/v1/score-range/?from=<score>&to=<score>
# EXAMPLE: https://world-happiness-index-2021-api.herokuapp.com/v1/score-range/?from=7.5&to=7.8
# METHOD: USE SUITABLE HTTP METHOD

Response: 

{
  "data": [{
    "countryName": "Finland",
    "rank": "1",
    "ladderScore": "7.842",
    "healthyLifeExpectancy": "72",
    "generosity": "-0.098",
    "gdp": "10.775"
  },
    "countryName": "Denmark",
    "rank": "2",
    "ladderScore": "7.62",
    "healthyLifeExpectancy": "72.7",
    "generosity": "0.03",
    "gdp": "10.933"
  },
    "countryName": "Switzerland",
    "rank": "3",
    "ladderScore": "7.571",
    "healthyLifeExpectancy": "74.4",
    "generosity": "0.025",
    "gdp": "11.117"
  },
    "countryName": "Iceland",
    "rank": "4",
    "ladderScore": "7.554",
    "healthyLifeExpectancy": "73",
    "generosity": "0.16",
    "gdp": "10.878"
  }]
}
