# Python Automation for DevOps

## Overview
This project automates **repetitive DevOps tasks**, specifically **managing server logs**, using Python.  
The script archives old logs, compresses them, enforces a retention policy, and generates error/warning summaries automatically.  
This ensures efficient log management and saves server storage space.

---

## Features
- **Automatic Log Archiving**: Moves existing `server.log` to an `archive/` folder with a timestamp.  
- **Compression**: Archived logs are compressed (`.gz`) to save storage.  
- **Retention Policy**: Keeps only the last N archived logs (default: 5); older logs are deleted automatically.  
- **Error Summary**: Scans logs for `ERROR` or `Warning` messages and generates a summary file.  
- **New Log Creation**: Automatically creates a fresh `server.log` after archiving.  
- **Version Controlled**: Fully tracked using Git.

---

## Prerequisites
- Python 3.10+ installed
- Git installed (for version control)

---

## Flowchart: Python Server Log Automation

           +----------------+
           |   server.log   |
           +----------------+
                    |
                    v
        +----------------------+
        | Check if log exists  |
        +----------------------+
                    |
          +---------+---------+
          |                   |
          v                   v
   Log exists?             Log missing?
      Yes                     No
      |                        |
      v                        v
+----------------+         +-----------------+
| Move log to    |         | Create new      |
| archive/       |         | empty server.log|
| with timestamp |         +-----------------+
+----------------+
      |
      v
+----------------+
| Compress log   |
+----------------+
      |
      v
+----------------+
| Clean old logs |
| (Retention)    |
+----------------+
      |
      v
+----------------+
| Generate Error |
| Summary        |
+----------------+
      |
      v
+----------------+
| Create new     |
| server.log     |
+----------------+


## Installation
1. Clone the repository:
```bash
git clone https://github.com/Sampath-0325/Python-Automation-for-DevOps.git
cd Python-Automation-for-DevOps
