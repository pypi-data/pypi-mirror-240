# Manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Business Source Licence: https://mariadb.com/bsl11
"""
google api client logic

"""
from googleapiclient.discovery import build

from manuscriptify.google_api.auth import Auth

class Clients(dict):
    """Google API clients"""

    def __init__(self, token=None):
        if not token:
            token = Auth()
        docs = build('docs', 'v1', credentials=token)
        drive = build('drive', 'v3', credentials=token)
        clients = {
            'docs': docs,
            'drive': drive
        }
        super().__init__(**clients)
