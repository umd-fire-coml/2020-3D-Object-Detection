#!/bin/sh

cd "${0%/*}"
cd ../data

fileid="1e6C1WYIqHvtuf6HoRXJXrQTNA_fCDxyr"
filename="nuScenes.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

unzip ${filename}

rm ${filename}