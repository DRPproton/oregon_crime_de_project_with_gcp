if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import os
import pyarrow as pa
import pyarrow.parquet as pq

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/oregon-crime-e130b790c75d.json"

bucket_name = 'oregon-crime-bucket'

table_name = 'clean_uniform_data_parquet/arrets'

root_path = f'{bucket_name}/{table_name}'

@data_loader
def load_data(*args, **kwargs):
    
    gcs = pa.fs.GcsFileSystem()

    dataset = pq.ParquetDataset(root_path, filesystem=gcs)
    table = dataset.read()
    return table.to_pandas()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
