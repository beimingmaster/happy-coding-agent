"""Configuration constants for HCA CLI."""

from pathlib import Path

# Default source repository
DEFAULT_SOURCE = "https://github.com/notedit/happy-coding-agent"
DEFAULT_BRANCH = "main"

# Metadata directory and file names
METADATA_DIR = ".hca"
METADATA_FILE = "metadata.json"

# Components that can be deployed
COMPONENTS = ["agents", "commands", "skills"]

# Claude directory name
CLAUDE_DIR = ".claude"


def get_claude_dir(project_path: Path) -> Path:
    """Get the .claude directory path for a project."""
    return project_path / CLAUDE_DIR


def get_metadata_path(project_path: Path) -> Path:
    """Get the metadata file path for a project."""
    return get_claude_dir(project_path) / METADATA_DIR / METADATA_FILE
