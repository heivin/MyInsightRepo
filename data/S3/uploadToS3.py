#!/usr/bin/env python

#title           :uploadToS3.py
#description     :This class will upload to s3 bucket
#author		     :Ajay Krishna Teja Kavuri
#date            :02122017
#version         :0.1
#==============================================================================

# Libraries
import os
import boto3
import botocore

#==============================================================================

# Implementation
class S3():

    # Initialize
    def __init__(self):

        # Define the bucket name
        self.bcktNme = "de-ny-ajay"

        # Get the boto s3 instance
        self.botoS3 = boto3.resource('s3')

        # Debug statement
        # print "Initialized"

    # Method to read all the buckets from the s3
    def getAllBuckets(self):
        # loop through
        for bucket in self.botoS3.buckets.all():
            # Print the bucket
            print bucket

    # Method to check for the bucket
    def checkBucket(self):
        # create a bucket instance
        myBucket = self.botoS3.Bucket(self.bcktNme)

        # Default to exists
        exists = True

        # Try to get the head bucket from meta
        try:
            self.botoS3.meta.client.head_bucket(Bucket=self.bcktNme)
        except botocore.exceptions.ClientError as e:
            # Check for specific error code
            error_code = int(e.response['Error']['Code'])
            if error_code == 404:
                exists = False

        # Return statement
        return exists

# Main method
if __name__=="__main__":

    # Get the arguments

    # Initialize the class
    thisS3 = S3()
