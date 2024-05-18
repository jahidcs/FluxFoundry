import yaml

with open('../intro.yaml', 'r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as e:
        print(e)