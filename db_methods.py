from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import Session
import pandas as pd
from typing import Union
from .db_orm import User, Temperature
from pathlib import Path

class DB:
    def __init__(self, db_path):    
        self.engine = create_engine(db_path, echo=False)

    def get_all_users(self):
        with self.engine.connect() as conn:
            query = select(User)
            result = pd.read_sql_query(query, con=conn)
            return result

    def get_all_temperatures(self):
        with self.engine.connect() as conn:
            query = select(Temperature)
            result = pd.read_sql_query(query, con=conn)
            return result