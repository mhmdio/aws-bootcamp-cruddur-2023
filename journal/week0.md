# Week 0 — Billing and Architecture

- use https://github.com/mhmdio/dotfiles-gitpod for better installation of tools
- USE AWS Organization
- Implement AWS GuardRails with SCPs
- use AWS SSO instead of IAM credentials
- download WAF report
- work on development environment

## Development environments

### macOS

Local development environment (LDE) by Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

```bash
brew install --cask visual-studio-code
```

### GitHub codespaces

Cloud development environment (CDE) by GitHub

- <https://docs.github.com/en/codespaces>

```markdown
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](COPIED-URL)
```

### GitPod

Cloud development environment (CDE) by Gitpod

- <https://www.gitpod.io/docs/introduction>
- https://www.gitpod.io/docs/references/gitpod-yml

```markdown
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#<your-repository-url>)
```

## momento

```bash
brew tap momentohq/tap
brew install momento-cli
momento account signup aws --email my.almusaddar@gmail.com --region us-east-1
momento configure
```

![arch-concept](../_docs/assets/arch-concept.png)

---

![arch-logical](../_docs/assets/arch-logical.png)

