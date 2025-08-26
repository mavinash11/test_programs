resource "aws_s3_bucket" "finance" {
  bucket= "avinashmalgave200820251847pm"
  tags={
    Description = "This is a bucket for storing financial test data"
  }
}

resource "aws_s3_object" "finance-2025" {
  bucket = aws_s3_bucket.finance.id
  key    = "finance-2025.doc"
  content = "/root/finance/finance-2025.doc"
}

resource "aws_s3_bucket_policy" "finance-policy" {
  bucket = aws_s3_bucket.finance.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = "s3:GetObject"
        Resource = "${aws_s3_bucket.finance.arn}/*"
      }
    ]
  })
}