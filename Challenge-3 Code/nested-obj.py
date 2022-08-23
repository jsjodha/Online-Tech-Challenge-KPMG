
import json


def find_deep(input_str, check_key):
    obj = json.loads(input_str)
    #print("pattern to check" , check_key)

    keys =check_key.split("/")
    rs = None
    for key in keys:
        if isinstance(obj, dict):
            obj = obj.get(key, "Missing")
            rs = obj
            #print(obj)
        else:
            #print("Pattern does not match")
            rs  = None
    
    print("{} Pattern Matched !!!".format(check_key) if rs != None else "Invalid Pattern {}".format(check_key))



## Samples
find_deep('{"a":{"b":{"c":"d"}}}', "a/b/c")
find_deep('{"x":{"y":{"z":"a"}}}', "x/y/z")
find_deep('{"x":{"y":{"z":"a"}}}', "x/y/z/a")
