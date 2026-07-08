import subprocess
import tempfile
import os


def clone_repository(repo_url: str):
    temp_directory = tempfile.mkdtemp()

    subprocess.run(
        ["git", "clone", repo_url, temp_directory],
        check=True
    )

    return temp_directory