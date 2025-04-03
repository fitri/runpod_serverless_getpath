import os
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/load', methods=['GET'])
def list_directory_contents():
    """
    Handles GET requests to /load.
    Lists the contents of the current working directory inside the container.
    """
    try:
        # Get the current working directory within the container
        current_directory = os.getcwd()

        # List all files and directories in the current directory
        contents = os.listdir(current_directory)

        # Return the directory path and its contents as JSON
        return jsonify({
            'directory': current_directory,
            'contents': contents,
            'message': f'Successfully listed contents of {current_directory}'
        }), 200 # HTTP status code 200 OK

    except FileNotFoundError:
        return jsonify({
            'error': f'Directory not found: {current_directory}'
        }), 404 # HTTP status code 404 Not Found
    except PermissionError:
        return jsonify({
            'error': f'Permission denied to access directory: {current_directory}'
        }), 403 # HTTP status code 403 Forbidden
    except Exception as e:
        # Catch any other potential errors
        return jsonify({
            'error': f'An unexpected error occurred: {str(e)}'
        }), 500 # HTTP status code 500 Internal Server Error

# Run the Flask app
if __name__ == '__main__':
    # Run on port 5000 and make it accessible from outside the container ('0.0.0.0')
    app.run(host='0.0.0.0', port=5000, debug=False) # Turn debug=False for production/simple examples
