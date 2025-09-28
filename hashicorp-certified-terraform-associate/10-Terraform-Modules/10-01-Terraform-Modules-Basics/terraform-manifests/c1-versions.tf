# Terraform Block
terraform {
  required_version = ">= 1.4" 
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.33"
    }
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
  profile = "user_avinash"
  shared_credentials_files = ["$HOME/.aws/credentials"]
  shared_config_files = ["$HOME/.aws/config"]
}
/*
Note-1:  AWS Credentials Profile (profile = "default") configured on your local desktop terminal  
$HOME/.aws/credentials
*/
