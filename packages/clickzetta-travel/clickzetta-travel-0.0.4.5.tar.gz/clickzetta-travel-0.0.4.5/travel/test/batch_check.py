import sys
import json
from time import sleep
import travel.util.validation_util as validation_util
from migration.connector.source.mysql.source import MysqlSource
from migration.connector.source.pg.source import PGSource
from migration.connector.destination.clickzetta.destination import ClickZettaDestination


def write_validation_table_result(source_df_result, destination_df_result, out_path, source_table, destination_table):
    try:
        if source_df_result.equals(destination_df_result):
            with open(out_path + '/result.txt', 'w') as f:
                f.write(
                    f'{source_table} result is equal with {destination_table} result')
        else:
            with open(out_path + '/result.txt', 'w') as f:
                f.write(
                    f'{source_table} result is not equal with {destination_table} result')
            diff_result = source_df_result.compare(destination_df_result,
                                                   result_names=(source_table,
                                                                 destination_table))
            with open(out_path + '/diff_result.csv', 'w') as f:
                f.write(diff_result.to_csv(index=True))
    except Exception as e:
        raise e
def validate(source, destination, source_tables, destination_tables, validation_type, out_path):
    if len(source_tables) != len(destination_tables):
        raise Exception("Source tables and destination tables should have the same length")
    try:
        index = 0
        for source_table, destination_table in zip(source_tables, destination_tables):
            index += 1
            if index % 10 == 0:
                sleep(3)
                index = 0
            if int(validation_type) == 0:
                source_df_result, destination_df_result = validation_util.gen_basic_validation_table_result(source, destination, source_table, destination_table)
                write_validation_table_result(source_df_result, destination_df_result, out_path, source_table, destination_table)
            elif int(validation_type) == 1:
                source_df_result, destination_df_result = validation_util.multidimensional_validation_table(source, destination, source_table, destination_table)
                write_validation_table_result(source_df_result, destination_df_result, out_path, source_table, destination_table)
    except Exception as e:
        raise e


def get_source_connection_params(source_engine_conf):
    host = source_engine_conf['host']
    port = source_engine_conf['port']
    username = source_engine_conf['username']
    password = source_engine_conf['password']
    db_type= source_engine_conf['db_type']
    database = source_engine_conf['database']
    return {
        'host': host,
        'port': port,
        'user': username,
        'password': password,
        'db_type': db_type,
        'database': database,
    }

def get_destination_connection_params(destination_engine_conf):
    service = destination_engine_conf['service']
    workspace = destination_engine_conf['workspace']
    instance = destination_engine_conf['instance']
    vcluster = destination_engine_conf['vcluster']
    username = destination_engine_conf['username']
    password = destination_engine_conf['password']
    schema = destination_engine_conf['schema']
    instance_id = destination_engine_conf['instanceId']

    return {
        'service': service,
        'workspace': workspace,
        'instance': instance,
        'vcluster': vcluster,
        'username': username,
        'password': password,
        'schema': schema,
        'instanceId': instance_id,
    }

def construct_source_engine(connection_dict: dict):
    db_type = connection_dict['db_type']
    if db_type == 'mysql':
        return MysqlSource(connection_dict)
    elif db_type == 'postgres':
        return PGSource(connection_dict)
    else:
        raise Exception(f"Unsupported db type {db_type}")

def construct_destination_engine(connection_dict: dict):
    return ClickZettaDestination(connection_dict)


def get_source_tables(source_tables_file):
    source_tables = []
    with open(source_tables_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            source_tables.append(line.strip())
    return source_tables

def get_destination_tables(destination_tables_file):
    destination_tables = []
    with open(destination_tables_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            destination_tables.append(line.strip())
    return destination_tables


if __name__ == '__main__':
    source_engine_conf = sys.argv[1]
    destination_engine_conf = sys.argv[2]
    source_tables_file = sys.argv[3]
    destination_tables_file = sys.argv[4]
    validation_type = sys.argv[5]
    out_path = sys.argv[6]
    try:
        source_engine_conf = json.load(open(source_engine_conf))
        source = construct_source_engine(get_source_connection_params(source_engine_conf))
        destination_engine_conf = json.load(open(destination_engine_conf))
        destination = construct_destination_engine(get_destination_connection_params(destination_engine_conf))
        source_tables = get_source_tables(source_tables_file)
        destination_tables = get_destination_tables(destination_tables_file)
        validate(source, destination, source_tables, destination_tables, validation_type, out_path)
    except Exception as e:
        print('validation error')
        raise e

