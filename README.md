# Advanced XAI Project: Credit Score Modeling

## Overview
This project aims to develop an explainable AI (XAI) model for credit score prediction. The model provides not only accurate credit scoring but also interpretable insights into the factors influencing individual predictions. By integrating XAI techniques such as SHAP and LIME, the project enhances transparency, regulatory compliance, and stakeholder trust.

## Features
- **Credit Scoring Model**: Predicts the likelihood of borrower default.
- **Explainability Integration**: Uses SHAP and LIME for local and global interpretability.
- **Bias Mitigation**: Ensures fair lending practices through robust bias detection.

## Installation
To set up the project, follow these steps:

```sh
# Clone the repository
git clone https://github.com/ab3lT/Advanced-XAI-Project-Credit-Score-Modeling.git
cd Advanced-XAI-Project-Credit-Score-Modeling

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Training the Model
Run the following command to train the model:
```sh
python train.py
```

### Evaluating the Model
To evaluate model performance:
```sh
python evaluate.py
```

### Generating Explanations
To generate SHAP and LIME-based explanations:
```sh
python explain.py --input sample_data.json
```

## Explainability in Action
The project uses SHAP and LIME to interpret model decisions:
- **SHAP (SHapley Additive exPlanations)** provides a breakdown of feature importance across predictions.
- **LIME (Local Interpretable Model-agnostic Explanations)** generates local explanations for specific predictions.

## Deployment
To deploy the model as an API:
```sh
python app.py
```
The API will be available at `http://localhost:5000`.

## Ethical Considerations
- Ensures compliance with **GDPR** and **ECOA** regulations.
- Provides model transparency for fairness and bias mitigation.
- Allows users to contest and understand credit decisions.

## Contributing
Contributions are welcome! Please open an issue or pull request for suggestions or improvements.

## Project Team
This project was developed by the following team members:

| Name               | ID Number      |
|--------------------|---------------|
| Abel Tadesse      | GSR/2025/17   |
| Simreteab Mekbib  | GSR/4500/17   |
| Melat Dagnachew   | GSR/2402/17   |
