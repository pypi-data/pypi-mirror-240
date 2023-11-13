# first line: 64
def predict_message_intent(message, min_confidence=0.5):
    """Runs the trained model pipeline on a student's message

    >>> result = predict_message_intent('I want to change topics')
    >>> sorted(result.keys())
    ['confidence', 'data', 'intents', 'predict_probas', 'type']
    """
    global INTENT_RECOGNIZER_MODEL
    INTENT_RECOGNIZER_MODEL = INTENT_RECOGNIZER_MODEL or joblib.load(
        download_model(Path(MODEL_BUCKET) / MODEL_KEY)
    )

    pred_probas = INTENT_RECOGNIZER_MODEL.predict_proba([message])[0]

    predicted_labels_and_scores = pd.Series(
        list(pred_probas), index=INTENT_RECOGNIZER_MODEL.label_mapping
    )

    predictions = (
        predicted_labels_and_scores.sort_values(ascending=False)[:3].to_dict().items()
    )

    intents = [
        {"type": "intent", "data": name, "confidence": conf}
        for name, conf in predictions
    ]

    data = intents[0]["data"]
    confidence = intents[0]["confidence"]
    if confidence < min_confidence:
        data = "no_match"
        confidence = 0

    return {
        "type": "intent",
        "data": data,
        "confidence": confidence,
        "intents": intents,
        "predict_probas": [
            {"type": "intent", "data": name, "confidence": conf}
            for name, conf in predicted_labels_and_scores.to_dict().items()
        ],
    }
