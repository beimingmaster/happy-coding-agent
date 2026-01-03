"""Git operations for fetching and managing source repositories."""

import subprocess
import urllib.request
from pathlib import Path
from typing import Optional


class GitOps:
    """Handle git operations for deployment."""

    def clone(
        self, url: str, target: str, branch: str = "main", depth: int = 1
    ) -> None:
        """Clone a repository with minimal history.

        Args:
            url: Repository URL to clone
            target: Target directory path
            branch: Branch to clone
            depth: Clone depth (1 for shallow clone)
        """
        cmd = [
            "git",
            "clone",
            "--depth",
            str(depth),
            "--branch",
            branch,
            "--single-branch",
            url,
            target,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Git clone failed: {result.stderr}")

    def get_commit_hash(self, repo_path: Optional[str]) -> str:
        """Get the current commit hash of a repository.

        Args:
            repo_path: Path to the git repository

        Returns:
            Commit hash or "unknown" if not available
        """
        if not repo_path:
            return "unknown"

        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return "unknown"

        return result.stdout.strip()

    def get_remote_commit(self, url: str, branch: str = "main") -> str:
        """Get the latest commit hash from remote without cloning.

        Args:
            url: Repository URL
            branch: Branch name

        Returns:
            Commit hash or "unknown" if not available
        """
        result = subprocess.run(
            ["git", "ls-remote", url, f"refs/heads/{branch}"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return "unknown"

        output = result.stdout.strip()
        if output:
            return output.split()[0]
        return "unknown"

    def is_git_repo(self, path: Path) -> bool:
        """Check if a directory is a git repository.

        Args:
            path: Directory path to check

        Returns:
            True if the directory is a git repository
        """
        return (path / ".git").exists()

    def fetch_raw_file(self, url: str, branch: str, file_path: str) -> str:
        """Fetch a single file from remote repository via raw URL.

        Args:
            url: Repository URL (GitHub)
            branch: Branch name
            file_path: Path to file within repository

        Returns:
            File contents as string
        """
        if "github.com" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com")
            raw_url = raw_url.replace(".git", "")
            full_url = f"{raw_url}/{branch}/{file_path}"

            with urllib.request.urlopen(full_url) as response:
                return response.read().decode("utf-8")

        raise NotImplementedError(
            "Only GitHub repositories are supported for single file fetch"
        )
