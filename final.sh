#!/bin/bash

# Define the container name or ID
contname="data"

# Define the source directory in the container where the output files are located
file1="/home/doc-bd-a1/res_dpre.csv"
file2="/home/doc-bd-a1/vis.png"
file3="/home/doc-bd-a1/eda-in-1.txt"
file4="/home/doc-bd-a1/eda-in-2.txt"
file5="/home/doc-bd-a1/eda-in-3.txt"
file6="/home/doc-bd-a1/k.txt"


# Define the local directory where you want to save the files on your local machine
path="C:\Users\20110\Downloads\bd-a1\service-result"

# Ensure the local directory exists
mkdir -p $path
# Copy files from the container to your local machine
docker cp $contname:$file1 $path
docker cp $contname:$file2 $path
docker cp $contname:$file3 $path
docker cp $contname:$file4 $path
docker cp $contname:$file5 $path
docker cp $contname:$file6 $path

docker stop $contname


