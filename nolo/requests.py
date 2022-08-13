class BaseRequest:
    @staticmethod
    def pars_params(raw_query_string: str) -> dict:
        res = {key: value for (key, value) in [param.split('=') for param in raw_query_string.split('%')]}
        print(res)
        # params = raw_query_string.split('&')
        # for param in params:
        #     key, value = param.split('=')
        #     res[key] = value
        return res


class PostRequests:
    pass


class GetRequests(BaseRequest):
    @staticmethod
    def get_request_pararms(env):
        if env('QUERY_STRING'):
            return GetRequests.pars_params(env['QUERY_STRING'])
        return {}
