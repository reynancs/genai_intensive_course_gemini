import json
import os
import grpc
try:
    import grpc_status
except ImportError:
    grpc_status = None

# Path to the notebook file
notebook_path = 'ai_agent_stocks_insights.ipynb'

# Load the notebook
with open(notebook_path, 'r', encoding='utf-8') as file:
    notebook = json.load(file)

# Find the first code cell (the one with the imports)
for i, cell in enumerate(notebook['cells']):
    if cell.get('cell_type') == 'code' and 'from google import genai' in cell.get('source', [''])[0]:
        # Add the grpc_status import
        current_source = cell['source']
        
        # Prepare new import code
        new_imports = 'from google import genai\nfrom google.genai import types\nimport requests\nimport os\nfrom dotenv import load_dotenv\nimport grpc\n\n# Try to import grpc_status, set to None if not available\ntry:\n    import grpc_status\nexcept ImportError:\n    grpc_status = None\n\nfrom IPython.display import Markdown\n'
        
        # Replace the imports section
        notebook['cells'][i]['source'] = new_imports.split('\n')
        break

# Save the modified notebook
with open(notebook_path, 'w', encoding='utf-8') as file:
    json.dump(notebook, file, indent=1)

print(f"Notebook '{notebook_path}' has been updated with the grpc_status import.") 