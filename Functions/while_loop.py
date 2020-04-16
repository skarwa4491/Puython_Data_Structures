unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models=[]

def unprinted_models(unprinted,completed=""):
    while unprinted:
        completed=unprinted.pop()
        completed_models.append(completed)
def show_completed_models():
    for item in completed_models:
        print(item)


unprinted_models(unprinted_designs)
show_completed_models()