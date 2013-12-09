ripple-federation-python
------------------------

What ripple/federation-php does for Python. Provides a very simple
mapping between names an Ripple addresses. Integrate into your site
to receive Ripple payments at ``you@yourdomain.org``.


Usage
-----

Using werkzeug, for example, you might do::

    CORS = {"Access-Control-Allow-Origin": "*"}

    from .ripple_federation import Federation, get_ripple_txt
    federation = Federation({
        'elsdoerfer.name': {'michael': 'rpLJBGZRT8D9ktgdsYv5AWYtePdyLPrEHy'},
    })

    @expose('/ripple.txt')
    def ripple_txt(request):
        return Response(get_ripple_txt(
            domain=request.host,
            federation_url='https://{}{}'.format(
                request.host, request.urlmap.build('ripple_federation'))
            ),
            mimetype='text/plain',
            headers=CORS)


    @expose('/ripple/federation')
    def ripple_federation(request):
        return Response(
            json.dumps(federation.endpoint(request.args)),
            mimetype='application/json',
            headers=CORS
        )



Other notes
-----------

Test your ripple.txt setup here: https://ripple.com/tools/txt/

Note that HTTPS is needed.
