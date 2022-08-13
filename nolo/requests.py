import quopri


class BaseRequest:
    @staticmethod
    def pars_params(raw_query_string: str) -> dict:
        res = {key: value for (key, value) in [param.split('=') for param in raw_query_string.split('&')]}

        return res


class PostRequests(BaseRequest):
    @staticmethod
    def get_request_data(env) -> dict:
        raw_data = env['wsgi.input'].read(int(env['CONTENT_LENGTH']) if env['CONTENT_LENGTH'] else 0)

        data_str = raw_data.decode(encoding='utf-8')
        data = PostRequests.pars_params(data_str)
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            data[k] = val_decode_str

        return data


class GetRequests(BaseRequest):
    @staticmethod
    def get_request_params(env):
        if env['QUERY_STRING']:
            return GetRequests.pars_params(env['QUERY_STRING'])
        return {}
