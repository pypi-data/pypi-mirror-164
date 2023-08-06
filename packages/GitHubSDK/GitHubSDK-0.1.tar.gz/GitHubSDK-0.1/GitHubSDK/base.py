from operator import itemgetter
import html

DEFUALT_BASE_URL = "https://api.github.com"

__url_cache__ = {}

class GitHubBase:
    def __init__(self, requester, attributes):
        self.base_url = DEFUALT_BASE_URL
        self.requester = requester
        self.attributes = attributes

    def _instance_or_null(self, instance_class, json):
        if not json:
            return None

        return instance_class(json, self)

    def get__repr__(self, params):
        """
        Converts the object to a nicely printable string.
        """

        def format_params(params):
            items = list(params.items())
            for k, v in sorted(items, key=itemgetter(0), reverse=True):
                if isinstance(v, bytes):
                    v = v.decode("utf-8")
                if isinstance(v, str):
                    v = f'"{v}"'
                yield f"{k}={v}"

        return "{class_name}({params})".format(
            class_name=self.__class__.__name__,
            params=", ".join(list(format_params(params))),
        )

    def _repr_html_(self):
        try:
            return self.to_html()
        except AttributeError:
            return f'<pre>{html.escape(str(self))}</pre>'

    def build_url(self, *args, **kwargs):
        """Build a new API url from scratch."""
        parts = [kwargs.get("base_url") or self.base_url]
        parts.extend(args)
        parts = [str(p) for p in parts]
        key = tuple(parts)
        if key not in __url_cache__:
            __url_cache__[key] = "/".join(parts)
        return __url_cache__[key]
