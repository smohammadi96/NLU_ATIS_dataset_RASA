# NLU_ATIS_dataset_RASA

[RASA](https://rasa.com/) | 
[ATIS dataset](https://datasets.activeloop.ai/docs/ml/datasets/atis-dataset/)

Train Natural Language Understanding (NLU) on ATIS dataset:

**Steps:**
- Tockenizer
- Featurizer
- Intent Classification
- Entity Recognition and Extraction


## Dataset

ATIS dataset has been used in the training and evaluation stage, which has 4978 sentences for the training dataset and 850 sentences for the evaluation stage.

### Sample

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/ATIS_sample.PNG)

## Configs

### config 1

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config1.PNG))

### config 2

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config2.PNG))

### config 3

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config3.PNG))

## How to run?

Ubuntu 18.04

### install requirements

`python3 -m venv ./venv`

`source ./venv/bin/activate`

`pip3 install -U --user pip`

`pip3 install rasa`

### training

`rasa train nlu -u train.json -c config.yml`

### evaluation

`rasa test nlu -u test.json --model models/nlu-20220215-184331.tar.gz`

## Results

### Intent Classifier

| Metric | Model 1 | Model 2 | Model 3 |
| ------------- | ------------- | ------------- | ------------- |
Weighted average precision | 0.96 | 0.88 | 0.94 |
Weighted average recall | 0.96 | 0.89 | 0.94 |
Weighted average f1 score | 0.96 | 0.88 | 0.93 |

[**Comparison Intent Classifiers outputs**](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/outputs_intent.csv)

Intent classifier for model one is DIET, which is a 256-bit binary transformer that It is superior to model two, which is a linear SVM, and model three, which uses the MITIE language model.

### Entity Extractor

| Metric | Model 1 | Model 2 | Model 3 |
| ------------- | ------------- | ------------- | ------------- |
Weighted average .precision | 0.96 | 0.90 | 0.95 |
Weighted average recall | 0.94 | 0.89 | 0.92 |
Weighted average f1 score | 0.94 | 0.89 | 0.93 |

[**Comparison Entity Extractors outputs**](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/outputs_entity.csv)

In the first model, DIET is used as Entity extractor. As mentioned in the description, DIET can both classify intents and extract entities. In the second model, CRF is used as entity extractor, which has a lower efficiency than DIET. In the third model, MITIE Entity Extractor is used, which performs worse than DIET and better than CRF.
