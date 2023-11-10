import datetime

import pandas as pd
import pymysql
import sqlalchemy.engine.url as engineUrl
from sqlalchemy import create_engine


def get_db_engine(db):
    try:
        db_url = engineUrl.URL.create("mysql+pymysql", **db)
    except Exception as e:
        print(e)
        db["drivername"] = "mysql+pymysql"
        db_url = engineUrl.URL(**db)
    db_engine = create_engine(db_url, pool_pre_ping=True)
    return db_engine


def create(database: dict, date=None):
    if not date:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    db_engine = get_db_engine(database)
    show_sql = "Show table status;"
    show_res = pd.read_sql(show_sql, db_engine)
    show_frame = show_res[show_res["Create_options"] == "partitioned"][["Name", "Create_options"]]
    name_list = []
    for x in show_frame["Name"]:
        name_list.append(x)
    partition_list = []
    for name in name_list:
        last_sql = f"SELECT PARTITION_NAME FROM INFORMATION_SCHEMA.PARTITIONS WHERE table_name = '{name}' ORDER BY " \
                   f"partition_ordinal_position DESC LIMIT 1;"
        last_res = pd.read_sql(last_sql, db_engine)
        partition_list.append(last_res["PARTITION_NAME"][0])
    partition_dict = dict(zip(name_list, partition_list))
    conn = pymysql.connect(host=database.get("host"), port=database.get("port"), user=database.get("username"),
                           password=database.get("password"), database=database.get("database"))
    cursor = conn.cursor()
    for table_name in partition_dict:
        partition_date = datetime.datetime.strptime(partition_dict.get(table_name).replace("p", ""), "%Y%m%d")
        while partition_date < date:
            partition_date = partition_date + datetime.timedelta(days=1)
            partition_date_str = "p" + partition_date.strftime("%Y%m%d")
            partition_end_str = (partition_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            try:
                create_sql = f"ALTER TABLE {table_name} ADD PARTITION (PARTITION {partition_date_str} VALUES LESS THAN (TO_DAYS ('{partition_end_str}')));"
                cursor.execute(create_sql)
                conn.commit()
                print(f"table: {table_name} add TO_DAYS partition succeeded, the current latest partition is: {partition_date_str}")
            except Exception as e:
                print(e)
                create_sql = f"ALTER TABLE {table_name} ADD PARTITION (PARTITION {partition_date_str} VALUES LESS THAN ('{partition_end_str}'));"
                cursor.execute(create_sql)
                conn.commit()
                print(f"table: {table_name} add DATE partition succeeded, the current latest partition is: {partition_date_str}")
    conn.close()


def show(database):
    show_sql = "show table status;"
    db_engine = get_db_engine(database)
    show_res = pd.read_sql(show_sql, db_engine)
    show_frame = show_res[show_res["Create_options"] == "partitioned"][["Name", "Create_options"]]
    name_list = []
    for x in show_frame["Name"]:
        name_list.append(x)
    partition_list = []
    for name in name_list:
        last_sql = f"SELECT PARTITION_NAME FROM INFORMATION_SCHEMA.PARTITIONS WHERE table_name = '{name}' " \
                   f"ORDER BY partition_ordinal_position DESC LIMIT 1;"
        last_res = pd.read_sql(last_sql, db_engine)
        partition_list.append(last_res["PARTITION_NAME"][0])
    partition_dict = dict(zip(name_list, partition_list))
    return partition_dict
