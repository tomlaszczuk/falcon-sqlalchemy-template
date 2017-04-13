from . import endpoints


pet_collection = endpoints.PetCollection()

routes = [
    ('/pets', pet_collection)
]
