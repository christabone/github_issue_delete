Delete All Open GitHub Issues with GraphQL
==========================================

This Python script fetches and **permanently deletes** all open issues in a specified GitHub repository using GitHub's GraphQL API. It provides a summary of the issues found, including their titles, and asks for your confirmation before proceeding with deletion.

> **Warning**\
> This script uses the `deleteIssue` mutation, which **removes issues permanently**---there is no undo. Make sure you have backups or are absolutely certain you want to delete these issues.

* * * * *

Features
--------

-   Fetches all open issues (with pagination via GraphQL).
-   Displays each issue's **number** and **title**.
-   Shows the **count** of open issues.
-   Asks for user **confirmation** before deletion.
-   Permanently deletes all listed issues on confirmation.

* * * * *

Requirements
------------

1.  **Python 3.7+** recommended.
2.  A **Personal Access Token (PAT)** with the [`repo`](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) scope (or higher) to access and modify your repository.
3.  Sufficient permissions (admin/maintain) on the repository you are modifying.

* * * * *

Setup
-----

1.  **Clone or download** this repository (or copy the script into a file, e.g. `delete_issues.py`).
2.  **Install dependencies (if any)**:

    `pip install requests`

3.  **Open** the script in your text editor and update:
    -   `TOKEN`: Your GitHub personal access token.
    -   `REPO_OWNER`: The owner/organization of the repository.
    -   `REPO_NAME`: The name of the repository.

* * * * *

Usage
-----

1.  **Run** the script from your terminal:

    `python delete_issues.py`

2.  The script will:
    1.  Fetch all open issues in the specified repository.
    2.  List each issue by **number** and **title**.
    3.  Show the **total count** of open issues.
    4.  Prompt you:

        `Are you sure you want to DELETE all these issues? [y/N]:`

3.  **Confirm** by typing `y` (or `yes`). Any other input will abort the deletion.

**Example**:

```
Open issues found:
  #1 - Example Issue 1
  #2 - Example Issue 2
  ...
Total open issues: 2

Are you sure you want to DELETE all these issues? [y/N]: y
Deleting issue #1: Example Issue 1 (ID: MDU6SXNzdWUx)
Deleting issue #2: Example Issue 2 (ID: MDU6SXNzdWU2)

All specified issues have been deleted.
```


Troubleshooting & Tips
----------------------

-   **Authentication Failures**: Ensure your Personal Access Token (`TOKEN`) is correct and has the required scopes.
-   **Permissions**: You need admin (or similarly high-level) permissions on the repo to delete issues.
-   **No Issues Found**: If you get `No open issues found. Nothing to delete.`, your repository might have no open issues or your filters may need adjustment.
-   **Different Organization/Repo**: Update `REPO_OWNER` and `REPO_NAME` accordingly.