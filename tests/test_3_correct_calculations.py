from conftest import normalize_text, load_or_reload_module
import importlib
import sys

# checks if correct outputs are calculated from dividing input by 2.
# inputs are gathered from the inputs_and_expected_outputs fixture in conftest.py

def test_3_correct_calculations(capsys, mock_inputs, inputs_and_expected_outputs):
    for test_case in inputs_and_expected_outputs:
        test_input = test_case[0]
        expected_output = str(test_case[1])

        # Manually set the inputs for the test
        inputs = [test_input]
        
        # Call the fixture to mock_input() with the desired inputs
        _ = mock_inputs(inputs)

        # Load the module (if it is the first test run) or reload it into memory to reset global functions.
        load_or_reload_module()
        
        # Capture the output from the print statements
        captured = capsys.readouterr().out

        # Normalize the captured output to remove spaces, punctuation, and symbols
        normalized_captured = normalize_text(captured)

        assert expected_output in normalized_captured, (
            f"\nGiven {test_input} as an input, your output should include {expected_output}, but the test couldn't find that."
            f"\n\nBelow is all your printed output, ignoring punctuation and capitalization. Double check your output:" 
            f"\n\n{normalized_captured}\n\n"
        )