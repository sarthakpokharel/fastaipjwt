# from fastapi import Query, HTTPException
from app.database import db
import re
# from app.messages import Messages

# messages = Messages
    
class Validator:   
    
    def validation(model, required, table):   
        for key, value in model.items():
            if value == "":
                for r in required:
                    if r.lower() == key.lower():
                        return {"validation_code" : False,
                                "message": key +" cannot be empty"
                                }                
            else:
                if re.findall(r"<\s*script[^>]*>|<\s*/\s*script[^>]*>", value, re.IGNORECASE):
                    return {"validation_code" : 0,
                            "message": "Script tag not allowed"
                            }
                elif re.findall(r"[;-]", value):
                #this is supposed to replace them with whitespaces not throw an error, change that later
                    return {"validation_code" : 0,
                            "message": "; - special characters not allowed"
                            }
                else:
                    query = "SELECT " + key + " FROM " + table +" WHERE " + key + " = '" + value + "';"
                    if len(db.execute_query(query, res=True))>0:
                        return {"validation_code" : 1,
                                "message": "'"+value + "' already exists in " + key
                                }             
                    return True











            
                
                
                
                
                
                
                
                
        
#To Prevent Cross-site scripting (XSS)
# def escape_output(output: str):
# escape any special characters or HTML tags in the output
#   return html.escape(output)  



# def script_injection_filter(form_input):
#   # sanitize the name input by removing any script tags
# #   form_input.name = form_input.replace("<script>", "").replace("</script>", "")
#   form_input = re.sub(r"<script[^>]*>.*?</script>", "", form_input)
#   return form_input


# def sql_injection_filter(form_input):
#   # sanitize the name input by removing any semicolons or hyphens
#   form_input = re.sub(r"[;-]", "", form_input)
#   return form_input    

             
        # for key, value in model.items():
        #     for r in required:
        #         if r==key:
        #             if not value:
        #                 if r.lower() == key.lower:
        #                     return True
        #                 else: 
        #                     return False
        
        # for key, value in model.items():
        #     if not value:
        #         #chcek if it exists in required
        #         for r in required:
        #             if r.lower() == key.lower():
        #                 # value = messages.custom_message(key + ' cannot be empty:')
        #                 return True
        #             else:
        #                 return False
        

    
    # def read_items(q: str = Query(...,max_length=255)):
    #     if q.lower() == "error":
    #         raise HTTPException(status_code=400, detail="Error query not allowed")
    #     return {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}