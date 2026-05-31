import mmap
import os
from typing import BinaryIO

class BinaryPatcher:
    """Low-level binary patching utilities for DaVinci Resolve."""

    @staticmethod
    def patch_file(file_path: str, offset: int, new_bytes: bytes) -> bool:
        """Patch a binary file at a specific offset."""
        try:
            with open(file_path, "r+b") as f:
                with mmap.mmap(f.fileno(), 0) as mm:
                    mm[offset:offset+len(new_bytes)] = new_bytes
            return True
        except (IOError, ValueError):
            return False