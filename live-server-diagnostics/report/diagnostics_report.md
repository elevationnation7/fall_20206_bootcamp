# Live Server Diagnostics Report

## Project Purpose
This project uses Python and Bash scripts to collect basic system and disk information.

## Python System Information
The system_info.py script reports:
- Date and time
- Operating system and release
- Machine architecture
- Processor information
- CPU count

## Shell Disk Snapshot
The disk_snapshot.sh script reports:
- Date and time
- Disk usage
- Current working directory

## Log File
The server.log file stores the output collected by both scripts.

## How to Run
Run these commands from the project root directory:

python live-server-diagnostics/python/system_info.py

bash live-server-diagnostics/shell/disk_snapshot.sh
