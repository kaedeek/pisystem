from VersaLog import *

import argparse
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

def package_list():
    result = subprocess.run(["pip", "list", "--outdated", "--format=json"], capture_output=True, text=True)
    packages = json.loads(result.stdout)

    print(f"\n📝 Update Package List")
    print("=" * 45)
    for pkg in packages:
        print(pkg["name"])
    print("=" * 45)

def main():
    parser = argparse.ArgumentParser(
        prog="Pyn",
        description="pynexusx - A tool for updating and managing PyPI packages.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--update", action="store_true", help="Update all packages")
    group.add_argument("--list", action="store_true", help="List outdated packages")


    args = parser.parse_args()

    if args.update:
        try:
            update_package()
        except Exception as e:
            logger.error(f"Update error: {e}")

    elif args.list:
        try:
            package_list()
        except Exception as e:
            logger.error(f"List error: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()