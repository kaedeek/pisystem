import subprocess
import json

def update_package():
    result = subprocess.run(["pip", "list", "--outdated", "--format=json"], capture_output=True, text=True)
    packages = json.loads(result.stdout)

    if not packages:
        print("[Notify]  No outdated packages found :(")
        return
    
    def upgrade_package(pip_name):
        print(f"[Notify]  Updating {pip_name}...")
        subprocess.run(["pip", "install", "--upgrade", pip_name], check=True)

    for pip in packages:
        upgrade_package(pip["name"])
    print("[Notify]  All packages updated successfully :)")

if __name__ == "__main__":
    update_package()