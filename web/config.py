HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'aijiu'
USERNAME = 'root'
PASSWORD = 'syt20010907'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True


# 密钥
SECRET_KEY = "absdjahjkwhkasdby1g26r6fsysvd"
