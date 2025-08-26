variable "profile" {
    description = "AWS profile to use for authentication"
    type        = string
    default     = "avinash_test"
}

variable "region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "ap-south-1"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0d0ad8bb301edb745"
}

variable "instance_type" {
  description = "Type of EC2 instance to create"
  type        = string
  default     = "t3.micro"
}

variable "instance_count" {
  description = "Number of EC2 instances to create"
  type        = number
  default     = 1
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
  default     = "MyKey"
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "Terraform-EC2-Example"
}

variable "allowed_ssh_cidr" {
  description = "CIDR block allowed to SSH into the instance"
  type        = string
  default     = "0.0.0.0/0" # Restrict to your IP in production
}