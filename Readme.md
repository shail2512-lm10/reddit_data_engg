## Data Engineering Pipeline - Reddit API

The pipeline consists of 
1. Reddit pipeline: 
    
    ingesting data from reddit api, do the basic transformation and save it as csv file in local path

2. AWS pipeline: 
    
    take this csv file and load to s3 bucket.

3. AWS Glue: 

    It transforms the data located in s3 bucket and saves it in another folder on the bucket.

4. Glue Crawler: 

    It automatically infers the schema from s3 bucket and creates an Athena Table.

5. Athena: 

    Can be helpful to perform query on s3 bucket data

6. Visualization: 
    
    Integrate Quicksight to visualize data

7. AWS Redshift: 
    
    Alternatively, save the Athena table in Data Warehouse

Steps to run:

1. Modify config.conf file located in config/ folder
2. Modify configs.py file located in utils/ folder
3. Modify airflow.env
4. Modify docker-copose.yml to configure airflow username and password
5. Then run: `pip install -r requirements.txt` in a new python 3.9 environment
6. Ensure you have docker engine and docker-compose set up, then run:

    `docker-compose up -d`
7. An airflow webserver should have started on localhost:8080 port.


