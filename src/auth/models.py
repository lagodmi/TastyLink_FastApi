# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base

# # Создание базы данных
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db_name"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Определение моделей данных
# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     is_active = Column(Boolean, default=True)

#     followers = relationship("Follower", back_populates="user")

# class Follower(Base):
#     __tablename__ = "followers"

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     subscriber_id = Column(Integer, ForeignKey("users.id"))

#     user = relationship("User", back_populates="followers", foreign_keys=[user_id])
#     subscriber = relationship("User", foreign_keys=[subscriber_id])

# # Создание таблиц в базе данных
# Base.metadata.create_all(bind=engine)
