from conftest import normalize_text
import pytest
# import importlib

# test_1_printed_messages:
# checks if the expected printed messages actually appear, but doesn't check for specific
# inputs or correct calculations.


@pytest.mark.parametrize("mock_inputs", [
    (["10"]),
], indirect=True)
def test_1_printed_messages( capsys, mock_inputs):
    
    expected_printed_statements = ["divided by 2 is"]

    # this calls the fixture, "mock_inputs" which replaces the normal input function
    # this also returns the captured inputs from the module, but 
    _ = mock_inputs

    # Import and reload the student's script
    import a2_solution_submitting_to_github
    # importlib.reload(a2_solution_submitting_to_github)

    # Capture the output from the print statements
    captured = capsys.readouterr().out

    # Normalize the captured output to remove spaces, punctuation, and symbols
    normalized_captured = normalize_text(captured)

    # Check that each required phrase is found in the normalized captured output
    for expected_phrase in expected_printed_statements:
        expected_phrase = normalize_text(expected_phrase)  # Ensure the expected phrase is normalized as well
        assert expected_phrase in normalized_captured, (
            f"\nExpected phrase '{expected_phrase}' wasn't not found in the output."
            f"\nBelow are all print statements. Make sure you double check your spelling: \n\n{normalized_captured}"
        )