from typing import Any
from .glue import list_columns_of_table


def substitute_params(params: dict[str, Any]) -> dict[str, Any]:
    params['fill_na_value'] = 'NULL'
    if params['fill_na']:
        params['fill_na_value'] = params['fill_na']

    return params


def create_select_features(
            select_columns: list[str],
            params: dict[str, Any],
        ) -> str:
    columns = []
    for col in select_columns:
        columns.append('\t\tCOALESCE(' + col + f', {params["fill_na_value"]}) AS {col}')
    columns.append(f"\t\tCAST({params['targets_database']}.{params['targets_table']}.event_time AS TIMESTAMP(3)) "
                   "AS event_time")
    columns.append(f"\t\t{params['targets_database']}.{params['targets_table']}.mach_id")
    columns.append(f"\t\t{params['targets_database']}.{params['targets_table']}.target_value")
    return ',\n'.join(columns)


def create_statement_join_features(params: dict[str, Any]) -> str:
    join_features_list = []
    for feature in params['features_list']:
        join_features_list.append(f"""
            LEFT JOIN {params["ATHENA_MACHINE_LEARNING"]}.{feature}
                ON {params["targets_database"]}.{params['targets_table']}.mach_id =
                    {params["ATHENA_MACHINE_LEARNING"]}.{feature}.mach_id
                AND {params["ATHENA_MACHINE_LEARNING"]}.{feature}.event_time =
                    {params["targets_database"]}.{params['targets_table']}.event_time
                AND {params["ATHENA_MACHINE_LEARNING"]}.{feature}.is_current_version = True
                AND {params["ATHENA_MACHINE_LEARNING"]}.{feature}.is_deleted = False
        """)
    return ''.join(join_features_list)


def create_statement_filter_base_table(params: dict[str, Any]) -> str:
    statement_filters = f"""
        {params['targets_database']}.{params['targets_table']}.event_time
            BETWEEN DATE_PARSE(\'{params['ref_date']}\', '%Y-%m-%d') - INTERVAL '{params["monthly_window"] - 1}' MONTH
            AND DATE_PARSE('{params['ref_date']}', '%Y-%m-%d')
            {params['targets_filter'] if 'targets_filter' in params else ''}
    """
    return statement_filters


def create_query_features_dataset(
            select_features: str,
            join_features: str,
            filters_base_table: str,
            params: dict[str, Any],
        ) -> str:
    query_features = f"""
        SELECT
            {select_features}
        FROM {params['targets_database']}.{params['targets_table']}
        {join_features}
        WHERE {filters_base_table}
    """
    return query_features


def get_feature_columns(params: dict[str, Any]) -> list[str]:
    feature_columns = []
    for feature in params['features_list']:
        feature_columns += list_columns_of_table(
            params['glue_client'],
            params['ATHENA_MACHINE_LEARNING'],
            feature,
            params['cols_to_exclude'],
            params['chars_to_exclude']
        )
    return feature_columns


def create_dataset_query(params: dict[str, Any]) -> str:

    params = substitute_params(params)
    feature_columns = get_feature_columns(params)
    select_features = create_select_features(feature_columns, params)
    join_features = create_statement_join_features(params)
    filters = create_statement_filter_base_table(params)
    query_features_dataset = create_query_features_dataset(select_features, join_features, filters, params)
    return query_features_dataset
