from asklora.brokerage.journals import ReverseJournalEntries, JournalEntries
from asklora.brokerage.rest import Broker, APIError
import random
import uuid
import pytest
from pytest_mock import MockerFixture


def test_reverse_batch_journal(mocker: MockerFixture):
    """
    should ok
    """

    entries = []
    for _ in range(20):
        entries.append(
            ReverseJournalEntries(str(uuid.uuid4()), random.randint(10, 2000))
        )
    broker: Broker = Broker()
    broker_mock = mocker.patch("asklora.brokerage.rest.Broker.post")
    broker_mock.return_value = True
    resp = broker.batch_transfer_reverse(str(uuid.uuid4()), entries)
    assert resp


def test_fail_entries_reverse_batch_journal(mocker: MockerFixture):
    """
    should raise APIError
    """
    with pytest.raises(APIError):
        entries = []
        for _ in range(20):
            entries.append(
                {"from_account": str(uuid.uuid4()), "amount": random.randint(10, 2000)}
            )
        broker: Broker = Broker()
        broker_mock = mocker.patch("asklora.brokerage.rest.Broker.post")
        broker_mock.return_value = True
        broker.batch_transfer_reverse(str(uuid.uuid4()), entries)


def test_batch_journal(mocker: MockerFixture):
    """
    should ok
    """

    entries = []
    for _ in range(20):
        entries.append(JournalEntries(str(uuid.uuid4()), random.randint(10, 2000)))
    broker: Broker = Broker()
    broker_mock = mocker.patch("asklora.brokerage.rest.Broker.post")
    broker_mock.return_value = True
    resp = broker.batch_transfer(str(uuid.uuid4()), entries)
    assert resp


def test_fail_entries_batch_journal(mocker: MockerFixture):
    """
    should raise APIError
    """
    with pytest.raises(APIError):
        entries = []
        for _ in range(20):
            entries.append(
                {"to_aacount": str(uuid.uuid4()), "amount": random.randint(10, 2000)}
            )
        broker: Broker = Broker()
        broker_mock = mocker.patch("asklora.brokerage.rest.Broker.post")
        broker_mock.return_value = True
        broker.batch_transfer(str(uuid.uuid4()), entries)
