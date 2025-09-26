from sqlalchemy import create_engine, select, update, delete, func
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
            result = pd.read_sql_query(sql=query, con=conn)
            return result

    def get_all_temperatures(self):
        with self.engine.connect() as conn:
            query = select(Temperature)
            result = pd.read_sql_query(sql=query, con=conn)
            return result

    # 
    # ANALYTICS PAGE: DNF (not part of requirements. see L1-web-application/src/pages/analytics.py for details)
    #

    # def get_daily_readings(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id,
    #             func.count().label("count"),
    #             func.date(Temperature.timestamp).label("date")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp)
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_averages(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.avg(Temperature.temperature_c).label("avg_temp_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_minimums(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.min(Temperature.temperature_c).label("min_temp_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_maximums(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.max(Temperature.temperature_c).label("max_temp_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_std_dev(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.stddev(Temperature.temperature_c).label("std_dev_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_variance(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.var_pop(Temperature.temperature_c).label("var_pop_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

    # def get_daily_modes(self):
    #     with self.engine.connect() as conn:
    #         query = select(
    #             Temperature.sensor_id, 
    #             func.date(Temperature.timestamp).label("date"),
    #             func.mode(Temperature.temperature_c).label("mode_c")
    #         ).group_by(
    #             Temperature.sensor_id,
    #             func.date(Temperature.timestamp) 
    #         )
    #         result = pd.read_sql_query(sql=query, con=conn, parse_dates=["date"])
    #         return result

