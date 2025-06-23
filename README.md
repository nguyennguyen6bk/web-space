# Multi-Domain Web App Playground
A collection of diverse web applications across different domains, designed to serve as an interactive environment for agents, humans, and automated scripts. This project provides a unified playground to test, train, or simulate interactions in various web-based scenarios.
## 📚 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)
- [License](#license)

---

## 🔍 Introduction

This project is a centralized environment that hosts a variety of web applications spanning multiple domains, such as e-commerce, CRM, ERP, Forum and more. Each application is intentionally designed with different UI/UX patterns, workflows, and functionalities to simulate real-world websites.

All web applications are containerized using Docker, making them easy to deploy and run with minimal setup. Users can simply pull the pre-built Docker images and start interacting with the apps locally or in their preferred environments.

The main purpose of this playground is to provide a versatile and realistic environment where different types of agents — including humans, automated scripts, or AI-driven agents — can interact, test behaviors, and perform various tasks.

Whether you're developing and testing autonomous agents, evaluating automation strategies, conducting software testing, or researching web interaction patterns, this project offers a rich set of use cases and scenarios in a single, consistent platform.

## 🚀 Features

- ✅ Multiple Web Apps Across Domains – Includes e-commerce, CRM, ERP, and more to simulate real-world interactions.
- ✅ Docker-Based Deployment – Each app is containerized, allowing quick and consistent setup with just a `docker compose up -d`.
- ✅ Agent-Friendly Interfaces – Designed with consistent and clean structures to support automated agents, RPA, or AI-based interaction testing.
- ✅ Human & Script Interaction Support – Suitable for both manual testing and automated script execution.
- ✅ Modular & Scalable – Easily extendable with new domains or custom apps by adding new Docker images.
- ✅ Pre-configured Scenarios – Some apps include built-in workflows (e.g., login, checkout, posting, etc.) for easier interaction and simulation.

## 💻 System Requirements

To run the web applications in this playground, ensure your system meets the following minimum requirements:

- **Operating System**: Windows 10+, macOS, or Linux
- **Docker**: Docker Engine v20.10+ and Docker Compose v2.0+
- **CPU**: Dual-core processor or higher
- **Memory**: Minimum 8 GB RAM (recommended: 16 GB+ for running multiple containers)
- **Disk Space**: At least 20 GB of free space for Docker images and volumes (Good to have 50GB of free space)
- **Internet Connection**: Required to pull Docker images

## ⚙️ Installation

Clone the project and run web apps using Docker:

```bash
git clone https://github.com/nguyennguyen6bk/web-space.git
cd web-space
# Navigate into any app folder and start it using Docker Compose:
cd magento
docker compose up -d --wait
#Each app will be available on a different local port. Example:
E-commerce App: http://localhost:8084
CRM App: http://localhost:8087
ERP App: http://localhost:8069
# To stop a running app:
docker compose down -v
📘 Note: For specific usage instructions, credentials, or extra configurations, please refer to the guide.txt inside each app's folder
