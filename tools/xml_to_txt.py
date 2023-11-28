import os
from xml.etree import ElementTree as ET


def get_text(element):
    """Get text of an XML element safely."""
    return element.text if element is not None else None


def convert_bounding_box(bndbox, img_width, img_height):
    """Convert bounding box coordinates from XML to YOLO format."""
    xmin = float(bndbox.find("xmin").text)
    ymin = float(bndbox.find("ymin").text)
    xmax = float(bndbox.find("xmax").text)
    ymax = float(bndbox.find("ymax").text)

    x_center = ((xmin + xmax) / 2) / img_width
    y_center = ((ymin + ymax) / 2) / img_height
    width = (xmax - xmin) / img_width
    height = (ymax - ymin) / img_height

    return f"0 {x_center} {y_center} {width} {height}"


def parse_xml_file(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    img_width = int(root.find("size/width").text)
    img_height = int(root.find("size/height").text)

    objects = [
        convert_bounding_box(obj.find("bndbox"),
                             img_width,
                             img_height)
        for obj in root.findall("object")
    ]

    return objects


def xml_to_yolo(xml_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith(".xml"):
            xml_file_path = os.path.join(xml_folder, xml_file)
            objects = parse_xml_file(xml_file_path)

            with open(
                os.path.join(
                    output_folder, xml_file.rstrip(".").replace(
                        ".xml",
                        ".txt")
                ),
                "w",
            ) as txt_file:
                for obj in objects:
                    txt_file.write(obj + "\n")


# Usage example:
# xml_to_yolo('data/train/xml', 'data/train/labels')
# xml_to_yolo('data/test/xml', 'data/test/labels')
