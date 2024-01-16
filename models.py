from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Voter(Base):
    __tablename__ = 'voters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    votes = relationship('Vote', back_populates='voter')

class Candidate(Base):
    __tablename__ = 'candidates'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    votes = relationship('Vote', back_populates='candidate')

class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    voter_id = Column(Integer, ForeignKey('voters.id'), nullable=False)
    candidate_id = Column(Integer, ForeignKey('candidates.id'), nullable=False)
    voter = relationship('Voter', back_populates='votes')
    candidate = relationship('Candidate', back_populates='votes')


