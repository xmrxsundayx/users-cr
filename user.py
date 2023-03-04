from mysqlconnection import connectToMySQL

class Users:
    DB = "users_cr"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #CRUD METHODS

    #CREATE
    @classmethod
    def save (cls, data):
        query ="""
                    INSERT into users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #READ

    @classmethod
    def get_user(cls, data):
        query = """SELECT * from users
                    WHERE id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        all_users =[]
        for row in results:
            #make an object
            all_users. append(cls(row))
            #add to list
        return all_users

    #UPDATE

    @classmethod
    def edit(cls,data):
        query = """UPDATE users 
                SET first_name=%(first_name)s,
                last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
        

    #DELETE

    @classmethod
    def delete(cls, data):
        query = """
                    DELETE FROM users WHERE id = %(id)s;
                    """
        return connectToMySQL(cls.DB).query_db(query,data)