# Create EC2 Instance
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

resource "aws_instance" "my-ec2-vm" {
  ami               = "ami-01b6d88af12965bb6"
  instance_type     = "t3.micro"
  availability_zone = "ap-south-1b"
  tags = {
    "Name" = "web"
    "tag1" = "Update-test-1"
  }
}

