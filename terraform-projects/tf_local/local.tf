terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "> 2.0.0"
    }
  }
}

resource "local_file" "test" {
  filename = var.testfile
  content = <<EOF
testfile2 id attribute: ${local_file.test2.id}
${var.testfile_content}
EOF
  file_permission = var.testfile_permission
}

resource "local_file" "test2" {
  filename = var.testfile2
  content = <<EOF
  name: ${var.testfile2_content.name}
  age:  ${var.testfile2_content.age}
  available_for_sale: ${var.testfile2_content.is_available}
  EOF
  file_permission = var.testfile2_permission
  lifecycle {
    create_before_destroy = true // Ensures the new file is created before the old one is destroyed
  }
}

