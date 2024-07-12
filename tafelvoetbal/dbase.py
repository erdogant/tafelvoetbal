"""Database connection.

* Copyright (C) 2024-2025, E.Taskesen - All Rights Reserved
* Written by Erdogan Taskesen, <erdogant@gmail.com>, April 2024

"""

import streamlit as st
import json
from google.cloud import firestore
from google.oauth2 import service_account
from helper import check_internet_connection


# %%
class Dbase():
    def __init__(self, dbtype='firestore', projectname='tafelvoetbal-db', collection=None):
        """Initialize dbase with user-defined parameters."""
        self.dbtype = dbtype
        self.projectname = projectname
        self.collection = collection
        self.status = None
        self.message = None
        if not check_internet_connection():
            self.status = 'error'
            self.message = 'Internet connection failed'
            return

        # Connect to database
        self.connect(projectname=self.projectname)

    def connect(self, projectname='skywalk-db'):
        self.client = None
        if self.dbtype == 'firestore':
            try:
                # Get key
                key_dict = json.loads(st.secrets["firestore"]["textkey"])
                creds = service_account.Credentials.from_service_account_info(key_dict) #noqa
                # Access db
                self.client = firestore.Client(credentials=creds, project=projectname) #noqa
                # Set the status. The "success" state is used throughout the code. Do not change naming or it will break somewhere else.
                self.status = 'success'
                self.message = 'Connection succesfull'
            except Exception as e:
                self.status = 'error'
                self.message = 'Something else happened, completely unrelated to Firestore'

    def create_entry(self, document, values={}, collection=None, overwrite=False, verbose=False):
        if not self.db_status():
            return None
        if collection is None:
            collection = self.collection

        if self.dbtype == 'firestore':
            # Check whether entry exists
            if self.get_entry(document=document) is None:
                print(f'No entry found. New document for {document} will be created.')
                overwrite = True

            # Make the collection reference
            collection_ref = self.client.collection(collection)
            if overwrite:
                # Overwrite entry
                write_result = collection_ref.document(document).set(values)
            else:
                # Add new entry and keep the rest
                write_result = collection_ref.document(document).update(values)

            # Check
            if write_result:
                if verbose: print(f"Document '{document}' added to collection '{collection}' successfully.")
                return True
            else:
                if verbose: print("Error: Failed to add document to collection.")
                return False

    def get_entry(self, collection=None, document=None, values=None):
        if not self.db_status():
            return None

        if collection is None:
            collection = self.collection

        if self.dbtype == 'firestore':
            if document is None:
                collection_ref = self.client.collection(collection)
                # Get all documents from the collection
                docs = collection_ref.get()
                # Iterate over the documents and store data
                data = {}
                for doc in docs:
                    data[doc.id] = doc.to_dict()
                return None if data == {} else data
            else:
                # Get the document reference within the collection
                doc_ref = self.client.collection(collection).document(document)
                data = doc_ref.get()
                if data.exists:
                    # Return only the specific values in dict
                    data = data.to_dict()
                    if values is not None:
                        data = data.get(values, None)
                    # Return
                    return None if data == {} else data
                else:
                    return None

    def update(self, document, values, collection=None, verbose=False):
        if not self.db_status():
            return False

        if collection is None:
            collection = self.collection

        if self.dbtype == 'firestore':
            # Make the collection reference
            collection_ref = self.client.collection(collection)
            # Get the collection name
            key = next(iter(values))

            collection = self.get_entry(document=document, values=key)
            if collection is None: collection = {}
            # Update the collection with the new dict info
            collection.update(values[key])
            # Write back to collection
            write_result = self.create_entry(document=document, values={key: collection}, overwrite=False)
            # Show message
            if verbose: print(f"Update in document '{document}' with collection '{key}' successfull.")
            return True

    def db_status(self):
        if self.status is None or self.status != 'success':
            self.message = 'Database connection failed.'
            st.error(self.message)
            return False
        else:
            return True

