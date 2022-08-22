import json
import csv

def read_json1(json_file):
    f = open(json_file)
    test = json.load(f)
    return test
   
def return_model_error(model_error):

    m = []
    for j in range(len(model_error)):
        m.append(model_error[j]['text'])
    
    return m
        
test = read_json1('test2.json')
samples = test['rasa_nlu_data']['common_examples']

model1_errors = read_json1('nlu-20220207-220347/DIETClassifier_errors.json')
m1 = return_model_error(model1_errors)
print(len(m1))
model2_errors = read_json1('nlu-20220218-130317/CRFEntityExtractor_errors.json')
m2 = return_model_error(model2_errors)
print(len(m2))
model3_errors = read_json1('nlu-20220218-204717/MitieEntityExtractor_errors.json')
m3 = return_model_error(model3_errors)
print(len(m3))

# list1 = []
# list1.append(['text', 'DIET_intent', 'sklearn_intent', 'MITIE_intent', 'groundtruth'])
# for i in range(len(samples)):
    # dict1 = []
    # text1 = samples[i]['text']
    # print(text1)
    
    # if text1 in m1:
        # text_index = m1.index(text1)
        # intent_model1 = model1_errors[text_index]['intent_prediction']['name']
        # print(intent_model1)
      
    # else:
        # intent_model1 = samples[i]['intent']
        
    # if text1 in m2:
        # text_index = m2.index(text1)
        # intent_model2 = model2_errors[text_index]['intent_prediction']['name']
    # else:
        # intent_model2 = samples[i]['intent']    
        
    # if text1 in m3:
        # text_index = m3.index(text1)
        # intent_model3 = model3_errors[text_index]['intent_prediction']['name']
    # else:
        # intent_model3 = samples[i]['intent']
    
    # dict1.append(text1)
    # dict1.append(intent_model1)
    # dict1.append(intent_model2)
    # dict1.append(intent_model3)
    # dict1.append(samples[i]['intent'])
    # list1.append(dict1)

# with open('data.json', 'w') as f:
    # json.dump(list1, f)

# with open("outputsdd_intent.csv", "w", newline="") as f:
    # writer = csv.writer(f)
    # writer.writerows(list1)

    
list1 = []
list1.append(['text', 'DIET_entity', 'CRF_entity', 'MITIE_entity', 'groundtruth'])
for i in range(len(samples)):
    dict1 = []
    text1 = samples[i]['text']
    print(text1)
    
    if text1 in m1:
        text_index = m1.index(text1)
        intent_model1 = model1_errors[text_index]['entities']
        print(intent_model1)
      
    else:
        intent_model1 = samples[i]['entities']
        
    if text1 in m2:
        text_index = m2.index(text1)
        intent_model2 = model2_errors[text_index]['entities']
    else:
        intent_model2 = samples[i]['entities']    
        
    if text1 in m3:
        text_index = m3.index(text1)
        intent_model3 = model3_errors[text_index]['entities']
    else:
        intent_model3 = samples[i]['entities']
    
    dict1.append(text1)
    dict1.append(intent_model1)
    dict1.append(intent_model2)
    dict1.append(intent_model3)
    dict1.append(samples[i]['entities'])
    list1.append(dict1)

with open("outputs_entity.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list1)