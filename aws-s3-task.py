"""

Given statement:
# Write a script to:
# 1. Download a file from AWS S3 and read it
# 2. This file will contain the name of a docker image.  For example, `postgres:13`
# 3. Use the Python or Golang Docker libraries (or plain HTTP APIs for Docker) to download this image locally. (This is `docker pull` but via code).

Environment used:
Python Version: 3.9
Boto3 package Version: 1.21.15
Docker package version: 5.0.3

"""

import boto3
import docker
from boto3 import Session

# Check if the credentials are configured
def verify_credentials():
    session = Session()
    credentials = session.get_credentials()
    creds = credentials.get_frozen_credentials()

    # If any of the key is not present, exit the program
    if creds.access_key is None:
        print("Access Key is incorrect in the credentials, please use `aws configure` to setup credentials")
        exit()

    if creds.secret_key is None:
        print("Secret Key is incorrect in the credentials, use `aws configure` to setup  to setup credentials")
        exit()

# Download the Dockerfile from a S3 bucket. 
def download_s3_object():
    s3=boto3.resource("s3")
    bucket_name=input("Enter the bucket name: ")
    ojb_name=input("Enter the file name to download: ")
    try:
        s3.Bucket(bucket_name).download_file(ojb_name,"../downloads/"+ojb_name)
        print("Downloaded "+ojb_name+" file in the src directory...")
        return ojb_name
    except:
        print("Error while downloading object. Please check the bucket name and please also verify the aws credentials.")
        return 0

# Pulling docker image which is mentioned in the object downloaded from S3 bucket 
def pull_image(file_name):
    docker_client=docker.from_env()
    fs=open("../downloads/"+file_name)
    image_name=fs.readline().strip()
    try:
        print("Pulling docker image: ",image_name+"")
        print(docker_client.images.pull(image_name))
        print("Downloaded the image "+image_name+" . Please use `docker images` to list the images")
    except:
        print("Error pulling ",image_name,"image. Please check the image name and tag mentioned in the file or check the internet connectivity.")

if __name__== "__main__":

    # Check if the credentials are configured
    verify_credentials()

    # Download the file from S3 bucket and obtain the filename
    s3_obj=download_s3_object()

    # Pull the docker image specified in Dockerfile
    if s3_obj != 0:
        pull_image(s3_obj)
