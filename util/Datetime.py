from datetime import datetime

def get_date()->str:
    '''
    format: 2023-01-01
    '''
    return datetime.today().strftime('%Y-%m-%d')
