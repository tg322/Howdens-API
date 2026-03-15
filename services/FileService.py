from pathlib import Path
from typing import List
import uuid

from fastapi import HTTPException, UploadFile

from schemas.files import UploadedFile


class FileService:

    async def store_files(self, base_path:str, folder_name:str, files:List[UploadFile]) -> List[UploadedFile]:
        
        # Clean the folder name, remove illegal characters.
        safe_folder_name = folder_name.replace("/", "_")

        # Clean the base folder name, remove illegal characters.
        safe_base_path = base_path.replace("/", "_")

        # Create a path object from the base_path folder name
        base_dir = Path(safe_base_path)

        # If the directory does not exist, create it.
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # Create the path to the folder_name directory
        folder_dir = base_dir / safe_folder_name

        # If the directory does not exist, create it.
        folder_dir.mkdir(parents=True, exist_ok=True)

        # Array of saved files file paths.
        saved_files = []

        # Begin looping through each file.
        for file in files:
            # If for whatever reason the file does not have a name, throw error.
            if not file.filename:
                raise HTTPException(status_code=400, detail="One of the files does not have a name")
            
            # Clean the filename, remove illegal characters.
            safe_filename = file.filename.replace("/", "_")

            # Ensure that the file name is unique, slap a uuid at the start.
            unique_file_name = f"{uuid.uuid4()}_{safe_filename}"
            # directory to save file
            file_path = folder_dir / unique_file_name

            # Begin reading the file
            contents = await file.read()

            #Open the directory we intend to save the file in
            with file_path.open("wb") as buffer:
                # Wite the file contents to the directory
                buffer.write(contents)

            # Add the UploadedFile object of saved file to saved_files array
            saved_files.append(UploadedFile(file_path=str(file_path), file_name=unique_file_name))

        # Return list of file paths.
        return saved_files