# python-devops-tooling

```text
		      PYTHON DEVOPS TOOLING
			      │
	      ┌─────────────┴─────────────┐
	      │                           │
	 Python Basics               Linux/Shell
	      │                           │
	      └─────────────┬─────────────┘
			      │
		      1. argparse
			      │
		      Build CLI tools
			      │
		      2. logging
			      │
		    Add production logs
			      │
			3. pytest
			      │
			Test the tool
			      │
		      4. Shell + Python
			      │
		    Automate DevOps tasks
			      │
			      ▼
		   Production CLI Utility
```

Python DevOps Tooling is a hands-on learning repository for building automation,
delivery, infrastructure, monitoring, and observability workflows with Python.
It focuses on the practical connection between Python code and the tools used
to operate modern applications and platforms.

## What This Repository Covers

- **Python and Linux/Shell:** Create CLI tools and automate repeatable
	operational tasks with scripts, subprocesses, logging, and tests.
- **Docker:** Inspect containers, automate image and container workflows, and
	connect Python services to the Docker API.
- **Kubernetes:** Work toward Python-driven cluster operations, deployments,
	service inspection, and automation using Kubernetes APIs and tooling.
- **GitHub Actions:** Build CI/CD workflows that run tests, package tools, and
	automate delivery from repository events.
- **Prometheus:** Expose and collect metrics that describe application and
	infrastructure health.
- **Grafana:** Build dashboards and visualize metrics for faster diagnosis and
	operational decision-making.
- **OpenTelemetry:** Add vendor-neutral traces, metrics, and logs so activity
	can be followed across services and deployment environments.

## Learning Goal

The goal is to progress from small Python scripts to dependable production
tooling. Along the way, the repository brings together infrastructure
automation, CI/CD, container and cluster management, metrics, dashboards, and
distributed tracing. Each topic can be extended with configuration, error
handling, security practices, automated tests, and deployment-ready packaging.

## Building DevOps and Developer Platform Tools

The repository also explores how to package these integrations into useful
tools for engineers. Python CLI applications can provide a consistent interface
for common workflows instead of requiring developers to remember long sequences
of Docker, Kubernetes, or shell commands.

Examples of tools and workflows include:

- A CLI that builds, tags, and publishes Docker images.
- A deployment tool that validates configuration and applies releases to
  Kubernetes environments.
- A GitHub Actions helper that creates CI workflows, runs checks, or reports
  deployment status.
- An operations tool that queries Prometheus metrics and opens Grafana views
  for a service or environment.
- An observability helper that configures OpenTelemetry instrumentation and
  checks trace or metric availability.
- A developer platform command that scaffolds a new service with standard
  repositories, CI/CD, deployment configuration, dashboards, and alerts.

Good tools should have clear commands and options, useful help text, structured
logs, safe defaults, meaningful exit codes, validation, and automated tests.
They should make the paved path easier for developers while still exposing
 enough detail for operators to troubleshoot failures.
