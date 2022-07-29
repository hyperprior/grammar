from grammar.dataframes import DataFrame


def test_empty_dataframe():
    dataframe = DataFrame()

    assert dataframe
