from VersaLog import *

import json
import subprocess

logger = VersaLog(enum="detailed", tag="Pisystem", show_tag=True, all_save=False, save_levels=[])

def update_package():
    result = subprocess.run(["pip", "list", "--outdated", "--format=json"], capture_output=True, text=True)
    packages = json.loads(result.stdout)

    if not packages:
        logger.warning("No outdated packages found :(")
        return
    
    def upgrade_package(pip_name):
        logger.info(f"Updating {pip_name}...")
        if pip_name.lower() == "pip":
            subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], check=True)
        else:
            subprocess.run(["pip", "install", "--upgrade", pip_name], check=True)

    for pip in packages:
        upgrade_package(pip["name"])
    logger.info("All packages updated successfully :)")

if __name__ == "__main__":
    update_package()