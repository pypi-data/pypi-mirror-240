from simpleetl._functions._db_quoting import quote


def _get_nextid(pgconn, schema, table, key):
    q = f"""SELECT
        coalesce(MAX({quote(key, pgconn)})+1,1) as maxid
        FROM {quote(schema, pgconn)}.{quote(table, pgconn)};"""
    with pgconn.cursor() as cursor:
        cursor.execute(q)
        return cursor.fetchone()[0]
