import json 
import importlib.resources as pkg_resources


# data = json.dumps({
#     "scripts":"C:/codes/GUIs/Scriptx/UIs/Scripts.ui",
#     "logo":"C:/codes/GUIs/Scriptx/UIs/logo.jpg",
#     "enlarged":"C:/codes/GUIs/Scriptx/UIs/enlarged.ui"
#     })


# # with open("data.json","w") as f:
# #     json.dump(data,f)
# # print("Saved sucessfully ")


# sources = json.loads(str(json.load(open("./data.json","r"))))
# print(sources)
# print(sources["scripts"])


with pkg_resources.path("assets", 'Scripts.ui') as resource_path:
    print(resource_path)
    