#!/usr/bin/python3
"""The __init__ module contains the variable storage."""

from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
