import streamlit as st
from commit_message_generator import create_commit_message
from pull_request_summarizer import fetch_pull_request_data, summarize_pull_request
from versioning import update_version

def main():
    st.title("Code Workflow Automation")

    # Section for Commit Message Generation
    st.header("Generate Commit Message")
    repo_path_commit = st.text_input("Repository Path for Commit Message:")
    if st.button("Generate Commit Message"):
        if repo_path_commit:
            commit_message = create_commit_message(repo_path_commit)
            st.write(f"Generated Commit Message: {commit_message}")
        else:
            st.error("Please provide a repository path.")

    # Section for Pull Request Summarization
    st.header("Summarize Pull Request")
    repo_owner = st.text_input("Repository Owner:")
    repo_name = st.text_input("Repository Name:")
    pr_number = st.text_input("Pull Request Number:")
    github_token = st.text_input("GitHub Token:", type="password")
    if st.button("Summarize Pull Request"):
        if repo_owner and repo_name and pr_number and github_token:
            pr_data = fetch_pull_request_data(repo_owner, repo_name, pr_number, github_token)
            summary = summarize_pull_request(pr_data)
            st.write(f"Pull Request Summary: {summary}")
        else:
            st.error("Please provide all required fields.")

    # Section for Versioning
    st.header("Update Version")
    repo_path_version = st.text_input("Repository Path for Version Update:")
    if st.button("Update Version"):
        if repo_path_version:
            new_version = update_version(repo_path_version)
            st.write(f"New Version: {new_version}")
        else:
            st.error("Please provide a repository path.")

if __name__ == "__main__":
    main()
