def insert(name, phone, email):
    return"""
        INSERT INTO users(nome, phone, email)
            VALUES('{}', '{}', '{}')
    """.format(name, phone, email)