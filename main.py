from databaseconn import usersCrud

from flask import Flask ,request


app = Flask(__name__)

dd= usersCrud()


########################################
############    Get Api    #############
########################################

@app.route('/user/get')
def getUsers():
    return dd.getuserDetails()


  ########################################
  ############    Add Api    #############
  ########################################
@app.route('/user/add', methods=['POST'])
def addUsers():
    return dd.addusersDetail(request.form)

  ##################################################
  ############    Add With Body Api    #############
  ##################################################
@app.route('/user/addbody', methods=['POST'])
def addUsersBody():


    return dd.addusersDetailBody(request.json)

  ###########################################
  ############    Update Api    #############
  ###########################################
@app.route('/user/update', methods=['PUT'])
def update():
    return dd.UpdateusersDetail(request.form)

 ###########################################
  ############    Delete Api    #############
  ###########################################
@app.route('/user/delete/<id>', methods=['DELETE'])
def delete(id):
    return dd.DeleteusersDetail(id)

  ########################################
  ###########   Run Program   ############
  ########################################
if __name__ == "__main__":
    app.run(debug=True , port=8000)