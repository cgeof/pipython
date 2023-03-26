from importlib import metadata

np_data = metadata.metadata("numpy")

print("Metadata about numpy package:")
print("Version - ", np_data['Version'])
print("Summary - ", np_data['Summary'])

print("-"*8)
print("Metadata dictionary - ")
print(dict(np_data))

# pour ne pas passer par création d'une fct
# from importlib import metadata
# print(dict(metadata.metadata("numpy")))
