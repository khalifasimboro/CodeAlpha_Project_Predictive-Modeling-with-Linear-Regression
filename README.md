# CodeAlpha_Project_Predictive-Modeling-with-Linear-Regression

# House Price Prediction

This project leverages machine learning to predict house prices using a dataset of house sales in Seattle, USA. The primary goal is to build a linear regression model that accurately predicts house prices based on various features.

## Project Structure

1. **Data Preparation:**
   - Loading the dataset `kc_house_data.csv`.
   - Exploring and processing the data to prepare relevant features for the model.
   - Visualizing data distributions and identifying outliers.

2. **Modeling:**
   - Using linear regression to build the price prediction model.
   - Splitting the dataset into training and testing sets.
   - Applying logarithmic transformation to certain features to improve model accuracy.

3. **Model Evaluation:**
   - Evaluating the model using metrics like Mean Squared Error (MSE), Mean Absolute Error (MAE), and R² Score.
   - Visualizing predictions against actual values.

4. **Deployment:**
   - Saving the trained model in `pkl` format for local deployment.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Khalifasimboro/CodeAlpha_Project_Predictive-Modeling-with-Linear-Regression
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Load the saved model (`model.pkl`).
2. Use the `pipeline` function to predict the price of a house based on its features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## ML-Model-Flask-Deployment
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.
5. Source code : The notebook wich contain the code line of data processing and the creating of the model

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Homepage.png)

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
## Contribution

Contributions are welcome! If you would like to contribute, please submit a pull request with a detailed description of the changes.
