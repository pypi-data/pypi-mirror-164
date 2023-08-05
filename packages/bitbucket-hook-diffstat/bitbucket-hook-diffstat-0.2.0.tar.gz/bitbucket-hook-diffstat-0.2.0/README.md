# Bitbucket hook diffstat

## Overview

Bitbucket push webhook handler to generate a list of files changed on a push.

It processes branch updates, and the branch creates events and extracts the file paths of the files whose content was changed in that event, including the removal or creation of the file itself.
In the case of a branch update event, it gets the changeset between the current HEAD of the branch and the previous HEAD of that branch.
In case the branch is created, it gets the changeset between the current HEAD of the branch and the HEAD of the main branch of the repository.

## Usage
```python
from bitbucket_hook_diffstat import process_branch_events

process_branch_events(
    push_payload, repo_owner, repo_name, bitbucket_user, bitbucket_password
)
```
Where `bitbucket_password` is an "app password" and `bitbucket_user` is available as "Username" in Bitbucket profile settings. This user should be authorized to do Repositories Read.
`push_payload` is a repository push event - https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/#Push
`repo_owner` and `repo_name` one can retrieve from the repository URL https://bitbucket.org/`repo_owner`/`repo_name` 