import logging
from app.models.models import *
from app.models.dtos import *

from psycopg2 import pool, extras
from contextlib import contextmanager
from app.utils.config import config
from typing import List, Dict

logger = logging.getLogger(__name__)

class PostgresRepository:
    def __init__(self):
        self.pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname=config.POSTGRES_DATABASE,
            user=config.POSTGRES_USER,
            password=config.POSTGRES_PASSWORD,
            host=config.POSTGRES_HOST,
            cursor_factory=extras.RealDictCursor,
        )

    @contextmanager
    def connection(self):
        conn = self.pool.getconn()
        try:
            yield conn
        finally:
            self.pool.putconn(conn)

    def get_burgers(self, offset: int, limit: int) -> List[BurgerRead]:
        query = "SELECT * FROM burgers OFFSET %s LIMIT %s"
        params=(offset, limit)
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    results = cur.fetchall()
                    logger.debug(f"Fetched {len(results)} number of rows from burgers.")
        except Exception as e:
            logger.error("DB query error: %s", e)
            raise
        
        return [Burger(**record) for record in results]

    def get_burger_by_id(self, id: int) -> Optional[Burger]:
        query = f"SELECT * FROM burgers WHERE burger_id = %s"
        params = (id,)
        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    result = cur.fetchone()

                    if result:
                        logger.debug(f"Fetched burger with ID: {id}")
                    else:
                        logger.debug(f"No burger found with ID: {id}")
        except Exception as e:
            logger.error("DB query error: %s", e)
            raise

        return Burger(**result) if result else None

    def insert_burger(self, name: str, description: str) -> int:
        query = """
            INSERT INTO burgers (name, description)
            VALUES (%s, %s)
            RETURNING id
        """
        params = (name, description)

        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    burger_id = cur.fetchone()["burger_id"]
                    conn.commit()
                    logger.debug(f'New burger added ID: {burger_id}')
                    return burger_id
        except Exception as e:
            logger.error("DB insert error: %s", e)
            raise

    def delete_burger(self, id: int) -> None:
        query = """
            DELETE FROM burgers
            WHERE burger_id = %s
            RETURNING id
        """
        params = (id,)

        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    deleted_row = cur.fetchone()
                    if not deleted_row:
                        raise ValueError(
                            f"No burger found with ID: {id}"
                        )
                    conn.commit()
                    logger.debug(
                        f"Deleted burger with ID: {id}"
                    )
        except Exception as e:
            logger.error("DB delete error: %s", e)
            raise

    def get_burger_ingredients(self, burger_id: int) -> List[IngredientRead]:
        query = """
        SELECT i.ingredient_id, i.name, i.is_available
        FROM ingredients as i
            INNER JOIN burger_ingredients as bi ON i.ingredient_id = bi.ingredient_id
        WHERE bi.burger_id = %s
        """
        params = (burger_id,)

        try:
            with self.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, params)
                    results = cur.fetchall()
                    logger.debug(f"Fetched ingredients for burger with ID: {burger_id}")
        except Exception as e:
            logger.error("DB query error: %s", e)
            raise
        
        return [IngredientRead(**record) for record in results]
