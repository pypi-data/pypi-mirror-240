# Docker Network Integration Script (ncomp)

## Overview

This script is designed to streamline the process of integrating a custom network into Docker Compose services. It automates the task of adding a specified network to all services in a Docker Compose file and ensures the network is properly defined and recognized by Docker Compose.

## Features

- **Automatic Network Creation**: Creates a Docker network if it does not already exist.
- **Dynamic Network Integration**: Adds a specified network to all services in a Docker Compose file.
- **Custom Network Support**: Supports custom network names as specified by the user environment.
- **Error Handling**: Provides error output if the Docker Compose process encounters issues.

## Requirements

- Python 3.x
- Docker Python SDK
- PyYAML

## Environment Variables

- `SHARED_NETWORK`: The name of the network to be integrated into Docker Compose services. Default is "shared_network".
- `COMPOSE_FILE`: The path to the Docker Compose file. Default is "docker-compose.yml".

## Usage

1. **Set Environment Variables** (optional): Define `SHARED_NETWORK` and `COMPOSE_FILE` if you want to use custom values.
2. **Run the Script**: Execute the script in the same directory as your Docker Compose file or specify the path using the `COMPOSE_FILE` environment variable.

## Example

```bash
# Run with custom network name and Docker Compose file
SHARED_NETWORK=my_network COMPOSE_FILE=my_docker_compose.yml ncomp up
```
