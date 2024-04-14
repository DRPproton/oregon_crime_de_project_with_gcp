import io
import pandas as pd
from datetime import datetime
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    all_data = []
    dtypes = {
        'Address': pd.StringDtype(), 
        'CaseNumber': pd.StringDtype(), 
        'CrimeAgainst': pd.StringDtype(), 
        'Neighborhood': pd.StringDtype(), 
        'OccurTime': pd.StringDtype(), 
        'OffenseCategory': pd.StringDtype(), 
        'OffenseType': pd.StringDtype(), 
        'OpenDataLat': pd.Float64Dtype(),
        'OpenDataLon': pd.Float64Dtype(), 
        'OpenDataX': pd.Float64Dtype(), 
        'OpenDataY': pd.Float64Dtype(),  
        'OffenseCount': pd.Int32Dtype()
    }

    # parse_dates = ['ReportDate', 'OccurDate']

    previous_year_data_entered = False
    year = datetime.now().year

    if previous_year_data_entered is not True: 
        for year in range(2015, year):
            url = f'https://public.tableau.com/views/PPBOpenDataDownloads/CrimeData-{str(year)}.csv?:showVizHome=no'
            df = pd.read_csv(url, dtype=dtypes) # , parse_dates=parse_dates
            all_data.append(df)
        return pd.concat(all_data)
    else:
        url = f'https://public.tableau.com/views/PPBOpenDataDownloads/CrimeData-{str(year - 1)}.csv?:showVizHome=no'
        return pd.read_csv(url, dtype=dtypes, parse_dates=parse_dates)

    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
