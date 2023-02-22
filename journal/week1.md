# Week 1 — App Containerization

- improve Dockerfiles
- improve docker-compose
- improve gitpod yaml file with tasks, ports, and VSCode extensions
- register and use Snyk for codebase security scanning
- add notifications API and route to backend
- add notifications page and route to frontend
- add local dynamodb NoSQL DB and Postgre SQL DB to docker-compose
- add SQL VSCODE extensions to gitpod yaml file and dynamodb table port 
- add AWS VSCode extension to gitpod yaml file
- add HealthCheck for backend
- add RollBar to Frontend
- update docker base images for frontend and backend based on Snyk findings

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
