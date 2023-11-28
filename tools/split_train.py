import os
import shutil
from sklearn.model_selection import train_test_split


def split_dataset(
    data_folder,
        train_output_folder,
        val_output_folder,
        test_size=0.2,
        random_state=42
):
    os.makedirs(train_output_folder, exist_ok=True)
    os.makedirs(val_output_folder, exist_ok=True)

    # Get list of files in the data folder
    files = [
        f
        for f in os.listdir(data_folder)
        if os.path.isfile(os.path.join(data_folder, f))
    ]

    # Split files into training and validation sets
    train_files, val_files = train_test_split(
        files, test_size=test_size, random_state=random_state
    )

    # Copy files into respective folders
    for f in train_files:
        shutil.copy(os.path.join(data_folder, f),
                    os.path.join(train_output_folder, f))

    for f in val_files:
        shutil.copy(os.path.join(data_folder, f),
                    os.path.join(val_output_folder, f))
