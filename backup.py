import shutil
import os
from datetime import datetime


class BackupTool:
    def __init__(self):
        self.source = "source"
        self.backup_dir = "backups"
    

    def backup(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        folder_name = f"backup_{timestamp}"
        target_path = os.path.join(self.backup_dir, folder_name)

        os.makedirs(self.backup_dir, exist_ok=True)
        