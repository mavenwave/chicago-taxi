# Chicago Taxi
A wide and deep neural net implemented using the Keras Functional API to predict trip duration for Chicago taxi rides.

## Files
```
chicago-taxi
│   README.md
│   AI Platform.ipynb
|   hptuning_config.yaml
|   create_sample.py
|   requirements.txt
|   setup.py    
│
└───trainer
│   │   __init__.py
│   │   create_data_func.py
│   │   model.py
|   |   task.py
```
**AI Platform.ipynb** 
<br>
All of the commands necessary to tune, train, and host the neural network on AI Platform.

**hptuning_config.yaml**
<br>
Parameters to be used in hyperparameter tuning.

**create_sample.py**
<br>
A script that can be used to generate a sample model for inference.

**requirements.txt**
<br>
Packages required in order to complete the Training in local execution mode.

**setup.py**
<br>
Specifies additional packages that are required for a training job submission to AI Platform.

**trainer/create_data_func.py**
<br>
Logic required to complete preprocessing and generate training, validation, and test datasets.  This step is callable as an attribute in trainer/task.py.

**trainer/model.py**
<br>
Includes logic necessary to build the wide and deep neural network using the Keras Functional API.

**trainer/task.py**
<br>
Main module responsible for accepting input parameters and executing the training job.

## Running Instructions
Instructions for running the process are outlined in AI Platform.ipynb.
