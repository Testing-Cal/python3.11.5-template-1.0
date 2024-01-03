from main import greet  # Import the greet function from your module
from unittest.mock import patch

# Assuming you're testing a Flask route
def test_greet_render_template_called():
	with patch('main.render_template') as mock_render_template:
		# Call the function
		greet()

		# Assert that render_template was called with 'index.html'
		mock_render_template.assert_called_once_with('index.html')