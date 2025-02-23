# Potato-Disease-Classification--Project


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml (dvc init , dvc repro, dvc dag)

steps to run this project in your own system :

1.Clone the GitHub Repository
   
    "git clone https://github.com/kartheek2003/potato-disease-class.git"
    "cd potato-disease-class"

2.Create and Activate a Virtual Environment
   
    "python -m venv potenv"
    ".\potenv\Scripts\activate"

3.Install Dependencies

    "pip install -r requirements.txt"


4.Run the Application

    "python app.py"

5.train the model  (in any browser)
   "http://localhost:8080/train"

6.prediction
   "http://localhost:8080"
