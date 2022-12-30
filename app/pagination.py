table = 'users'
base_query = "select username, email from " + table

perPage = 10
pageNo = 1

searchables = ['username,','email']

search_term : str

#IF SEARCH TERM EXISTS
base_query = base_query + " WHERE"
for s in searchables:
    base_query = base_query + " "+ s 
    base_query = base_query + " ILIKE " + "'%"+search_term+"%' " + " OR"

#IF SEARCH TERM DOES NOT EXIST
base_query = base_query + " ILIKE " + " LIMIT 10 OFFSET 0"

# offset = ((pageNo - 1) * perPage)

#Front bata patahuna parne page number(HELPS CALCULATE OFFSET), per page (LIMIT)

#this should also return 'showing 2 of 256'


def Paginate(base_query):
    query = "SELECT * FROM table_name WHERE column_name ILIKE '%search_term%' LIMIT 10 OFFSET 0;"
    
    searchq = "SELECT * FROM users WHERE username ILIKE '%search_term%' OR email ILIKE '%search_term%'"
    
    base_query = base_query + ""
    
    if (search_term is None):
        base_query = base_query + " "
    else:
        base_query = base_query + " WHERE "
        for s in searchables:
            base_query = base_query + s +" "
            base_query = base_query + " ILIKE " + "%"+search_term+"% " + " LIMIT 10 OFFSET 0"