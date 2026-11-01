from datetime import datetime, date
from sqlalchemy import String, Integer, Float, Date, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class User(Base):
    __tablename__='users'
    id: Mapped[int]=mapped_column(Integer, primary_key=True); name: Mapped[str]=mapped_column(String(100)); email: Mapped[str]=mapped_column(String(150), unique=True, index=True); password_hash: Mapped[str]=mapped_column(String(255)); role: Mapped[str]=mapped_column(String(20), default='user'); created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
    profile=relationship('FinancialProfile', back_populates='user', uselist=False, cascade='all, delete-orphan')
class FinancialProfile(Base):
    __tablename__='financial_profiles'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id'), unique=True); age: Mapped[int|None]=mapped_column(Integer, nullable=True); monthly_income: Mapped[float]=mapped_column(Float, default=0); savings: Mapped[float]=mapped_column(Float, default=0); risk_tolerance: Mapped[str]=mapped_column(String(20), default='moderate'); updated_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user=relationship('User', back_populates='profile')
class Income(Base):
    __tablename__='income'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id'), index=True); source: Mapped[str]=mapped_column(String(40)); amount: Mapped[float]=mapped_column(Float); received_on: Mapped[date]=mapped_column(Date, default=date.today); description: Mapped[str|None]=mapped_column(Text, nullable=True)
class Expense(Base):
    __tablename__='expenses'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id'), index=True); category: Mapped[str]=mapped_column(String(40), index=True); amount: Mapped[float]=mapped_column(Float); spent_on: Mapped[date]=mapped_column(Date, default=date.today); description: Mapped[str|None]=mapped_column(Text, nullable=True)
class Investment(Base):
    __tablename__='investments'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id'), index=True); name: Mapped[str]=mapped_column(String(120)); investment_type: Mapped[str]=mapped_column(String(40)); amount_invested: Mapped[float]=mapped_column(Float); current_value: Mapped[float]=mapped_column(Float); purchase_date: Mapped[date]=mapped_column(Date); expected_return: Mapped[float]=mapped_column(Float, default=10); risk_level: Mapped[str]=mapped_column(String(20), default='medium')
class Goal(Base):
    __tablename__='financial_goals'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id'), index=True); name: Mapped[str]=mapped_column(String(120)); target_amount: Mapped[float]=mapped_column(Float); current_amount: Mapped[float]=mapped_column(Float, default=0); target_date: Mapped[date]=mapped_column(Date); priority: Mapped[str]=mapped_column(String(20), default='medium')
class Loan(Base):
    __tablename__='loans'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id')); lender: Mapped[str]=mapped_column(String(120)); outstanding_amount: Mapped[float]=mapped_column(Float); monthly_emi: Mapped[float]=mapped_column(Float, default=0)
class SimulationRun(Base):
    __tablename__='simulation_runs'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id')); initial_amount: Mapped[float]=mapped_column(Float); monthly_contribution: Mapped[float]=mapped_column(Float); annual_return: Mapped[float]=mapped_column(Float); volatility: Mapped[float]=mapped_column(Float); years: Mapped[int]=mapped_column(Integer); simulations: Mapped[int]=mapped_column(Integer); goal_target: Mapped[float|None]=mapped_column(Float, nullable=True); created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
class Scenario(Base):
    __tablename__='scenarios'
    id: Mapped[int]=mapped_column(primary_key=True); user_id: Mapped[int]=mapped_column(ForeignKey('users.id')); name: Mapped[str]=mapped_column(String(120)); income_change_pct: Mapped[float]=mapped_column(Float, default=0); expense_change_pct: Mapped[float]=mapped_column(Float, default=0); contribution_change: Mapped[float]=mapped_column(Float, default=0); created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
