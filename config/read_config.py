import yaml 

# Default path of config file
DEFAULT_CONFIG  = "config/config.yaml"

class ReadConfig():
    """
        readConfig class is used to read a yaml config file

        Args: 
            path: path of config file
    """
    def __init__(self, path=DEFAULT_CONFIG):
        self.path = path 
    def read(self):
        """
            Load yaml file 

            Return:
                a dictionary of config data
        """
        with open(self.path, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data 
    
