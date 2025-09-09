import os
from datetime import datetime

# File to manage
log_file = "server.log"
archive_dir = "archive"

def manage_logs():
    # Step 1: Create archive folder if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Step 2: Check if log file exists and archive it
    if os.path.exists(log_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"{archive_dir}/server_{timestamp}.log"
        os.rename(log_file, new_name)
        print(f"Archived log as {new_name}")

    # Step 3: Create a new empty log file
    open(log_file, "w").close()
    print("Created new empty server.log")

if __name__ == "__main__":
    manage_logs()
