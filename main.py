from enum import Enum
from turtle import st
from unittest import skip
from fastapi import FastAPI
from typing import Union


app=FastAPI()




'''
@app.get("/items/{item_id}")
async def read_item(item_id:str,needy:str,skip:int=0,limit:Union[str,None]=None):
    item={"item_id":item_id,"needy":needy,"skip":skip,"limit":limit}
    return item'''

'''@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}    
  


''''''
@app.get("/files/{file_path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

'''

@app.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id:str,item_id:str , q : Union[str,None]=None,short:bool=False):
    item={"item_id":item_id,"user_id":user_id}
    
    if q:
        item.update({"q":q})
    
    if not short:
        item.update(
            {"tanım": "kardeşler"}
        )

    return item














'''app=FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]
'''
'''@app.get("/items/{item_id}")
async def read_item(item_id:str,q:Union[str,None]=None):
  if q:
    return{"item_id":item_id,"q":q}
  return{"item_id":item_id}
  
'''


'''class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}'''
'''
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}


    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
       '''

'''class Item(BaseModel):
    name : str
    price : float
    is_offer : Union[bool,None]=None



@app.get("/")
async def read_root():
    return{"Hello":"world"}
'''
'''@app.get("/items/{item_id}")
def read_item(item_id:int , q:Union[str,None]=None):
    return{"item_id":item_id,"q":q}
    
@app.put("/items/{items_id}")
def update_item(item_id:int , item:Item):
    return{"item_name":item.name, "item_id":item_id }'''



