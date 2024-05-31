from sqlalchemy import select, insert, delete, update
from integration_tests.config import settings
from integration_tests.database import async_session_maker
from integration_tests.models import Users, Product, TestUser, TestProduct
#  just example, not all models present

class UsersDAO:
    model = Users if settings.MODE == "DEV" else TestUser

    @classmethod
    async def get_user(cls, **filter_data):
        print(cls.model)
        async with async_session_maker() as session:
            query = select("*").select_from(cls.model).filter_by(**filter_data)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def add_user(cls, name, email):
        async with async_session_maker() as session:
            query = insert(cls.model).values(name=name, email=email)
            await session.execute(query)
            await session.commit()


class ProductDAO:
    model = Product if settings.MODE == "DEV" else TestProduct

    @classmethod
    async def add_product(cls, name, price):
        async with async_session_maker() as session:
            query = insert(cls.model).values(name=name, price=price)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_product(cls, **filter_data):
        async with async_session_maker() as session:
            query = select("*").select_from(cls.model).filter_by(**filter_data)
            results = await session.execute(query)
            return results.mappings().all()

    @classmethod
    async def update_product(cls, name, price):
        async with async_session_maker() as session:
            query = update(cls.model).where(name == cls.model.name).values(price=price)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_product(cls, **filter_data):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_data)
            await session.execute(query)
            await session.commit()
