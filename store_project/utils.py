import hashlib


def image_path_generator(instance, filename):
    # download.jpeg
    name = filename.split('.')
    return f"product_{instance.id}/{hash(name[0])}.{name[-1]}"

