import shutil
import os


def delete_folder(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"The folder '{folder_path}' "
                  f"has been deleted successfully.")
        else:
            print(f"The folder '{folder_path}' "
                  f"does not exist.")
    except Exception as e:
        print(f"An error occurred while "
              f"deleting the folder: {e}")


# Usage example:
# delete_folder('path/to/your/folder')
