################################################################
####controllers#################################################
################################################################

################################
####about#######################
################################
def about():

    return dict(message=T('Hello World'))  

################################
####account#####################
################################
def account():

    return dict(message=T('Hello World'))

################################
####discover####################
################################
def discover():

    return dict(message=T('Hello World'))  


################################
####faq#########################
################################
def faq():

    return dict(message=T('Hello World'))    

################################
####index#######################
################################
def index():
    project_list = db(db.project).select()

    return dict(project_list=project_list)


################################
####member######################
################################
def member():

    return dict(message=T('Hello World'))
    
################################
####mission#####################
################################
def mission():

    return dict(message=T('Hello World')) 

################################
####privacy#####################
################################
def privacy():

    return dict(message=T('Hello World'))   

################################
####partner#####################
################################
def partner():

    return dict(message=T('Hello World')) 

################################
####partners####################
################################
def partners():
    return dict(message=T('Hello World')) 

################################
####project#####################
################################
def project():
    try:
        selected_project = db(db.project.url_title == request.args(0)).select()

    except IndexError:
        redirect(URL('projects'))

    return dict(selected_project=selected_project)

################################
####projects####################
################################
def projects():
    project_list = db(db.project).select()

    return dict(project_list=project_list)

################################
####search######################
################################
def search():
    return dict(message=T('Hello World'))  

################################
####terms#######################
################################
def terms():

    return dict(message=T('Hello World'))

################################
####transparency################
################################
def transparency():

    return dict(message=T('Hello World'))

################################################################
####helpers#####################################################
################################################################

service = Service(globals())

@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

@auth.requires_signature()
def data():
    return dict(form=crud())