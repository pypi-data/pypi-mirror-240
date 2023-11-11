import teradataml as tdml
from tdfs4ds import feature_store
data_domain             = feature_store.data_domain
schema                  = feature_store.schema
feature_catalog_name    = feature_store.feature_catalog_name
process_catalog_name    = feature_store.process_catalog_name
end_period              = feature_store.end_period
date_in_the_past        = feature_store.date_in_the_past
feature_version_default = feature_store.feature_version_default
display_logs            = feature_store.display_logs

def process_store_catalog_creation(if_exists='replace', comment='this table is a process catalog'):
    """
    This function creates a feature store catalog table in Teradata database.
    The catalog table stores information about features such as their names, associated tables, databases, validity periods, etc.

    Parameters:
    - schema: The schema name in which the catalog table will be created.
    - if_exists (optional): Specifies the behavior if the catalog table already exists. The default is 'replace', which means the existing table will be replaced.
    - table_name (optional): The name of the catalog table. The default is 'FS_FEATURE_CATALOG'.

    Returns:
    The name of the created or replaced catalog table.

    """

    # SQL query to create the catalog table
    query = f"""
    CREATE MULTISET TABLE {schema}.{process_catalog_name},
            FALLBACK,
            NO BEFORE JOURNAL,
            NO AFTER JOURNAL,
            CHECKSUM = DEFAULT,
            DEFAULT MERGEBLOCKRATIO,
            MAP = TD_MAP1
            (

                PROCESS_ID VARCHAR(36) NOT NULL,
                PROCESS_TYPE VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC NOT NULL,
                METADATA JSON(32000),
                ValidStart TIMESTAMP(0) WITH TIME ZONE NOT NULL,
                ValidEnd TIMESTAMP(0) WITH TIME ZONE NOT NULL,
                PERIOD FOR ValidPeriod  (ValidStart, ValidEnd) AS VALIDTIME
            )
            PRIMARY INDEX (PROCESS_ID);
    """

    # SQL query to create a secondary index on the feature name
    query2 = f"CREATE INDEX (PROCESS_TYPE) ON {schema}.{process_catalog_name};"

    # SQL query to comment the table
    query3 = f"COMMENT ON TABLE {schema}.{process_catalog_name} IS '{comment}'"

    try:
        # Attempt to execute the create table query
        execute_query(query)
        if tdml.display.print_sqlmr_query:
            print(query)
        if display_logs: print(f'TABLE {schema}.{process_catalog_name} has been created')
        execute_query(query3)
    except Exception as e:
        # If the table already exists and if_exists is set to 'replace', drop the table and recreate it
        if display_logs: print(str(e).split('\n')[0])
        if str(e).split('\n')[0].endswith('already exists.') and (if_exists == 'replace'):
            execute_query(f'DROP TABLE  {schema}.{process_catalog_name}')
            print(f'TABLE {schema}.{process_catalog_name} has been dropped')
            try:
                # Attempt to recreate the table after dropping it
                execute_query(query)
                if display_logs: print(f'TABLE {schema}.{process_catalog_name} has been re-created')
                if tdml.display.print_sqlmr_query:
                    print(query)
                execute_query(query3)
            except Exception as e:
                print(str(e).split('\n')[0])

    try:
        # Attempt to create the secondary index
        execute_query(query2)
        if tdml.display.print_sqlmr_query:
            print(query)
        if display_logs: print(f'SECONDARY INDEX ON TABLE {schema}.{process_catalog_name} has been created')
    except Exception as e:
        print(str(e).split('\n')[0])

    return feature_catalog_name