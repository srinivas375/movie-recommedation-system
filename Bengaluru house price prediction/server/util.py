# import json
# import pickle
# import numpy as np

# __locations = None
# __model = None
# __data_columns = None



# def load_saved_artifacts():
#     print("loading saved artifacts...start")
#     global __locations
#     global __model
#     global __data_columns
    
#     with open("./artifacts/columns.json","r") as file:
#         __data_columns = json.load(file)['column']
#         __locations = __data_columns[3:]
        
#     with open("./artifacts/bengaluru_dataset.pickle","rb") as file:
#         __model = pickle.load(file)
        
#     print("loading saved artifacts .....done")


# def get_estimated_price(sqft, bath, bhk, location):
#     try:
#         loc = __data_columns.index(location.lower())
#     except:
#         loc = -1
    
#     a = np.zeros(len(__data_columns))
#     a[0] = sqft
#     a[1] = bath
#     a[2] = bhk
#     if loc >= 0:
#         a[loc] = 1
    
#     return round(__model.predict([a])[0], 2)



# def get_location_names():
#     return __data_columns




# if __name__ == '__main__':
#     load_saved_artifacts()
#     print(get_location_names())
#     print(get_estimated_price(1000,2,2,'Indira Nagar'))

















import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['column']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/bengaluru_dataset.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location