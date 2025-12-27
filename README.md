# 🛡️ System Watchdog (Sentry)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

A real-time system monitoring tool designed to detect and alert on new unauthorized processes running in the background.

---

### 📝 Description
**System Watchdog** (internally codenamed "Sentry") is a security script that creates a snapshot of the currently running processes on a Windows system. It continuously monitors the background activity and triggers an immediate alert via the console whenever a new process is spawned.

This tool is useful for identifying hidden background tasks, potential malware execution, or simply monitoring system activity.

### ✨ Features
* **Baseline Snapshot:** Captures the state of the system upon startup.
* **Real-Time Monitoring:** Scans for changes every 3 seconds.
* **Instant Alerts:** Logs the name and timestamp of any new process detected.
* **Lightweight:** Built using standard Windows system calls (`tasklist`) with zero external dependencies.

### 🚀 How to Run

#### Option 1: Run via Python
1. Ensure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run the script:
   ```bash
   python sentry.py
