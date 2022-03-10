
# Script to read image name from a file which is downloaded from S3 and download that docker image into local machine

### Given statement:

Write a script to:
1. Download a file from AWS S3 and read it
2. This file will contain the name of a docker image.  For example, `postgres:13`
3. Use the Python or Golang Docker libraries (or plain HTTP APIs for Docker) to download this image locally. (This is `docker pull` but via code).

### Assumptions and setup:

To run this script, following are the pre-requisites and assumptions ,
- You need to have an AWS account created and create a IAM user with programmatic access. The user should have AWS S3 readonly/fullaccess policy attached
- Create a S3 Bucket and upload a file which contains just an image name. As a sample, you can find there is file `image_name` in this repo. While running the script, you need to provide this as an input.

- You need to install AWS CLI and assuming that you have done setup of AWS CLI for configuration of credentials. Please configure access key and secret access key using `aws configure` if it is not done (Refer: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

- Setup Python 3.x in your local machine to run this script. I have used python 3.9 for development

- S3 bucket file will be downloaded inside `downloads` folder.


### Installing Pre-requisites

Run `pip install -r requirements.txt` in your shell to install all the dependencies


#### Usage

```
$ python3 aws-s3-task.py
```

This needs few inputs to locate the file from S3.

#### Example Input:
```
Enter the bucket name: mybucket-santhosh
Enter the file name to download: image_name
```

#### Sample output:
```
Downloaded image_name file...
Pulling docker image:  postgres:13
<Image: 'postgres:13'>
Downloaded the image postgres:13 . Please use `docker images` to list the images
```
