# outputs.tf

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.example[0].public_ip
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.example[0].id
}

# Simple output: Public DNS name
output "instance_public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.example[0].public_dns
}

# List output: Availability zones
output "availability_zone" {
  description = "Availability zone of the EC2 instance"
  value       = aws_instance.example[0].availability_zone
}

# Map output: Instance details
output "instance_details" {
  description = "Map of EC2 instance details"
  value = {
    id         = aws_instance.example[0].id
    public_ip  = aws_instance.example[0].public_ip
    private_ip = aws_instance.example[0].private_ip
  }
}

# Sensitive output: Instance ARN (marked as sensitive)
output "instance_arn" {
  description = "ARN of the EC2 instance"
  value       = aws_instance.example[0].arn
  sensitive   = true # Hides value in CLI output
}

