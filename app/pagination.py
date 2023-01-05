class Pagination:
    def page(table, perPage, pageNo, searchables, search_term, order_by, column_names, orand):
        base_query = "SELECT "
        count_query = base_query + "count (*)"
        for c in column_names:
            base_query = base_query + c + ", "

        base_query = base_query[:-2]
        base_query = base_query + " FROM " + table
        count_query = count_query + " FROM " + table

        search_terms = ["{} ILIKE '%{}%'".format(s, search_term) for s in searchables]
        if orand == "OR":
            search_clause = " OR ".join(search_terms)
        elif orand == "AND":
            search_clause = " AND ".join(search_terms)
        else:
            return "Invalid OR/AND Clause"
        base_query = "{} WHERE {}".format(base_query, search_clause)
        count_query = "{} WHERE {}".format(count_query, search_clause)
        offset = ((pageNo-1) * perPage)

        try:
            base_query = base_query + " ORDER BY " + column_names[0] + ' ' + order_by 
        except:
            print("Error")
        base_query = base_query + " LIMIT " + str(perPage) + ' offset ' + str(offset)
        return {
            "base_query" : base_query,
            "count_query" : count_query}   


# searchables = ["username like '%one%'","email like '%asdjfl%'"]
# condtn = " OR ".join(searchables)




# table = 'users'
# base_query = "SELECT username, email FROM " + table+"t1 join table2 t2 on t2.id=t.id"

# perPage:str = 10
# pageNo:int = 1

# searchables = ['username','email']

# search_term = 'search'

# base_query = base_query + " WHERE"
# for s in searchables:
#     base_query = base_query + " "+ s 
#     base_query = base_query + " ILIKE " + "'%"+search_term+"%' " + "OR"

# base_query = base_query[:-3]
# offset = ((pageNo-1) * perPage)

# base_query = base_query + " LIMIT " + str(perPage) + ' offset ' + str(offset) 

# print (base_query)


# table = 'users'
# base_query = "select username, email from " + table

# perPage = 10
# pageNo = 1

# searchables = ['username,','email']

# search_term : str

# #IF SEARCH TERM EXISTS
# base_query = base_query + " WHERE"
# for s in searchables:
#     base_query = base_query + " "+ s 
#     base_query = base_query + " ILIKE " + "'%"+search_term+"%' " + " OR"

# #IF SEARCH TERM DOES NOT EXIST
# base_query = base_query + " ILIKE " + " LIMIT 10 OFFSET 0"

# # offset = ((pageNo - 1) * perPage)

# #Front bata patahuna parne page number(HELPS CALCULATE OFFSET), per page (LIMIT)

# #this should also return 'showing 2 of 256'


# def Paginate(base_query):
#     query = "SELECT * FROM table_name WHERE column_name ILIKE '%search_term%' order by username asc LIMIT 10 OFFSET 0;"
    
#     searchq = "SELECT * FROM users WHERE username ILIKE '%search_term%' OR email ILIKE '%search_term%'"
    
#     base_query = base_query + ""
    
#     if (search_term is None):
#         base_query = base_query + " "
#     else:
#         base_query = base_query + " WHERE "
#         for s in searchables:
#             base_query = base_query + s +" "
#             base_query = base_query + " ILIKE " + "%"+search_term+"% " + " LIMIT 10 OFFSET 0"


