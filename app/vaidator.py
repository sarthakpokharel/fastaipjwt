class Validator:
    def validation(model, required):
        for key, value in model.items():
            if value == "":
                print ("NONE is the item")
            