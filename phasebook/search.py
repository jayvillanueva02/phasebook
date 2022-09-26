from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):

    id1 = args.get('id')
    name1 = args.get('name')
    age1 = args.get('age')
    occupation1 = args.get('occupation')
    result_list = []

    for user in USERS:
        for att in user:
            if att == 'age' and age1 is not None:
                if int(age1) - 1 <= user.get('age') <= int(age1) + 1:
                    result_list.append(user)
                    break
            elif att == 'name' or att == 'id' or att == 'occupation':
                if name1 is not None and name1.casefold() in user.get('name').lower():
                    result_list.append(user)
                    break
                if id1 is not None and user.get('id') == id1:
                    result_list.append(user)
                    break
                if occupation1 is not None and occupation1.casefold() in user.get('occupation').lower():
                    result_list.append(user)
                    break

            elif age1 is None and name1 is not None and id1 is not None and occupation1 is not None:
                return USERS
            elif age1 is None and name1 is None and id1 is None and occupation1 is None:
                return USERS

    return result_list













