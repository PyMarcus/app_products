from os import getenv
from typing import Any
from dotenv import load_dotenv
from config.Access import Access


load_dotenv("./config/.env")


class ApiController:
    def __init__(self, values: Any):
        self.__values = values
        self.access = Access(host=getenv("HOST"),
                    database=getenv("DATABASE"),
                    password=getenv("PASSWORD"),
                    user=getenv("USER")
                    )

    @property
    def values(self):
        return self.__values

    def postSignIn(self) -> bool:
        sql: str = "INSERT INTO" \
                   " users(name, email, password, cpf)" \
                   f" VALUES {self.values};"
        print(f"[+] {sql}")

        with self.access.accessDataBase() as cursor:
            try:
                cursor.execute(sql)
            except Exception as e:
                print(f"[-] Fail to execute {e}")
                return False
            else:
                # send mail to user
                print("[+] success")
                return True
