#!/bin/sh

cd "${0%/*}"
cd ../data

curl https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_image_2.zip -o data_object_image_2.zip
curl https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_image_3.zip -o data_object_image_3.zip
curl https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_label_2.zip -o data_object_label_2.zip
curl https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_velodyne.zip -o data_object_velodyne.zip
curl https://s3.eu-central-1.amazonaws.com/avg-kitti/data_object_calib.zip -o data_object_calib.zip

unzip data_object_image_2.zip
unzip data_object_image_3.zip
unzip data_object_label_2.zip
unzip data_object_velodyne.zip
unzip data_object_calib.zip

rm data_object_image_2.zip
rm data_object_image_3.zip
rm data_object_label_2.zip
rm data_object_velodyne.zip
rm data_object_calib.zip