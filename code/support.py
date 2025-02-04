from settings import * 

def folder_importer(*path):
    surf = []
    name_image = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surf.append(pygame.image.load(full_path).convert_alpha())
            file_name = str(file_name).split('.')[0]
            name_image[file_name] = surf
    return name_image