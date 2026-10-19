# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, HOST, PORT, DB, COL): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'YourSecurePasswordHere' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # i
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        """
        Inserts a document into a specified MongoDB database
        Input: data(dict) - key/value pairs
        Output: True for successful insertion, false otherwise
        """
        if data is not None:
            try:
                self.database.animals.insert_one(data)  # data should be dictionary  
                return True
            except Exception as e:
                print(f"Insert Failed: {e}")
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            

    # Create method to implement the R in CRUD.
    def read(self, query=None):
        """
        Queries a document from a specified MongoDB database using find()
        Input: query(dict) - key/value pairs
        Output: list - a list of documents if successful, else and empty list
        """
        if query is not None:
            try:
                cursor = self.database.animals.find(query)
                result_list = list(cursor)
                return result_list
            except Exception as e:
                print(f"Query failed: {e}")
                return []
        else: 
            raise Exception("Query failed: Query must be a dictionary")
            
        
    #Create method to implement the U in CRUD.
    def update(self, query, update_data):
        """
        Queries for and changes document(s) from a specified MongoDB database and specified collection
        Input: key/value lookup pair, acceptable key/value pair data type for update_one() or update_many()
        Output: number of objects modified
        """
        if query is not None and update_data is not None:
            try:
                result = self.database.animals.update_many(query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            print("Both query and update_data must be provided")
            return 0
        
    #Create method to implement the D in CRUD
    def delete(self, query):
        """
        Queries for and removes documeent(s) from a specified MongoDB database and specified collection
        Input: key/value lookup pair
        Output: number of removed objects
        """
        if query is not None:
            try:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            print("Query must be a dictionary")
            return 0