import pytest
import test_util

from tsgettoolbox import ulmo


def test_get_stations():
    stations_file = "usace/swtwc/shefids.html"
    with test_util.mocked_urls(stations_file):
        stations = ulmo.usace.swtwc.get_stations()

    test_stations = [
        {"code": "DSNT2", "description": "Lake Texoma, Denison Dam"},
        {"code": "MYST2", "description": "Pat Mayse Lake"},
    ]

    for test_station in test_stations:
        assert stations[test_station["code"]] == test_station
    assert 700 <= len(stations) <= 800


def test_get_station_data():
    test_station_data = [
        (
            "DSNT2",
            "2017-07-25",
            {
                "code": "DSNT2",
                "description": "Lake Texoma, Denison Dam",
                "station_type": "Reservoir",
                "timezone": "US/Central",
                "values": {
                    "2017-07-25 01:00:00": {
                        "AIR-TEMP": 80.10,
                        "BAT-LOAD": 11.37,
                        "ELEVATION": 617.73,
                        "INFLOW": 564,
                        "PRECIP": 0.0,
                        "PRECIP(A)": 0.0,
                        "REL-HUMID": 81.98,
                        "RELEASE": 19,
                        "SOLAR-RAD": 0.0,
                        "STORAGE": 2572324.0,
                        "VOLTAGE": 11.77,
                        "WIND-DIR": 135.90,
                        "WIND-SPEED": 1.42,
                        "TW-ELEV": 501.87,
                    }
                },
            },
        ),
    ]

    for code, date, test_data in test_station_data:
        url_date = date.replace("-", "")
        filename = f"{code}.{url_date}.html"
        data_file = f"usace/swtwc/{filename}"
        with test_util.mocked_urls(data_file):
            station_data = ulmo.usace.swtwc.get_station_data(code, date)

        for key, value in test_data.items():
            if key == "values":
                _compare_values(test_data["values"], station_data["values"])
            else:
                assert station_data[key] == test_data[key]


def test_get_station_data_current():
    # can't easily test current since it is a moving target changes, but mostly
    # just make sure it parses correctl: current will have '---' values where
    # previous days do not
    data_file = "usace/swtwc/DSNT2.current.html"
    with test_util.mocked_urls(data_file):
        station_data = ulmo.usace.swtwc.get_station_data("DSNT2")
    assert len(station_data.get("values")) > 0


def test_get_station_data_out_of_range():
    # can't easily test current since it is a moving target changes, but mostly
    # just make sure it parses correctl: current will have '---' values where
    # previous days do not
    data_file = "usace/swtwc/empty.html"
    with test_util.mocked_urls(data_file):
        with pytest.raises(ValueError):
            station_data = ulmo.usace.swtwc.get_station_data("MYST2", "1945-01-01")


def _compare_values(test_values, station_values):
    for key, test_value in test_values.items():
        assert station_values[key] == test_value
