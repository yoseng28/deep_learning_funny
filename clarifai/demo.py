from clarifai import rest
from clarifai.rest import ClarifaiApp


app = ClarifaiApp("GyofBHxUbjQxOYizbpO0Rr9XdkK8aflZZtb5r0au", "2zEWNYG5Ab1K9EdH0uWaItmMg4mko38ii7QzeDmD")

# get the general model
model = app.models.get("general-v1.3")

# predict with the model
#result = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
result = model.predict_by_filename('3.jpg')

print(result)