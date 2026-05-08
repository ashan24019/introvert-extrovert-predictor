# Personality Predictor API

Machine Learning API to predict whether a person is an Introvert or Extrovert based on behavioral characteristics.


## API Endpoint

### POST

http://personality-predictor-env.eba-yrw5xypn.us-east-1.elasticbeanstalk.com/predict

## Example Request Body

```json id="w4y6pd"
{
  "Time_spent_Alone": 5,
  "Stage_fear": "No",
  "Social_event_attendance": 3,
  "Going_outside": 2,
  "Drained_after_socializing": "No",
  "Friends_circle_size": 7,
  "Post_frequency": 2
}
```

## Example Response

```json id="gbupiv"
{
  "personality": "Introvert",
  "confidence": 0.9508,
  "introvert_probability": 0.9508,
  "extrovert_probability": 0.0492
}
```

## Public URL

http://personality-predictor-env.eba-yrw5xypn.us-east-1.elasticbeanstalk.com/
