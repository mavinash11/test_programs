module "local_file" {
  source = "./modules"
  testfile = var.testfile
  testfile_content = var.testfile_content
  testfile2 = var.testfile2
  testfile2_content = var.testfile2_content
}

output "dummy_output" {
  value = "avinash aravind malagave"
}
output "testfile_name" {
  value = module.local_file.testfile_name
}

output "testfile2_name" {
  value = module.local_file.testfile_name
}

