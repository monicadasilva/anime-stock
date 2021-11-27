from app.exceptions.exceptions import AnimeNotFound

from . import conn_cur, create_table


def create_new(data):
    conn, cur = conn_cur()
    create_table()
    
    
    new_animes = (data['anime'],data['released_date'],data['seasons'], )
    query = 'INSERT INTO animes (anime, released_date, seasons) VALUES (%s, %s, %s)'
    cur.execute(query, new_animes)


    cur.execute("""
                SELECT * FROM animes WHERE anime like (%s);
                """,
                (data['anime'],),
        ) 
        
    datas = cur.fetchall()
    
    FIELDNAMES = ['id', 'anime', 'released_date', 'seasons']
    processed =[dict(zip(FIELDNAMES, row)) for row in datas]
    
    conn.commit()
    cur.close()
    conn.close()

    return {'data': processed}, 200


def get_all():
    conn, cur =  conn_cur()
    create_table()
    
    cur.execute("""
            SELECT * FROM animes;
                """)
    
    data = cur.fetchall()
    
    FIELDNAMES = ['id', 'anime', 'released_date', 'seasons']
    processed =[dict(zip(FIELDNAMES, row)) for row in data]

    
    conn.commit()
    cur.close()
    conn.close()

    if not data:
        return {'data':[]},200

    
    return {'data':processed},200


def get_one(data):
    conn, cur =  conn_cur()
    create_table()
    
    cur.execute("""
            SELECT * FROM animes WHERE id = (%s);
            """,
            (data,),
    ) 
    
    data = cur.fetchall()
    
    FIELDNAMES = ['id', 'anime', 'released_date', 'seasons']
    processed =[dict(zip(FIELDNAMES, row)) for row in data]

    
    conn.commit()
    cur.close()
    conn.close()

    if not processed:
        raise AnimeNotFound({'error': 'Not found!'})


    
    return {'data':processed}


def delete_one(id):
    conn, cur =  conn_cur()
    create_table()
    
    
    cur.execute("""
            SELECT * FROM animes WHERE id = (%s);
            """,
            (id,),
    ) 
    
    data = cur.fetchall()    
    
    if not data:
        raise AnimeNotFound({'error': 'Not found!'})
    
    
    cur.execute("""
            DELETE FROM animes WHERE id = (%s);
            """,
            (id,),
    ) 
    
    conn.commit()
    cur.close()
    conn.close()

    return ""
    
    
def update_anime(data, id):
    conn, cur = conn_cur()
    create_table()
    
    cur.execute("""
            SELECT * FROM animes WHERE id = (%s);
            """,
            (id,),
    ) 
    
    datas = cur.fetchall()    
    
    if not datas:
        raise AnimeNotFound({'error': 'Not found!'})
    
    
    
    updated = (data['anime'],data['released_date'],data['seasons'], id)
    query = 'UPDATE animes SET (anime, released_date, seasons) = (%s, %s, %s) WHERE id = (%s)'
    cur.execute(query, updated)

    conn.commit()
    cur.close()
    conn.close()

    return data

