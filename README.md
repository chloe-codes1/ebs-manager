# EBS Manager

👩🏼‍🔬 Manage your AWS EBS volumes easily and efficiently 

<br>
<br>

### Features

#### EBS
- [x] List your EBS Volumes
- [x] Check EBS volume types
- [x] Check if your EBS volume's instance is composed with ASG
- [x] Modify your EBS volume type


#### EC2
- [x] Get EC2 Tags
- [x] Get VPC ID of your instance



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
- `FILE_PATH`
  - Literally file path
- `VOLUME_FILE`
  - Name of the file to save ebs volumes
- `CURRENT_EBS_TYPE`
  - You're current EBS volume type
- `DESIRED_EBS_TYPE`
  - Desired EBS volume type to change
- `DEVEL_VPC`
  - Your devel environment VPC ID
- `PRODUCT_VPC`
  - Your product environment VPC ID
- `MANAGE_VPC`
  - Your manage environment VPC ID

<br>

#### 5. Call modify_volume_type() method 

You may call modify_volume_type() method on your desired condition.

##### Usage w/ example


```python

self.volume_modifier.modify_volume_type(volume_id)
```


<br>

#### 6. Now, run!

```bash
cd src
python3 main.py 
```

