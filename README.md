
# AnacondaScan
AnacondaScan is a Python-based multi-threaded port scanner that identifies open TCP ports and their services on a target IP, featuring colorful terminal output and ASCII art.



## Features

- Scans 65,535 TCP ports.
- Detects services on open ports.
- Multi-threading for faster scans.
- Colorful terminal output with `colorama`.
- Includes an ASCII art banner.

---

## Prerequisites

Ensure Python 3.8+ is installed. Install dependencies with:

```bash
pip install colorama rich
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AnacondaScan.git
   cd AnacondaScan
   ```
2. Run the script:
   ```bash
   python port_scanner.py
   ```

---

## Usage

1. Run the script:
   ```bash
   python port_scanner.py
   ```
2. Enter the target IP address.
3. View open ports and their services.

Example:

```
[12:00:00] [>] | Ip -> 192.168.1.1
[12:00:01] [~] | Scanning...
[12:00:02] [+] | Port: 80 Status: Open Service: http
[12:00:05] [>] | FINISHED -> Discovered 1 ports! finished scanning in 5.0 seconds
```

---

## Limitations

- Only scans TCP ports.
- Full scans may take time depending on system performance.

---
