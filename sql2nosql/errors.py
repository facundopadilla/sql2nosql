class NoDBClients(Exception):
    def __init__(
        self,
        msg: str = "In order to use this method, you first need to connect to the databases.",
    ):
        if msg:
            self.msg = msg
