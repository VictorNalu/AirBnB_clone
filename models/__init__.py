#!/usr/bin/python3
"""Package Initializer"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
