'''
Created on Jan 22, 2017

@author: ebarrer
'''

#Create and engineer class
class Engineer:
    def __init__(self, login, bucket, location, role):
        self.login = login
        self.bucket = bucket
        self.location = location
        self.role = role

eng_list = []

def list_engineers(eng_list):
    for i in range(len(eng_list)):
        print "Login: %20s Bucket: %20s Location: %20s Role: %20s" % (eng_list[i].login, eng_list[i].bucket, eng_list[i].location, eng_list[i].role)
        
list_engineers(eng_list)