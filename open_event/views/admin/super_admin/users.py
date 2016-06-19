from flask_admin import expose

from open_event.views.admin.super_admin.super_admin_base import SuperAdminBaseView
from ....helpers.data_getter import DataGetter

class SuperAdminUsersView(SuperAdminBaseView):

    @expose('/')
    def index_view(self):
        user_list = []
        users = DataGetter.get_all_users()
        for user in users:
            roles = DataGetter.get_event_roles_for_user(user.id)
            user_list.append({
                'user': user,
                'roles': roles,}
            )
        return self.render('/gentelella/admin/super_admin/users/users.html', user_list=user_list)
