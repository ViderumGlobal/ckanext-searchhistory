import ckan.plugins as p
import ckan.authz as authz


def search_add(context, data_dict):
    username = context.get('user')
    user = authz.get_user_id_for_username(username, allow_none=True)
    if user is None:
        return {'success': False, 'msg': 'Not authorized'}
    return {'success': True}

def search_list(context, data_dict):
    return search_add(context, data_dict)
