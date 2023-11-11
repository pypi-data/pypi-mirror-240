"""Interactions with configuration file"""
import configparser
from pathlib import Path
from typing import Dict, Optional, Tuple, List
import requests


USER_HOME_FOLDER = Path.home()
TRACEFORWARD_FOLDER = USER_HOME_FOLDER / ".traceforward"
CONFIG_FILE = TRACEFORWARD_FOLDER / "traceForwardConfig.ini"

NETWORKS_ENDPOINT = "{url}/api/networks"


def _get_available_networks(
    server_url: str, username: str, password: str
) -> Optional[List[Tuple[str, str]]]:
    try:
        response = requests.get(
            NETWORKS_ENDPOINT.format(url=server_url),
            verify=False,
            auth=(username, password),
            timeout=30)
        if response.status_code != 200:
            return None
        return [
            (network['name'], network['id']) for network in response.json()
        ]
    except Exception:
        return None


def _set_network_id(
    config: configparser.ConfigParser
) -> configparser.ConfigParser:
    networks = _get_available_networks(
        config['FORWARD_SERVER']['URL'],
        config['FORWARD_SERVER']['username'],
        config['FORWARD_SERVER']['password']
    )
    if networks:
        print("Found the following networks available on the Forward Server")
        for index, network in enumerate(networks):
            print(f"#{index}: ID {network[1]} network name: '{network[0]}'")
        if len(networks) > 1:
            config['FORWARD_SERVER']['network_id'] = input(
                "Please enter the network ID from available"
                " on the Forward Server: "
            )
        else:
            config['FORWARD_SERVER']['network_id'] = networks[0][1]
    else:
        config['FORWARD_SERVER']['network_id'] = input(
            "Please enter the network ID: "
        )
    return config


def init() -> None:
    """Used to initialize or locate configuration file"""

    if Path(CONFIG_FILE).is_file():
        return
    print(f"No config file located at {CONFIG_FILE}, creating one...")
    Path(TRACEFORWARD_FOLDER).mkdir(parents=True, exist_ok=True)
    config = configparser.ConfigParser()
    config['FORWARD_SERVER'] = {}
    config['FORWARD_SERVER']['URL'] = input(
        "Please enter Forward Server URL: "
    )
    config['FORWARD_SERVER']['username'] = input(
        "Please enter Forward Server username: "
    )
    config['FORWARD_SERVER']['password'] = input(
        "Please enter Forward Server password: "
    )
    config = _set_network_id(config)
    Path(TRACEFORWARD_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(CONFIG_FILE).touch()
    with open(CONFIG_FILE, 'w', encoding='utf-8') as config_file:
        config.write(config_file)
    return


def get_config_file_data() -> Dict:
    """Used to get configuration file data"""

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    try:
        return {
            "forward_server_url": config['FORWARD_SERVER']['URL'],
            "username": config['FORWARD_SERVER']['username'],
            "password": config['FORWARD_SERVER']['password'],
            "network_id": config['FORWARD_SERVER']['network_id']
        }
    except KeyError:
        return {}
