import textwrap
import json

try:  # python3
    from urllib import parse as urlparse
    from urllib.parse import urlencode
except ImportError:  # python2
    import urlparse
    from urllib import urlencode


def add_parameters_to_url(url, parameters):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(parameters)

    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def client_side_login_redirect(url_template):
    if "_callbackUrl_" not in url_template:
        raise ValueError("Template missing _callbackUrl_ placeholder")

    return textwrap.dedent(
        """\
        <!doctype html>
        <script>
            var urlTemplate = {url_template_json};
            window.location.href = urlTemplate.replace(
                '_callbackUrl_',
                encodeURIComponent(location.pathname + location.search + location.hash)
            );
        </script>
        Aguarde...
    """.format(
            url_template_json=json.dumps(url_template)
        )
    )
