# main.tf

# Specify the provider (AWS)
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}


provider "aws" {
  region = var.region # Replace with your desired AWS region
  profile = var.profile # Optional: Specify the AWS profile to use
}

# Define the EC2 instance
resource "aws_instance" "example" {
  count         = var.instance_count  #Number of instances to be created.
  ami           = var.ami_id # Replace with a valid AMI ID for your region
  instance_type = var.instance_type               # Free-tier eligible instance type
  key_name      = var.key_name            # Replace with your SSH key pair name (optional)

  # Optional: Add tags to the instance
  tags = {
    Name = var.instance_name
  }

  # Optional: Associate a security group to allow SSH access
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
}

# Optional: Define a security group to allow SSH access
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh_service"
  description = "Allow SSH inbound traffic"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_cidr] # Allow SSH from anywhere (restrict for production)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # Allow all outbound traffic
    cidr_blocks = [var.allowed_ssh_cidr]
  }

  tags = {
    Name = "allow_ssh_service"
  }
}

# Optional: Output the public IP of the EC2 instance
#output "instance_public_ip" {
#  description = "Public IP address of the EC2 instance"
#  value       = aws_instance.example.public_ip
#}