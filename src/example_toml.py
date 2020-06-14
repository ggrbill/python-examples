import toml
from colorama import init 
from termcolor import colored 

def load_and_print_toml():
    init() 

    toml_str = """
    # This is a TOML document.

    title = "TOML Example in a string"

    [fluid-properties]
    density = 9000
    viscosity = 200
    """

    # Load toml from a String
    parsed_toml = toml.loads(toml_str)
    print(colored(parsed_toml, 'blue', attrs=['bold']))

    # Load toml from a File
    parsed_toml = toml.load('../input/example_file.toml')
    print(colored(parsed_toml, 'red', attrs=['bold']))


if __name__ == '__main__':
    load_and_print_toml()
