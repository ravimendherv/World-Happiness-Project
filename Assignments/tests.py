from rest_framework import response, status
from rest_framework.test import APITestCase

class TestAPICountryName (APITestCase):
    def testByCountryName1(self):
        response = self.client.get("/v1/country/finland/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByCountryName2(self):
        response = self.client.get("/v1/country/denmark/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByCountryName3(self):
        response = self.client.get("/v1/country/switzerland/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByCountryName4(self):
        response = self.client.get("/v1/country/iceland/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class TestAPIByScoreRange (APITestCase):
    def testByScoreRange1(self):
        response = self.client.get("/v1/score-range/?from=7.5&to=7.8")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByScoreRange2(self):
        response = self.client.get("/v1/score-range/?from=6.1&to=6.4")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByScoreRange3(self):
        response = self.client.get("/v1/score-range/?from=5.5&to=5.8")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testByScoreRange4(self):
        response = self.client.get("/v1/score-range/?from=4.8&to=5.3")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
