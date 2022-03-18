import subprocess
import pandas as pd

def main():
    """a function to use a big query query to make a csv"""
    cmd = ("""bq --format=csv query \
    --max_rows=10000 \
    --use_legacy_sql=false \
    '
    SELECT title
    , LENGTH(title) AS title_length
    , body
    , LENGTH(body) AS body_length
    , answer_count
    , score
    , (LENGTH(tags) - LENGTH(REPLACE(tags, "|", "")) + 1) AS num_tags
    FROM `bigquery-public-data.stackoverflow.stackoverflow_posts`
    LIMIT 10000
    ' > output.csv
    """)
    subprocess.call(cmd, shell=True)
    return None

if __name__ == "__main__":
    main()
    df = pd.read_csv("output.csv")
    print(df.shape)
    print(df.head())