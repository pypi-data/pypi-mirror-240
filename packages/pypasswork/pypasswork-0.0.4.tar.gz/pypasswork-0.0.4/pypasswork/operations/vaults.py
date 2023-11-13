"""Password Vaults operations"""

import base64
import binascii
import dataclasses
import logging
from collections.abc import Sequence, Mapping
from dataclasses import dataclass
from typing import Any, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from pypasswork.passwork import PassworkAPI

from pypasswork.exceptions import PassworkInteractionError
from pypasswork.operations.folders import Folder
from pypasswork.response import PassworkResponse, PassworkStatus

logger = logging.getLogger(__name__)


@dataclass
class Vault:
    id: str
    name: str
    access: str
    scope: str
    visible: Optional[bool]
    encrypted_password: Optional[str] = None
    encrypted_domain_master: Optional[str] = None
    folders_amount: Optional[int] = None
    passwords_amount: Optional[int] = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id="{self.id}", name="{self.name}")'

    def as_dict(self) -> Mapping[str, Any]:
        return dataclasses.asdict(self)

    @property
    def vault_password(self) -> str:
        """
        Get vaultPasswordCrypted property and return it's decrypted
        Returns:
            password string
        """

        try:
            return base64.b64decode(self.encrypted_password).decode('utf-8')
        except binascii.Error as e:
            raise PassworkInteractionError(f'Cannot decrypt Vault password: {e}')

    @property
    def domain_master(self) -> str:
        """
        Returns decrypted string with domainMaster property

        Returns:
            decrypted base64 string
        """

        try:
            return base64.b64decode(self.encrypted_domain_master).decode('utf-8')
        except binascii.Error as e:
            raise PassworkInteractionError(f'Cannot decrypt Vault domain master: {e}')


class Vaults:
    """
    Implement operations with Passwork vaults:
    - list
    - folders
    ...
    """

    def __init__(self, api: 'PassworkAPI'):
        self._api = api

    def list_vaults(self) -> Sequence[Vault]:
        """
        Get all available vaults

        Returns:
            a list of Vault objects
        """

        logger.debug('In list')

        resp: PassworkResponse = self._api.req('GET', endpoint='vaults/list', timeout=10)
        if resp.status is not PassworkStatus.SUCCESS:
            raise PassworkInteractionError(f'Cannot get list of vaults: {resp}')

        vaults = []
        for vault in resp.data:
            try:
                vaults.append(
                    Vault(
                        id=vault['id'],
                        name=vault['name'],
                        access=vault['access'],
                        scope=vault['scope'],
                        visible=vault['visible'] if vault.get('visible') else None,
                        folders_amount=vault['foldersAmount'],
                        passwords_amount=vault['passwordsAmount'],
                        encrypted_domain_master=vault['domainMaster'],
                        encrypted_password=vault['vaultPasswordCrypted']
                    )
                )
            except KeyError as e:
                raise PassworkInteractionError(f'Cannot prepare Vault() object from: "{vault}": missing key {e}')

        return vaults

    def get(self, vault_id: str) -> Optional[Vault]:
        """
        Get vault object by vault id

        Returns:
            Instance of Vault object
        Raises:
            PassworkInteractionError
        """

        try:
            vault = self._api.req('GET', endpoint=f'vaults/{vault_id}')
        except PassworkInteractionError as e:
            raise PassworkInteractionError(f'Cannot get Vault with id={vault_id}: {e}')

        if vault.status is not PassworkStatus.SUCCESS:
            raise PassworkInteractionError(f'Vault retrieve error: {vault.data}')

        return Vault(
            id=vault.data['id'],
            name=vault.data['name'],
            access=vault.data['access'],
            scope=vault.data['scope'],
            visible=vault.data['visible'],
            encrypted_domain_master=vault.data['domainMaster'],
            encrypted_password=vault.data['vaultPasswordCrypted']
        )

    def colors(self, vault_id: str) -> Sequence[int]:
        """
        Get all color tags used in vault

        Args:
            vault_id: target vault id
        Returns:
            a list of colors as integer numbers
        """

        try:
            colors = self._api.req('GET', endpoint=f'vaults/{vault_id}/colors')
        except PassworkInteractionError as e:
            raise PassworkInteractionError(f'Cannot get colors for Vault with id={vault_id}: {e}')

        if colors.status is not PassworkStatus.SUCCESS:
            raise PassworkInteractionError(f'Vault retrieve error: {colors.data}')

        return colors.data

    def folders(self, vault_id: str | Vault) -> Sequence[Folder]:
        """
        Get all vault folders

        Returns:
            a list of Folder object in given Vault
        Raises:
            PassworkInteractionError
        """

        logger.debug('In folders')

        vault_id = vault_id.id if isinstance(vault_id, Vault) else vault_id
        resp: PassworkResponse = self._api.req('GET', endpoint=f'/vaults/{vault_id}/folders')

        folders = []
        for folder in resp.data:
            try:
                folders.append(
                    Folder(
                        vault_id=folder['vaultId'],
                        id=folder['id'],
                        name=folder['name'],
                        parent_id=folder['parentId'] if folder.get('parentId') else None
                    )
                )
            except KeyError as e:
                raise PassworkInteractionError(f'Cannot prepare Folder() object from: "{folder}": missing key {e}')

        return folders

    def full_info(self, vault_id: str) -> dict[str, list[dict]]:
        """
        Get all color tags used in vault

        Args:
            vault_id: target vault id
        Returns:
            a list of colors as integer numbers
        """

        try:
            full_info = self._api.req('GET', endpoint=f'vaults/{vault_id}/fullInfo')
        except PassworkInteractionError as e:
            raise PassworkInteractionError(f'Cannot get full info for Vault with id={vault_id}: {e}')

        if full_info.status is not PassworkStatus.SUCCESS:
            raise PassworkInteractionError(f'Vault info retrieve error: {full_info.data}')

        return full_info.data

    def passwords(self, vault_id: str) -> list[dict[str, Optional[str]]]:
        """
        Get all passwords in Vault root

        Args:
            vault_id: target vault id
        Returns:
            a list of raw passwords in Vault root directory as dict
        """

        try:
            passwords = self._api.req('GET', endpoint=f'vaults/{vault_id}/passwords')
        except PassworkInteractionError as e:
            raise PassworkInteractionError(f'Cannot get passwords for Vault with id={vault_id}: {e}')

        if passwords.status is not PassworkStatus.SUCCESS:
            raise PassworkInteractionError(f'Vault passwords retrieve error: {passwords.data}')

        return passwords.data
