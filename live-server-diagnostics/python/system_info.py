import platform
import os
from datetime import datetime

print("=== Server System Information ===")
print(f"Date and Time: {datetime.now()}")
print(f"Operating System: {platform.system()}")
print(f"OS Release: {platform.release()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"CPU Count: {os.cpu_count()}")
