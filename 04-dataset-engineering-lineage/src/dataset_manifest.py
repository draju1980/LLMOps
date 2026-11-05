"""Module 04: Dataset Manifest & Lineage"""
import hashlib, json
from datetime import datetime
from pathlib import Path

class DatasetManifest:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.created_at = datetime.now().isoformat()
        self.files = {}
        self.lineage = []

    def add_file(self, path, purpose="train"):
        with open(path, 'rb') as f:
            content_hash = hashlib.sha256(f.read()).hexdigest()
        self.files[path] = {"hash": content_hash, "purpose": purpose}

    def save_manifest(self, output_path="manifest.json"):
        manifest = {
            "name": self.name,
            "version": self.version,
            "created_at": self.created_at,
            "files": self.files,
            "lineage": self.lineage
        }
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        return output_path
