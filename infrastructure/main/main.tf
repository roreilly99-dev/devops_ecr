terraform {

    backend "s3" {
        bucket = "ecr-devops-state"
        key = "main/terraform.tfstate"
        region = "eu-west-1"
        profile = "terraform-user"
        dynamodb_table = "ecr-devops-state-locking"
        encrypt = true
    }
    required_providers{
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.0"
        }
    }
}

provider "aws"{
    region = "eu-west-1"
    profile = "terraform-user"
    default_tags{

    }
}

module "ecr"{
    source = "./modules/ecr"
    name = "nextjs-app"
}

module "vpc" {
    source = "./modules/vpc"
}

module "iam" {
    source = "./modules/iam"
}

module "alb" {
  source     = "./modules/alb"
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.subnet_ids
}

module "ecs" {
  source              = "./modules/ecs"
  image_url           = module.ecr.repository_url
  execution_role_arn  = module.iam.role_arn
  subnet_ids          = module.vpc.subnet_ids
  security_group_id   = module.alb.security_group_id
  target_group_arn    = module.alb.target_group_arn
  listener_dependency = module.alb
}
