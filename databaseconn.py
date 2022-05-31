import mysql.connector
import json

class usersCrud():
  ########################################
  ######### DataBase Connection ##########
  ########################################
  def __init__(self):
    try:
        self.con = mysql.connector.connect(
          host="localhost",
          database='test',
          user="root",
          password="junaid4422"
        )
        self.con.autocommit=True
        self.cur=self.con.cursor(dictionary=True)
        print('successfully')
    except Exception as e:
        print('error',e)

  ########################################
  ############    Get Api    #############
  ########################################
  def getuserDetails(self):
    self.cur.execute("SELECT * FROM users")
    result =self.cur.fetchall()

    if len(result)>0:

      dd ={"status":True,
           "massage":"successfull",
           "res":result}
      return json.dumps(dd)
    else:
      dd = {"status": True,
            "massage": "no result found",
            "res": []
            }
      return json.dumps(dd)


  ########################################
  ############    Add Api    #############
  ########################################
  def addusersDetail(self,userInput):
    self.cur.execute(f"INSERT INTO users(first_name, last_name, email) VALUES ('{userInput['first_name']}','{userInput['last_name']}','{userInput['email']}')")
    return 'User created'

    ########################################
    ############    Add Api    #############
    ########################################

  def addusersDetailBody(self, userInput):
    self.cur.execute(
      f"INSERT INTO users(first_name, last_name, email) VALUES ('{userInput['first_name']}','{userInput['last_name']}','{userInput['email']}')")
    return 'User body created'

  ########################################
  ############    Update Api    #############
  ########################################
  def UpdateusersDetail(self,userInput):
    self.cur.execute(f"UPDATE users SET first_name='{userInput['first_name']}',last_name='{userInput['last_name']}',email='{userInput['email']}' WHERE id={userInput['id']} ")
    return 'User Update successfully'

    ########################################
    ############    Update Api    #############
    ########################################

  def DeleteusersDetail(self, id):
    self.cur.execute(
      f"DELETE FROM users WHERE id={id} ")
    return 'User Deleted successfully'
