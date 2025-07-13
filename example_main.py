#!/usr/bin/env python3
"""
Main entry point for your Dify plugin.
This file is used for local testing and should not be modified.
"""

import sys
from pathlib import Path

# Add the current directory to the Python path
sys.path.insert(0, str(Path(__file__).parent))

from dify_plugin.main import main

if __name__ == "__main__":
    main() 