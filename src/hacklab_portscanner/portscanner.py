import socket
from multiprocessing import Process

class PortScanner():
    """
    Port Scanner class for
    the HackLab tool kit 
    """

    host = ''
    ip = ''
    ports = []


    def __init__(self, ports, host=None, ip=None):
        """
        Initalize class with
        parameters.
        ip and host are optional in that
        one or the other should be provided.
        """
        print "here" 
        if host == None and ip == None:
            print "Please provide an ip or a host."
            print "If you provide both ip will be used"
        elif host != None and ip == None:
            self.host = host
            self.grab_ip()
        else: 
            self.ip = ip
            self.port_scanner()
        

    def grab_ip(self):
        """
        Grab IP address of a host
        """

        try:
            self.ip = socket.gethostbyname(self.host)
        except:
            print "Unknown host: Unable to obtain IP address for %s " % self.host
            return False

    
    def port_scanner(self):
        """
        Scan target port
        """

        for port in self.ports:
            print "Scanning port %s" % port
            p = Process(target=self.socket_connector, args=(port))
            p.start()
            p.join()


    def socket_connector(self, port):
        """
        Attempt to create a socket 
        on the target hosts port
        """

        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.ip, port))
            connection.send('HELO\r\n')
            results = connection.recv(100)
            print "%s open" % port
            print results
        except:
            print "%s closed" % port
        finally:
            connection.close()
    
