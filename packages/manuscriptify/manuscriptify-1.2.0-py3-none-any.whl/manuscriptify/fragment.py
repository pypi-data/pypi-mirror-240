# Manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Business Source Licence: https://mariadb.com/bsl11
"""
doc getter

"""
from manuscriptify.google_api.clients import Clients


class Fragment(list):

    def __init__(self, id_, creds=None):
        """get the content fragment"""
        docs = Clients(creds)['docs']
        doc = docs.documents().get(documentId=id_).execute()
        useful_stuff = ['paragraph']
        stuff = [{k:elem[k]}
                 for k in useful_stuff
                 for elem in doc['body']['content']
                 if k in elem]
        super().__init__(doc['body']['content'])
