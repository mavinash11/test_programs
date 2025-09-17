provider "aws" {
    region = "ap-south-1"  # Set your desired AWS region
}

resource "aws_instance" "example" {
    ami           = "ami-0d0ad8bb301edb745"  # Specify an appropriate AMI ID
    instance_type = "t3.micro"
    key_name      = "MyKey" 
    vpc_security_group_ids =  ["sg-08243a0b95b8cc267"]
    tags = {
    Name = "Configured via TF"
    }
}