import psycopg2
from business_model.compte import Compte
from dao.abstract_dao import  AbstractDao


class CompteDao(AbstractDao):

    def create(self, compte):
        cur = AbstractDao.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO account (pseudo, motdepasse) VALUES (%s, %s) RETURNING id;", (compte.pseudo, compte.motdepasse))

            compte.id = cur.fetchone()[0]
            # la transaction est enregistrée en base
            AbstractDao.connection.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            AbstractDao.connection.rollback()
            raise error
        finally:
            cur.close()

        return compte

    def delete(self, compte):
        cur = AbstractDao.connection.cursor()
        try:
            cur.execute(
                "delete from account where id=%s", (compte.id,))

            # la transaction est enregistrée en base
            AbstractDao.connection.commit()
        except psycopg2.Error as error:
            # la transaction est annulée
            AbstractDao.connection.rollback()
            raise error
        finally:
            cur.close()

    def find_by_pseudo(self, pseudo):
        with AbstractDao.connection.cursor() as cur:
            cur.execute(
                "select id, pseudo, motdepasse from account where pseudo=%s", (pseudo,))

            found = cur.fetchone()
            if found:
                return Compte(found[1], found[2], found[0])

            return None
