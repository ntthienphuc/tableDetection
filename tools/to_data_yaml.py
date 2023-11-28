import os
import yaml


def generate_dataset_files(
    train_folder,
        val_folder,
        test_folder,
        output_folder,
        class_names
):
    os.makedirs(output_folder, exist_ok=True)

    # Mapping from folder name to split name
    folder_to_split = {train_folder: "train",
                       val_folder: "val",
                       test_folder: "test"}

    # Generate .txt files with paths to images
    for folder, split in folder_to_split.items():
        output_file = os.path.join(output_folder,
                                   f"{split}.txt")

        with open(output_file, "w") as f:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.endswith(
                            ".jpg") or file.endswith(".png"):
                        file_path = os.path.join(root, file)
                        normalized_path = \
                            os.path.normpath(file_path).replace("\\", "/")
                        f.write(normalized_path + "\n")

    # Generate data.yaml file
    data_yaml = {
        "train": os.path.abspath(os.path.join(output_folder,
                                              "train.txt")),
        "val": os.path.abspath(os.path.join(output_folder,
                                            "val.txt")),
        "test": os.path.abspath(os.path.join(output_folder,
                                             "test.txt")),
        "nc": len(class_names),
        "names": class_names,
    }

    with open(os.path.join(output_folder,
                           "data.yaml"),
              "w") as outfile:
        yaml.dump(data_yaml,
                  outfile,
                  default_flow_style=False)
