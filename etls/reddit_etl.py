import sys
import praw
from praw import Reddit
import pandas as pd
import numpy as np

from utils.configs import POST_FIELDS

def connect_reddit(client_id: str, client_secret: str, user_agent: str) -> Reddit:
    """_This function helps connect with Reddit API_

    Args:
        client_id (str): Enter your client ID
        client_secret (str): Enter your secret key
        user_agent (str): User Agent

    Returns:
        Reddit: A reddit instance
    """
    try:

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent)
        
        print("Connected to Reddit!")
        return reddit
    
    except Exception as e:
        print(e)
        sys.Exit(1)


def extract_posts(reddit: Reddit, subreddit_name: str, time_filter: str, limit: int = 10) -> list:
    """_This function Extarcts subreddit posts_

    Args:
        reddit (Reddit): Reddit Instance
        subreddit_name (str): Subreddit name
        time_filter (str): time interval
        limit (int, optional): Number of posts to fetch. Defaults to 10.

    Returns:
        list: List of dictionary of fetched posts
    """
    subreddit = reddit.subreddit(subreddit_name)

    posts = subreddit.top(time_filter=time_filter, limit=limit)

    posts_list = []

    for post in posts:
        post_dict = vars(post)
        post = {key: post_dict[key] for key in POST_FIELDS}
        posts_list.append(post)

    return posts_list

def transform_data(post_df: pd.DataFrame) -> pd.DataFrame:
    """_This function Transforms the data

    Args:
        post_df (pd.DataFrame): A pandas DataFrame

    Returns:
        pd.DataFrame: A tansformed pandas DataFrame
    """ 
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)

    return post_df

def load_to_csv(data: pd.DataFrame, path: str) -> None:
    """_Loads the data to csv_

    Args:
        data (pd.DataFrame): A transformed pandas DataFrame
        path (str): path to the csv filename
    """
    data.to_csv(path, index=False)


    
