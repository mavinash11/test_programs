# Create EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-01b6d88af12965bb6" # Amazon Linux
  instance_type = "t3.micro"
  count         = 2
  tags = {
#    "Name" = "web"
    "Name" = "web-${count.index}"
  }
}
