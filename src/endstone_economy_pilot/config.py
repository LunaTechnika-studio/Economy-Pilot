import tomllib
import tomlkit
import os


version = "0.0.7"

config_file_name = f'economy-pilot.toml'

currency_symbol = "$"
database_type = "sqlite"
directory = 'config'

database_host = 'change if not using sqlite'
database_port = 'change if not using sqlite'
database_username = 'change if not using sqlite'
database_password = 'change if not using sqlite'
database_name = 'change if not using sqlite'


config = {
        "version": version,
        "currency_symbol": currency_symbol,
        "database_type": database_type,

        "database_host": database_host,
        "database_port": database_type,
        "database_username": database_username,
        "database_password": database_password,
        "database_name": database_name
    }

def check_config():

    file_path = os.path.join(directory, config_file_name)

    os.makedirs(directory, exist_ok=True)

    if not os.path.isfile(file_path):
        toml_doc = tomlkit.document()

        toml_doc.add(tomlkit.comment("This is the Economy Pilot configuration file\n"))

        toml_doc.add(tomlkit.comment("The version of the configuration"))
        toml_doc["version"] = config["version"]

        toml_doc.add(tomlkit.comment("The currency symbol to use"))
        toml_doc["currency_symbol"] = config["currency_symbol"]

        toml_doc.add(tomlkit.comment("Type of the database (sqlite, mysql)"))
        toml_doc["database_type"] = config["database_type"]

        toml_doc.add(tomlkit.comment("The database host ip"))
        toml_doc["database_host"] = config["database_host"]
        
        toml_doc.add(tomlkit.comment("The database host port"))
        toml_doc["database_port"] = config["database_port"]

        toml_doc.add(tomlkit.comment("The database host username"))
        toml_doc["database_username"] = config["database_username"]

        toml_doc.add(tomlkit.comment("The database host password"))
        toml_doc["database_password"] = config["database_password"]

        toml_doc.add(tomlkit.comment("The name of the database"))
        toml_doc["database_name"] = config["database_name"]

        toml_doc.update(config)

        with open(file_path, 'a') as file:
            file.write(tomlkit.dumps(toml_doc))


def load_config():
    file_path = os.path.join(directory, config_file_name)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'rb') as file:
        toml_data = tomllib.load(file)
        u_version = toml_data.get("version")
        u_currency_symbol = toml_data.get("currency_symbol")
        u_database_type = toml_data.get("database_type")

        u_database_host = toml_data.get("database_host")
        u_database_port = toml_data.get("database_port")
        u_database_username = toml_data.get("database_username")
        u_database_password = toml_data.get("database_password")
        u_database_name = toml_data.get("database_name")

    return u_version, u_currency_symbol, u_database_type, u_database_host, u_database_username, u_database_password, u_database_name, u_database_port

def update_config():
    current_config = load_config()
    old_config_name = f'economy-pilot.toml'
    old_config_path = f'{directory}/{old_config_name}'

    config["currency_symbol"] = current_config[1]
    config["database_type"] = current_config[2]

    config["database_host"] = current_config[3]
    config["database_username"] = current_config[4]
    config["database_password"] = current_config[5]
    config["database_name"] = current_config[6]
    config["database_port"] = current_config[7]

    #if current_config[2] != "sqlite" or current_config[2] != "mysql" or current_config[2] != "postgres":
    #    print(current_config[2])
    #    config["database_type"] = "sqlite"
    os.remove(old_config_path)

    file_path = os.path.join(directory, config_file_name)

    os.makedirs(directory, exist_ok=True)

    if not os.path.isfile(file_path):
        toml_doc = tomlkit.document()

        toml_doc.add(tomlkit.comment("This is the Economy Pilot configuration file\n"))

        toml_doc.add(tomlkit.comment("The version of the configuration"))
        toml_doc["version"] = config["version"]

        toml_doc.add(tomlkit.comment("The currency symbol to use"))
        toml_doc["currency_symbol"] = config["currency_symbol"]

        toml_doc.add(tomlkit.comment("Type of the database (sqlite, mysql, postgres)"))
        toml_doc["database_type"] = config["database_type"]

        toml_doc.add(tomlkit.comment("The database host ip"))
        toml_doc["database_host"] = config["database_host"]
        
        toml_doc.add(tomlkit.comment("The database host port"))
        toml_doc["database_port"] = config["database_port"]

        toml_doc.add(tomlkit.comment("The database host username"))
        toml_doc["database_username"] = config["database_username"]

        toml_doc.add(tomlkit.comment("The database host password"))
        toml_doc["database_password"] = config["database_password"]

        toml_doc.add(tomlkit.comment("The name of the database"))
        toml_doc["database_name"] = config["database_name"]

        toml_doc.update(config)

        with open(file_path, 'a') as file:
            file.write(tomlkit.dumps(toml_doc))

