# Bengaluru House Price Prediction

This project provides a comprehensive solution for predicting house prices in Bengaluru based on various input features such as square footage, number of bedrooms, number of bathrooms, and location.

## Project Structure

The project is organized into three main components:

### 1. Client

The `client` folder contains the front-end application, which allows users to interact with the house price prediction system. Users can input the property details, and the application provides them with an estimated house price based on the machine learning model's predictions.

### 2. Model

The `model` folder contains the Jupyter Notebook (`ipynb` file) that showcases the data preprocessing, exploratory data analysis, feature engineering, and model creation steps. It's an essential resource for understanding how the machine learning model was trained and the data used in the process.

### 3. Server

The `server` folder houses the back-end server built using Flask. This server serves as the bridge between the client application and the machine learning model. It handles user requests, processes the input data, and returns the predicted house prices using the trained model.

## How it Works

1. Users interact with the `client` front-end, providing property details, including square footage, number of bedrooms, number of bathrooms, and the location in Bengaluru.

2. The client application sends the input data to the `server` for processing.

3. The `server` uses the trained machine learning model, located in the `model` folder, to make predictions based on the input data.

4. The predicted house price is sent back to the client and displayed to the user.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.

2. Navigate to the `client`, `model`, and `server` directories and follow the setup instructions provided in their respective README files.

3. Make sure you have the necessary dependencies and libraries installed for both the client and server components.

4. Run the client and server applications to interact with the house price prediction system.

## Dependencies

The project relies on several libraries and frameworks, including but not limited to:

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

## Contribution

We welcome contributions to this project. If you have ideas for improvements or feature additions, feel free to open issues, create pull requests, or get in touch with us.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Disclaimer: This project is for educational and demonstration purposes. House price predictions are made using a machine learning model, and the accuracy may vary based on the quality and quantity of data used for training.*
