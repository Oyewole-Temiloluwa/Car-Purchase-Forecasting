# Car Purchase Forecasting Project

## Overview
The Car Purchasing Prediction Project utilizes machine learning techniques to predict the likelihood of a customer purchasing a car based on various features. This project can be used to enhance sales strategies and target potential buyers more effectively.

## Features
- Data preprocessing and scaling
- Machine learning model training and prediction
- Web interface for making predictions

## Requirements
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Jupyter Notebook

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Oyewole-Temiloluwa/CarPurchaseForecasting.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CarPurchaseForecasting
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Files

### app.py
This is the main script that runs the web application. It uses Flask to create a web interface where users can input features and get predictions on car purchasing likelihood.

### car_purchasing.csv
This CSV file contains the dataset used for training the machine learning model. It includes various features related to customers and their car purchasing history.

### model.pkl
This file contains the trained machine learning model used for making predictions.

### scaler.pkl
This file contains the scaler used to normalize the data before making predictions.

### Notebook.ipynb
This Jupyter Notebook contains the data preprocessing steps, model training process, and evaluation metrics. It provides a detailed walkthrough of how the model was developed.

## Usage
1. Ensure you have the required packages installed.
2. Run the web application:
    ```bash
    python app.py
    ```
3. Open your web browser and go to `http://127.0.0.1:5000` to access the web interface.
4. Input the required features and click "Predict" to see the likelihood of a car purchase.

## How It Works
1. The `Notebook.ipynb` contains the data preprocessing, model training, and evaluation process.
2. The trained model and scaler are saved as `model.pkl` and `scaler.pkl`, respectively.
3. The `app.py` script loads these files and sets up a web interface using Flask.
4. Users can input features into the web interface, and the model will predict the likelihood of a car purchase.

## Contributing
Feel free to fork this repository, make your changes, and submit a pull request. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- The Scikit-learn library for providing the machine learning tools.
- Flask for the web framework.
- Pandas for data manipulation.
