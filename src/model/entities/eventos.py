from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String

class Eventos(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)