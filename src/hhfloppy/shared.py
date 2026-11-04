import sys
import uuid


class UuidGenerator:

    @staticmethod
    def uuid7() -> uuid.UUID:
        if sys.version_info[:3] < (3, 14):
            try:
                from uuid_extensions import uuid7
                return uuid7()
            except ModuleNotFoundError:
                print("Please install uuid extensions:")
                print("pip install uuid7")
                exit(1)
        else:
            return uuid.uuid7()
