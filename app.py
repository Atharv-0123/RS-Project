from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pickled model file
with open('model.pkl', 'rb') as file:
    model_data = pickle.load(file)

# Define recommendation function
def recommend(restaurant_name):
    # Retrieve data from the loaded model
    cuisines = model_data['cuisines']
    mean_rating = model_data['mean_rating']
    cost = model_data['cost']

    # Perform recommendations based on the restaurant name
    # Add your recommendation logic here...

    # Return recommendations
    return cuisines, mean_rating, cost

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        restaurant_name = request.form['restaurant_name']

        # Call the recommendation function
        cuisines, mean_rating, cost = recommend(restaurant_name)

        # Pass the recommendations to the results page
        return render_template('results.html', cuisines=cuisines, mean_rating=mean_rating, cost=cost)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
