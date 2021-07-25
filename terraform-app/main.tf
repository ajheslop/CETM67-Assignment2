provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  token      = var.secret_token
  region     = "us-east-1"
}

resource "aws_dynamodb_table" "example" {
  name           = "testTerra"
  hash_key       = "employeeid"
  range_key      = "manager"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "employeeid"
    type = "S"
  }

  attribute {
    name = "manager"
    type = "S"
  }
}

resource "aws_dynamodb_table_item" "example" {
  table_name = aws_dynamodb_table.example.name
  hash_key   = aws_dynamodb_table.example.hash_key
  range_key  = aws_dynamodb_table.example.range_key

  item = <<ITEM
  {
    "employeeid": {"S": "tim robins"},
    "manager": {"S": "joe blogs"},
    "courses": {"L": [{"M": {"Certificate": {"S": "aws foundation course"},"CourseName": {"S": "AWS Foundation"},"CourseProvided": {"S": "AWS"},"Expires": {"S": "07-07-2023"}}},{"M": {"Certificate": {"S": "python foundation"},"CourseName": {"S": "Python"},"CourseProvider": {"S": "python.org"},"Expires": {"S": "N/A"}}}]}
  }
  ITEM
}

resource "aws_s3_bucket" "example" {
  bucket = "cetm67testterra"
  
}

resource "aws_s3_bucket_public_access_block" "example" {
bucket = aws_s3_bucket.example.bucket
block_public_acls = true
block_public_policy = true
restrict_public_buckets = true
ignore_public_acls =  true
}