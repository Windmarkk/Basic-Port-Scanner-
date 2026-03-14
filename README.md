# Basic TCP Port Scanner

A straightforward, interactive Python script designed to perform TCP connect scans on target IP addresses or hostnames. This tool is built to assist in fundamental network reconnaissance, allowing users to identify open ports and available services on a specific machine.

## Features

* **Interactive Interface:** Simple command-line menu for easy navigation.
* **Single Port Scan:** Quickly verify the connection status of a specific port.
* **Range Scan:** Sweep a defined range of ports sequentially to map out a target's open attack surface.
* **Robust Exception Handling:** Gracefully catches and handles common socket errors, including timeouts, connection refusals, and unresolved DNS queries.
* **Performance Tracking:** Calculates and outputs the total execution time when running bulk port scans.
* **Multithreading** Improved scan speed with multithreading.

## Prerequisites

This script is built using Python's standard library. No external dependencies or packages (like `pip install`) are required.
* Python 3.x

## Installation

Simply clone the repo, and execute the python code.

```bash
# Clone the repo
git clone https://github.com/Windmarkk/Basic-Port-Scanner-.git

# Make the script executable (for linux users)
chmod +x socketpython.py
```
## Usage

```bash
#Run with Python
python3 socketpython.py
```
## What will be added
* **Service & Banner Grabbing** To identify specific services used on open ports
* **Result Exporting** To export scan results to files.
