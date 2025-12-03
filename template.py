import os
from pathlib import Path

project_name = "Llama3-Medical-Finetune"

list_of_files = [
    f"{project_name}/data/medical_instructions.json",
    f"{project_name}/notebooks/01_SFT_Training.ipynb",
    f"{project_name}/notebooks/02_DPO_Alignment.ipynb",
    f"{project_name}/notebooks/03_GGUF_Quantization.ipynb",
    f"{project_name}/models/.gitkeep",
    f"{project_name}/src/app.py",
    f"{project_name}/src/__init__.py",
    #f"{project_name}/.gitignore",
    #f"{project_name}/README.md",
   # f"{project_name}/requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # 1. Create Directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # 2. Create Empty File
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # Creates an empty file
            
print(f"✅ Project structure for '{project_name}' created!")