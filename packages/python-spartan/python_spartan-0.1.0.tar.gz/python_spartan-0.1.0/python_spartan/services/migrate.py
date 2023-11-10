import os
import shutil
from alembic import command

class MigrateService:
    def __init__(self, alembic_cfg):
        self.alembic_cfg = alembic_cfg

    def migrate_create(self, message=""):
        command.revision(self.alembic_cfg, message=message)
        print("Migration created")

    def migrate_downgrade(self):
        command.downgrade(self.alembic_cfg, "base")
        print("Migration downgraded")

    def migrate_upgrade(self):
        command.upgrade(self.alembic_cfg, "head")
        print("Migration upgraded")

    def migrate_refresh(self):
        command.downgrade(self.alembic_cfg, "base")
        command.upgrade(self.alembic_cfg, "head")
        print("Refresh all tables")
