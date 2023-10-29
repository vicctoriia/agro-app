from .database import db
from sqlalchemy import text

def get_crop_data(filters=None):
    base_sql = "SELECT * FROM crop.crop_data"
    conditions = []
    params = {}
    accepted_filters = ['cod_variavel', 'cod_produto_lavouras_temporarias', 'cod_ano', 'cod_municipio']

    # Criando filtros para a query, caso existam parametros
    if filters:
        for column, value in filters.items():
            if column in accepted_filters:
                conditions.append(f"{column} = :{column}")
                params[column] = value

    # Fazendo o append na query
    if conditions:
        base_sql += " WHERE " + " AND ".join(conditions)

    sql = text(base_sql)

    with db.engine.begin() as conn:
        result = conn.execute(sql, params)
        
        # Extraindo os nomes das colunas
        column_names = result.keys()

        # Convertendo o resultado em um dicionário
        crop_data = [{column: value for column, value in zip(column_names, row)} for row in result]
        
        return crop_data


