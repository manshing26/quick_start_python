import os
from util.Built import build_structure
from util.Argument import MY_argument
from util.Config import MY_config
from util.Logger import get_logger

PWD = os.path.dirname(__file__)    

def handle_argument(my_argument:MY_argument):
    
    my_argument.get_instance().add_argument(
        '-c',
        '--config',
        type=str,
        default='default',
        dest='config',
        help='Name of the config file, example: default.ini',
        )

def setup():
    
    build_structure(PWD)
    my_argument = MY_argument()
    handle_argument(my_argument)
    my_config = MY_config(my_argument, PWD)
    my_logger = get_logger(my_config)
    
    return my_config, my_logger
    
def main(my_config,my_logger):
    
    my_logger.debug('Welcome back')

if __name__ == "__main__":
        
    my_config, my_logger = setup()
            
    main(my_config, my_logger)