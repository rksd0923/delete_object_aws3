import logging
import boto3
from botocore.exceptions import ClientError
import pathlib
from numpy import random
import os
import sys

def menu():

    print('******************************************************')
    print('Welcome to the Python SDEV400 Homework 1 Application.')
    print('******************************************************\n')

    print('What would you like to do today?')

    print('a. Create a S3 bucket with the name consisting of your firstname, lastname and a random 6-digit suffix.')
    print('b. Put an object (current error.log) in a previously created bucket.')
    print('c. Delete an object in a bucket. ')
    print('d. Delete a bucket.')
    print('e. Copy and object from one bucket to another.')
    print('f. Downloads an existing object from a bucket.')
    print('q. Exit the program.')

menu()

user_input = input('Enter selection: ')


if user_input == 'c':

    def bucket_choice():
        s3 = boto3.client('s3')

        response = s3.list_buckets()

        buckets = [bucket['Name'] for bucket in response['Buckets']]

        for i, item in enumerate(buckets, start=1):

            print(i, item)

        bucket_choice = int(input('Please select a bucket to list objects '))

        global x

        if bucket_choice == 1:
            x = buckets[0]


        elif bucket_choice == 2:
            x = buckets[1]


        elif bucket_choice == 3:
            x = buckets[2]

        elif bucket_choice == 4:
            x = buckets[3]

        elif bucket_choice == 5:
            x = buckets[3]

    bucket_choice()

    def list_bucket_objects(bucket_name):


        # Retrieve the list of bucket objects
        s3 = boto3.client('s3')
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
        except ClientError as e:
            # AllAccessDisabled error == bucket not found
            logging.error(e)
            return None
        return response['Contents']


    def list_bucket_main():
        """Exercise list_bucket_objects()"""

        # Assign this value before running the program
        test_bucket_name = x
        global z
        z = test_bucket_name

        # Set up logging
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s: %(asctime)s: %(message)s')

        # Retrieve the bucket's objects
        objects = list_bucket_objects(test_bucket_name)
        if objects is not None:
            # List the object names
            logging.info(f'Objects in {test_bucket_name}')
            for i, item in enumerate(objects,start=1):
            #for obj, item in enumerate(objects, start=1):
                logging.info(f'  {item["Key"]}')
                print(i)

            object_choice = int(input('Please select an object to delete '))

            global object_key

            if object_choice == 1:
                object_key = objects[0]


            elif object_choice == 2:
                object_key = objects[1]


            elif object_choice == 3:
                object_key = objects[2]

            elif object_choice == 4:
                object_key = objects[3]

            elif object_choice == 5:
                object_key = objects[4]

            print(object_key['Key'])



    list_bucket_main()

    def delete_object(bucket_name, object_name):
        """Delete an object from an S3 bucket

        :param bucket_name: string
        :param object_name: string
        :return: True if the referenced object was deleted, otherwise False
        """

        # Delete the object
        s3 = boto3.client('s3')
        try:
            s3.delete_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True


    def delete_object_main():
        """Exercise delete_object()"""

        # Assign these values before running the program
        test_bucket_name = z

        test_object_name = object_key

        #Set up logging
        logging.basicConfig(level=logging.DEBUG,
                         format='%(levelname)s: %(asctime)s: %(message)s')

        #Delete the object
        if delete_object(test_bucket_name, test_object_name):
            logging.info(f'{test_object_name} was deleted from {test_bucket_name}')


    delete_object_main()
