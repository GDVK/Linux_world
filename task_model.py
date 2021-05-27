import joblib
model = joblib.load("salary_model.pkl")

#predict
years=int(input("Enter years of experience: "))
predict=model.predict([[years]])
print("Your salary as per your year of experience is :",round(predict[0],2)," INR")