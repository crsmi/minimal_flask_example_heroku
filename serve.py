import pickle
from forecast import Forecaster

# Function that takes loads in our pickled word processor
# and defines a function for using it. This makes it easy
# to do these steps together when serving our model.
def get_forecaster_api():
    # read in pickled word processor. You could also load in
    # other models as this step.
    with open("audl_forecaster.pkl", "rb") as file:
        f = pickle.load(file)

    # Function to apply our model & extract keywords from a
    # provided bit of text
    def forecaster_api(teams):
        forecast = f.forecast(teams[0],teams[1])
        return forecast

    # return the function we just defined
    return forecaster_api
