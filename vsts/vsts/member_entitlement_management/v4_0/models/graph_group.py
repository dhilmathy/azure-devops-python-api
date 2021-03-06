# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .graph_member import GraphMember


class GraphGroup(GraphMember):
    """GraphGroup.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <microsoft.-visual-studio.-services.-web-api.v4_0.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the name of the directory, for Vsts groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by Vsts.
    :type principal_name: str
    :param description: A short phrase to help human readers disambiguate groups with similar names
    :type description: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, origin=None, origin_id=None, subject_kind=None, url=None, domain=None, mail_address=None, principal_name=None, description=None):
        super(GraphGroup, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, origin=origin, origin_id=origin_id, subject_kind=subject_kind, url=url, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.description = description
