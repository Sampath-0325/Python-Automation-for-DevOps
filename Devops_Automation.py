# devops_automation.py
import os
from datetime import datetime
import glob
import gzip
import shutil

# Configuration
log_file = "server.log"
archive_dir = "archive"
retention_count = 5  # Keep only the last 5 archived logs

def archive_log():
    """Archive the existing log file with timestamp and compress it."""
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    if os.path.exists(log_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archived_name = f"{archive_dir}/server_{timestamp}.log"
        os.rename(log_file, archived_name)
        print(f"Archived log as {archived_name}")

        # Compress the archived log
        with open(archived_name, 'rb') as f_in:
            with gzip.open(f"{archived_name}.gz", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        os.remove(archived_name)  # remove uncompressed log
        print(f"Compressed archived log: {archived_name}.gz")

def cleanup_old_archives():
    """Keep only the last N archived logs, delete older ones."""
    archived_logs = sorted(glob.glob(f"{archive_dir}/server_*.log.gz"))
    if len(archived_logs) > retention_count:
        old_logs = archived_logs[:-retention_count]
        for f in old_logs:
            os.remove(f)
            print(f"Deleted old archived log: {f}")

def generate_error_summary():
    """Scan the new log for ERROR/WARNING lines and save a summary."""
    if not os.path.exists(log_file):
        open(log_file, "w").close()

    error_lines = []
    with open(log_file, "r") as f:
        for line in f:
            if "ERROR" in line or "Warning" in line:
                error_lines.append(line.strip())

    if error_lines:
        summary_file = f"{archive_dir}/error_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(summary_file, "w") as f:
            f.write("\n".join(error_lines))
        print(f"Generated error summary: {summary_file}")
    else:
        print("No errors or warnings found in the log.")

def create_new_log():
    """Create a new empty log file for future logging."""
    open(log_file, "w").close()
    print("Created new empty server.log")

if __name__ == "__main__":
    archive_log()
    cleanup_old_archives()
    generate_error_summary()
    create_new_log()
