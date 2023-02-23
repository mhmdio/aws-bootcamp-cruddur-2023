# Week 1 — App Containerization

- improve Dockerfiles with multi-stage builds, dockerignore, and hadolint linter
- improve docker-compose, add HealthChecks, local dynamodb NoSQL DB and Postgre SQL DB
- improve gitpod yaml file with tasks, ports ( dynamodb port), and VSCode extensions (AWS and SQL)
- register and use Snyk for codebase security scanning
- fix docker base images for frontend and backend based on Snyk findings
- add notifications API and route to backend
- add notifications page and route to frontend
- add RollBar to Frontend and Backend
- push frontend and backend to docker hub
- use drawio as free alternative
- use Taskfile for DevX for cli commands
- use dotfiles with GitPod for easy bootstrap

```bash
docker build -t  backend-flask ./backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask
unset FRONTEND_URL="*"
unset BACKEND_URL="*"
```

```bash
docker-compose build
docker-compose up
```
