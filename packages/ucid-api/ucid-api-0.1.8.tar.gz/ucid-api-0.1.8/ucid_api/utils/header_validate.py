import ipaddress
import logging
import re

from ucid_api.exception.ucid_exception import UcidError
from ucid_api.constant.ucidconstants import HeaderConstants


class HeaderValidate:

    def validate_headers(self, headers):
        '''
        Validating mandatory header data from the request to block user from access of service.
        matching the mandatory headers from the header list.
        '''
        try:
            # convert header key to lowercase
            header_lst = [k.lower() for k, v in headers.items()]

            logging.info("Mandatory headers list:: {}".format(str(header_lst)))

            # check if all headers are available in request header or not
            header_check = all(ele in header_lst for ele in HeaderConstants.MANDATORY_HEADERS)

            if header_check:
                header_lower = {k.lower(): v for k, v in headers.items()}
                logging.info("Mandatory headers values:: {}".format(str(header_lower)))

                ip = header_lower[HeaderConstants.IP]
                client_name = header_lower[HeaderConstants.CLIENT_NAME]
                client_type = header_lower[HeaderConstants.CLIENT_TYPE]
                project_name = header_lower[HeaderConstants.PROJECT_NAME]
                timestamp = header_lower[HeaderConstants.TIMESTAMP]

                is_ip = self.validate_ip(ip)
                is_cn = self.validate_string(HeaderConstants.CLIENT_NAME, client_name)
                is_ct = self.validate_string(HeaderConstants.CLIENT_TYPE, client_type)
                is_pn = self.validate_string(HeaderConstants.PROJECT_NAME, project_name)
                is_ts = self.validate_timestamp(timestamp)

                res = header_lower

                if is_ip and is_cn and is_ct and is_pn and is_ts:
                    return True, res
            else:
                raise UcidError("One or more mandatory headers are missing or invalid. Please check your request "
                                "headers")

        except UcidError as uciderror:
            raise uciderror

    # validate an Ip address
    def validate_ip(self, ip_address):
        '''
        Validating an IP address (IPv4) from the request header
        '''

        split_ip = re.split(r'[;,\s]\s*', ip_address)

        for ip in split_ip:
            try:
                ip = ipaddress.ip_address(ip)

                if isinstance(ip, ipaddress.IPv4Address):
                    pass
                elif isinstance(ip, ipaddress.IPv6Address):
                    pass
                else:
                    return False
            except ValueError:
                logging.error("{} is an invalid IP address".format(ip))
                return False

        return True

    def validate_string(self, header_type, string):
        '''
        Validate the string in client name, client type and project name in request header
        accept only space, hyphen and alpho numberic string.
        '''
        regex_string = "^[a-zA-Z0-9]([\w -]*[a-zA-Z0-9])?$"
        if len(string) == 0:
            logging.info("Invalid {} in header with zero length".format(header_type))
            return False
        else:
            if re.search(regex_string, string):
                return True
            else:
                logging.info("Invalid {} in header".format(header_type))
                return False

    def validate_timestamp(self, timestamp):
        '''
        Validate the string in timestamp in request header
        to accept only numeric value.
        '''
        if timestamp.isdigit():
            return True
        else:
            logging.info("Invalid timestamp in header")
            return False
