#!/bin/bash
echo " - - - - - - - PREPARING TEST DATA - - - - - - - "

echo "Installing AWS CLI - - - - - - - "
sudo apt-get install -y awscli

# Download data from S3 bucket
echo "copying data from s3 bucket - - - - - - - "
aws s3 cp --no-sign-request s3://MTABusTime/AppQuest3/MTA-Bus-Time_.2014-08-01.txt.xz data

# Unzipping archive with XZ utility
echo "unzipping - - - - - - - "
unxz data/MTA-Bus-Time_.2014-08-01.txt.xz

# Transform from TXT to CSV format
echo "transforming data to csv format - - - - - - - "
tr -s '[:blank:]' , < data/MTA-Bus-Time_.2014-08-01.txt > data/MTA_2014-08-01.csv
rm data/MTA-Bus-Time_.2014-08-01.txt

# Download JDBC driver with WGET
echo "copying JDBC driver - - - - - - - "
wget "https://jdbc.postgresql.org/download/postgresql-42.4.0.jar" -P apps
