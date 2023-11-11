"""
*******************************************************************************
File: deUtils.py

Purpose: Creates some nice helper functions

Dependencies/Helpful Notes : 

*******************************************************************************
"""

from eimutils.aws_secrets import get_secrets
from eimutils.decrypt import getDERKey
from eimutils.delogging import log_to_console
import snowflake.connector as snc
import json

"""
*******************************************************************************
Function: get_db_connection_from_secret

Purpose: Generate a database connection from AWS secret.

Parameters:
     secret_name - AWS secret name from the account the process is running in
                   that contains the db connection information.  

Calls:
    get_secret
    connect_database
    
Called by:

Returns: database connection

*******************************************************************************
"""

def get_snowflake_connection_from_secret(secret_arn, env, account, aws_region):

    try:
        # get the secret
        # ToDo: Add Role to the secret. Then we can remove env.
        secrets = get_secrets(secret_arn, aws_region)
        dictSecrets = json.loads(secrets)

        my_user = dictSecrets["DW30SFSVCUSER"]

        #Decrypt the pkbDER key
        pkbDER = getDERKey(dictSecrets["DW30SFSVCPKEY"], dictSecrets["DW30SFSVCPPRS"])

        # ToDo: Create the connection to snowflake
                
        db_connection = snc.connect(
            user=f'{my_user}',
            account=account,
            private_key=pkbDER,
            role=f'EIM_{env}_DW3_ADMIN'
        )

    except Exception as e:
        log_to_console(__name__, 'Err', str(e))
        db_connection = {"Status":"Failed"}

    return db_connection

"""
*******************************************************************************
Change History:

Author		Date		Description
----------	----------	-------------------------------------------------------
Frank		2023-09-19  Initial Iteration

*******************************************************************************
"""