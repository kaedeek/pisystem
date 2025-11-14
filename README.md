## What is pynexusx?

[![PyPI version](https://badge.fury.io/py/pynexusx.svg)](https://badge.fury.io/py/pynexusx)
[![Downloads](https://pepy.tech/badge/pynexusx)](https://pepy.tech/project/pynexusx)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Discord](https://img.shields.io/badge/Discord-Support%20Server-7289DA?style=flat&logo=discord)](https://discord.gg/cY8QxHN5)

`pynexusx` is a CLI tool that allows you to easily update all installed Python packages to their latest versions.

---

## Features

- Current: Update all installed packages to the latest version
- Planned features:
  - Update specific packages only
  - Version pinning and automatic scheduled updates

---

## Installation

```bash
pip install pynexusx
```

## Usage

### Update all packages

```bash
Pyn --update
```

```bash
[2025-11-15 03:43:54][INFO][Pisystem] : Updating certifi...
Requirement already satisfied: certifi in c:\users\***\appdata\local\programs\python\python311\lib\site-packages (2025.10.5)
Collecting certifi
  Downloading certifi-2025.11.12-py3-none-any.whl.metadata (2.5 kB)
Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
Installing collected packages: certifi
  Attempting uninstall: certifi
    Found existing installation: certifi 2025.10.5
    Uninstalling certifi-2025.10.5:
      Successfully uninstalled certifi-2025.10.5
Successfully installed certifi-2025.11.12
```

### List outdated packages

```bash
Pyn --list
```

```bash
📝 Update Package List
=============================================
certifi
prettytable
yt-dlp
=============================================
```