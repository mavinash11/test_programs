# Terraform Block
terraform {
  required_version = ">= 1.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

# Provider Block
provider "aws" {
  region  = "ap-south-1"
  profile = "user_avinash"
  shared_credentials_files = ["$HOME/.aws/credentials"]
  shared_config_files = ["$HOME/.aws/config"]
}
