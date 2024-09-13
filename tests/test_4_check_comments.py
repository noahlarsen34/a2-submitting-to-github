import re
import pytest

def test_4_check_comments():
    # Open and read the student's script as a string
    with open("a2_solution_submitting_to_github.py", "r") as file:
        script_content = file.read()

    # Regex to match single-line comments (#) and multi-line comments (''' ''' or """ """)
    comment_pattern = r"(#.*)|('''[\s\S]*?'''|\"\"\"[\s\S]*?\"\"\")"

    # Find all matches for comments
    comments = re.findall(comment_pattern, script_content)

    # Count total number of comments
    num_comments = len(comments)

    # Ensure there are at least 3 comments
    assert num_comments >= 3, f"\n\nNot enough comments found. You need at least 3. Only {num_comments} comment(s) detected."