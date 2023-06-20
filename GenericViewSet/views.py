from rest_framework.viewsets import GenericViewSet

""" Attributes """
""" 

allowed_methods = <property object
authentication_classes = [<class
content_negotiation_class = <class
default_response_headers = <property object
filter_backends = []
http_method_names = []
lookup_field = 'pk'
lookup_ulr_kwarg = None
metadata_class = <class
pagination_class = None
paginator = <property object
parser_classes = [<class
permission_classes = [<class
queryset = None
renderer_classes = [<class
schema = 
serializer_class = None
settings = 
throttle_classes = []
versioning_class = None
view_is_async = False

"""




""" Methods """
def _allowed_methods(self):
    pass

def as_view(cls, actions=None, **initkwargs):
    pass

def check_object_permissions(self, request, obj):
    pass

def check_permissions(self, request):
    pass

def check_throttles(self, request):
    pass

def determine_version(self, request, *args, **kwargs):
    pass

def dispatch(self, request, *args, **kwargs):
    # APIView View
    pass

def filter_queryset(self, queryset):
    pass

def finalize_response(self, request, response, *args, **kwargs):
    pass

def get_authenticate_header(self, request):
    pass

def get_authenticators(self):
    pass

def get_content_negotiator(self):
    pass

def get_exception_handler(self):
    pass

def get_exception_handler_context(self):
    pass

def get_extra_action_url_map(self):
    pass
@classmethod
def get_extra_actions(cls):
    pass

def get_format_suffix(self, **kwargs):
    pass

def get_object(self):
    pass

def get_paginated_response(self, data):
    pass

def get_parser_context(self, http_request):
    pass

def parsers(self):
    pass

def get_permissions(self):
    pass

def get_queryset(self):
    pass

def get_renderer_context(self):
    pass

def get_renderers(self):
    pass

def get_serializer(self, *args, **kwargs):
    pass

def get_serializer_class(self):
    pass

def get_serializer_context(self):
    pass

def get_throttles(self):
    pass

def get_view_description(self, html=False):
    pass

def get_view_name(self):
    pass

def handle_exception(self, exc):
    pass

def http_method_not_allowed(self, request, *args, **kwargs):
    # APIView View
    pass

def initial(self, request, *args, **kwargs):
    pass

def initialize_request(self, request, *args, **kwargs):
    # ViewSetMixin APIView
    pass

def options(self, request, *args, **kwargs):
    # APIView View
    pass

def paginate_queryset(self, queryset):
    pass

def perform_authentication(self, request):
    pass

def perform_content_negotiation(self, request, force=False):
    pass

def permission_denied(self, reqeust, message=None, code=None):
    pass

def raise_uncaught_exception(self, exc):
    pass

def reverser_action(self, url_name, *args, **kwargs):
    pass

def setup(self, request, *args, **kwargs):
    pass

def throttled(self, request, wait):
    pass