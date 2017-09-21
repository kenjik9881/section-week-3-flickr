#using the sample_diction.json file to pull this data

import json

class Photo(object):
    def __init__(self, photo_diction):
        self.owner = photo_diction['owner']['username'] #just trying to get username
        self.title = photo_diction['title']['_content'] #Photo1
        self.tags = [] #initializing tags by looping through list of tags (dictionaries), creating a list of strings
        for tag in photo_diction['tags']['tag']:
            self.tags.append(tag['raw'])
        self.id = photo_diction['id']
        self.date_taken =photo_diction['dates']['taken']
        self.url = photo_diction['urls']['url'][0]['_content']
        self.license = photo_diction ['license']

        def __str__(self):
            return self.title
        def _repr__(self): #can get more details than string
            return "ID: {0}, Title: {1}, URL: {2}".format(self.id, self,title, self.url)

        def __contains__(self, test_string): #enable 'in' operator on this object/class
            return test_string in self.tags or test_string in self.title #checking if there is a string in self.tags which is a list

with open("sample_diction.json", "r") as f:
    f_string = f.read()
    response_diction = json.loads(f_string)

pd = response_diction['photo']
print (Photo(pd))


# f.close() #remember to close the file
