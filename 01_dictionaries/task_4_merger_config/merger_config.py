def merge_configs(dev: dict[str, str], prod: dict[str, str]) -> dict[str, set]:
    common_keys = dev.keys() & prod.keys()

    config = {
    key: {dev[key], prod[key]} for key in common_keys
    }

    return config

def main():
    dev_config = {
            "db_host": "localhost",
            "debug": "True",
            "port": "5432",
            "user": "postgres",
            "password": "qwerty",
            "database": "postgres",
    }
    prod_config = {
            "db_host": "remote host",
            "debug": "False",
            "status": "admin",
            "port": "7750",
            "login": "disha",
            "loglevel": "warn",
    }

    result = merge_configs(dev_config, prod_config)

    print("\nMerger configs:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()