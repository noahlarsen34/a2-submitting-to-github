from conftest import normalize_text, load_or_reload_module
import importlib
import sys

# checks if the input prompts (from using input()) contain the expected prompts.

def test_1_input_prompts(mock_inputs):
    
    # Manually set the inputs for the test
    inputs = ["10"]
    
    # Call the fixture to mock input() with the desired inputs
    captured_input_prompts = mock_inputs(inputs)

    load_or_reload_module()

    # Normalize the captured input prompts to remove spaces, punctuation, and symbols
    normalized_captured_input_prompts = [normalize_text(captured_prompt) for captured_prompt in captured_input_prompts]
    normalized_captured_input_prompts = ' '.join(normalized_captured_input_prompts)

    # Expected phrases in the print output
    expected_input_prompts = ["Please enter a whole number: "]

    # Check that each required phrase is found in the normalized captured output
    for expected_phrase in expected_input_prompts:
        expected_phrase = normalize_text(expected_phrase)  # Ensure the expected phrase is normalized as well
        assert expected_phrase in normalized_captured_input_prompts, (
            f"\nExpected input prompt:\n\n\t'{expected_phrase}'\n\nwasn't displayed from the input() function."
            f"\n\nBelow are all the input prompts from your code, ignoring punctuation and capitalization. Make sure to double check your spelling: " 
            f"\n\n{normalized_captured_input_prompts}\n\n"
        )