# Terraform Block
terraform {
  /*
  required_version = ">= 1.4.1"
  */
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = ">= 6.0"
    }
  }
}

# Provider Block
provider "aws" {
  region = "ap-south-1"
  profile = "avinash_test"
  shared_credentials_files = ["$HOME/.aws/credentials"]
  shared_config_files = ["$HOME/.aws/config"]
}

/*
Note-1:  AWS Credentials Profile (profile = "default") configured on your local desktop terminal  
$HOME/.aws/credentials
*/
