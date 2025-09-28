# AWS EC2 Instance Module
module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  ami = data.aws_ami.amzlinux.id
  name = "single-instance-${terraform.workspace}-${count.index}"
  instance_type = "t3.micro"
  count = 2
  key_name      = "terraform-key"
  monitoring    = true
  vpc_security_group_ids = ["sg-08243a0b95b8cc267"]
  subnet_id = "subnet-0630088c30be7f773"
  user_data = file("apache-install.sh")
  tags = {
    Name        = "Modules-Demo-${terraform.workspace}-${count.index}"
    Terraform   = "true"
    Environment = "dev"
  }
}

