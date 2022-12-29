class Messages:
    def success():
        return {'message' : 'Success'}

    def error():
        return {"message" : "Failire"}
    
    def custom_message(custom_message):
        return {"message": custom_message}