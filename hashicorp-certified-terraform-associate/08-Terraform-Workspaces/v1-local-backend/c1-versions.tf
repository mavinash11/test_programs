# Terraform Block
terraform {
  required_version = ">= 1.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
  backend "s3" {
    bucket = "terraform-stacksimplify-avinash-malagave"
    key = "workspaces/terraform.tfstate"
    region = "ap-south-1"
    dynamodb_table = "terraform-dev-state-table"
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
  profile = "user_avinash"
}
/*
Note-1:  AWS Credentials Profile (profile = "default") configured on your local desktop terminal  
$HOME/.aws/credentials
*/
