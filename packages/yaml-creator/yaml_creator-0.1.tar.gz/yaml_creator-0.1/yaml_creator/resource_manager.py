import yaml

from functools import wraps

deployment_file = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "example-deployment",
        "labels": {
            "app": "example"
        }
    },
    "spec": {
        "replicas": 3,
        "selector": {
            "matchLabels": {
                "app": "example"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "example"
                }
            },
            "spec": {
                "containers": [{
                    "name": "example-container",
                    "image": "nginx:1.14.2",
                    "ports": [{
                        "containerPort": 80
                    }]
                }]
            }
        }
    }
}

def yaml_generator():
    pass

def deployment(cpu=1, memory=512):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('CPU: {} Memory: {}'.format(cpu, memory))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def create_deployment():
    with open('deployment.yaml', 'w') as file:
        yaml.dump(deployment_file, file)
        
    # To verify, let's read it back
    with open('deployment.yaml', 'r') as file:
        loaded_data = yaml.safe_load(file)
        print(loaded_data)
    

@deployment(cpu=1, memory=512)
def example():
    print("Hello World!")


#example()

#create_deployment()