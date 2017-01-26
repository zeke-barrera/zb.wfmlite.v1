'''
Created on Jan 22, 2017

@author: ebarrer
'''

#Create an engineer class
class Engineer:
    def __init__(self, name, login, whid, role, bucket):
        self.name = name
        self.login = login
        self.whid = whid
        self.role = role
        self.bucket = bucket
    #method for retrieving the engineer's current attributes
    def get_stats(self):
        print "Name: %s \t Login: %s \t WHID: %s \t Role: %s \t Bucket: %s" % (self.name, self.login, self.whid, self.role, self.bucket)
    #the following methods are ways to adjust engineer attributes and will tie in with the GUI
    def change_name(self, new_name):
        self.name = new_name
    
    def change_whid(self, new_whid):
        self.whid = new_whid
        
    def change_role(self, new_role):
        self.role = new_role
        
    def change_bucket(self, new_bucket):
        self.bucket = new_bucket