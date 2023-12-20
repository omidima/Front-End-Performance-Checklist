import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MultiLabelBinarizer
import joblib

data = json.loads(open("data.json","r").read())

mlb = MultiLabelBinarizer()
categories = [phone["content"]["usages"] for phone in data]
encoded_categories = mlb.fit_transform(categories)

X_train, X_test, y_train, y_test = train_test_split(data, encoded_categories, test_size=0.2, random_state=42)

def extract_features(phone):
    return [
        phone["post"]["price"],
        phone["post"]["image_count"],
        len(phone["content"]["usages"]),
    ]

X_train_features = [extract_features(phone) for phone in X_train]
X_test_features = [extract_features(phone) for phone in X_test]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_features, y_train)

y_pred = model.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Classification Report:\n", classification_report(y_test, y_pred))

joblib.dump(model, 'phone_classifier_model.joblib')

