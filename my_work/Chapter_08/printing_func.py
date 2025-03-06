def print_models(unprinted_models, completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model {current_model}...")
        completed_models.append(current_model)


def show_models(completed_models):
    for model in completed_models:
        print(f"Model {model} completed")


unprinted_models = ['geralt', 'ciri', 'ada wong']
completed_models = []
