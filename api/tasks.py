from celery import shared_task
from .models import BlacklightNeuralNetworkRun
import os
from django.conf import settings
from blacklight.autoML import FeedForward


@shared_task
def fit_neural_network(nn_id, X_train, y_train, X_test, y_test, options):
    nn = BlacklightNeuralNetworkRun.objects.get(id=nn_id)
    nn.status = "in progress"
    nn.save()

    # Initialize your custom FeedForward class
    ff = FeedForward(
        number_of_individuals=options["number_of_individuals"],
        num_parents_mating=options["num_parents_mating"],
        death_percentage=options["death_percentage"],
        number_of_generations=options["number_of_generations"],
        options=options["options"]
    )

    ff.fit(X_train, y_train, X_test, y_test)

    # Save the model to a file
    model_filename = f"model_{nn_id}.h5"
    model_path = os.path.join(settings.MEDIA_ROOT, model_filename)
    ff.model.save(model_path)

    nn.status = "completed"
    nn.result = "your_result_representation"  # Serialize the result as needed
    nn.save()
