from firebase import firebase

class FireDB():

    url = 'https://fresh-base-246509.firebaseio.com/'
    db = firebase.FirebaseApplication(url)

    def __init__(self,table_name,name,_id):
        self.table_name = table_name
        self.name = name
        self._id = _id
    
    def CreateData(self):
        return {
            'id' : self._id,
            'name' : self.name
        }
    
    def update(self):
        FireDB.db.put('/'+self.table_name,self.name,self.CreateData())


    def delete(self):
        FireDB.db.delete('/'+self.table_name,self.name,self.CreateData())

    def get(self):
        get_url = ('/'+self.table_name)
        FireDB.db.get(url=get_url)

# if __name__ == "__main__":
#     User('uncle','book2','12348586789').sendData()

class User(FireDB):
    def __init__(self, table_name,name,_id,session):
        super().__init__(table_name,name,_id)
        self.session = session

    def CreateData(self):
            data = {
            'id' : self._id,
            'name' : self.name
            }
            data['session'] = self.session
            print(data)
            return data

# if __name__ == "__main__":
#     User('uncle','book3','55555555',session = 'buying').update()
    



        




# engineer = {'id':1001,'name':'Uncle Engineer'}
# engineer2 = {'id':1002,'name':'Lung Tu'}

# result = messenger.put('/Project/user','Book',engineer)
# result2 = messenger.put('/Project/user','book2',engineer2)

# print("Engineer 1", result)
# print("Engineer 2", result2)
