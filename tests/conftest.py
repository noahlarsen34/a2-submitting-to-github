import pytest
import re


# Removes extra spaces, punctuation, and makes the text lowercase.
# Also normalizes any sequences of multiple spaces into a single space.
def normalize_text(text):
    lines = text.splitlines()  # Split the text into lines
    cleaned_lines = [re.sub(r'[^\w\s]', '', line).strip().lower() for line in lines if line.strip()]
    normalized_text = ' '.join(cleaned_lines)  # Join all cleaned lines into a single string
    normalized_text = re.sub(r'\s+', ' ', normalized_text)  # Replace multiple spaces/tabs with a single space
    return normalized_text

@pytest.fixture
def mock_inputs(monkeypatch, request):
    """
    A fixture that mocks the built-in input() function to return a sequence of predefined inputs.
    The inputs are passed in as parameters to the test function using pytest.mark.parametrize.
    """
    # Get the simulated inputs passed from pytest.mark.parametrize via request.param
    simulated_inputs = request.param
    input_iter = iter(simulated_inputs)
    
    # Create a list to store the captured input prompts from the file being tested
    captured_prompts = []

    # Define the mock input function
    def mock_input(prompt):
        captured_prompts.append(prompt)
        return next(input_iter, '') # grabs the next input, or a blank string if empty
    
    # Use monkeypatch to replace the built-in input() with the mock input function
    monkeypatch.setattr('builtins.input', mock_input)
    
    # Return the expected input prompts for the test to validate them
    return captured_prompts

# to use the above on any test, use the structure below
# because indirect=True the parameters will be passed directly to
# the mock_inputs fixture above, rather than directly to the test that uses it.

'''
@pytest.mark.parametrize("mock_inputs", [
    (["Example input response 1", "Example input response 2"]),
    (["Another input 1", "Another input 2"]),
], indirect=True)

'''

