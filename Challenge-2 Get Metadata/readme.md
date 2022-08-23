# Get AWS Ec2 Instance metedata.


the easiest way to get metadata is to use bash/curl 
as all of aws or any other cloud vendor provides api over their services and resources we can get metadata using curl command 

I am using WS2 Ubuntu instnace to work on it. this is to keep things isolated from main machine. 

generate a pem 
> ssh -i "file.pem" devops@123.123.123.123

? enter password on ask

Once you are connected to your instance you can run below command to get isntance-id from terminal

> curl -X GET http://169.254.169.254/latest/meta-data/instnace-id




# From EC2 Instance Connect over AWS Cli.

get all avaiable metadata items list.
> curl -X GET http://169.254.169.254/latest/meta-data/

to get instance id
> curl -X GET http://169.254.169.254/latest/meta-data/instnace-id