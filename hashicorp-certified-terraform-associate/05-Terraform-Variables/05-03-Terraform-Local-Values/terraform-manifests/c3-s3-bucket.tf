# Create S3 Bucket - with Input Variables 
/*
resource "aws_s3_bucket" "mys3bucket" {
  bucket = "${var.app_name}-${var.environment_name}-bucket"
  acl = "private"
  tags = {
    Name = "${var.app_name}-${var.environment_name}-bucket"
    Environment = var.environment_name
  }
}
*/
resource "random_id" "bucket_id" {
  byte_length = 4
}

# Define Local Values
locals {
  bucket-name = "${var.app_name}-${var.environment_name}-bucket-${random_id.bucket_id.hex}" # Complex expression
}

# Create S3 Bucket - with Input Variables & Local Values
resource "aws_s3_bucket" "mys3bucket" {
  bucket = local.bucket-name
  tags = {
    Name        = local.bucket-name
    Environment = var.environment_name
  }
}