from dotenv import load_dotenv
from os import getenv
from contextlib import contextmanager
import mysql.connector
from typing import TypeVar


T = TypeVar("T")
load_dotenv(".env")


class Access:
    """
    Get access to database
    """
    def __init__(self,
                 database: str,
                 host: str,
                 user: str,
                 password: str,
                 port: int = None
                 ) -> None:
        self.__port = port
        self.__database = database
        self.__host = host
        self.__user = user
        self.__password = password

    @property
    def port(self) -> int:
        return self.__port

    @property
    def database(self) -> str:
        return self.__database

    @property
    def host(self) -> str:
        return self.__host

    @property
    def user(self) -> str:
        return self.__user

    @property
    def password(self) -> str:
        return self.__password

    def __str__(self) -> str:
        return "ACCESS CLASS"

    @contextmanager
    def accessDataBase(self) -> T:
        """
        connect into mysql
        :return: cursor [generator]
        """
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        try:
            print(f"[+] Connected with {self.database}")
            yield connection.cursor()
        except Exception as e:
            print(f"Failed to connect\nERROR: {e}")
        finally:
            connection.commit()
            connection.close()


if __name__ == '__main__':
    access = Access(host=getenv("HOST"),
                    database=getenv("DATABASE"),
                    password=getenv("PASSWORD"),
                    user=getenv("USER"))
