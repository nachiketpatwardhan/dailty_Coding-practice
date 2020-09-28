import json
import re

Dict_parameters = {}
Dict_template = {}
json_object = {}


def function_parse_parameters():
    #load parameters JSON file
    with open('C:\\Users\\Nachiket\\Downloads\\template (2)\\parameters.json') as parameters_json:
        data_parameters = json.load(parameters_json)

    
    #to get the value associated with the 'parameters' key as a root
    d_parameters = data_parameters.get('parameters')

    #print(d_parameters)

    d_parameters_key = []
    d_parameters_value = []

    for key,value in d_parameters.items():
        #print(key, '-->', value)
        d_parameters_key.append(key)
        d_parameters_value.append(value)

    #print(d_parameters_key)

    d_parameters_key_value = []
    d_parameters_key_key = []

    for key in d_parameters_key:
        #print(key)
        key_name = d_parameters.get(key)
        #print("This is Key name", key_name)
        for key,value in key_name.items():
            #print(key, '-->', value)
            d_parameters_key_key.append(key)
            d_parameters_key_value.append(value)
        
    #print(d_parameters_key_value)

    global Dict_parameters 
    Dict_parameters = dict(zip(d_parameters_key,d_parameters_key_value))

    #print("This are params", Dict_parameters)
    return Dict_parameters


def function_parse_template(dict_params):
    with open('C:\\Users\\Nachiket\\Downloads\\template (2)\\template.json') as template_json:
        Dict_template = json.load(template_json)

    print("This is data_template",Dict_template)

    #make it generic & robust
    for k2,v2 in Dict_template.items():
        if isinstance(v2, list):
            for e in v2:
                for k1,v1 in Dict_parameters.items():
                    for k,v in e.items():
                        #print("this is e:", e)
                        #print(e.keys())
                        try:
                            x = re.search(k1, v)
                            if x:
                                print("YES! We have a match!")
                                print("k2:", k2, "k1:", k1, "k:", k, "v:", v, "v1:", v1)
                                e[k] = v1
                            else:
                                print("No match")
                        except:
                            pass
                        
        else:
            pass
                

    print("Final",Dict_template)

    json_object = json.dumps(Dict_template, indent = 4)   
    print(json_object)
    return Dict_template
    

def function_writeJSON_outputFile(dict):
    with open("C:\\Users\\Nachiket\\Downloads\\template (2)\\sample_output.json", "w") as outfile:  
        json.dump(dict, outfile)
         

        

def main():
    dict_params=function_parse_parameters()
    dict_template = function_parse_template(dict_params)
    function_writeJSON_outputFile(dict_template)

if __name__=="__main__": 
    main() 
