class Messages:
    def success():
        return {'message' : 'Query Success'}

    def error():
        return {"message" : "Query Failure"}

    def null():
        return {"message" : "No Value"}
    
    def custom_message(custom_message):
        return {"message": custom_message}