
import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_directory_abs,file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs,target_dir]) == working_directory_abs


        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        # if error occur change this one first
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        

        if not file_path.endswith('py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python",target_dir]  

        if args:
            command.extend(args)

        result = subprocess.run(
                command,
                cwd=working_directory_abs,
                capture_output=True,
                text=True,
                timeout=30
            )
        
        output = ""

        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"

        if result.stdout:
            output += f"STDOUT:\n{result.stdout}"

        if result.stderr:
            output += f"STDERR:\n{result.stderr}"

        if not result.stdout and not result.stderr:
            output += "No output produced"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(

    name="run_python_file",
    description="Executes a Python script located in the working directory. Optionally accepts command line arguments. Returns the script's standard output and any error messages produced during execution.",

    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Optional command line arguments to pass to the Python script"
            )
        },
        required=['file_path']
    )

)