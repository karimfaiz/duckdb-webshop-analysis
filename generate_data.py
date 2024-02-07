import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

data = {
    'order_id': [1, 2],
    'product_name': ['Product A', 'Product B'],
    'category': ['Category 1', 'Category 2'],
    'price': [10, 15],
    'order_date': ['2023-01-01', '2023-01-02']
}

df = pd.DataFrame(data)
table = pa.Table.from_pandas(df)

pq.write_table(table, 'my_shop_data.parquet')
