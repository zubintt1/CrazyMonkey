from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from static_components import ROOT_DIR
import logging
import random


class Ftp_Control():

    def start_ftp_server(self,port):
        authorizer = DummyAuthorizer()
        authorizer.add_user("user", "12345", ROOT_DIR+"\\User_Profiles", perm="elradfmw")
        authorizer.add_anonymous(ROOT_DIR+"\\User_Profiles")
        handler = FTPHandler
        handler.authorizer = authorizer
        logging.basicConfig(filename=ROOT_DIR+"\\File_Logs\\ftp.log", level=logging.DEBUG)
        server = FTPServer(("127.0.0.1", port), handler)
        server.max_cons = 512
        server.max_cons_per_ip = 5
        server.serve_forever()

    def random_port_gen(self):
        a = random.randint(100,10000)
        a = a * (22/7)
        b = random.randint(200,400)
        c = a * b
        c = int(c)
        d = random.randint(1,c)
        d = int(str(d)[:4])
        return d



