import os
import pytest

from app.trivia_service import list_question

CI_ENV = os.getenv("CI") == "true"

@pytest.mark.skipif(CI_ENV==True, reason="to avoid issuing HTTP requests on the CI server")
def test_list_question():
    # with valid geography, returns the city name and forecast info:
    results = list_question(country_code="US", zip_code="20057")
    assert len(results["response_data"]) == 2 
    assert results["question"] == "list"
    assert results["correct_answer"] == "?"

    invalid_results = list_question(country_code="US", zip_code="OOPS")
    assert invalid_results == None


#others
    #assert len(results["hourly_forecasts"]) == 24
    #forecast = results["hourly_forecasts"][0]
    #assert sorted(list(forecast.keys())) == ["conditions", "image_url", "temp", "timestamp"]
    #assert forecast["timestamp"].endswith(":00")
    #assert f"{DEGREE_SIGN}F" in forecast["temp"]

    # with invalid geography, fails gracefully and returns nothing:
    #invalid_results = get_hourly_forecasts(country_code="US", zip_code="OOPS")
    #assert invalid_results == None

