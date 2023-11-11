import os
import requests
import zipfile
import io
import shutil

class ApplicationService:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.repository_name = "spartan-framework"

    def is_valid_folder_name(self):
        return self.project_name.isidentifier() and not self.project_name[0].isdigit()

    def download_zip(self):
        release_url = f"https://github.com/nerdmonkey/{self.repository_name}/archive/refs/heads/main.zip"
        try:
            response = requests.get(release_url)
            response.raise_for_status()
            return io.BytesIO(response.content)
        except requests.exceptions.RequestException as err:
            print(f"Request error: {err}")
            return None

    def extract_zip(self, zip_data):
        temp_folder = "temp_extracted_folder"
        try:
            with zipfile.ZipFile(zip_data, "r") as zip_ref:
                zip_ref.extractall(temp_folder)
            return temp_folder
        except zipfile.BadZipFile:
            print("Error: The downloaded file is not a valid ZIP file.")
            return None

    def setup_project(self, temp_folder):
        extracted_files = os.listdir(temp_folder)
        if len(extracted_files) == 1 and os.path.isdir(os.path.join(temp_folder, extracted_files[0])):
            extracted_folder = os.path.join(temp_folder, extracted_files[0])
            os.rename(extracted_folder, self.project_name)
            shutil.rmtree(temp_folder)
            return True
        return False

    def create_app(self):
        if os.path.exists(self.project_name):
            print(f"The {self.project_name} folder already exists. Aborting.")
            return
        if not self.is_valid_folder_name():
            print(f"{self.project_name} is not a valid project name. Aborting.")
            return

        zip_data = self.download_zip()
        if zip_data:
            temp_folder = self.extract_zip(zip_data)
            if temp_folder and self.setup_project(temp_folder):
                print(f"Successfully setup the project to {self.project_name}.")
                print(f"\nTODO:")
                print(f"-----")
                print(f"cd {self.project_name}")
                print(f"pip install -r requirements.txt")
                print(f"copy the .env.example and name it as .env")
                print(f"uvicorn public.main:app --reload")
                print(f"or")
                print(f"artisan serve")
            else:
                print("Error: The ZIP file should contain a single top-level folder.")
