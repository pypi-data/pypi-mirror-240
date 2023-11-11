"""
*******************************************************************************
File: data_hub_connection.py

Purpose: Core functions invoked by the Data Hub class that interact with the db.

Dependencies/Helpful Notes :

*******************************************************************************
"""
from eimutils.delogging import log_to_console
import snowflake


def connect_database(env, ACCOUNT, pkbDER):
    """
    Creates a pymssql connection for use by the class
    :return: pymssql connection
    """
    try:

        db_connection =  snowflake.connect(
        user=f"EIM_{env}_DW3_SVC_USER",
        account=ACCOUNT,
        private_key=pkbDER,
        role=f"EIM_{env}_DW3_ADMIN",
        )

    except snowflake.Error as err:
        e_msg = "snowflake_connection.connect_database :: Connection error. " + err
        log_to_console(__name__,'Error',e_msg)
        return {'Status': 'Failure'}

    return db_connection

"""
*******************************************************************************
Change History:

Author		Date		Description
----------	----------	-------------------------------------------------------
ffortunato  11/03/2023  Initial Iteration

*******************************************************************************
"""