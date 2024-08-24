from dotenv import load_dotenv
import os
import streamlit as st
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
import git

# Load environment variables
load_dotenv()

# Retrieve IBM API credentials from environment variables
ibm_key = os.environ["WATSONX_APIKEY"]
ibm_project_id = os.environ.get('PROJECT_ID')
ibm_url = os.environ.get('WATSONX_URL')

parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 100,
    "min_new_tokens": 1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 1,
}

watsonx_llm = WatsonxLLM(
    model_id="ibm/granite-13b-instruct-v2",
    url=ibm_url,
    project_id=ibm_project_id,
    params=parameters,
)

# Streamlit UI
st.title('Git Conflict Resolver')
st.text('Merge branches and resolve conflicts using AI')

repo_path = st.text_input('Enter your local Git repository path')
branch_to_merge = st.text_input('Enter the branch to merge')

if st.button('Check PR Conflicts and Suggest Resolutions'):
    try:
        # Open the repository
        st.info("Opening the Git repository...")
        repo = git.Repo(repo_path)
        st.success("Git repository opened successfully.")

        # Check for uncommitted changes and stash them if present
        if repo.is_dirty():
            st.warning("You have uncommitted changes. Stashing them temporarily...")
            repo.git.stash('save', 'Auto stash before branch operations')
            st.success("Uncommitted changes stashed.")

        # Fetch all branches from remote
        st.info("Fetching the latest changes from the remote repository...")
        repo.remotes.origin.fetch()
        st.success("Fetched latest changes successfully.")

        # Get the current branch
        current_branch = repo.active_branch.name
        st.info(f"Current branch: {current_branch}")

        # Check if the branch exists locally, if not check it out from remote
        st.info(f"Ensuring branch '{branch_to_merge}' is available locally...")
        if branch_to_merge not in repo.heads:
            repo.git.checkout('-b', branch_to_merge, f'origin/{branch_to_merge}')
        else:
            repo.git.checkout(branch_to_merge)
        st.success(f"Branch '{branch_to_merge}' is now checked out locally.")

        # Switch back to the current branch
        st.info(f"Switching back to the current branch '{current_branch}'...")
        repo.git.checkout(current_branch)

        # Simulate the PR merge
        st.info(f"Attempting to merge branch '{branch_to_merge}' into '{current_branch}'...")
        try:
            # Perform the merge using the correct branch reference
            repo.git.merge(f'origin/{branch_to_merge}', '--no-commit')
            st.success(f"No conflicts detected. Branch '{branch_to_merge}' merged successfully into '{current_branch}'.")

            # If we stashed changes, attempt to pop them back
            if repo.git.stash('list'):
                st.info("Reapplying stashed changes...")
                try:
                    repo.git.stash('pop')
                    st.success("Stashed changes reapplied.")
                except git.exc.GitCommandError as stash_error:
                    st.warning(f"Could not reapply stashed changes due to conflicts. Manual resolution required: {stash_error}")

        except git.exc.GitCommandError as merge_error:
            if 'CONFLICT' in str(merge_error):
                st.warning('Merge conflicts detected!')

                # Get conflict details
                st.info("Identifying conflicts...")
                conflicts = repo.index.unmerged_blobs()
                conflict_suggestions = {}

                for path, blobs in conflicts.items():
                    conflict_text = ""
                    for stage, blob in blobs:
                        conflict_text += f"Stage {stage}:\n{blob.data_stream.read().decode()}\n\n"

                    # Use Watson model to generate conflict resolution suggestions
                    st.info(f"Generating conflict resolution suggestions for '{path}'...")
                    prompt = f"Here is a conflict in a file:\n{conflict_text}\nSuggest a way to resolve this conflict."
                    prompt_template = PromptTemplate(template=prompt)
                    suggestion = watsonx_llm(prompt_template.format())

                    conflict_suggestions[path] = suggestion

                # Display suggestions
                st.info("Displaying conflict resolution suggestions...")
                for file, suggestion in conflict_suggestions.items():
                    st.write(f"Conflict in file: {file}")
                    st.write(f"Suggestion: {suggestion}")
            else:
                raise merge_error

        # Final clean-up: Warn if conflicts still exist after popping stash
        if repo.is_dirty(untracked_files=True):
            st.warning("Unresolved conflicts or untracked files remain. Please resolve them manually.")

    except Exception as e:
        st.error(f'An error occurred: {e}')