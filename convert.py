import os
import csv
import xml.etree.ElementTree as ET

def xml_to_csv(xml_folder, csv_file):
    xml_files = [file for file in os.listdir(xml_folder) if file.endswith('.xml')]

    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        csvwriter.writerow(header)

        for xml_file in xml_files:
            xml_path = os.path.join(xml_folder, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            filename = images files path'
            width = int(root.find('size/width').text)
            height = int(root.find('size/height').text)
            obj_name = root.find('object/name').text
            xmin = int(root.find('object/bndbox/xmin').text)
            ymin = int(root.find('object/bndbox/ymin').text)
            xmax = int(root.find('object/bndbox/xmax').text)
            ymax = int(root.find('object/bndbox/ymax').text)

            csvwriter.writerow([filename, width, height, obj_name, xmin, ymin, xmax, ymax])

# Specify the folder containing XML files and the output CSV file
xml_folder = 'xml files path'
csv_file = 'your csv file where you want to save your csv with  name'

# Convert XML to CSV
xml_to_csv(xml_folder, csv_file)
