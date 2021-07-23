provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  token = var.secret_token
  region = "us-east-1"
}

resource "aws_dynamodb_table" "my_first_table" {
  name     = "testTerra"
  hash_key = "employee-id"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "employee-id"
    type = "S"
  }

}