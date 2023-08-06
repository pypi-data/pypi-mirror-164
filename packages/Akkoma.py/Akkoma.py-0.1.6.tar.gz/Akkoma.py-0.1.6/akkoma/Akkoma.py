import os
import os.path
import mimetypes
import time
import random
import string
import datetime
import collections
import pytz
import requests
import dateutil
import dateutil.parser
import re
import copy
import sys
import six
from decorator import decorate
import hashlib
import pdb

###
# Version check functions, including decorator and parser
###
def parse_version_string(version_string):
    """Parses a semver version string, stripping off "rc" stuff if present."""
    string_parts =  version_string.split(".")
    version_parts = [
        int(re.match("([0-9]*)", string_parts[0]).group(0)),
        int(re.match("([0-9]*)", string_parts[1]).group(0)),
        int(re.match("([0-9]*)", string_parts[2]).group(0))
    ]
    return version_parts

def bigger_version(version_string_a, version_string_b):
    """Returns the bigger version of two version strings."""
    major_a, minor_a, patch_a = parse_version_string(version_string_a)
    major_b, minor_b, patch_b = parse_version_string(version_string_b)

    if major_a > major_b:
        return version_string_a
    elif major_a == major_b and minor_a > minor_b:
        return version_string_a
    elif major_a == major_b and minor_a == minor_b and patch_a > patch_b:
        return version_string_a
    return version_string_b

def api_version(created_ver, last_changed_ver, return_value_ver):
    """Version check decorator. Currently only checks Bigger Than."""
    def api_min_version_decorator(function):
        def wrapper(function, self, *args, **kwargs):
            if not self.version_check_mode == "none":
                if self.version_check_mode == "created":
                    version = created_ver
                else:
                    version = bigger_version(last_changed_ver, return_value_ver)
                major, minor, patch = parse_version_string(version)
                if major > self.akkoma_major:
                    raise AkkomaVersionError("Version check failed (Need version " + version + ")")
                elif major == self.akkoma_major and minor > self.akkoma_minor:
                    print(self.akkoma_minor)
                    raise AkkomaVersionError("Version check failed (Need version " + version + ")")
                elif major == self.akkoma_major and minor == self.akkoma_minor and patch > self.akkoma_patch:
                    raise AkkomaVersionError("Version check failed (Need version " + version + ", patch is " + str(self.akkoma_patch) + ")")
            return function(self, *args, **kwargs)
        function.__doc__ = function.__doc__ + "\n\n        *Added: Akkoma v" + created_ver + ", last changed: Akkoma v" + last_changed_ver + "*"
        return decorate(function, wrapper)
    return api_min_version_decorator

###
# Dict helper class.
# Defined at top level so it can be pickled.
###

class AttribAccessDict(dict):
    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            raise AttributeError("Attribute not found: " + str(attr))

    def __setattr__(self, attr, val):
        if attr in self:
            raise AttributeError("Attribute-style access is read only")
        super(AttribAccessDict, self).__setattr__(attr, val)

