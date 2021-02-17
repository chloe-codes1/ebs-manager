# EBS Manager

🧑‍🔬 Manage your AWS EBS volumes easily and efficiently 

<br>
<br>

### Features

#### EBS
- List your EBS Volumes
- Check EBS volume types
- Check if your EBS volume's instance is composed with ASG
- Modify your EBS volume type


#### EC2
- Get EC2 Tags
- Get VPC ID of your instance



<br>
<br>

### How to run

#### 1. Create a virtual environment called venv
```bash
python3 -m venv venv
```
<br>

#### 2. Activate your virtual environment

```
source venv/bin/activate
```
<br>

#### 3. Install the required packages
```bash
python3 -m pip install --upgrade pip # upgrade your pip
pip3 install -r requirements.txt
```

<br>

#### 4. Modify configs

In `src/configs/configs.py`, you'll see some variables in there.
Make changes to them as desired.

##### Variables
- FILE_PATH
  - Literally file path
- VOLUME_FILE
  - Name of the file to save ebs volumes
- DEVEL_VPC
  - Your devel environment VPC ID
- PRODUCT_VPC
  - Your product environment VPC ID
- MANAGE_VPC
  - Your manage environment VPC ID

<br>

#### 5. Now, run!

```bash
cd src
python3 main.py 
```

