# Diabetes-prediction
Predict diabetes using a neural network trained on medical data (Keras &amp; TensorFlow).
## Dataset
The dataset `diabetes2.csv` contains the following features:

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of times pregnant |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body mass index (weight in kg/(height in m)^2) |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age in years |
| Outcome | Target variable (0: No diabetes, 1: Diabetes) |

> **Note:** The dataset has been cleaned and preprocessed in Excel prior to analysis.
>
> ### Folder Explanation

- **data/**: Contains the cleaned dataset.  
- **notebooks/**: Includes a Jupyter Notebook for **Data Analysis**:
  - Visualizing the distribution of Outcome using `seaborn.countplot`
  - Checking correlation between features using `seaborn.heatmap`
  - Understanding feature importance for the project  
- **scripts/**: Contains the main model script `diabet-DL.py`:
  - Reads the dataset
  - Prepares the training and testing sets
  - Designs and trains a **Sequential neural network**
  - Evaluates the model's performance
  - Predicts diabetes for a sample input
- **requirements.txt**: Lists Python libraries required for the project.  
- **README.md**: Provides detailed project documentation.  

---

## Data Analysis (Exploratory Analysis)

Before training the model, the dataset was analyzed to understand feature importance:

- Checked distribution of `Outcome` (0 vs 1)  
- Calculated correlation between features using a heatmap  
- This analysis helped to better understand which features are more impactful in predicting diabetes.

---

## Neural Network Model

- **Input layer:** 8 features  
- **Hidden layer 1:** 12 neurons, ReLU  
- **Hidden layer 2:** 8 neurons, ReLU  
- **Output layer:** 1 neuron, Sigmoid (binary classification)  
- **Loss function:** Binary Crossentropy  
- **Optimizer:** Adam  
- **Epochs:** 200  
- **Batch size:** 10

---

## How to Run
Clone the repository

---

## Example Output
Training Accuracy: 85.00%  
Testing Accuracy: 78.00%  
Sample prediction (for input [0, 200, 200, 1, 300, 35, 0.2, 19]): 0.92 → Predicts Diabetes

---
## Author
Milad Ganjali

## License
MIT License

