import pandas
import test_util

from tsgettoolbox import ulmo
from tsgettoolbox import tsgettoolbox

test_sets = [
    {
        "filename": "cpc/drought/palmer88",
        "start_date": "1989-01-22",
        "end_date": "1989-01-28",
        "state": "TX",
        "climate_division": 1,
        "values": [
            {
                "cmi": -0.11,
                "pdsi": 0.0,
                "period": "1989-01-22/1989-01-28",
                "potential_evap": 0.1,
                "precipitation": 0.4,
                "runoff": 0.0,
                "soil_moisture_lower": 0.3,
                "soil_moisture_upper": 0.3,
                "temperature": 43.0,
            }
        ],
    },
    {
        "filename": "cpc/drought/palmer94",
        "start_date": "1995-02-19",
        "end_date": "1995-02-25",
        "state": "NC",
        "climate_division": 4,
        "values": [
            {
                "cmi": 1.92,
                "pdsi": 0.88,
                "period": "1995-02-19/1995-02-25",
                "potential_evap": 0.17,
                "precipitation": 0.1,
                "runoff": 0.0,
                "soil_moisture_lower": 5.0,
                "soil_moisture_upper": 0.93,
                "temperature": 47.0,
            }
        ],
    },
    {
        "filename": "cpc/drought/palmer99",
        "start_date": "1999-07-25",
        "end_date": "1999-07-31",
        "state": "TX",
        "climate_division": 3,
        "values": [
            {
                "cmi": -2.31,
                "pdsi": -1.37,
                "period": "1999-07-25/1999-07-31",
                "potential_evap": 1.75,
                "precipitation": 0.0,
                "runoff": 0.0,
                "soil_moisture_lower": 1.68,
                "soil_moisture_upper": 0.0,
                "temperature": 87.0,
            }
        ],
    },
    {
        "filename": "cpc/drought/palmer10",
        "start_date": "2010-5-20",
        "end_date": "2010-6-13",
        "state": "AL",
        "climate_division": 1,
        "values": [
            {
                "cmi": 0.05,
                "pdsi": 0.53,
                "period": "2010-06-06/2010-06-12",
                "potential_evap": 1.37,
                "precipitation": 0.71,
                "runoff": 0.0,
                "soil_moisture_lower": 4.86,
                "soil_moisture_upper": 0.0,
                "temperature": 77.6,
            }
        ],
    },
]


def test_get_data_by_state():
    for test_set in test_sets:
        with test_util.mocked_urls(test_set["filename"]):
            data = tsgettoolbox.cpc(
                state=test_set["state"],
                start_date=test_set["start_date"],
                end_date=test_set["end_date"],
            )
        assert len(data) == 1
        assert test_set["state"] in data


def test_get_data():
    for test_set in test_sets:
        with test_util.mocked_urls(test_set["filename"]):
            data = tsgettoolbox.cpc(
                start_date=test_set["start_date"], end_date=test_set["end_date"]
            )

        values = data.get(test_set["state"], {}).get(test_set["climate_division"])
        test_values = test_set["values"]

        for test_value in test_values:
            assert test_value in values


def test_get_data_as_dataframe():
    with test_util.mocked_urls("cpc/drought/palmer10"):
        data = tsgettoolbox.cpc(
            start_date="2010-5-20", end_date="2010-6-13", as_dataframe=True
        )

        assert isinstance(data, pandas.DataFrame)


# TODO: add proper marks to these
# def test_prelim_overlap_doesnt_break():
# data = tsgettoolbox.cpc(start_date='2012-01-01', end_date='2013-03-07',
# as_dataframe=True)
# assert len(data) > 0


# def test_prelim_overlap_start_end_dates_obeyed():
# data = tsgettoolbox.cpc(start_date='2012-01-01', end_date='2013-03-07',
# as_dataframe=True)
# assert data['period'][0] == pandas.Period('2012-01-01/2012-01-07', 'W-SAT')
# assert data['period'][data.index[-1]] == pandas.Period('2013-03-03/2013-03-09', 'W-SAT')
