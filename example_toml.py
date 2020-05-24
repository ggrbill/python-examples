import toml
from colorama import init 
from termcolor import colored 
  
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
parsed_toml = toml.load('./files/example_file.toml')
print(colored(parsed_toml, 'red', attrs=['bold']))
