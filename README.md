# NLU_ATIS_dataset_RASA


## dataset sample

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/ATIS_sample.PNG)

## Configs

### config 1

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config1.PNG))

### config 2

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config2.PNG))

### config 3

![alt text](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/images/config3.PNG))


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
