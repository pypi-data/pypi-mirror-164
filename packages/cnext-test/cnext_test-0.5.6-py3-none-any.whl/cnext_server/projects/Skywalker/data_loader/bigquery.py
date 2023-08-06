from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from pybigquery.api import ApiClient
import pandas as pd
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'data/bigquery-350804-f8ec4f3aeea7.json'
db = create_engine('bigquery://')

query = """
SELECT
  name, gender,
  SUM(number) AS total
FROM
  `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY
  name, gender
ORDER BY
  total DESC
LIMIT
  1000"""

df = pd.read_sql(query, db)