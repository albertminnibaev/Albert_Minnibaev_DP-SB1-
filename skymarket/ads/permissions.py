from rest_framework.permissions import BasePermission


# пользователь является автором
class IsAuthor(BasePermission):
    message = "Вы не являетесь автором"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


# Проверка на то, что нользователь является администратором
class IsAdmin(BasePermission):
    message = 'Вы не являетесь администратром'

    def has_permission(self, request, view):
        return request.user.role == 'admin'


# Проверка на то, что нользователь аноним
class IsAnonymous(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_anonymous


# class IsRetrieveAuthor(BasePermission):
#     message = "Вы не являетесь создателем"
#
#     def has_permission(self, request, view):
#         if request.user == view.get_object().author:
#             return True
#         return False
