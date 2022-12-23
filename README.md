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


<!-- Intent class | support | percision | recall | F1-score | Confused with |
Flight: 4, Airfare: 3
flight+airfare 12 1.0 0.41 0,58


flight_no 8 1.0 0.25 0.4 Flight: 6
flight_time 1 1.0 1.0 1.0
day_name 2 0.0 0.0 0.0 Flight: 2
Quantity 3 0.37 1.0 0.54
Airfare 48 0.88 1.0 0.94
Quantity: 4
Airline: 4
Flight 613 0.96 0.98 0.97
Distance 10 1.0 0.9 0.94 Airport: 1
Aircraft 8 0.7 0.87 0.77 quantity: 1
Flight: 1
Aircraft: 2
Capacity 21 1.0 0.80 0.89
ground_service: 1
airfare: 1
ground_fare 7 0.83 0.71 0.76
flight_no+airli
1 0.0 0.0 0.0 Flight:
1
ne
Airline 28 0.87 1.0 0.93
ground_servic 36 0.97 1.0 0.98 e
airfare+flight
1 0.0 0.0 0.0 Airfare:
1
Nlu_fallback:
1
City:
1
Airport 13 0.91 0.84 0.87
Flight:
3
Ground_fare:
1
City
5 0.2
0.2 0.2
flight+airline
1 0.0 0.0 0.0 Flight:
1
City:
1
Restriction:
1
Abbreviation 26 0.96
0.92 0.94
Flight:
3
City:
2
Meal
6 1.0 0.16 0.28 -->


## Results

### Intent Classifier

| Metric | Model 1 | Model 2 | Model 3 |
| ------------- | ------------- | ------------- | ------------- |
Weighted average precision | 0.96 | 0.88 | 0.94 |
Weighted average recall | 0.96 | 0.89 | 0.94 |
Weighted average f1 score | 0.96 | 0.88 | 0.93 |

**Comparison Intent Classifiers outputs:** https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/outputs_entity.csv

Intent classifier for model one is DIET, which is a 256-bit binary transformer that It is superior to model two, which is a linear SVM, and model three, which uses the MITIE language model.

### Entity Extractor

| Metric | Model 1 | Model 2 | Model 3 |
| ------------- | ------------- | ------------- | ------------- |
Weighted average .precision | 0.96 | 0.90 | 0.95 |
Weighted average recall | 0.94 | 0.89 | 0.92 |
Weighted average f1 score | 0.94 | 0.89 | 0.93 |

[**Comparison Entity Extractors outputs:**](https://github.com/smohammadi96/NLU_ATIS_dataset_RASA/blob/main/outputs_intent.csv)

In the first model, DIET is used as Entity extractor. As mentioned in the description, DIET can both classify intents and extract entities. In the second model, CRF is used as entity extractor, which has a lower efficiency than DIET. In the third model, MITIE Entity Extractor is used, which performs worse than DIET and better than CRF.
