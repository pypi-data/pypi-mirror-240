from collections.abc import Iterable, Mapping
from typing import Any

from itertools import chain

from .entity import Entity
from .role import Role


class GroupEntity(Entity):
    """Represents an entity containing several others with different roles.

    A :class:`.GroupEntity` represents an :class:`.Entity` containing
    several other :class:`.Entity` with different :class:`.Role`, and on
    which calculations can be run.

    Args:
        key: A key to identify the group entity.
        plural: The ``key``, pluralised.
        label: A summary description.
        doc: A full description.
        roles: The list of :class:`.Role` of the group entity.
        containing_entities: The list of keys of group entities whose members
            are guaranteed to be a superset of this group's entities.

    """  # noqa RST301

    def __init__(
        self,
        key: str,
        plural: str,
        label: str,
        doc: str,
        roles: Iterable[Mapping[str, Any]],
        containing_entities: Iterable[str] = (),
    ) -> None:
        super().__init__(key, plural, label, doc)
        self.roles_description = roles
        self.roles = []
        for role_description in roles:
            role = Role(role_description, self)
            setattr(self, role.key.upper(), role)
            self.roles.append(role)
            if role_description.get("subroles"):
                role.subroles = []
                for subrole_key in role_description["subroles"]:
                    subrole = Role({"key": subrole_key, "max": 1}, self)
                    setattr(self, subrole.key.upper(), subrole)
                    role.subroles.append(subrole)
                role.max = len(role.subroles)
        self.flattened_roles = tuple(
            chain.from_iterable(role.subroles or [role] for role in self.roles)
        )

        self.is_person = False
        self.containing_entities = containing_entities
