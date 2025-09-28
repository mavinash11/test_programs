data "aws_iam_policy_document" "s3_put_policy" {
  statement {
    principals {
      type        = "AWS"
      identifiers = ["arn:aws:iam::786439848661:user/avinash_am"] # Replace with your account ID and IAM role ARN
    }
    actions = [
      "s3:PutObject",
    ]
    resources = [
      "${aws_s3_bucket.mywebsite.arn}/*", # Allows PutObject on all objects within the bucket
    ]
  }
}
