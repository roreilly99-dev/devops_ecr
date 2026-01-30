# Perth Events Infrastructure

This directory contains Terraform configuration for deploying the Perth Events application to AWS.

## Structure

- `bootstrap/` - S3 backend setup for Terraform state
- `main/` - Main infrastructure configuration
  - `modules/` - Reusable infrastructure modules
    - `ecr/` - Frontend ECR repository
    - `ecr-backend/` - Backend ECR repository
    - `vpc/` - VPC and networking
    - `iam/` - IAM roles and policies
    - `alb/` - Application Load Balancer
    - `ecs/` - ECS cluster and services

## Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured
- Terraform 1.x installed

## Deployment

### 1. Bootstrap (First time only)

```bash
cd bootstrap
terraform init
terraform apply
```

This creates:
- S3 bucket for Terraform state
- DynamoDB table for state locking

### 2. Deploy Main Infrastructure

```bash
cd main
terraform init
terraform plan
terraform apply
```

This creates:
- ECR repositories for backend and frontend
- VPC with public/private subnets
- Application Load Balancer
- ECS cluster with Fargate
- IAM roles and security groups

### 3. Deploy Applications

After infrastructure is deployed, use GitHub Actions to build and push Docker images to ECR.

## Resources Created

### Networking
- VPC with CIDR 10.0.0.0/16
- Public and private subnets across multiple AZs
- Internet Gateway
- NAT Gateway (optional)
- Route tables

### Compute
- ECS Cluster
- ECS Task Definitions for frontend and backend
- ECS Services with auto-scaling
- Fargate launch type

### Load Balancing
- Application Load Balancer
- Target Groups for frontend and backend
- Listeners on ports 80 and 443

### Storage
- ECR repositories with image scanning enabled

### Security
- Security groups for ALB and ECS tasks
- IAM roles for ECS task execution and tasks

## Outputs

After applying, Terraform outputs:
- `ecr_url` - Frontend ECR repository URL
- `ecr_backend_url` - Backend ECR repository URL
- ALB DNS name (from ECS module)

## Environment Variables

For production deployment, configure:
- `AWS_ACCESS_KEY_ID` - AWS access key
- `AWS_SECRET_ACCESS_KEY` - AWS secret key
- `AWS_REGION` - AWS region (default: eu-west-1)

## Cost Considerations

Main cost drivers:
- ECS Fargate tasks (pay per vCPU and memory per hour)
- Application Load Balancer (hourly + LCU charges)
- NAT Gateway (if enabled)
- Data transfer

Estimated monthly cost: $50-150 depending on usage and configuration.

## Cleanup

To destroy all resources:

```bash
cd main
terraform destroy
```

⚠️ This will delete all resources created by Terraform. Use with caution in production!

## Customization

### Scaling

Modify ECS service desired count in `modules/ecs/main.tf`:
```hcl
desired_count = 2  # Increase for more instances
```

### Instance Size

Modify task definition CPU and memory in `modules/ecs/main.tf`:
```hcl
cpu    = "512"   # 0.5 vCPU
memory = "1024"  # 1 GB
```

### Region

Update region in `main/main.tf`:
```hcl
provider "aws" {
  region = "us-west-2"  # Change to desired region
}
```

## Troubleshooting

### State Lock Issues
If Terraform state is locked:
```bash
# Check DynamoDB for locks
aws dynamodb scan --table-name ecr-devops-state-locking

# Force unlock (use carefully)
terraform force-unlock <LOCK_ID>
```

### ECR Push Failures
Ensure you're logged in to ECR:
```bash
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.eu-west-1.amazonaws.com
```

### ECS Task Failures
Check CloudWatch Logs for task logs and errors.

## Security Best Practices

- Enable encryption at rest for all storage
- Use VPC endpoints to avoid NAT Gateway costs
- Implement least privilege IAM policies
- Enable CloudTrail for audit logging
- Use AWS Secrets Manager for sensitive data
- Implement WAF rules on ALB for production

## Support

For issues or questions about infrastructure:
1. Check Terraform plan output
2. Review AWS CloudWatch logs
3. Check GitHub Actions workflow logs
4. Create an issue in the repository
