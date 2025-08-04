variable "region" {
  default = "ap-south-1"
}

variable "ami_id" {
  default = "ami-0d0ad8bb301edb745"
}

variable "instance_type" {
  default = "t3.micro"
}

variable "instance_count" {
  default = 1
}

variable "key_name" {
  description = "Name of the SSH key pair"
  type        = string
  default     = "My_Key_1"
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