class DbServer:

    def __init__(self, dbHost, dbPort, dbType, dbUser, userPassword):
        self.dbHost = dbHost
        self.dbPort = dbPort
        self.dbType = dbType
        self.dbUser = dbUser
        self.userPassword = userPassword

    # todo : Aca debe ir los datos para la conexion al servidor de bd
