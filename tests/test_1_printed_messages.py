from conftest import normalize_text
import pytest
# import importlib

# test_1_printed_messages:
# checks if the expected printed messages actually appear, but doesn't check for specific
# inputs or correct calculations.

def test_1_printed_messages(capsys, mock_inputs):
    
    # Manually set the inputs for the test
    inputs = ["10"]
    
    # Call the fixture to mock input() with the desired inputs
    _ = mock_inputs(inputs)

    # Import the student's script (don't reload it)
    import a2_submitting_to_github

    # Capture the output from the print statements
    captured = capsys.readouterr().out

    # Normalize the captured output to remove spaces, punctuation, and symbols
    normalized_captured = normalize_text(captured)

    # Expected phrases in the print output
    expected_printed_statements = ["divided by 2 is"]

    # Check that each required phrase is found in the normalized captured output
    for expected_phrase in expected_printed_statements:
        expected_phrase = normalize_text(expected_phrase)  # Ensure the expected phrase is normalized as well
        assert expected_phrase in normalized_captured, (
            f"\nExpected phrase:\n\n\t'{expected_phrase}'\n\nwasn't printed out."
            f"\n\nBelow are all printed statements from your code. Make sure to double check your spelling: \n\n{normalized_captured}\n\n"
        )