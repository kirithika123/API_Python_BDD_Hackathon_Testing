import psycopg2


def get_data_from_DB(strhostname, strDatabase, strUser, strPassword, strQuery):
    conn = psycopg2.connect(host=strhostname, database=strDatabase, user=strUser, password=strPassword)
    cursor = conn.cursor()
    cursor.execute(strQuery)
    headers = [i[0] for i in cursor.description]
    print("headers", headers)
    resultSet = cursor.fetchall()
    print("resultSet", resultSet)
    for result in resultSet:
        result = list(result)
        dictionary = dict(zip(headers, result))
        print("dictionary",dictionary)
    return dictionary

def get_deleted_data_from_DB(strhostname, strDatabase, strUser, strPassword, strQuery):
    conn = psycopg2.connect(host=strhostname, database=strDatabase, user=strUser, password=strPassword)
    cursor = conn.cursor()
    cursor.execute(strQuery)
    headers = [i[0] for i in cursor.description]

    resultSet = cursor.fetchall()

    for result in resultSet:
        result = list(result)
        dictionary = dict(zip(headers, result))

    return dictionary


