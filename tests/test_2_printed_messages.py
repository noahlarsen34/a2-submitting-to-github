from conftest import normalize_text, load_or_reload_module
import importlib
import sys

# checks if the expected printed messages actually appear, but doesn't check for specific
# inputs or correct calculations.

def test_2_printed_messages(capsys, mock_inputs):
    
    # Manually set the inputs for the test
    inputs = ["10"]
    
    # Call the fixture to mock input() with the desired inputs
    _ = mock_inputs(inputs)

    # Load the module (if it is the first test run) or reload it into memory to reset global functions.
    load_or_reload_module()

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
            f"\n\nBelow are all printed statements from your code, ignoring punctuation and capitalization. Make sure to double check your spelling:" 
            f"\n\n{normalized_captured}\n\n"
        )