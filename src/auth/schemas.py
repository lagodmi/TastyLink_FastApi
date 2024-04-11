from pydantic import BaseModel, EmailStr, Field, PositiveInt


class UserBase(BaseModel):
    username: str = Field(..., title="Логин", max_length=50)
    email: EmailStr = Field(..., title="Электронная почта", max_length=50)
    first_name: str = Field(..., title="Имя пользователя", max_length=100)
    last_name: str = Field(..., title="Фамилия пользователя", max_length=100)


class UserCreate(UserBase):
    password: str = Field(..., title="Пароль", max_length=20)


class User(UserBase):
    id: PositiveInt
    is_active: bool = Field(..., title="Активность")

    class Config:
        orm_mode = True


class FollowerBase(BaseModel):
    user_id: PositiveInt = Field(..., title="Автор")
    subscriber_id: PositiveInt = Field(..., title="Подписчик")


class Follower(FollowerBase):
    id: PositiveInt

    class Config:
        orm_mode = True
