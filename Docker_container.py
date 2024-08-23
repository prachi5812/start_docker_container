import docker

def start_container(image_name, container_name):
    client = docker.from_env()
    container = client.containers.run(image_name, name=container_name , detach = True)
    return container


# When calling start_container
if __name__ == "__main__":
     container1=start_container('nginx', 'my_nginx')
     print(f"Container '{container1.name}' started with ID: {container1.id}")
