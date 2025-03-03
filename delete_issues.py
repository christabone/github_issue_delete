import requests

# Replace with your personal access token (with 'repo' scope).
TOKEN = "ADD TOKEN HERE."

# Repository info
REPO_OWNER = "REPO ORGANIZATION"
REPO_NAME  = "REPO NAME"

# GraphQL endpoint and headers
API_URL = "https://api.github.com/graphql"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# GraphQL query to fetch open issues (in batches of 100)
FETCH_ISSUES_QUERY = """
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    issues(states: OPEN, first: 100, after: $after) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        id
        number
        title
      }
    }
  }
}
"""

# GraphQL mutation to delete an issue
DELETE_ISSUE_MUTATION = """
mutation($issueId: ID!) {
  deleteIssue(input: {issueId: $issueId}) {
    clientMutationId
  }
}
"""

def fetch_all_open_issues():
    """Fetch all open issues from the repository, returning a list of dicts."""
    all_issues = []
    after_cursor = None
    
    while True:
        variables = {
            "owner": REPO_OWNER,
            "name": REPO_NAME,
            "after": after_cursor
        }
        response = requests.post(
            API_URL,
            json={"query": FETCH_ISSUES_QUERY, "variables": variables},
            headers=HEADERS
        )
        if response.status_code != 200:
            raise Exception(f"Query failed: {response.status_code}\n{response.text}")
        
        data = response.json()
        issues_data = data["data"]["repository"]["issues"]
        
        for issue in issues_data["nodes"]:
            all_issues.append(issue)
        
        if issues_data["pageInfo"]["hasNextPage"]:
            after_cursor = issues_data["pageInfo"]["endCursor"]
        else:
            break
    
    return all_issues

def delete_issue(issue_id):
    """Delete an issue with the given GitHub GraphQL ID."""
    variables = {"issueId": issue_id}
    response = requests.post(
        API_URL,
        json={"query": DELETE_ISSUE_MUTATION, "variables": variables},
        headers=HEADERS
    )
    if response.status_code != 200:
        raise Exception(f"Delete mutation failed: {response.status_code}\n{response.text}")

def main():
    # 1. Fetch all open issues
    issues = fetch_all_open_issues()
    
    # 2. Print summary and ask for confirmation
    count = len(issues)
    if count == 0:
        print("No open issues found. Nothing to delete.")
        return
    
    print("Open issues found:")
    for issue in issues:
        print(f"  #{issue['number']} - {issue['title']}")
    print(f"\nTotal open issues: {count}")

    confirm = input("Are you sure you want to DELETE all these issues? [y/N]: ").strip().lower()
    if confirm not in ["y", "yes"]:
        print("Aborted.")
        return
    
    # 3. Proceed with deletion
    for issue in issues:
        print(f"Deleting issue #{issue['number']}: {issue['title']} (ID: {issue['id']})")
        delete_issue(issue['id'])
    
    print("\nAll specified issues have been deleted.")

if __name__ == "__main__":
    main()
