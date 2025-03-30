import pandas as pd

# Load the dataset
df = pd.read_csv("E:\\only proj\\maternal_health_model.csv")  # Double backslashes


# Display the first few rows
print(df.head())
# Check for missing values
print(df.isnull().sum())

# Encode categorical variables (if any)
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['RiskLevel'] = le.fit_transform(df['RiskLevel'])  


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numerical_columns = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Define features and target
X = df.drop(columns=['RiskLevel'])  # Features
y = df['RiskLevel']  # Target

# Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
import joblib

# Save the trained model
joblib.dump(model, "maternal_health_model.pkl")
