import yaml 

""" 
    Configuration of the API 
    cateDict: a dictionary for mapping ID to Name of a category
    validDict: a dictionary for mappting which category is valid for showing
"""

config = {
    "cateDict":{
    1 : "Resturant", 
    2 : "Retail",
    3 : "Hotel",
    4 : "Activity"
    }, 
    "validDict": {
    "Resturant" : True, 
    "Retail" : True, 
    "Hotel" : False, 
    "Activity" : True  
    }
}

# Write the config to .yaml
with open("config/config.yaml", "w") as f:
    yaml.dump(config, f)
