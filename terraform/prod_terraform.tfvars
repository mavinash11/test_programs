# terraform.tfvars
# terraform apply -var-file="prod_terraform.tfvars"

region          = "ap-south-1"
ami_id          = "ami-0d0ad8bb301edb745" # Example AMI for us-west-2
instance_type   = "t3.micro"
key_name        = "My_Key_1"
instance_name   = "Production-EC2"
allowed_ssh_cidr = "192.168.1.0/24" # Restrict SSH to a specific CIDR