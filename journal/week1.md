# Week 1 — App Containerization

- use https://github.com/mhmdio/dotfiles-gitpod for better installation of tools
- USE AWS Organization
- Implement AWS GuardRails with SCPs
- use AWS SSO instead of IAM credentials
- download WAF report
- complete Dockerfiles
- complete docker-compose
- register and use Snyk for codebase security scanning

```bash
docker build -t  backend-flask ./backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask
unset FRONTEND_URL="*"
unset BACKEND_URL="*"
```
