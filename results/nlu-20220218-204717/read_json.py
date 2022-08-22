import json

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

model1_errors = read_json1('DIETClassifier_errors.json')
m1 = return_model_error(model1_errors)
print(len(m1))
model2_errors = read_json1('CRFEntityExtractor_errors.json')
m2 = return_model_error(model2_errors)
print(len(m2))
model3_errors = read_json1('MitieEntityExtractor_errors.json')
m3 = return_model_error(model3_errors)
print(len(m3))

for i in range(len(samples)):
    text1 = samples[i]['text']
    print(text1)
    if text1 in m1:
        print('1111111111111')
        text_index = m1.index(text1)
        print(text_index)
        intent_model1 = model1_errors[text_index]
        print(intent_model1)
        print(rkjh)
    else:
        intent_model1 = samples[i]['intent']
    if text1 in m2:
        print('22222222222222')
        intent_model2 = m2
    else:
        intent_model2 = samples[i]['intent']    
    if text1 in m3:
        print('333333333')
        intent_model3 = m3
    else:
        intent_model3 = samples[i]['intent']

    
#    print(test['rasa_nlu_data']['common_examples'][0]['text'])
