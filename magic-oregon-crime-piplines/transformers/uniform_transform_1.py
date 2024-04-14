if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


@transformer
def transform(data, *args, **kwargs):

    # Convert date columns to datetime objects.
    data.IncidentDate = pd.to_datetime(data.IncidentDate, format='%m/%d/%Y').dt.date
    data.columns = data.columns.str.replace('\(|\)', '', regex=True).str.lower()
    data.columns = data.columns.str.replace(' ', '_')

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
