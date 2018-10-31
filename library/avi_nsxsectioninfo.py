#!/usr/bin/python
#
# Created on Aug 25, 2016
# @author: Gaurav Rastogi (grastogi@avinetworks.com)
#          Eric Anderson (eanderson@avinetworks.com)
# module_check: supported
# Avi Version: 17.1
#
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'status': ['preview'], 'supported_by': 'community', 'version': '1.0'}

DOCUMENTATION = '''
---
module: avi_nsxsectioninfo
author: Gaurav Rastogi (grastogi@avinetworks.com)

short_description: Module for setup of NsxSectionInfo Avi RESTful Object
description:
    - This module is used to configure NsxSectionInfo object
    - more examples at U(https://github.com/avinetworks/devops)
requirements: [ avisdk ]
version_added: "2.3"
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent","present"]
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
    id:
        description:
            - Id of nsxsectioninfo.
        required: true
    name:
        description:
            - Name of the object.
        required: true
    obj_uuid:
        description:
        required: true
    rule:
        description:
            - List of nsxfirewallrule.
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
    type:
        description:
            - Type of nsxsectioninfo.
        required: true
    url:
        description:
            - Avi controller URL of the object.
    uuid:
        description:
            - Unique object identifier of the object.
extends_documentation_fragment:
    - avi
'''

EXAMPLES = """
- name: Example to create NsxSectionInfo object
  avi_nsxsectioninfo:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_nsxsectioninfo
"""

RETURN = '''
obj:
    description: NsxSectionInfo (api/nsxsectioninfo) object
    returned: success, changed
    type: dict
'''

from pkg_resources import parse_version
from ansible.module_utils.basic import AnsibleModule
from avi.sdk.utils.ansible_utils import avi_common_argument_spec

HAS_AVI = True
try:
    import avi.sdk
    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or (sdk_version and
            (parse_version(sdk_version) < parse_version('16.3.5.post1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    from avi.sdk.utils.ansible_utils import avi_ansible_api
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        cloud_ref=dict(type='str',),
        id=dict(type='str', required=True),
        name=dict(type='str', required=True),
        obj_uuid=dict(type='str', required=True),
        rule=dict(type='list',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=16.3.5.post1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))
    return avi_ansible_api(module, 'nsxsectioninfo',
                           set([]))


if __name__ == '__main__':
    main()
