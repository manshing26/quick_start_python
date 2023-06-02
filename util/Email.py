import smtplib
import ssl

class EmailClass:
    
    def __init__(self, host, address, password, port=465):
        self.host = host
        self.address = address
        self.password = password
        self.port = port
    
    def login(self):
        try:
        
            context = ssl.create_default_context()
            
            self.server =  smtplib.SMTP_SSL(self.host, self.port, context=context)
            self.server.login(self.address, self.password)
                
            return True
        
        except Exception as e:
            
            raise e
        
    def logout(self):
        self.server.close()
        
    def send(self, receiver_address, msg):
        try:
            self.server.sendmail(
                from_addr=self.address,
                to_addrs=receiver_address,
                msg=msg
            )
        except Exception as e:
            raise e
