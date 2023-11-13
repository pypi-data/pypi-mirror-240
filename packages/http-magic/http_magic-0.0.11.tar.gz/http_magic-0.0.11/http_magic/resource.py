def resource_folder(resource_type: str) -> str:
    import importlib.util
    spec = importlib.util.find_spec('rest_magic')
    if spec:
        if "files" in spec.submodule_search_locations:
            folder = spec.submodule_search_locations + "/files"
            import os
            if os.path.isdir(folder):
                return folder + "/" + resource_type
    return "files/" + resource_type


def resource_file_path(resource_type: str, resource_file_name: str):
    file_path = resource_folder(resource_type=resource_type) + "/" + resource_file_name
    print(file_path)
    return file_path
