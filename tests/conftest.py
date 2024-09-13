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

# this replaces the built in input() function using monkeypatch. Can be called by any test.
# it needs to be called for any assignment that uses the input() function, as that will cause
# any test to crash.
@pytest.fixture
def mock_inputs(monkeypatch):
    # Create a function to set inputs
    def _mock_inputs(simulated_inputs):
        input_iter = iter(simulated_inputs)
        captured_prompts = []

        # Define the mock input function
        def mock_input(prompt):
            captured_prompts.append(prompt)
            return next(input_iter, '') # grabs the next input, or a blank string if empty

        # Use monkeypatch to replace the built-in input() with the mock input function
        monkeypatch.setattr('builtins.input', mock_input)

        return captured_prompts

    return _mock_inputs

# Note that GitHub Classroom currently has an error where it cannot process parametrize in pytest.
# if this is ever fixed, I can use the below syntax on any test.
'''
@pytest.mark.parametrize("mock_inputs", [
    (["Example input response 1", "Example input response 2"]),
    (["Another input 1", "Another input 2"]),
], indirect=True)

'''

