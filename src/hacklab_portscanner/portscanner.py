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


    def __init__(self, ports, ip_or_host, flag):
        """
        Initalize class with
        parameters.
        ip and host are optional in that
        one or the other should be provided.
        """

        if len(ports) < 1:
            print ("No ports specified")
            return False

        self.ports = ports

        if ip_or_host == None:
            print ("Please provide an ip or a host.")
        elif flag == "host":
            self.host = ip_or_host
            self.grab_ip()
            self.port_scanner()
        else: 
            self.ip = ip_or_host
            self.port_scanner()
        

    def grab_ip(self):
        """
        Grab IP address of a host
        """

        try:
            self.ip = socket.gethostbyname(self.host)
        except:
            print ("Unknown host: Unable to obtain IP address for %s " % self.host)
            return False

    
    def port_scanner(self):
        """
        Scan target port
        """

        print ("Scanning ip %s" % self.ip)
        for port in self.ports:
            print ("Scanning port %s" % port)
            p = Process(target=self.socket_connector, args=(str(port),))
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
            print ("%s open" % port)
            print (results)
        except:
            print ("%s closed" % port)
        finally:
            connection.close() 
