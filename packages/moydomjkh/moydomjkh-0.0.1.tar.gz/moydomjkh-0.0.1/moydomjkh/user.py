import logging

from moydomjkh import Account

_LOGGER = logging.getLogger(__name__)


class UserException(BaseException):
    pass


class User:
    def __init__(self, session):
        self.session = session
        self.__accounts = None

    def __fetch_accounts(self) -> None:
        self.__accounts = {}
        data = self.session.call('user/accounts')
        for item in data['accounts']:
            obj = Account(session=self.session, **item)
            self.__accounts[f'{item["id_company"]}-{item["id_account"]}'] = obj

    @property
    def accounts(self):
        if self.__accounts is None:
            self.__fetch_accounts()
        return self.__accounts

    def to_json(self, verbose):
        result = {'accounts': [v.to_json(verbose) for v in self.accounts.values()]}
        return result
