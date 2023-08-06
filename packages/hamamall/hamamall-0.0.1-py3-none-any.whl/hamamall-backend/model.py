from lib2to3.pytree import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from typing import Optional

import numpy as np

class LottoTable(Base):
    __tablename__ = "t_lotto"
    
    no = Column(Integer, primary_key=True, index=True)
    num1 = Column(Integer, nullable=False)
    num2 = Column(Integer, nullable=False)
    num3 = Column(Integer, nullable=False)
    num4 = Column(Integer, nullable=False)
    num5 = Column(Integer, nullable=False)
    num6 = Column(Integer, nullable=False)
    bonus = Column(Integer, nullable=False)

class Lotto(BaseModel):
    t_lotto_no    : Optional[int] = 0
    t_lotto_num1  : int
    t_lotto_num2  : int
    t_lotto_num3  : int
    t_lotto_num4  : int
    t_lotto_num5  : int
    t_lotto_num6  : int
    t_lotto_bonus : Optional[int] = 0