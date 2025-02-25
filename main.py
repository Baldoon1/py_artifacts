"""
Module Docstring
"""

__author__ = "Nico Bressler"
__version__ = "2025.02.24"
__license__ = "MIT"

import os
import requests
import time
import datetime
import pytz
from logzero import logger
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_TOKEN")
BASE_URL = "https://api.artifactsmmo.com"

def get_status():
    url = f"{BASE_URL}"

    headers = {
        "Accept": "application/json"
        }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_bank_details():
    url = f"{BASE_URL}/my/bank"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_bank_items():
    url = f"{BASE_URL}/my/bank/items"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_ge_sell_orders():
    url = f"{BASE_URL}/my/grandexchange/orders"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_ge_sell_history():
    url = f"{BASE_URL}/my/grandexchange/history"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_account_details():
    url = f"{BASE_URL}/my/details"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_my_characters():
    url = f"{BASE_URL}/my/characters"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_all_characters_logs():
    url = f"{BASE_URL}/my/logs"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def get_character(name):
    url = f"{BASE_URL}/characters/{name}"

    headers = {
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return(response.json())
    except requests.exceptions.HTTPError as e:
        logger.error(f'HTTP error: {e}')

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_move(name, x, y):
    url = f"{BASE_URL}/my/{name}/action/move"

    payload = {
        "x": x,
        "y": y
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        check_cooldown("Baldoon_01")
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        logger.info(f'Successfully moved to {x}, {y}.')
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.error("Map not found.")
        elif e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 490:
            logger.error("Character already at destination.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_fight(name):
    url = f"{BASE_URL}/my/{name}/action/fight"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 497:
            logger.error("Character inventory is full.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_rest(name):
    url = f"{BASE_URL}/my/{name}/action/rest"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_gathering(name):
    url = f"{BASE_URL}/my/{name}/action/gathering"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        check_cooldown(name)
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 493:
            logger.error("Not skill level required.")
        elif e.response.status_code == 497:
            logger.error("Character inventory is full.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")
        elif e.response.status_code == 598:
            logger.error("Resource not found on this map.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_unequip_item(name, slot, quant=1):
    url = f"{BASE_URL}/my/{name}/action/unequip"

    payload = {
        "slot": slot,
        "quantity": quant
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.error("Item not found.")
        elif e.response.status_code == 478:
            logger.error("Missing item or insufficient quantity.")
        elif e.response.status_code == 483:
            logger.error("Character has no enough HP to unequip this item.")
        elif e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 491:
            logger.error("Slot is empty.")
        elif e.response.status_code == 497:
            logger.error("Character inventory is full.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_crafting(name, code, quant=1):
    url = f"{BASE_URL}/my/{name}/action/crafting"

    payload = {
        "code": code,
        "quantity": quant
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.error("Craft not found.")
        elif e.response.status_code == 478:
            logger.error("Missing item or insufficient quantity.")
        elif e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 491:
            logger.error("Slot is empty.")
        elif e.response.status_code == 493:
            logger.error("Not skill level required.")
        elif e.response.status_code == 497:
            logger.error("Character inventory is full.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")
        elif e.response.status_code == 598:
            logger.error("Workshop not found on this map.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def post_action_equip_item(name, code, slot, quant=1):
    url = f"{BASE_URL}/my/{name}/action/equip"

    payload = {
        "code": code,
        "slot": slot,
        "quantity": quant
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.error("Item not found.")
        elif e.response.status_code == 478:
            logger.error("Missing item or insufficient quantity.")
        elif e.response.status_code == 484:
            logger.error("Character can't equip more than 100 utilities in the same slot.")
        elif e.response.status_code == 485:
            logger.error("This item is already equipped.")
        elif e.response.status_code == 486:
            logger.error("An action is already in progress by your character.")
        elif e.response.status_code == 491:
            logger.error("Slot is empty.")
        elif e.response.status_code == 496:
            logger.error("Character level is insufficient.")
        elif e.response.status_code == 497:
            logger.error("Character inventory is full.")
        elif e.response.status_code == 498:
            logger.error("Character not found.")
        elif e.response.status_code == 499:
            logger.error("Character in cooldown.")

    except requests.exceptions.ConnectionError:
        logger.error("There was a connection error.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
    except requests.exceptions.RequestException as e:
        logger.error(f'Request failed: {e}')

def check_cooldown(name):
    character = get_character(name)
    character = character["data"]

    cooldown_expiration = character["cooldown_expiration"]
    cooldown_expiration = datetime.datetime.strptime(cooldown_expiration, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)

    local_tz = pytz.timezone("America/Los_Angeles")
    now = datetime.datetime.now(local_tz)

    if cooldown_expiration > now:
        cooldown_seconds = (cooldown_expiration - now).total_seconds()
        logger.warning(f'Character {name} is currently in cooldown. Waiting {cooldown_seconds} seconds.')
        while cooldown_seconds > 0:
            logger.info(f'Waiting... {cooldown_seconds} seconds remaining.')
            time.sleep(5)
            now = datetime.datetime.now(local_tz)
            cooldown_seconds = (cooldown_expiration - now).total_seconds()
    else:
        logger.info(f'Character {name} is not in cooldown.')

def main():
    """ Main entry point of the app """
    post_action_move("Baldoon_01", 0, 0)
    # post_action_fight("Baldoon_01")
    # post_action_rest("Baldoon_01")
    # post_action_gathering("Baldoon_01")
    # post_action_unequip_item("Baldoon_01", "weapon")
    # post_action_crafting("Baldoon_01", "wooden_staff")
    # post_action_equip_item("Baldoon_01", "wooden_staff", "weapon")

    # while True:
    #     action = post_action_gathering("Baldoon_01")
    #     action = action['data']
        
    #     items = action['details']['items']

    #     for item in items:
    #         logger.info(f'Successfully gathered {item["quantity"]} {item["code"]}')

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
