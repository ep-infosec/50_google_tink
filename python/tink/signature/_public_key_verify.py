# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Interface for PublicKeyVerify."""

import abc


class PublicKeyVerify(metaclass=abc.ABCMeta):
  """Interface for public key verifying.

  Digital Signatures provide functionality of signing data and verification of
  the signatures. They are represented by a pair of primitives (interfaces)
  'PublicKeySign' for signing of data, and 'PublicKeyVerify' for verification
  of signatures. Implementations of these interfaces are secure against
  adaptive chosen-message attacks. Signing data ensures the authenticity and
  the integrity of that data, but not its secrecy.
  """

  @abc.abstractmethod
  def verify(self, signature: bytes, data: bytes) -> bytes:
    """Verifies that signature is a digital signature for data.

    Args:
      signature: The signature bytes to be checked.
      data: The data bytes to be checked.

    Raises:
      tink.TinkError if the verification fails.
    """
    raise NotImplementedError()
