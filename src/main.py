from colorama import init, Fore, Style

import subprocess
import json
import logging

init(autoreset=True)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def update_package():
    result = subprocess.run(["pip", "list", "--outdated", "--format=json"], capture_output=True, text=True)
    packages = json.loads(result.stdout)

    if not packages:
        logging.warning(Style.BRIGHT + Fore.YELLOW  + "No outdated packages found :(")
        return
    
    def upgrade_package(pip_name):
        logger.info(Fore.GREEN + f"Updating {pip_name}...")
        subprocess.run(["pip", "install", "--upgrade", pip_name], check=True)

    for pip in packages:
        upgrade_package(pip["name"])
    logger.info(Fore.GREEN + "All packages updated successfully :)")

if __name__ == "__main__":
    update_package()