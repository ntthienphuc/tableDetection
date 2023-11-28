
# Document Table Recognition Using YOLOv8

## Introduction
This initiative focuses on creating a reliable system for detecting tables in documents, leveraging the potential of YOLOv8 model and utilizing the rich WTW Dataset. The primary model in focus is YOLOv8 due to its superior performance, with YOLOv7 being an optional consideration.

## Highlights
- **Innovative Approach**: Integration of the state-of-the-art YOLOv8 model for superior table detection.
- **Rich Dataset**: Application of the extensive WTW Dataset for model training and testing.
- **Ease of Use**: Comprehensive setup and user manual for ease of operation.

## Insight into the WTW Dataset

### Dataset Description
WTW-Dataset is the first wild table dataset for table detection and table structure recognition tasks. It is constructed from photoing, scanning, and web pages, covering 7 challenging cases like Inclined tables, Curved tables, Occluded or blurred tables, Extreme aspect ratio tables, Overlaid tables, Multi-color tables, and Irregular tables in table structure recognition.

### Dataset Components
It comprises 14581 images with detailed annotations, including table cell bounding boxes and their respective row/column positions.

### Accessing the Dataset
The dataset can be downloaded from [here](https://tianchi.aliyun.com/dataset/108587).

## YOLOv8 Model Specifications

### What is YOLOv8?
YOLOv8 is the latest state-of-the-art YOLO model designed for object detection, image classification, and instance segmentation tasks. Developed by Ultralytics, YOLOv8 introduces several architectural and developer experience enhancements over its predecessor, YOLOv5. This model is currently under active development, signifying continuous improvements and community-driven optimizations.

### Evolution of YOLO to YOLOv8
The YOLO (You Only Look Once) series has gained immense popularity in the computer vision community due to its exceptional accuracy while maintaining a compact model size. YOLO models are GPU-trainable, making them accessible to a broad spectrum of developers. They are deployable at a low cost on both edge devices and cloud platforms.

### Key Features of YOLOv8
- **High Accuracy**: YOLOv8 boasts commendable accuracy rates as evidenced by its performance on benchmarks like COCO and Roboflow 100.
- **Developer Features**: The model offers a host of developer-friendly features, including an intuitive CLI and a well-organized Python package.
- **Robust Community Support**: A growing community around YOLOv8 ensures continued support, updates, and guidance for users.

### YOLOv8 Architecture Deep Dive
YOLOv8's architecture introduces several advancements over its predecessors:
- **Anchor Free Detection**: This model is anchor-free, predicting object centers directly rather than offsets from predefined anchor boxes.
- **New Convolution Layers**: Modifications in the convolution layers lead to performance and detection improvements.
- **Mosaic Augmentation**: A unique augmentation technique that aids in better generalization during training.

## Model Evaluation Results
Upon evaluating the YOLOv8 model on the WTW dataset, the following results were observed:

- **Precision**: 0.981
- **Recall**: 0.722
- **mAP50**: 0.853
- **mAP50-95**: 0.768
- **Speed**: Preprocessing: 0.1ms, Inference: 12.6ms, Loss Calculation: 0.0ms, Post-processing: 1.9ms per image.

These results highlight the model's ability to detect tables with a high degree of precision and a reasonable recall rate, making it suitable for real-world applications.

## How to Use
This project provides a `pipeline.py` script that allows users to execute the entire data processing and training workflow seamlessly. Here's a step-by-step breakdown of the pipeline:

1. Convert XML annotations to YOLO format.
2. Split the dataset into training and validation subsets.
3. Prepare the final datasets for train, validation, and test.
4. Generate a `data.yaml` file for YOLO training configurations.
5. Execute the training script with the specified configurations.
6. Inference on the test set.
7. Launch a Streamlit application for real-time predictions.

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies using the provided `requirements.txt` file.
3. Download the WTW dataset using the link provided in the dataset section.
4. Execute the `pipeline.py` script to kickstart the training and evaluation process.

```bash
pip install -r requirements.txt
python pipeline.py
```

## Get in Touch
For any queries, suggestions, or contributions, please reach out to the project maintainers via the provided communication channels.

## Credits and References
- YOLOv8 Official Repository
- WTW Dataset Official Repository
