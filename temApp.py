from db import get_connection

try:
    connection=get_connection()
    with connection.cursor()as cursor:
        cursor.execute('call consulta_alumnos()')
        resulset=cursor.fetchall()
        for row in resulset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)


try:
    connection=get_connection()
    with connection.cursor()as cursor:
        cursor.execute('call consulta_alumnos(%s)',(2,))
        resulset=cursor.fetchall()
        # for row in resulset:
        print(row)
    connection.close()

except Exception as ex:
    print(ex)


try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consulta_alumnos(%s,%s,%s)',("nombre","apellidos","correo"))
        

    connection.commit()
    connection.close()

except Exception as ex:
    print(ex)