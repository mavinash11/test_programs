variable "testfile" {
  description = "testfile location"
  type        = string
  default     = "/Users/AV346060/Desktop/test_avinash/test_programs/terraform/tf_local/testfile.txt"
}
variable "testfile_content" {
  description = "Content for the test file"
  type        = string
  default     = "This is a test file created by Terraform using the local_file resource. Created by Avinash."
}
variable "testfile_permission" {
  description = "File permission for the test file"
  type        = string
  default     = "0700"
}


variable "testfile2" {
  description = "testfile2 location"
  type        = string
  default     = "/Users/AV346060/Desktop/test_avinash/test_programs/terraform/tf_local/testfile2.txt"
}

variable "testfile2_content" {
  description = "Content for the test file"
  type        = object({
    name        = string
    age         = number
    is_available = bool
  })
  default     = {
    name        = "Luna"
    age         = 5
    is_available = true
  }
}

variable "testfile2_permission" {
  description = "File permission for the test file"
  type        = string
  default     = "0700"
}
