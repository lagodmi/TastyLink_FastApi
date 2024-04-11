from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


# Определение моделей данных
class User(Base):
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    is_active = Column(Boolean, default=True)

    followers = relationship("Follower", back_populates="user")


class Follower(Base):
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    subscriber_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)

    user = relationship("User", back_populates="followers", foreign_keys=[user_id])
    subscriber = relationship("User", foreign_keys=[subscriber_id])
