#!/usr/bin/env
import sys
from git_filter_repo import FilterRepo

def main():
    def rewrite_commit(commit):
        # Only change author/committer name/email
        commit.author_name = b"manishakhatri-11"
        commit.author_email = b"12345678+manishakhatri-11@users.noreply.github.com"
        commit.committer_name = b"manishakhatri-11"
        commit.committer_email = b"12345678+manishakhatri-11@users.noreply.github.com"

    repo = FilterRepo()
    repo.add_commit_callback(rewrite_commit)
    repo.run()

if __name__ == "__main__":
    main()
