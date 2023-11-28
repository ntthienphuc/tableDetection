import logging
import subprocess
from tools import (
    xml_to_txt, split_train, merge_folder,
    to_data_yaml, delete
)

# Configure logging
logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Starting the data pipeline...")

    # Step 1: Convert XML annotations to YOLO format
    logging.info("Step 1: Converting XML annotations to YOLO format...")
    xml_to_txt.xml_to_yolo('data/train/xml', 'data/train/labels')
    xml_to_txt.xml_to_yolo('data/test/xml', 'data/test/labels')
    logging.info("Step 1 completed.")

    # Step 2: Split the training data
    logging.info("Step 2: Splitting the training data...")
    split_train.split_dataset(
        'data/train/images', 'data/train/image_split', 'data/val/image_split'
    )
    split_train.split_dataset(
        'data/train/labels', 'data/train/labels_split', 'data/val/labels_split'
    )
    logging.info("Step 2 completed.")

    # Step 3: Merge folders for datasets
    logging.info("Step 3: Merging folders...")
    merge_folder.merge_folders(
        'data/train/image_split', 'data/train/labels_split', 'data/train/final'
    )
    merge_folder.merge_folders(
        'data/val/image_split', 'data/val/labels_split', 'data/val/final'
    )
    merge_folder.merge_folders(
        'data/test/images', 'data/test/labels', 'data/test/final'
    )
    logging.info("Step 3 completed.")

    # Step 4: Generate data.yaml file for YOLO training
    logging.info("Step 4: Generating data.yaml file...")
    to_data_yaml.generate_dataset_files(
        'data/train/final', 'data/val/final', 'data/test/final',
        'data', ['box']
    )
    logging.info("Step 4 completed.")

    # Step 5: Delete unnecessary folders
    logging.info("Step 5: Delete unnecessary folders...")
    folders_to_delete = [
        'data/train/images', 'data/train/image_split',
        'data/train/labels', 'data/train/labels_split',
        'data/train/xml', 'data/test/xml',
        'data/test/images', 'data/test/labels',
        'data/val/image_split', 'data/val/labels_split'
    ]
    for folder in folders_to_delete:
        delete.delete_folder(folder)
    logging.info("Step 5 completed.")

    logging.info("Step 6: Running the training script...")
    train_command = [
        "python", 
        "source/yolov8/ultralytics/models/yolo/detect/train_main.py ",
        "--model ", "configs/model/yolov8.yaml",
        "--data ", " data/data.yaml ",
        "--epochs ", "5",
        "--batch ", "8"
    ]
    subprocess.run(train_command)
    logging.info("Step 6 completed.")

    logging.info("Step 7: Running the inference script...")
    predict_command = [
        "python ", 
        "source/yolov8/ultralytics/models/yolo/detect/train_main.py ",
        "--model ", "configs/model/yolov8.yaml ",
        "--data ", "data/data.yaml ",
        "--epochs ", "10 ",
        "--batch ", "8"
    ]
    subprocess.run(predict_command)
    logging.info("Step 7 completed.")

    logging.info("Step 8: Running Streamlit...")
    streamlit_command = [
        "python", " -m", " streamlit", " run",
        " source/streamlit.py"
    ]
    subprocess.run(streamlit_command)
    logging.info("Step 8 completed.")

    logging.info("Data pipeline completed successfully.")


if __name__ == "__main__":
    main()
