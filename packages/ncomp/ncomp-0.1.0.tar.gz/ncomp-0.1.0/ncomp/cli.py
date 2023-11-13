import os
import shutil
import subprocess as sp
import sys
import tempfile

import docker
import yaml

NETWORK_NAME = os.getenv("SHARED_NETWORK", "shared_network")
COMPOSE_FILE = os.getenv("COMPOSE_FILE", "docker-compose.yml")


def create_network(network_name):
    client = docker.from_env()
    networks = client.networks.list(names=[network_name])
    if not networks:
        client.networks.create(network_name, driver="bridge")


def add_network_to_services(file_name, network_name):
    with open(file_name, "r") as file:
        compose_content = yaml.safe_load(file)

    services = compose_content.get("services", {})
    for service in services.values():
        networks = service.get("networks", [])
        if network_name not in networks:
            networks.append(network_name)
        service["networks"] = networks

    # Add the network definition at the top level
    networks = compose_content.get("networks", {})
    if network_name not in networks:
        networks[network_name] = None  # Or provide specific configurations
    compose_content["networks"] = networks

    with open(file_name, "w") as file:
        yaml.safe_dump(compose_content, file, indent=2)
    with open(file_name, "r") as file:
        print(file.read())


def main():
    # Create network if it doesn't exist
    create_network(NETWORK_NAME)

    # Create a temporary duplicate of the compose file
    with tempfile.NamedTemporaryFile(
        mode="w+t",
        delete=True,
        suffix=".yml",
        dir=os.path.dirname(COMPOSE_FILE),
    ) as temp_file:
        with open(COMPOSE_FILE, "rt") as f:
            shutil.copyfileobj(f, temp_file)
        temp_file.seek(0)

        # Add network to all services in the temporary file
        add_network_to_services(temp_file.name, NETWORK_NAME)

        # Pass arguments to docker compose
        sp.run(
            f'docker compose -f {temp_file.name} {" ".join(sys.argv[1:])}',
            shell=True,
            check=True,
        )


if __name__ == "__main__":
    main()
