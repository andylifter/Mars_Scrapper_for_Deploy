import os

# def delete_files_in_folder(folder_path):
#     '''Очистка папок от старых изображений'''
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#         if os.path.isfile(file_path):
#             os.remove(file_path)

# delete_files_in_folder('static/Curiosity/')
# delete_files_in_folder('static/Opportunity/')
# delete_files_in_folder('static/Perseverance/')
# delete_files_in_folder('static/Spirit/')

print(len(os.listdir('static/Curiosity/')))
print(len(os.listdir('static/Opportunity/')))
print(len(os.listdir('static/Perseverance/')))
print(len(os.listdir('static/Spirit/')))