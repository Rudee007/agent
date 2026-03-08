import os

from google.genai import types
def write_file(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)

        target_directory = os.path.normpath(os.path.join(working_directory_abs,file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs,target_directory]) == working_directory_abs


        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_directory):
            return f'Error: Cannot write to "{file_path}" as it is a directory'


        with open(target_directory, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
 



schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Writes content to a file in the working directory. Creates the file if it does not exist and overwrites it if it does.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content that should be written into the file"
            )
        },
        required=["file_path", "content"]
    )
)