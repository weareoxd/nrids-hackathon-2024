## NRIDS Hackathon 2024

- [Prerequisites](#prerequisites)
- [Getting started](#gettingstarted)
  - [Frontend development](#frontend)
  - [Backend development](#backend)
- [Deployment process](#servers-deployment)
---

The application is composed of a containerized [Django](https://www.djangoproject.com/) backend with a PostgreSQL database, and a frontend application built using [Vue.js](https://vuejs.org/). This project setup is optimized for [Visual Studio Code](https://code.visualstudio.com/).

## <a name="prerequisites"></a>Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/) for working on the project
  - [Sass extension](https://marketplace.visualstudio.com/items?itemName=Syler.sass-indented) for Sass syntax highlighting
  - [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) for linting Vue and JS files
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for linting Python files
  - [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for using the Docker container as a development environment
  - [EditorConfig for VS Code extension](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) for ensuring consistant end of line for files across machines for existing files
- [Node.JS 18+](https://nodejs.org/en/) for building and serving the Vue.js frontend
- [Docker](https://download.docker.com/mac/stable/Docker.dmg) for a containerized local development environment

## <a name="important"></a>Important

- **End of line**: Set your line endings to LF. If you're on Windows, it defaults to CRLF. In your VSCode settings, search for Eol (End of line) and set it to \n
    To change the line endings for CRLF to LF on Windows for the existing files:
    1. Run `git config --global core.autocrlf false` to disable automatic line conversion globally.
    2. Run `git rm --cached -r .` to remove all the files from the git index.
    3. Run `git add --renormalize .` to normalize the line endings in your working directory to match the normalization rules specified in your Git configuration.
    4. Discard all the changes
- **ESLint**: Ensure that it is enabled and is also set to be used as the formatter

## <a name="gettingstarted"></a>Getting started

The [frontend](frontend/) and [backend](backend/) are organized into separate directories and should be opened in separate Visual Studio Code windows for the `Remote - Containers` extension to work rather than opening the root directory.

### <a name="pre-commit"></a>Pre commit hooks

Pre-commit hooks run various code formatters and linters. Some (black, prettier) will automatically reformat your code. If you're
using Visual Studio code with the recommended extensions, the pre-commit hook formatting should match editor output.

1. Install [pre-commit](https://pre-commit.com/#install) (`brew install pre-commit` using homebrew or `pip install pre-commit` using python)
2. Setup the pre-commit and commit message git hooks in the local repository: `pre-commit install --hook-type pre-commit --hook-type commit-msg`

### <a name="frontend"></a>Frontend development

See the [Frontend README](frontend/README.md) for details on setting up and building the frontend, which is accessible at [http://localhost:9000](http://localhost:9000).

### <a name="backend"></a>Backend development

See the [Backend README](backend/README.md) for details on setting up and building the backend, which is accessible at [http://localhost:8000](http://localhost:8000).

## <a name="servers-deployment"></a>Deployment process

When code is merged to the `main` branch, webhooks in GitLab will trigger a build of the frontend and backend into a Docker image, tag the image, and deploy the image to [https://nrids-hackathon-2024.dev.oxd.com/](https://nrids-hackathon-2024.dev.oxd.com/). Notifications for the build and deployment status will be sent to the `#hackathon-dds` Slack channel.
