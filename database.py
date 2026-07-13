import aiosqlite
from datetime import datetime


DB_NAME = "users.db"



async def init_db():

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            register_date TEXT,
            tariff TEXT DEFAULT 'FREE',
            vpn_used INTEGER DEFAULT 0
        )
        """)

        await db.commit()



async def add_user(user_id, username, first_name):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT id FROM users WHERE id = ?",
            (user_id,)
        )

        result = await cursor.fetchone()


        if result is None:

            await db.execute(
                """
                INSERT INTO users
                (
                id,
                username,
                first_name,
                register_date
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    user_id,
                    username,
                    first_name,
                    datetime.now().strftime(
                        "%d.%m.%Y"
                    )
                )
            )


            await db.commit()



async def get_user(user_id):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            """
            SELECT *
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )


        return await cursor.fetchone()



async def get_users_count():

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT COUNT(*) FROM users"
        )

        result = await cursor.fetchone()

        return result[0]



async def set_tariff(user_id, tariff):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            UPDATE users
            SET tariff = ?
            WHERE id = ?
            """,
            (
                tariff,
                user_id
            )
        )

        await db.commit()
        
async def get_all_users():

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            """
            SELECT *
            FROM users
            """
        )

        return await cursor.fetchall()
