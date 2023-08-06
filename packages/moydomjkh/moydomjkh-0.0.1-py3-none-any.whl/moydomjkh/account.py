from moydomjkh.meter import Meter
import logging

_LOGGER = logging.getLogger(__name__)


class AccountException(BaseException):
    pass


class Account:
    def __init__(self, session, **kwargs):
        self.session = session
        self.inn = kwargs.get('inn')
        self.status = kwargs.get('status')
        self.account = kwargs.get('account')
        self.address = kwargs.get('address')
        self.account_id = kwargs['id_account']
        self.company_id = kwargs['id_company']
        self.status_text = kwargs.get('status_text')
        self.company_name = kwargs.get('company_name')
        self.company_full_name = kwargs.get('company_full_name')
        self.__balance = None
        self.balance_message = None
        self.__meters = None
        self.balance_history = []

    def __fetch_balance(self) -> None:
        data = self.session.call('user/account/balances',
                                 data={'id_company': self.company_id, 'id_account': self.account_id})
        self.__balance = -float(data['dolg']['value'])
        self.balance_message = data['dolg']['name']
        self.balance_history = data.get('year')

    def __fetch_meters(self) -> None:
        self.__meters = {}
        data = self.session.call('user/account/meters',
                                 data={'id_company': self.company_id, 'id_account': self.account_id})
        for item in data['meter']:
            item['id_company'] = self.company_id
            item['id_account'] = self.account_id
            obj = Meter(session=self.session, **item)
            self.__meters[f'{item["id_company"]}-{item["id_account"]}-{item["id_meter"]}'] = obj

    @property
    def meters(self):
        if self.__meters is None:
            self.__fetch_meters()
        return self.__meters

    @property
    def balance(self):
        if self.__balance is None:
            self.__fetch_balance()
        return self.__balance

    def to_json(self, verbose):
        result = {'account_id': f'{self.company_id}-{self.account_id}',
                  'account_name': self.account,
                  'meters': [v.to_json(verbose) for v in self.meters.values()],
                  'balance': self.balance}
        return result
        # if verbose == 2:
        #     result['accounts'] = {k: v.dumps(verbose) for k, v in self.accounts().items()}
