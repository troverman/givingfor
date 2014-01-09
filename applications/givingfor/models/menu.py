##########################################
####title#################################
##########################################
if request.function == 'index':                                                                                                                                 
    response.title = 'givingfor'                                                                                                                              
else:
    response.title = request.function


##########################################
####markup################################
##########################################
response.meta.author = 'Trevor Overman <troverman@gmail.com>'
response.meta.description = 'giving is receiving!'
response.meta.keywords = 'giving, charity, humanist'
response.meta.generator = 'giving is receiving'


##########################################
####analytics#############################
##########################################
response.google_analytics_id = None
