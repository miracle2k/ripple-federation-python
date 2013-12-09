import textwrap


def get_ripple_txt(domain, federation_url):
    """Return contents of a ripple.txt linking to the mapping endpoint.
    """
    return textwrap.dedent("""
    [domain]
    {domain}
    
    [federation_url]
    {federation_url}
    """.format(federation_url=federation_url, domain=domain)).strip()


class Federation(object):
    """Usage:

        federation = Federation({
            'example.org': {
                'joe': '{ripple address}'
            }
        })
        return Response(json.dumps(federation.endpoint(request.GET)))

    Make sure that all domains are lowercase.
    """

    errors = {
        'noSuchDomain': 'The supplied domain is not served here.',
        'noSuchUser': 'The supplied user was not found.'
    }

    def __init__(self, userdb):
        self.userdb = userdb

    def endpoint(self, GET):
        """Pass the GET parameters from the request.

        Returns a JSON-serializable structure.
        """
        domain = GET.get('domain', '').lower()
        user = GET.get('destination', GET.get('user'))

        if not domain:
            return self.error('invalidParams', 'No domain provided.')
        if not user:
            return self.error('invalidParams', 'No username provided.')
        
        if not domain in self.userdb:
            return self.error('noSuchDomain')
        if not user in self.userdb[domain]:
            return self.error('noSuchUser')

        return {
            'federation_json': {
                'type': 'federation_record',
                'destination': user,
                'user': user,   # deprecated
                'destination_address': self.userdb[domain][user],
                'domain': domain
            }
        }

    def error(self, code, msg=None):
        return {
            'result': 'error',
            'error': code,
            'error_message': msg or self.errors.get(code)
        }
