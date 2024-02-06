import boto3

#iam = boto3.resource('iam', profile_name="admin")

#admin = boto3.session.Session(profile_name='admin')
#boto3.setup_default_session(profile_name="admin")
#iam = admin.resource('iam')

#iam = boto3.resource('iam')
iam = boto3.client('iam')

users = iam.list_users()

for user in users['Users']:
    print("UserName: {0}\nCreateDate: {1}\n"
    .format(user['UserName'], user['CreateDate']))


pages = iam.get_paginator('list_users')
for page in pages.paginate():
    for user in page['Users']:
        print("UserName: {0}\nCreateDate: {1}\n"
        .format(user['UserName'], user['CreateDate']))
