# Stepwise Selection

Select the optimal features in a dataset using the stepwise method.

## Instructions

1. Install:

pip install Selection_Method

2. Plug in your train and test dataset, and your preferred algorithm.

# Forward_Stepwise
from Selection_Method.Forward_Stepwise import forward_stepwise

# initialize forward_stepwise object, inputting your already split train and test dataframes, and your already created regression model object.

selection = forward_stepwise(x_train, x_test, y_train, y_test, linear_model)

# select the best features using the stepwise algorithm through the .select() method.

final_list, final_score = selection.select()

# Backward_Stepwise
from Selection_Method.Backward_Stepwise import backward_stepwise

# initialize backward_stepwise object, inputting your already split train and test dataframes, and your already created regression model object.

selection = backard_stepwise(x_train, x_test, y_train, y_test, linear_model)

# select the best features using the stepwise algorithm through the .select() method.

final_list, final_score = selection.select()
