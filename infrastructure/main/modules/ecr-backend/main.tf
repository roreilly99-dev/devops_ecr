resource "aws_ecr_repository" "backend" {
    name = "${var.name}-backend"
    image_tag_mutability = "MUTABLE"
    image_scanning_configuration {
        scan_on_push = true
    }
}

output "repository_url" {
    value = aws_ecr_repository.backend.repository_url
}

output "repository_name" {
    value = aws_ecr_repository.backend.name
}
