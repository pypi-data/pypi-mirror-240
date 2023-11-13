# Copyright © Aptos Foundation
# SPDX-License-Identifier: Apache-2.0

import logging
import time
from typing import Any, Dict, List, Optional

import httpx

from .account import Account
from .account_address import AccountAddress
from .authenticator import Authenticator, MultiAgentAuthenticator
from .bcs import Serializer
from .metadata import Metadata
from .transactions import (
    EntryFunction,
    MultiAgentRawTransaction,
    RawTransaction,
    SignedTransaction,
    TransactionArgument,
    TransactionPayload,
)

U64_MAX = 18446744073709551615


class ClientConfig:
    """Common configuration for clients, particularly for submitting transactions"""

    expiration_ttl: int = 600
    gas_unit_price: int = 100
    max_gas_amount: int = 100_000
    transaction_wait_in_seconds: int = 20
    http2: bool = False


class RestClient:
    """A wrapper around the Aptos-core Rest API"""

    _chain_id: Optional[int]
    client_class: httpx.Client
    client_config: ClientConfig
    base_url: str

    def __init__(self, base_url: str, client_config: ClientConfig = ClientConfig()):
        self.base_url = base_url
        # Default limits
        limits = httpx.Limits()
        # Default timeouts but do not set a pool timeout, since the idea is that jobs will wait as
        # long as progress is being made.
        timeout = httpx.Timeout(60.0, pool=None)
        # Default headers
        headers = {Metadata.APTOS_HEADER: Metadata.get_aptos_header_val()}
        self.client = httpx.Client(
            http2=client_config.http2,
            limits=limits,
            timeout=timeout,
            headers=headers,
        )
        self.client_config = client_config
        self._chain_id = None

    def close(self):
        self.client.close()

    def chain_id(self):
        if not self._chain_id:
            info = self.info()
            self._chain_id = int(info["chain_id"])
        return self._chain_id

    #
    # Account accessors
    #

    def account(
        self, account_address: AccountAddress, ledger_version: Optional[int] = None
    ) -> Dict[str, str]:
        """Returns the sequence number and authentication key for an account"""

        if not ledger_version:
            request = f"{self.base_url}/accounts/{account_address}"
        else:
            request = f"{self.base_url}/accounts/{account_address}?ledger_version={ledger_version}"

        response = self.client.get(request)
        if response.status_code >= 400:
            raise ApiError(f"{response.text} - {account_address}", response.status_code)
        return response.json()

    def account_balance(
        self, account_address: AccountAddress, ledger_version: Optional[int] = None
    ) -> int:
        """Returns the test coin balance associated with the account"""
        resource = self.account_resource(
            account_address,
            "0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>",
            ledger_version,
        )
        return int(resource["data"]["coin"]["value"])

    def account_sequence_number(
        self, account_address: AccountAddress, ledger_version: Optional[int] = None
    ) -> int:
        account_res = self.account(account_address, ledger_version)
        return int(account_res["sequence_number"])

    def account_resource(
        self,
        account_address: AccountAddress,
        resource_type: str,
        ledger_version: Optional[int] = None,
    ) -> Dict[str, Any]:
        if not ledger_version:
            request = (
                f"{self.base_url}/accounts/{account_address}/resource/{resource_type}"
            )
        else:
            request = f"{self.base_url}/accounts/{account_address}/resource/{resource_type}?ledger_version={ledger_version}"

        response = self.client.get(request)
        if response.status_code == 404:
            raise ResourceNotFound(resource_type, resource_type)
        if response.status_code >= 400:
            raise ApiError(f"{response.text} - {account_address}", response.status_code)
        return response.json()

    def account_resources(
        self,
        account_address: AccountAddress,
        ledger_version: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        if not ledger_version:
            request = f"{self.base_url}/accounts/{account_address}/resources"
        else:
            request = f"{self.base_url}/accounts/{account_address}/resources?ledger_version={ledger_version}"

        response = self.client.get(request)
        if response.status_code == 404:
            raise AccountNotFound(f"{account_address}", account_address)
        if response.status_code >= 400:
            raise ApiError(f"{response.text} - {account_address}", response.status_code)
        return response.json()

    def current_timestamp(self) -> float:
        info = self.info()
        return float(info["ledger_timestamp"]) / 1_000_000

    def get_table_item(
        self,
        handle: str,
        key_type: str,
        value_type: str,
        key: Any,
        ledger_version: Optional[int] = None,
    ) -> Any:
        if not ledger_version:
            request = f"{self.base_url}/tables/{handle}/item"
        else:
            request = (
                f"{self.base_url}/tables/{handle}/item?ledger_version={ledger_version}"
            )
        response = self.client.post(
            request,
            json={
                "key_type": key_type,
                "value_type": value_type,
                "key": key,
            },
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()

    def aggregator_value(
        self,
        account_address: AccountAddress,
        resource_type: str,
        aggregator_path: List[str],
    ) -> int:
        source = self.account_resource(account_address, resource_type)
        source_data = data = source["data"]

        while len(aggregator_path) > 0:
            key = aggregator_path.pop()
            if key not in data:
                raise ApiError(
                    f"aggregator path not found in data: {source_data}", source_data
                )
            data = data[key]

        if "vec" not in data:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        data = data["vec"]
        if len(data) != 1:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        data = data[0]
        if "aggregator" not in data:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        data = data["aggregator"]
        if "vec" not in data:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        data = data["vec"]
        if len(data) != 1:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        data = data[0]
        if "handle" not in data:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        if "key" not in data:
            raise ApiError(f"aggregator not found in data: {source_data}", source_data)
        handle = data["handle"]
        key = data["key"]
        return int(self.get_table_item(handle, "address", "u128", key))

    #
    # Ledger accessors
    #

    def info(self) -> Dict[str, str]:
        response = self.client.get(self.base_url)
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()

    #
    # Transactions
    #

    def simulate_bcs_transaction(
        self,
        signed_transaction: SignedTransaction,
        estimate_gas_usage: bool = False,
    ) -> Dict[str, Any]:
        headers = {"Content-Type": "application/x.aptos.signed_transaction+bcs"}
        params = {}
        if estimate_gas_usage:
            params = {
                "estimate_gas_unit_price": "true",
                "estimate_max_gas_amount": "true",
            }

        response = self.client.post(
            f"{self.base_url}/transactions/simulate",
            params=params,
            headers=headers,
            content=signed_transaction.bytes(),
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)

        return response.json()

    def simulate_transaction(
        self,
        transaction: RawTransaction,
        sender: Account,
        estimate_gas_usage: bool = False,
    ) -> Dict[str, Any]:
        # Note that simulated transactions are not signed and have all 0 signatures!
        authenticator = sender.sign_simulated_transaction(transaction)
        signed_transaction = SignedTransaction(transaction, authenticator)

        headers = {"Content-Type": "application/x.aptos.signed_transaction+bcs"}
        params = {}
        if estimate_gas_usage:
            params = {
                "estimate_gas_unit_price": "true",
                "estimate_max_gas_amount": "true",
            }

        response = self.client.post(
            f"{self.base_url}/transactions/simulate",
            params=params,
            headers=headers,
            content=signed_transaction.bytes(),
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)

        return response.json()

    def submit_bcs_transaction(
        self, signed_transaction: SignedTransaction
    ) -> str:
        headers = {"Content-Type": "application/x.aptos.signed_transaction+bcs"}
        response = self.client.post(
            f"{self.base_url}/transactions",
            headers=headers,
            content=signed_transaction.bytes(),
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()["hash"]

    def submit_transaction(self, sender: Account, payload: Dict[str, Any]) -> str:
        """
        1) Generates a transaction request
        2) submits that to produce a raw transaction
        3) signs the raw transaction
        4) submits the signed transaction
        """

        txn_request = {
            "sender": f"{sender.address()}",
            "sequence_number": str(
                self.account_sequence_number(sender.address())
            ),
            "max_gas_amount": str(self.client_config.max_gas_amount),
            "gas_unit_price": str(self.client_config.gas_unit_price),
            "expiration_timestamp_secs": str(
                int(time.time()) + self.client_config.expiration_ttl
            ),
            "payload": payload,
        }

        response = self.client.post(
            f"{self.base_url}/transactions/encode_submission", json=txn_request
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)

        to_sign = bytes.fromhex(response.json()[2:])
        signature = sender.sign(to_sign)
        txn_request["signature"] = {
            "type": "ed25519_signature",
            "public_key": f"{sender.public_key()}",
            "signature": f"{signature}",
        }

        headers = {"Content-Type": "application/json"}
        response = self.client.post(
            f"{self.base_url}/transactions", headers=headers, json=txn_request
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()["hash"]

    def transaction_pending(self, txn_hash: str) -> bool:
        response = self.client.get(
            f"{self.base_url}/transactions/by_hash/{txn_hash}"
        )
        # TODO(@davidiw): consider raising a different error here, since this is an ambiguous state
        if response.status_code == 404:
            return True
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()["type"] == "pending_transaction"

    def wait_for_transaction(self, txn_hash: str) -> None:
        """
        Waits up to the duration specified in client_config for a transaction to move past pending
        state.
        """

        count = 0
        while self.transaction_pending(txn_hash):
            assert (
                count < self.client_config.transaction_wait_in_seconds
            ), f"transaction {txn_hash} timed out"
            time.sleep(1)
            count += 1
        response = self.client.get(
            f"{self.base_url}/transactions/by_hash/{txn_hash}"
        )
        assert (
            "success" in response.json() and response.json()["success"]
        ), f"{response.text} - {txn_hash}"

    def account_transaction_sequence_number_status(
        self, address: AccountAddress, sequence_number: int
    ) -> bool:
        """Retrieve the state of a transaction by account and sequence number."""

        response = self.client.get(
            f"{self.base_url}/accounts/{address}/transactions?limit=1&start={sequence_number}"
        )
        if response.status_code >= 400:
            logging.info(f"k {response}")
            raise ApiError(response.text, response.status_code)
        data = response.json()
        return len(data) == 1 and data[0]["type"] != "pending_transaction"

    def transaction_by_hash(self, txn_hash: str) -> Dict[str, Any]:
        response = self.client.get(
            f"{self.base_url}/transactions/by_hash/{txn_hash}"
        )
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        return response.json()

    #
    # Transaction helpers
    #

    def create_multi_agent_bcs_transaction(
        self,
        sender: Account,
        secondary_accounts: List[Account],
        payload: TransactionPayload,
    ) -> SignedTransaction:
        raw_transaction = MultiAgentRawTransaction(
            RawTransaction(
                sender.address(),
                self.account_sequence_number(sender.address()),
                payload,
                self.client_config.max_gas_amount,
                self.client_config.gas_unit_price,
                int(time.time()) + self.client_config.expiration_ttl,
                self.chain_id(),
            ),
            [x.address() for x in secondary_accounts],
        )

        authenticator = Authenticator(
            MultiAgentAuthenticator(
                sender.sign_transaction(raw_transaction),
                [
                    (
                        x.address(),
                        x.sign_transaction(raw_transaction),
                    )
                    for x in secondary_accounts
                ],
            )
        )

        return SignedTransaction(raw_transaction.inner(), authenticator)

    def create_bcs_transaction(
        self,
        sender: Account,
        payload: TransactionPayload,
        sequence_number: Optional[int] = None,
    ) -> RawTransaction:
        sequence_number = (
            sequence_number
            if sequence_number is not None
            else self.account_sequence_number(sender.address())
        )
        return RawTransaction(
            sender.address(),
            sequence_number,
            payload,
            self.client_config.max_gas_amount,
            self.client_config.gas_unit_price,
            int(time.time()) + self.client_config.expiration_ttl,
            self.chain_id(),
        )

    def create_bcs_signed_transaction(
        self,
        sender: Account,
        payload: TransactionPayload,
        sequence_number: Optional[int] = None,
    ) -> SignedTransaction:
        raw_transaction = self.create_bcs_transaction(
            sender, payload, sequence_number
        )
        authenticator = sender.sign_transaction(raw_transaction)
        return SignedTransaction(raw_transaction, authenticator)

    #
    # Transaction wrappers
    #

    def transfer(
        self, sender: Account, recipient: AccountAddress, amount: int
    ) -> str:
        """Transfer a given coin amount from a given Account to the recipient's account address.
        Returns the sequence number of the transaction used to transfer."""

        payload = {
            "type": "entry_function_payload",
            "function": "0x1::aptos_account::transfer",
            "type_arguments": [],
            "arguments": [
                f"{recipient}",
                str(amount),
            ],
        }
        return self.submit_transaction(sender, payload)

    # :!:>bcs_transfer
    def bcs_transfer(
        self,
        sender: Account,
        recipient: AccountAddress,
        amount: int,
        sequence_number: Optional[int] = None,
    ) -> str:
        transaction_arguments = [
            TransactionArgument(recipient, Serializer.struct),
            TransactionArgument(amount, Serializer.u64),
        ]

        payload = EntryFunction.natural(
            "0x1::aptos_account",
            "transfer",
            [],
            transaction_arguments,
        )

        signed_transaction = self.create_bcs_signed_transaction(
            sender, TransactionPayload(payload), sequence_number=sequence_number
        )
        return self.submit_bcs_transaction(signed_transaction)  # <:!:bcs_transfer

    def transfer_object(
        self, owner: Account, object: AccountAddress, to: AccountAddress
    ) -> str:
        transaction_arguments = [
            TransactionArgument(object, Serializer.struct),
            TransactionArgument(to, Serializer.struct),
        ]

        payload = EntryFunction.natural(
            "0x1::object",
            "transfer_call",
            [],
            transaction_arguments,
        )

        signed_transaction = self.create_bcs_signed_transaction(
            owner,
            TransactionPayload(payload),
        )
        return self.submit_bcs_transaction(signed_transaction)


class FaucetClient:
    """Faucet creates and funds accounts. This is a thin wrapper around that."""

    base_url: str
    rest_client: RestClient
    headers: Dict[str, str]

    def __init__(
        self, base_url: str, rest_client: RestClient, auth_token: Optional[str] = None
    ):
        self.base_url = base_url
        self.rest_client = rest_client
        self.headers = {}
        if auth_token:
            self.headers["Authorization"] = f"Bearer {auth_token}"

    def close(self):
        self.rest_client.close()

    def fund_account(self, address: AccountAddress, amount: int):
        """This creates an account if it does not exist and mints the specified amount of
        coins into that account."""
        request = f"{self.base_url}/mint?amount={amount}&address={address}"
        response = self.rest_client.client.post(request, headers=self.headers)
        if response.status_code >= 400:
            raise ApiError(response.text, response.status_code)
        for txn_hash in response.json():
            self.rest_client.wait_for_transaction(txn_hash)

    def healthy(self) -> bool:
        response = self.rest_client.client.get(self.base_url)
        return "tap:ok" == response.text


class ApiError(Exception):
    """The API returned a non-success status code, e.g., >= 400"""

    status_code: int

    def __init__(self, message: str, status_code: int):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.status_code = status_code


class AccountNotFound(Exception):
    """The account was not found"""

    account: AccountAddress

    def __init__(self, message: str, account: AccountAddress):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.account = account


class ResourceNotFound(Exception):
    """The underlying resource was not found"""

    resource: str

    def __init__(self, message: str, resource: str):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.resource = resource
