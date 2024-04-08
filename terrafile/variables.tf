variable "credentials" {
  description = "My Credentials"
  default     = "./keys/oregon-crime-e130b790c75d.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default = "oregon-crime"
}

variable "region" {
  description = "Region"
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default = "oregon-crime-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARDs"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  #Update the below to what you want your dataset to be called
  default     = "oregon_crime"
}