class Akkoma:
    """
    Easy to use Akkoma API wrapper.

    Main repository at https://git.mastodont.cat/spla/Akkoma.py
    """
    __DEFAULT_BASE_URL = 'https://akkoma.mastodont.cat'
    __DEFAULT_TIMEOUT = 300
    __DEFAULT_SCOPES = ['read', 'write', 'follow', 'push', 'admin']
    __SCOPE_SETS = {
        'read': [
            'read:accounts', 
            'read:blocks', 
            'read:favourites', 
            'read:filters', 
            'read:follows', 
            'read:lists', 
            'read:mutes', 
            'read:notifications', 
            'read:search', 
            'read:statuses',
            'read:bookmarks'
        ],
        'write': [
            'write:accounts', 
            'write:blocks', 
            'write:favourites', 
            'write:filters', 
            'write:follows', 
            'write:lists', 
            'write:media', 
            'write:mutes', 
            'write:notifications', 
            'write:reports', 
            'write:statuses',
            'write:bookmarks'
        ],
        'follow': [
            'read:blocks',
            'read:follows',
            'read:mutes',
            'write:blocks',  
            'write:follows',
            'write:mutes', 
        ],
        'admin:read': [
            'admin:read:accounts', 
            'admin:read:reports',
        ],
        'admin:write': [
            'admin:write:accounts', 
            'admin:write:reports',
        ],
    }    
    # Dict versions
    __DICT_VERSION_APPLICATION = "2.7.2"
    __DICT_VERSION_MENTION = "1.0.0"
    __DICT_VERSION_MEDIA = "2.8.2"
    __DICT_VERSION_ACCOUNT = "3.1.0"
    __DICT_VERSION_POLL = "2.8.0"
    __DICT_VERSION_STATUS = bigger_version(bigger_version(bigger_version(bigger_version(bigger_version("3.1.0", 
            __DICT_VERSION_MEDIA), __DICT_VERSION_ACCOUNT), __DICT_VERSION_APPLICATION), __DICT_VERSION_MENTION), __DICT_VERSION_POLL)    
    __DICT_VERSION_NOTIFICATION = bigger_version(bigger_version("1.0.0",  __DICT_VERSION_ACCOUNT), __DICT_VERSION_STATUS)

    @staticmethod
    def create_app(app_name, scopes=__DEFAULT_SCOPES, redirect_uris=None, website=None, to_file=None, api_base_url=__DEFAULT_BASE_URL,
                   request_timeout=__DEFAULT_TIMEOUT, session=None):
        """
        Create a new app with given app_name, redirect_uris and website.
        Specify `api_base_url` if you want to register an app on an different instance.
        Specify `website` if you want to give a website for your app.

        Returns `client_id` and `client_secret`, both as strings.
        """
        api_base_url = Akkoma.__protocolize(api_base_url)

        request_data = {
                'client_name': app_name,
                #'redirect_uris': redirect_uris,
                #'website': website
                'scopes': " ".join(scopes)
            }
        
        try:
            if redirect_uris is not None:
                if isinstance(redirect_uris, (list, tuple)):
                    redirect_uris = "\n".join(list(redirect_uris))
                request_data['redirect_uris'] = redirect_uris
            else:
                request_data['redirect_uris'] = 'urn:ietf:wg:oauth:2.0:oob'
            if website is not None:
                request_data['website'] = website
            if session:
                ret = session.post(api_base_url + '/api/v1/apps', data=request_data, timeout=request_timeout)
                response = ret.json()
            else:
                response = requests.post(api_base_url + '/api/v1/apps', data=request_data, timeout=request_timeout)
                response = response.json()
        except Exception as e:
            raise AkkomaNetworkError("Could not complete request: %s" % e)

        if to_file is not None:
            with open(to_file, 'w') as secret_file:
                secret_file.write(response['client_id'] + "\n")
                secret_file.write(response['client_secret'] + "\n")
                secret_file.write(api_base_url + "\n")

        return (response['client_id'], response['client_secret'])

    ###
    # Authentication, including constructor
    ###
    def __init__(self, client_id=None, client_secret=None, access_token=None,
                 api_base_url=None, debug_requests=False,
                 ratelimit_method="wait", ratelimit_pacefactor=1.1,
                 request_timeout=__DEFAULT_TIMEOUT, akkoma_version=None,
                 version_check_mode = "created", session=None, feature_set="mainline"):
        """
        Create a new API wrapper instance based on the given `client_secret` and `client_id`. If you
        give a `client_id` and it is not a file, you must also give a secret. If you specify an
        `access_token` then you don't need to specify a `client_id`. It is allowed to specify
        neither - in this case, you will be restricted to only using endpoints that do not
        require authentication.  If a file is given as `client_id`, client ID, secret and 
        base url are read from that file.

        You can also specify an `access_token`, directly or as a file (as written by `log_in()`_). If
        a file is given, Akkoma.py also tries to load the base URL from this file, if present. A
        client id and secret are not required in this case.

        Akkoma.py can try to respect rate limits in several ways, controlled by `ratelimit_method`.
        "throw" makes functions throw a `AkkomaRatelimitError` when the rate
        limit is hit. "wait" mode will, once the limit is hit, wait and retry the request as soon
        as the rate limit resets, until it succeeds. "pace" works like throw, but tries to wait in
        between calls so that the limit is generally not hit (How hard it tries to not hit the rate
        limit can be controlled by ratelimit_pacefactor). The default setting is "wait". Note that
        even in "wait" and "pace" mode, requests can still fail due to network or other problems! Also
        note that "pace" and "wait" are NOT thread safe.

        Specify `api_base_url` if you wish to talk to an instance other than the flagship one. When
        reading from client id or access token files as written by Akkoma.py 1.5.0 or larger,
        this can be omitted.

        By default, a timeout of 300 seconds is used for all requests. If you wish to change this,
        pass the desired timeout (in seconds) as `request_timeout`.

        For fine-tuned control over the requests object use `session` with a requests.Session.
                
        The `akkoma_version` parameter can be used to specify the version of Akkoma that Akkoma.py will
        expect to be installed on the server. The function will throw an error if an unparseable 
        Version is specified. If no version is specified, Akkoma.py will set `akkoma_version` to the 
        detected version.

        The version check mode can be set to "created" (the default behaviour), "changed" or "none". If set to 
        "created", Akkoma.py will throw an error if the version of Akkoma it is connected to is too old
        to have an endpoint. If it is set to "changed", it will throw an error if the endpoints behaviour has
        changed after the version of Akkoma that is connected has been released. If it is set to "none",
        version checking is disabled.

        `feature_set` can be used to enable behaviour specific to non-mainline Akkoma API implementations.
        Details are documented in the functions that provide such functionality. Currently supported feature
        sets are `mainline`, `fedibird` and `pleroma`.
        """
        self.api_base_url = None
        if not api_base_url is None:
            self.api_base_url = Akkoma.__protocolize(api_base_url)

        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.debug_requests = debug_requests
        self.ratelimit_method = ratelimit_method
        self._token_expired = datetime.datetime.now()
        self._refresh_token = None

        self.__logged_in_id = None

        self.ratelimit_limit = 300
        self.ratelimit_reset = time.time()
        self.ratelimit_remaining = 300
        self.ratelimit_lastcall = time.time()
        self.ratelimit_pacefactor = ratelimit_pacefactor

        self.request_timeout = request_timeout

        if session:
            self.session = session
        else:
            self.session = requests.Session()

        self.feature_set = feature_set
        if not self.feature_set in ["mainline", "fedibird", "pleroma"]:
            raise AkkomaIllegalArgumentError('Requested invalid feature set')

        # Token loading
        if self.client_id is not None:
            if os.path.isfile(self.client_id):
                with open(self.client_id, 'r') as secret_file:
                    self.client_id = secret_file.readline().rstrip()
                    self.client_secret = secret_file.readline().rstrip()

                    try_base_url = secret_file.readline().rstrip()
                    if (not try_base_url is None) and len(try_base_url) != 0:
                        try_base_url = Akkoma.__protocolize(try_base_url)
                        if not (self.api_base_url is None or try_base_url == self.api_base_url):
                            raise AkkomaIllegalArgumentError('Mismatch in base URLs between files and/or specified')
                        self.api_base_url = try_base_url
            else:
                if self.client_secret is None:
                    raise AkkomaIllegalArgumentError('Specified client id directly, but did not supply secret')

        if self.access_token is not None and os.path.isfile(self.access_token):
            with open(self.access_token, 'r') as token_file:
                self.access_token = token_file.readline().rstrip()

                try_base_url = token_file.readline().rstrip()
                if (not try_base_url is None) and len(try_base_url) != 0:
                    try_base_url = Akkoma.__protocolize(try_base_url)
                    if not (self.api_base_url is None or try_base_url == self.api_base_url):
                         raise AkkomaIllegalArgumentError('Mismatch in base URLs between files and/or specified')
                    self.api_base_url = try_base_url

        # Versioning
        if akkoma_version == None:
            self.retrieve_akkoma_version()
        else:
            try:
                self.akkoma_major, self.akkoma_minor, self.akkoma_patch = parse_version_string(akkoma_version)
            except:
                raise AkkomaVersionError("Bad version specified")

        if not version_check_mode in ["created", "changed", "none"]:
            raise AkkomaIllegalArgumentError("Invalid version check method.")
        self.version_check_mode = version_check_mode

        # Ratelimiting parameter check
        if ratelimit_method not in ["throw", "wait", "pace"]:
            raise AkkomaIllegalArgumentError("Invalid ratelimit method.")

    def retrieve_akkoma_version(self):
        """
        Determine installed akkoma version and set major, minor and patch (not including RC info) accordingly.

        Returns the version string, possibly including rc info.
        """
        try:
            version_str = self.__instance()["version"]
        except:
            # instance() was added in 1.1.0, so our best guess is 1.0.0.
            version_str = "1.0.0"

        self.akkoma_major, self.akkoma_minor, self.akkoma_patch = parse_version_string(version_str)
        return version_str

    def verify_minimum_version(self, version_str, cached=False):
        """
        Update version info from server and verify that at least the specified version is present.

        If you specify "cached", the version info update part is skipped.

        Returns True if version requirement is satisfied, False if not.
        """
        if not cached:
            self.retrieve_akkoma_version()
        major, minor, patch = parse_version_string(version_str)
        if major > self.akkoma_major:
            return False
        elif major == self.akkoma_major and minor > self.akkoma_minor:
            return False
        elif major == self.akkoma_major and minor == self.akkoma_minor and patch > self.akkoma_patch:
            return False
        return True

    def log_in(self, client_id=None, client_secret=None, grant_type=None, username=None, password=None, code=None, redirect_uri="urn:ietf:wg:oauth:2.0:oob", refresh_token=None, scopes=__DEFAULT_SCOPES, to_file=None):
        """
        Get the access token for a user.

        The username is the e-mail used to log in into akkoma.

        Can persist access token to file `to_file`, to be used in the constructor.

        Handles password and OAuth-based authorization.

        Will throw a `AkkomaIllegalArgumentError` if the OAuth or the
        username / password credentials given are incorrect, and
        `AkkomaAPIError` if all of the requested scopes were not granted.

        For OAuth2, obtain a code via having your user go to the url returned by 
        `auth_request_url()`_ and pass it as the code parameter. In this case,
        make sure to also pass the same redirect_uri parameter as you used when
        generating the auth request URL.

        Returns the access token as a string.
        """
        if username is not None and password is not None:
            params = self.__generate_params(locals(), ['scopes', 'to_file', 'code', 'refresh_token'])
            params['grant_type'] = 'password'
        elif code is not None:
            params = self.__generate_params(locals(), ['scopes', 'to_file', 'username', 'password', 'refresh_token'])
            params['grant_type'] = 'authorization_code'
        elif refresh_token is not None:
            params = self.__generate_params(locals(), ['scopes', 'to_file', 'username', 'password', 'code'])
            params['grant_type'] = 'refresh_token'
        else:
            raise AkkomaIllegalArgumentError('Invalid arguments given. username and password or code are required.')

        params['client_id'] = self.client_id
        params['client_secret'] = self.client_secret
        params['username'] = username
        params['password'] = password
        #params['scope'] = " ".join(scopes)

        try:
            response = self.__api_request('POST', '/oauth/token', params, do_ratelimiting=False)
            self.access_token = response['access_token']
            self.__set_refresh_token(response.get('refresh_token'))
            self.__set_token_expired(int(response.get('expires_in', 0)))
        except Exception as e:
            if username is not None or password is not None:
                raise AkkomaIllegalArgumentError('Invalid user name, password, or redirect_uris: %s' % e)
            elif code is not None:
                raise AkkomaIllegalArgumentError('Invalid access token or redirect_uris: %s' % e)
            else:
                raise AkkomaIllegalArgumentError('Invalid request: %s' % e)

        received_scopes = response["scope"].split(" ")
        for scope_set in self.__SCOPE_SETS.keys():
            if scope_set in received_scopes:
                received_scopes += self.__SCOPE_SETS[scope_set]

        if not set(scopes) <= set(received_scopes):
            raise AkkomaAPIError(
                'Granted scopes "' + " ".join(received_scopes) + '" do not contain all of the requested scopes "' + " ".join(scopes) + '".')

        if to_file is not None:
            with open(to_file, 'w') as token_file:
                token_file.write(response['access_token'] + "\n")
                token_file.write(self.api_base_url + "\n")

        self.__logged_in_id = None

        return response['access_token']

    ###
    # Reading data: Notifications
    ###
    #@api_version("1.0.0", "2.9.0", __DICT_VERSION_NOTIFICATION)
    def notifications(self, id=None, account_id=None, max_id=None, min_id=None, since_id=None, limit=None, mentions_only=None):
        """
        Fetch notifications (mentions, favourites, reblogs, follows) for the logged-in
        user. Pass `account_id` to get only notifications originating from the given account.

        Can be passed an `id` to fetch a single notification.
        Returns a list of `notification dicts`_.
        """
        if max_id != None:
            max_id = self.__unpack_id(max_id)

        if min_id != None:
            min_id = self.__unpack_id(min_id)

        if since_id != None:
            since_id = self.__unpack_id(since_id)

        if account_id != None:
            account_id = self.__unpack_id(account_id)

        if id is None:
            params = self.__generate_params(locals(), ['id'])
            return self.__api_request('GET', '/api/v1/notifications', params)
        else:
            id = self.__unpack_id(id)
            url = '/api/v1/notifications/{0}'.format(str(id))
            return self.__api_request('GET', url)

    ###
    # Reading data: Accounts
    ###
    @api_version("1.0.0", "1.0.0", __DICT_VERSION_ACCOUNT)
    def account(self, id):
        """
        Fetch account information by user `id`.

        Does not require authentication for publicly visible accounts.

        Returns a `user dict`_.
        """
        id = self.__unpack_id(id)
        url = '/api/v1/accounts/{0}'.format(str(id))
        return self.__api_request('GET', url)

    @api_version("1.0.0", "2.1.0", __DICT_VERSION_ACCOUNT)
    def account_verify_credentials(self):
        """
        Fetch logged-in user's account information.
        Returns a `user dict`_ (Starting from 2.1.0, with an additional "source" field).
        """
        return self.__api_request('GET', '/api/v1/accounts/verify_credentials')

    @api_version("1.0.0", "2.1.0", __DICT_VERSION_ACCOUNT)
    def me(self):
        """
        Get this users account. Symonym for `account_verify_credentials()`, does exactly
        the same thing, just exists becase `account_verify_credentials()` has a confusing
        name.
        """
        return self.account_verify_credentials()

    ###
    # Internal helpers, dragons probably
    ###

    @staticmethod
    def __json_allow_dict_attrs(json_object):
        """
        Makes it possible to use attribute notation to access a dicts
        elements, while still allowing the dict to act as a dict.
        """
        if isinstance(json_object, dict):
            return AttribAccessDict(json_object)
        return json_object    

    @staticmethod
    def __json_date_parse(json_object):
        """
        Parse dates in certain known json fields, if possible.
        """
        known_date_fields = ["created_at", "week", "day", "expires_at", "scheduled_at", "updated_at", "last_status_at", "starts_at", "ends_at", "published_at"]
        for k, v in json_object.items():
            if k in known_date_fields:
                if v != None:
                    try:
                        if isinstance(v, int):
                            json_object[k] = datetime.datetime.fromtimestamp(v, pytz.utc)
                        else:
                            json_object[k] = dateutil.parser.parse(v)
                    except:
                        raise AkkomaAPIError('Encountered invalid date.')
        return json_object

    @staticmethod
    def __json_truefalse_parse(json_object):
        """
        Parse 'True' / 'False' strings in certain known fields
        """
        for key in ('follow', 'favourite', 'reblog', 'mention'):
            if (key in json_object and isinstance(json_object[key], six.text_type)):
                if json_object[key].lower() == 'true':
                    json_object[key] = True
                if json_object[key].lower() == 'False':
                    json_object[key] = False
        return json_object

    @staticmethod
    def __json_strnum_to_bignum(json_object):
        """
        Converts json string numerals to native python bignums.
        """
        for key in ('id', 'week', 'in_reply_to_id', 'in_reply_to_account_id', 'logins', 'registrations', 'statuses', 'day', 'last_read_id'):
            if (key in json_object and isinstance(json_object[key], six.text_type)):
                try:
                    json_object[key] = int(json_object[key])
                except ValueError:
                    pass

        return json_object

    @staticmethod
    def __json_hooks(json_object):
        """
        All the json hooks. Used in request parsing.
        """
        json_object = Akkoma.__json_strnum_to_bignum(json_object)
        json_object = Akkoma.__json_date_parse(json_object)
        json_object = Akkoma.__json_truefalse_parse(json_object)
        json_object = Akkoma.__json_allow_dict_attrs(json_object)
        return json_object

    def __api_request(self, method, endpoint, params={}, files={}, headers={}, access_token_override=None, base_url_override=None, do_ratelimiting=True, use_json=False, parse=True):
        """
        Internal API request helper.
        """
        response = None
        remaining_wait = 0
        
        # "pace" mode ratelimiting: Assume constant rate of requests, sleep a little less long than it
        # would take to not hit the rate limit at that request rate.
        if do_ratelimiting and self.ratelimit_method == "pace":
            if self.ratelimit_remaining == 0:
                to_next = self.ratelimit_reset - time.time()
                if to_next > 0:
                    # As a precaution, never sleep longer than 5 minutes
                    to_next = min(to_next, 5 * 60)
                    time.sleep(to_next)
            else:
                time_waited = time.time() - self.ratelimit_lastcall
                time_wait = float(self.ratelimit_reset - time.time()) / float(self.ratelimit_remaining)
                remaining_wait = time_wait - time_waited

            if remaining_wait > 0:
                to_next = remaining_wait / self.ratelimit_pacefactor
                to_next = min(to_next, 5 * 60)
                time.sleep(to_next)

        # Generate request headers
        headers = copy.deepcopy(headers)
        if not self.access_token is None:
            headers['Authorization'] = 'Bearer ' + self.access_token
        if not access_token_override is None:
            headers['Authorization'] = 'Bearer ' + access_token_override

        # Determine base URL
        base_url = self.api_base_url
        if not base_url_override is None:
            base_url = base_url_override

        if self.debug_requests:
            print('Akkoma: Request to endpoint "' + base_url + endpoint + '" using method "' + method + '".')
            print('Parameters: ' + str(params))
            print('Headers: ' + str(headers))
            print('Files: ' + str(files))

        # Make request
        request_complete = False
        while not request_complete:
            request_complete = True

            response_object = None
            try:
                kwargs = dict(headers=headers, files=files,
                              timeout=self.request_timeout)
                if use_json == False:
                    if method == 'GET':
                        kwargs['params'] = params
                    else:
                        kwargs['data'] = params
                else:
                    kwargs['json'] = params
                
                # Block list with exactly three entries, matching on hashes of the instance API domain
                # For more information, have a look at the docs
                if hashlib.sha256(",".join(base_url.split("//")[-1].split("/")[0].split(".")[-2:]).encode("utf-8")).hexdigest() in \
                    [
                        "f3b50af8594eaa91dc440357a92691ff65dbfc9555226e9545b8e083dc10d2e1", 
                        "b96d2de9784efb5af0af56965b8616afe5469c06e7188ad0ccaee5c7cb8a56b6",
                        "2dc0cbc89fad4873f665b78cc2f8b6b80fae4af9ac43c0d693edfda27275f517"
                    ]:
                    raise Exception("Access denied.")
                    
                response_object = self.session.request(method, base_url + endpoint, **kwargs)
            except Exception as e:
                raise AkkomaNetworkError("Could not complete request: %s" % e)

            if response_object is None:
                raise AkkomaIllegalArgumentError("Illegal request.")

            # Parse rate limiting headers
            if 'X-RateLimit-Remaining' in response_object.headers and do_ratelimiting:
                self.ratelimit_remaining = int(response_object.headers['X-RateLimit-Remaining'])
                self.ratelimit_limit = int(response_object.headers['X-RateLimit-Limit'])

                try:
                    ratelimit_reset_datetime = dateutil.parser.parse(response_object.headers['X-RateLimit-Reset'])
                    self.ratelimit_reset = self.__datetime_to_epoch(ratelimit_reset_datetime)

                    # Adjust server time to local clock
                    if 'Date' in response_object.headers:
                        server_time_datetime = dateutil.parser.parse(response_object.headers['Date'])
                        server_time = self.__datetime_to_epoch(server_time_datetime)
                        server_time_diff = time.time() - server_time
                        self.ratelimit_reset += server_time_diff
                        self.ratelimit_lastcall = time.time()
                except Exception as e:
                    raise AkkomaRatelimitError("Rate limit time calculations failed: %s" % e)

            # Handle response
            if self.debug_requests:
                print('Akkoma: Response received with code ' + str(response_object.status_code) + '.')
                print('response headers: ' + str(response_object.headers))
                print('Response text content: ' + str(response_object.text))

            if not response_object.ok:
                try:
                    response = response_object.json(object_hook=self.__json_hooks)
                    if isinstance(response, dict) and 'error' in response:
                        error_msg = response['error']
                    elif isinstance(response, str):
                        error_msg = response
                    else:
                        error_msg = None
                except ValueError:
                    error_msg = None

                # Handle rate limiting
                if response_object.status_code == 429:
                    if self.ratelimit_method == 'throw' or not do_ratelimiting:
                        raise AkkomaRatelimitError('Hit rate limit.')
                    elif self.ratelimit_method in ('wait', 'pace'):
                        to_next = self.ratelimit_reset - time.time()
                        if to_next > 0:
                            # As a precaution, never sleep longer than 5 minutes
                            to_next = min(to_next, 5 * 60)
                            time.sleep(to_next)
                            request_complete = False
                            continue

                if response_object.status_code == 404:
                    ex_type = AkkomaNotFoundError
                    if not error_msg:
                        error_msg = 'Endpoint not found.'
                        # this is for compatibility with older versions
                        # which raised AkkomaAPIError('Endpoint not found.')
                        # on any 404
                elif response_object.status_code == 401:
                    ex_type = AkkomaUnauthorizedError
                elif response_object.status_code == 500:
                    ex_type = AkkomaInternalServerError
                elif response_object.status_code == 502:
                    ex_type = AkkomaBadGatewayError
                elif response_object.status_code == 503:
                    ex_type = AkkomaServiceUnavailableError
                elif response_object.status_code == 504:
                    ex_type = AkkomaGatewayTimeoutError
                elif response_object.status_code >= 500 and \
                     response_object.status_code <= 511:
                    ex_type = AkkomaServerError
                else:
                    ex_type = AkkomaAPIError

                raise ex_type(
                        'Akkoma API returned error',
                        response_object.status_code,
                        response_object.reason,
                        error_msg)

            if parse == True:
                try:
                    response = response_object.json(object_hook=self.__json_hooks)
                except:
                    raise AkkomaAPIError(
                        "Could not parse response as JSON, response code was %s, "
                        "bad json content was '%s'" % (response_object.status_code,
                                                    response_object.content))
            else:
                response = response_object.content
                
            # Parse link headers
            if isinstance(response, list) and \
                    'Link' in response_object.headers and \
                    response_object.headers['Link'] != "":
                tmp_urls = requests.utils.parse_header_links(
                    response_object.headers['Link'].rstrip('>').replace('>,<', ',<'))
                for url in tmp_urls:
                    if 'rel' not in url:
                        continue

                    if url['rel'] == 'next':
                        # Be paranoid and extract max_id specifically
                        next_url = url['url']
                        matchgroups = re.search(r"[?&]max_id=([^&]+)", next_url)

                        if matchgroups:
                            next_params = copy.deepcopy(params)
                            next_params['_pagination_method'] = method
                            next_params['_pagination_endpoint'] = endpoint
                            max_id = matchgroups.group(1)
                            if max_id.isdigit():
                                next_params['max_id'] = int(max_id)
                            else:
                                next_params['max_id'] = max_id
                            if "since_id" in next_params:
                                del next_params['since_id']
                            if "min_id" in next_params:
                                del next_params['min_id']
                            response[-1]._pagination_next = next_params

                    if url['rel'] == 'prev':
                        # Be paranoid and extract since_id or min_id specifically
                        prev_url = url['url']
                        
                        # Old and busted (pre-2.6.0): since_id pagination
                        matchgroups = re.search(r"[?&]since_id=([^&]+)", prev_url)
                        if matchgroups:
                            prev_params = copy.deepcopy(params)
                            prev_params['_pagination_method'] = method
                            prev_params['_pagination_endpoint'] = endpoint
                            since_id = matchgroups.group(1)
                            if since_id.isdigit():
                                prev_params['since_id'] = int(since_id)
                            else:
                                prev_params['since_id'] = since_id
                            if "max_id" in prev_params:
                                del prev_params['max_id']
                            response[0]._pagination_prev = prev_params
                            
                        # New and fantastico (post-2.6.0): min_id pagination
                        matchgroups = re.search(r"[?&]min_id=([^&]+)", prev_url)
                        if matchgroups:
                            prev_params = copy.deepcopy(params)
                            prev_params['_pagination_method'] = method
                            prev_params['_pagination_endpoint'] = endpoint
                            min_id = matchgroups.group(1)
                            if min_id.isdigit():
                                prev_params['min_id'] = int(min_id)
                            else:
                                prev_params['min_id'] = min_id
                            if "max_id" in prev_params:
                                del prev_params['max_id']
                            response[0]._pagination_prev = prev_params

        return response

    ###
    # Reading data: Apps
    ###
    @api_version("2.0.0", "2.7.2", __DICT_VERSION_APPLICATION)
    def app_verify_credentials(self):
        """
        Fetch information about the current application.

        Returns an `application dict`_.
        
        """
        return self.__api_request('GET', '/api/v1/apps/verify_credentials')

    def __generate_params(self, params, exclude=[]):
        """
        Internal named-parameters-to-dict helper.

        Note for developers: If called with locals() as params,
        as is the usual practice in this code, the __generate_params call
        (or at least the locals() call) should generally be the first thing
        in your function.
        """
        params = collections.OrderedDict(params)

        if 'self' in params:
            del params['self']
        
        param_keys = list(params.keys())
        for key in param_keys:
            if isinstance(params[key], bool) and params[key] == False:
                params[key] = '0'
            if isinstance(params[key], bool) and params[key] == True:
                params[key] = '1'
                
        for key in param_keys:
            if params[key] is None or key in exclude:
                del params[key]

        param_keys = list(params.keys())
        for key in param_keys:
            if isinstance(params[key], list):
                params[key + "[]"] = params[key]
                del params[key]
            
        return params

    ###
    # Writing data: Statuses
    ###
    @api_version("1.0.0", "2.8.0", __DICT_VERSION_STATUS)
    def status_post(self, status, in_reply_to_id=None, media_ids=None,
                    sensitive=False, visibility=None, spoiler_text=None,
                    language=None, idempotency_key=None, content_type=None,
                    scheduled_at=None, poll=None, quote_id=None):
        """
        Post a status. Can optionally be in reply to another status and contain
        media.
        
        `media_ids` should be a list. (If it's not, the function will turn it
        into one.) It can contain up to four pieces of media (uploaded via 
        `media_post()`_). `media_ids` can also be the `media dicts`_ returned 
        by `media_post()`_ - they are unpacked automatically.

        The `sensitive` boolean decides whether or not media attached to the post
        should be marked as sensitive, which hides it by default on the Mastodon
        web front-end.

        The visibility parameter is a string value and accepts any of:
        'direct' - post will be visible only to mentioned users
        'private' - post will be visible only to followers
        'unlisted' - post will be public but not appear on the public timeline
        'public' - post will be public

        If not passed in, visibility defaults to match the current account's
        default-privacy setting (starting with Mastodon version 1.6) or its
        locked setting - private if the account is locked, public otherwise
        (for Mastodon versions lower than 1.6).

        The `spoiler_text` parameter is a string to be shown as a warning before
        the text of the status.  If no text is passed in, no warning will be
        displayed.

        Specify `language` to override automatic language detection. The parameter
        accepts all valid ISO 639-2 language codes.

        You can set `idempotency_key` to a value to uniquely identify an attempt
        at posting a status. Even if you call this function more than once,
        if you call it with the same `idempotency_key`, only one status will
        be created.

        Pass a datetime as `scheduled_at` to schedule the toot for a specific time
        (the time must be at least 5 minutes into the future). If this is passed,
        status_post returns a `scheduled toot dict`_ instead.

        Pass `poll` to attach a poll to the status. An appropriate object can be
        constructed using `make_poll()`_ . Note that as of Mastodon version
        2.8.2, you can only have either media or a poll attached, not both at 
        the same time.

        **Specific to `pleroma` feature set:**: Specify `content_type` to set 
        the content type of your post on Pleroma. It accepts 'text/plain' (default), 
        'text/markdown', 'text/html' and 'text/bbcode. This parameter is not 
        supported on Mastodon servers, but will be safely ignored if set.

        **Specific to `fedibird` feature set:**: The `quote_id` parameter is 
        a non-standard extension that specifies the id of a quoted status.

        Returns a `toot dict`_ with the new status.
        """
        if quote_id != None:
            if self.feature_set != "fedibird":
                raise MastodonIllegalArgumentError('quote_id is only available with feature set fedibird')
            quote_id = self.__unpack_id(quote_id)
           
        if content_type != None:
            if self.feature_set != "pleroma":
                raise MastodonIllegalArgumentError('quote_id is only available with feature set pleroma')
            # It would be better to read this from nodeinfo and cache, but this is easier
            if not content_type in ["text/plain", "text/html", "text/markdown", "text/bbcode"]:
                raise MastodonIllegalArgumentError('Invalid content type specified')
            
        if in_reply_to_id != None:
            in_reply_to_id = self.__unpack_id(in_reply_to_id)
        
        if scheduled_at != None:
            scheduled_at = self.__consistent_isoformat_utc(scheduled_at)
        
        params_initial = locals()
        
        # Validate poll/media exclusivity
        if not poll is None:
            if (not media_ids is None) and len(media_ids) != 0:
                raise ValueError('Status can have media or poll attached - not both.')
        
        # Validate visibility parameter
        valid_visibilities = ['private', 'public', 'unlisted', 'direct']
        if params_initial['visibility'] == None:
            del params_initial['visibility']
        else:
            params_initial['visibility'] = params_initial['visibility'].lower()
            if params_initial['visibility'] not in valid_visibilities:
                raise ValueError('Invalid visibility value! Acceptable '
                                'values are %s' % valid_visibilities)

        if params_initial['language'] == None:
            del params_initial['language']

        if params_initial['sensitive'] is False:
            del [params_initial['sensitive']]

        headers = {}
        if idempotency_key != None:
            headers['Idempotency-Key'] = idempotency_key
            
        if media_ids is not None:
            try:
                media_ids_proper = []
                if not isinstance(media_ids, (list, tuple)):
                    media_ids = [media_ids]
                for media_id in media_ids:
                    if isinstance(media_id, dict):
                        media_ids_proper.append(media_id["id"])
                    else:
                        media_ids_proper.append(media_id)
            except Exception as e:
                raise MastodonIllegalArgumentError("Invalid media "
                                                   "dict: %s" % e)

            params_initial["media_ids"] = media_ids_proper

        if params_initial['content_type'] == None:
            del params_initial['content_type']

        use_json = False
        if not poll is None:
            use_json = True

        params = self.__generate_params(params_initial, ['idempotency_key'])
        return self.__api_request('POST', '/api/v1/statuses', params, headers = headers, use_json = use_json)

    ###
    # Writing data: Notifications
    ###
    #@api_version("1.0.0", "1.0.0", "1.0.0")
    def notifications_clear(self):
        """
        Clear out a users notifications
        """
        self.__api_request('POST', '/api/v1/notifications/clear')

    #@api_version("1.3.0", "2.9.2", "2.9.2")
    def notifications_dismiss(self, id):
        """
        Deletes a single notification
        """
        id = self.__unpack_id(id)

        url = '/api/v1/notifications/{0}/dismiss'.format(str(id))
        self.__api_request('POST', url)

    ###
    # Writing data: Media
    ###
    @api_version("1.0.0", "2.9.1", __DICT_VERSION_MEDIA)
    def media_post(self, media_file, mime_type=None, description=None, focus=None):
        """
        Post an image, video or audio file. `media_file` can either be image data or
        a file name. If image data is passed directly, the mime
        type has to be specified manually, otherwise, it is
        determined from the file name. `focus` should be a tuple
        of floats between -1 and 1, giving the x and y coordinates
        of the images focus point for cropping (with the origin being the images
        center).

        Throws a `AkkomaIllegalArgumentError` if the mime type of the
        passed data or file can not be determined properly.

        Returns a `media dict`_. This contains the id that can be used in
        status_post to attach the media file to a toot.
        """
        if mime_type is None and (isinstance(media_file, str) and os.path.isfile(media_file)):
            mime_type = guess_type(media_file)
            media_file = open(media_file, 'rb')
        elif isinstance(media_file, str) and os.path.isfile(media_file):
            media_file = open(media_file, 'rb')

        if mime_type is None:
            raise AkkomaIllegalArgumentError('Could not determine mime type'
                                               ' or data passed directly '
                                               'without mime type.')

        random_suffix = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        file_name = "akkomapy_upload_" + str(time.time()) + "_" + str(random_suffix) + mimetypes.guess_extension(mime_type)

        if focus != None:
            focus = str(focus[0]) + "," + str(focus[1])

        media_file_description = (file_name, media_file, mime_type)
        return self.__api_request('POST', '/api/v1/media',
                                  files={'file': media_file_description},
                                  params={'description': description, 'focus': focus})

    def __unpack_id(self, id):
        """
        Internal object-to-id converter

        Checks if id is a dict that contains id and
        returns the id inside, otherwise just returns
        the id straight.
        """
        if isinstance(id, dict) and "id" in id:
            return id["id"]
        else:
            return id

    def __set_token_expired(self, value):
        """Internal helper for oauth code"""
        self._token_expired = datetime.datetime.now() + datetime.timedelta(seconds=value)
        return

    def __set_refresh_token(self, value):
        """Internal helper for oauth code"""
        self._refresh_token = value
        return

    @staticmethod
    def __protocolize(base_url):
        """Internal add-protocol-to-url helper"""
        if not base_url.startswith("http://") and not base_url.startswith("https://"):
            base_url = "https://" + base_url

        # Some API endpoints can't handle extra /'s in path requests
        base_url = base_url.rstrip("/")
        return base_url

##
# Exceptions
##
class AkkomaError(Exception):
    """Base class for Akkoma.py exceptions"""

class AkkomaVersionError(AkkomaError):
    """Raised when a function is called that the version of Akkoma for which
       Akkoma.py was instantiated does not support"""

class AkkomaIllegalArgumentError(ValueError, AkkomaError):
    """Raised when an incorrect parameter is passed to a function"""
    pass

class AkkomaIOError(IOError, AkkomaError):
    """Base class for Akkoma.py I/O errors"""

class AkkomaNetworkError(AkkomaIOError):
    """Raised when network communication with the server fails"""
    pass

class AkkomaReadTimeout(AkkomaNetworkError):
    """Raised when a stream times out"""
    pass

class AkkomaAPIError(AkkomaError):
    """Raised when the akkoma API generates a response that cannot be handled"""
    pass

class AkkomaNotFoundError(AkkomaAPIError):
    """Raised when the akkoma API returns a 404 Not Found error"""
    pass

class AkkomaMalformedEventError(AkkomaError):
    """Raised when the server-sent event stream is malformed"""
    pass
