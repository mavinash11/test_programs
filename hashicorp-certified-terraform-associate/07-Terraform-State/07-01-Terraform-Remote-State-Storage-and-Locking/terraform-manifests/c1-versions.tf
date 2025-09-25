# Terraform Block
terraform {
  required_version = ">= 1.4" 
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
  # Adding Backend as S3 for Remote State Storage
  backend "s3" {
    bucket = "terraform-stacksimplify-avinash-malagave"
    key    = "dev/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "terraform-dev-state-table"
    /*
        # Enable during Step-09
        # For State Locking
        dynamodb_table = "terraform-dev-state-table"
    */
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
  shared_credentials_files = ["$HOME/.aws/credentials"]
  shared_config_files = ["$HOME/.aws/config"]
  profile = "user_avinash"
}
/*
Note-1:  AWS Credentials Profile (profile = "default") configured on your local desktop terminal  
$HOME/.aws/credentials
*/
