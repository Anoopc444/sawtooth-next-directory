# Copyright 2018 Contributors to Hyperledger Sawtooth
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

import logging
import pytest

from rbac.common.crypto.keys import Key
from rbac.app.config import BATCHER_KEY_PAIR
from rbac.addressing import addresser
from rbac.addressing.addresser import AddressSpace
from rbac.common.user.user_address import make_user_address
from rbac.common.protobuf.rbac_payload_pb2 import RBACPayload
from rbac.common.protobuf import user_transaction_pb2
from rbac.common.sawtooth.batcher import Batcher
from tests.rbac.common.sawtooth.batch_assertions import BatchAssertions


LOGGER = logging.getLogger(__name__)


@pytest.mark.unit
@pytest.mark.batch
class TestBatchClient(BatchAssertions, Batcher):
    def get_test_inputs(self, message_type=RBACPayload.CREATE_USER):
        """Returns test data inputs for testing batcher functions"""
        if message_type == RBACPayload.CREATE_USER:
            signer = Key()
            message = user_transaction_pb2.CreateUser(name="foobar")
            message.user_id = signer.public_key
            inputs = [make_user_address(user_id=message.user_id)]
            outputs = inputs
            return message, message_type, inputs, outputs, signer
        else:
            raise Exception(
                "batcher test doesn't support message_type: {}".format(message_type)
            )

    def get_test_payload(self, message_type=RBACPayload.CREATE_USER):
        """Returns a test data payload for testing batcher functions"""
        message, message_type, inputs, outputs, signer = self.get_test_inputs()
        return (
            self.make_payload(
                message=message,
                message_type=message_type,
                inputs=inputs,
                outputs=outputs,
            ),
            signer,
        )

    def test_get_test_inputs(self):
        """Verifies the test data inputs function returns the expected test data"""
        self.assertTrue(callable(self.get_test_inputs))
        self.assertTrue(callable(make_user_address))
        message, message_type, inputs, outputs, signer = self.get_test_inputs()
        self.assertIsInstance(signer, Key)
        self.assertEqual(message_type, RBACPayload.CREATE_USER)
        self.assertIsInstance(message, user_transaction_pb2.CreateUser)
        self.assertIsInstance(message.name, str)
        self.assertIsInstance(inputs, list)
        self.assertIsInstance(outputs, list)
        self.assertEqual(len(inputs), 1)
        self.assertEqual(len(outputs), 1)
        self.assertEqual(addresser.address_is(inputs[0]), AddressSpace.USER)
        self.assertEqual(addresser.address_is(outputs[0]), AddressSpace.USER)

    def test_make_payload(self):
        """Test the make payload batch function"""
        self.assertTrue(callable(self.make_payload))
        message, message_type, inputs, outputs, signer = self.get_test_inputs()
        payload = self.make_payload(
            message=message, message_type=message_type, inputs=inputs, outputs=outputs
        )
        self.assertIsInstance(payload, RBACPayload)
        self.assertEqual(payload.message_type, message_type)
        self.assertEqual(payload.inputs, inputs)
        self.assertEqual(payload.outputs, outputs)
        self.assertIsInstance(signer, Key)
        self.assertValidPayload(
            payload=payload, message=message, message_type=message_type
        )

    def test_get_test_payload(self):
        """Verifies the test data payload function returns the expected test data"""
        self.assertTrue(callable(self.get_test_payload))
        payload, signer = self.get_test_payload()
        self.assertIsInstance(payload, RBACPayload)
        self.assertIsInstance(signer, Key)

    def test_make_transaction_header(self):
        """Test the make transaction header batch function"""
        self.assertTrue(callable(self.make_transaction))
        payload, signer = self.get_test_payload()

        header, signature = self.make_transaction_header(
            payload=payload, signer_keypair=signer
        )

        self.assertValidTransactionHeader(
            header=header,
            signature=signature,
            payload=payload,
            signer_public_key=signer.public_key,
        )

    def test_make_transaction(self):
        """Test the make transaction batch function"""
        self.assertTrue(callable(self.make_transaction))
        payload, signer = self.get_test_payload()

        transaction = self.make_transaction(payload=payload, signer_keypair=signer)

        self.assertValidTransaction(
            transaction=transaction,
            payload=payload,
            signer_public_key=signer.public_key,
        )

    def test_make_batch(self):
        """Test the make batch batch function"""
        self.assertTrue(callable(self.make_batch))
        payload, signer = self.get_test_payload()

        transaction = self.make_transaction(payload=payload, signer_keypair=signer)

        batch = self.make_batch(transaction=transaction)

        self.assertValidBatch(
            batch=batch,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )

    def test_batch_to_list(self):
        """Test the make batch to list batch function"""
        self.assertTrue(callable(self.batch_to_list))
        self.assertTrue(callable(self.make_batch))
        payload, signer = self.get_test_payload()

        transaction = self.make_transaction(payload=payload, signer_keypair=signer)

        batch = self.make_batch(transaction=transaction)

        batch_list = self.batch_to_list(batch)

        self.assertValidBatchList(
            batch_list=batch_list,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )

    def test_make_batch_list(self):
        """Test the make batch list batch function"""
        self.assertTrue(callable(self.make_batch_list))
        payload, signer = self.get_test_payload()

        transaction = self.make_transaction(payload=payload, signer_keypair=signer)

        batch_list = self.make_batch_list(transaction=transaction)

        self.assertValidBatchList(
            batch_list=batch_list,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )

    def test_make_batch_request(self):
        """Test the make batch request batch function"""
        self.assertTrue(callable(self.make_batch_request))
        payload, signer = self.get_test_payload()

        transaction = self.make_transaction(payload=payload, signer_keypair=signer)

        batch_list = self.make_batch_list(transaction=transaction)

        batch_request = self.make_batch_request(batch_list=batch_list)

        self.assertValidBatchRequest(
            batch_request=batch_request,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )

    def test_make(self):
        """Test the make batch function"""
        self.assertTrue(callable(self.make_batch_request))
        payload, signer = self.get_test_payload()

        transaction, batch, batch_list, batch_request = self.make(
            payload=payload, signer_keypair=signer
        )
        self.assertValidTransaction(
            transaction=transaction,
            payload=payload,
            signer_public_key=signer.public_key,
        )
        self.assertValidBatch(
            batch=batch,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )
        self.assertValidBatchList(
            batch_list=batch_list,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )
        self.assertValidBatchRequest(
            batch_request=batch_request,
            payload=payload,
            signer_public_key=signer.public_key,
            batcher_public_key=BATCHER_KEY_PAIR.public_key,
        )
