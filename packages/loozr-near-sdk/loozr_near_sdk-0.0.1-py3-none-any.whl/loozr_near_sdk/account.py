import time

from loozr_near_sdk.utils.base import Base, LZR_MIXER_ACCOUNT_ID
from near_api.account import Account, TransactionError
from near_api.signer import Signer

from loozr_near_sdk.utils.constants import ACCOUNT_INIT_BALANCE


class AccountHelper(Base):
    def check_account(self, account_id):
        """Gets account details of `account_id` from
        the near blockchain or throw a JsonProviderError
        if account does not exist"""
        res = self.provider.get_account(account_id)
        return res

    def get_account_details(self, account_id):
        return self.provider.get_account(account_id)

    def get_account_id_from_name(self, account_name):
        return "%s.%s" % (account_name, LZR_MIXER_ACCOUNT_ID)

    def get_new_id_from_name(self, account_name):
        return "%s-%s.%s" % (account_name, int(
            time.time() * 10_000), LZR_MIXER_ACCOUNT_ID)

    def create_account(self, account_id, amount=ACCOUNT_INIT_BALANCE):
        res = self.lzr_mixer_account.create_account(
            account_id, self.lzr_mixer_account.signer.public_key, amount)
        signer = Signer(
            account_id, self.lzr_mixer_account.signer.key_pair)
        account = Account(
            self.lzr_mixer_account.provider, signer, account_id)
        return account, res

    def create_another_if_exist(self, account_name: str, amount=10 ** 24):
        account_id = self.get_account_id_from_name(
            account_name)
        try:
            if self.get_account_details(account_id):
                account_id = self.get_new_id_from_name(account_name)
                return self.create_account(account_id, amount)
        except TransactionError:
            return self.create_account(account_id, amount)
