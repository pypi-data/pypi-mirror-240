from damo_mysql_exec import *
from typing import List
def demo_info_key(key):
    secreid_info_get_order="SELECT * from  `config`.`SecretId` WHERE type='{}'".format(key)
    result = return_sql_info(host='10.0.1.31', user='ops', passwd='l351gqX6wrzXnrhO', port=3306,
                                                sql=secreid_info_get_order)[0]

    key=result[0]
    secret=result[1]
    return key,secret