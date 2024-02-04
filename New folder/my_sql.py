import mysql.connector

# print(dir(mysql.connector))

#  the methods and the attributes we are getting with the mysql at python environment are below 

# ['BINARY', 'Binary', 'CMySQLConnection', 'CharacterSet',
# 'ClientFlag', 'Connect', 'DATETIME', 'DataError', 'DatabaseError', 
# 'Date', 'DateFromTicks', 'Error', 'FieldFlag', 'FieldType', 'HAVE_CEXT',
# 'IntegrityError', 'InterfaceError', 'InternalError', 'MySQLConnection',
# 'NUMBER', 'NotSupportedError', 'OperationalError', 'PoolError', 'ProgrammingError', 
# 'ROWID', 'RefreshOption', 'STRING', 'Time', 'TimeFromTicks', 'Timestamp', 'TimestampFromTicks',
# 'Warning', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__path__', '__spec__', '__version__', '__version_info__',
# 'abstracts', 'apilevel', 'authentication', 'charsets', 'connect', 'connection',
# 'connection_cext', 'constants', 'conversion', 'cursor', 'cursor_cext', 
# 'custom_error_exception', 'custom_types', 'dbapi', 'errorcode', 'errors', 
# 'locales', 'logger', 'network', 'opentelemetry', 'optionfiles', 'paramstyle', 'plugins', 
# 'pooling', 'protocol', 'threadsafety', 'types', 'utils', 'version']


conn=mysql.connector.connect(
    host="11001 ",
    database="database_he_bahi_majak_nahi",
    user="sudarshan",
    password="sudarshan123"
)