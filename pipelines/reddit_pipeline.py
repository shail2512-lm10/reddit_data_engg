from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_to_csv
import pandas as pd

from utils.configs import REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, OUTPUT_PATH

def reddit_pipeline(filename: str, subreddit: str, time_filter="day", limit=None):

    instance = connect_reddit(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY, "Shail")
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    transformed_post_df = transform_data(post_df)

    file_path = f"{OUTPUT_PATH}/{filename}.csv"
    load_to_csv(transformed_post_df, file_path)

    return file_path