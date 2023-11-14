try:
    from sage_lib.FileManager import FileManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing FileManager: {str(e)}\n")
    del sys

class ForceFieldManager(FileManager):
    """
    Manages a collection of ForceFieldModel instances.
    This class allows for operations such as training, updating, and applying
    force fields on a collection of models.
    """

    def __init__(self):
        """
        Initialize the ForceFieldManager with an empty list of force field models.
        """
        self.models = []

    def add_model(self, model):
        """
        Add a new force field model to the manager.

        :param model: An instance of ForceFieldModel to be added.
        """
        self.models.append(model)

    def train_all(self, training_data):
        """
        Train all force field models using the provided training data.

        :param training_data: Data to be used for training all models.
        """
        for model in self.models:
            model.train(training_data)

    def predict_all(self, data):
        """
        Apply all force field models to the given data and return the results.

        :param data: The data to apply the models to.
        :return: A list of results from applying each model.
        """
        results = []
        for model in self.models:
            results.append(model.apply(data))
        return results

