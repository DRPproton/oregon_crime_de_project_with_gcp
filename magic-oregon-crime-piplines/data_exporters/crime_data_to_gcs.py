import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/oregon-crime-e130b790c75d.json"

bucket_name = 'oregon-crime-bucket'

table_name = 'oregon_crime'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args,**kwargs):

    # data['ReportDateYear'] = data['ReportDate'].dt.year
    # data['ReportDateMonth'] = data['ReportDate'].dt.month

    table = pa.Table.from_pandas(data)
    
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['ReportDate'],
        filesystem=gcs
    )