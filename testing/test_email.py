from util.Email import EmailClass

message = """\
Subject: Unittest

This message is sent from Python."""

def login_and_send():
    
    mail_box = EmailClass(
        host = "smtp.gmail.com",
        address= 'mansh9826@gmail.com',
        password= 'iwrvaiwoxhnnmqeh'
        )
    login_result = mail_box.login()
    # mail_box.send('mansh9826@gmail.com',msg=message)
    mail_box.logout()
    
    return login_result