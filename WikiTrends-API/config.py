class Config:
    USER = 'aaldea'
    PASSWORD = 'bM0JAgom2tszWgUAa6k16Ofl'
    HOST = 'oracle.cise.ufl.edu'
    PORT = 1521
    SID = 'orcl'

    SQLALCHEMY_DATABASE_URI = f'oracle+oracledb://{USER}:{PASSWORD}@{HOST}:{PORT}/{SID}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False