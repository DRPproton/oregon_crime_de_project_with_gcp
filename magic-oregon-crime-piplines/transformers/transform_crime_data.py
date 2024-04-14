if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


@transformer
def transform(data, *args, **kwargs):
    
    # Drop DataX and Y columns
    data = data.drop(columns=['OpenDataX', 'OpenDataY'])
    # Convert OccurTime to time object
    data.OccurTime = pd.to_datetime(data.OccurTime, format='%H%M').dt.time

    data.OccurDate = pd.to_datetime(data.OccurDate, format='%m/%d/%Y').dt.date
    data.ReportDate = pd.to_datetime(data.ReportDate, format='%m/%d/%Y').dt.date


    if (data.OffenseCount == 0).any():
        data =  data[data.OffenseCount > 0]
    
 
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output.shape[1] == 12, 'The data has more than 12 columns'
    assert (output.OffenseCount == 0).any() == False, 'There are rows with 0 offense count'
