from google.cloud import bigquery
import pandas as pd

def main():
    """A function to return a pandas dataframe from a big query query"""
    query = """SELECT title
    , LENGTH(title) AS title_length
    , body
    , LENGTH(body) AS body_length
    , answer_count
    , score
    , (LENGTH(tags) - LENGTH(REPLACE(tags, '|', '')) + 1) AS num_tags
    FROM `bigquery-public-data.stackoverflow.stackoverflow_posts`
    LIMIT 10"""
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    df = results.to_dataframe()
    return df

if __name__ == "__main__":
    print(main())