import logging
import numpy as np
import pandas as pd

from chai_flight_selection_pricing.predict_model import (
    clean_and_lower_str,
    normalized_by_m_lowest_values,
    min_by_group,
    inv_logit,
    correct_for_excessive_dropped_flights,
    PARAMETERS_ONEWAY,
    PARAMETERS_ROUNDTRIP,
    THRESHOLD_ONEWAY,
    THRESHOLD_ROUNDTRIP,
    MIN_ABSOLUTE,
    MAX_PROPORTION_DROPPED,
    M,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

test_df = pd.DataFrame(
    {
        "check_col": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "grouping": [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
    }
)


def modify_test_df(n_true):
    df = pd.DataFrame(
        {
            "outcome": [
                True,
                True,
                True,
                True,
                True,
                False,
                False,
                False,
                False,
                False,
            ],
            "score": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        }
    )
    df.loc[:, "outcome"] = False
    df.loc[0 : (n_true - 1), "outcome"] = True
    return df


test_score_df = pd.DataFrame(
    {
        "outcome": [True, True, True, True, True, False, False, False, False, False],
        "score": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    }
)

test_score_df_prop = modify_test_df(5)
test_score_df_prop2 = modify_test_df(4)
test_score_df_prop3 = modify_test_df(3)
test_score_df_cap = modify_test_df(0)


def test_string_mod():
    assert clean_and_lower_str("RoUnD-_*TrI5P") == "roundtrip"


def test_cutoff():
    assert (
        correct_for_excessive_dropped_flights(test_score_df.copy(), 1.0, 12)[
            "outcome"
        ].tolist()
        == test_score_df_cap["outcome"].tolist()
    )
    assert (
        correct_for_excessive_dropped_flights(test_score_df.copy(), 0.5, 3)[
            "outcome"
        ].tolist()
        == test_score_df_prop["outcome"].tolist()
    )
    assert (
        correct_for_excessive_dropped_flights(test_score_df.copy(), 0.4, 3)[
            "outcome"
        ].tolist()
        == test_score_df_prop2["outcome"].tolist()
    )
    assert (
        correct_for_excessive_dropped_flights(test_score_df.copy(), 0.3, 3)[
            "outcome"
        ].tolist()
        == test_score_df_prop3["outcome"].tolist()
    )


def test_param_values():
    assert THRESHOLD_ONEWAY <= 1.0
    assert THRESHOLD_ONEWAY >= 0.0
    assert THRESHOLD_ROUNDTRIP <= 1.0
    assert THRESHOLD_ROUNDTRIP >= 0.0
    assert len(PARAMETERS_ROUNDTRIP) == 4
    assert len(PARAMETERS_ONEWAY) == 4
    assert sum(np.isnan(PARAMETERS_ONEWAY)) == 0
    assert sum(np.isnan(PARAMETERS_ROUNDTRIP)) == 0
    assert isinstance(PARAMETERS_ONEWAY, np.ndarray)
    assert isinstance(PARAMETERS_ROUNDTRIP, np.ndarray)
    assert MAX_PROPORTION_DROPPED >= 0.0
    assert MAX_PROPORTION_DROPPED <= 1.0
    assert MIN_ABSOLUTE > 0
    assert isinstance(MAX_PROPORTION_DROPPED, float)
    assert isinstance(MIN_ABSOLUTE, int)
    assert isinstance(M, int)
    assert M < 10
    assert M > 1


def test_logit():
    assert inv_logit(0) == 0.5
    assert inv_logit(100.0) > 0.998
    assert inv_logit(-100.0) < 0.001


def test_normalized_by_m_lowest_values():
    assert normalized_by_m_lowest_values(test_df, "check_col").to_list() == [
        0.3333333333333333,
        0.6666666666666666,
        1.0,
        1.3333333333333333,
        1.6666666666666667,
        2.0,
        2.3333333333333335,
        2.6666666666666665,
        3.0,
        3.3333333333333335,
        3.6666666666666665,
        4.0,
        4.333333333333333,
        4.666666666666667,
    ]


def test_min_by_group():
    assert min_by_group(test_df, "grouping", "check_col").to_list() == [1, 8]


def test_payload():
    pass


# Need a test payload

# def test_predict():
#     predict("input data")