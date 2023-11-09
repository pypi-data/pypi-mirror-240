# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         14/12/22 4:21 AM
# Project:      Zibanu Django Project
# Module Name:  user
# Description:
# ****************************************************************
from django.contrib import auth
from rest_framework_simplejwt.models import TokenUser
from typing import Any


def get_user(user: Any) -> Any:
    """
    Function to get user from SimpleJWT TokenUser token or django user.

    Parameters
    ----------
    user : User object to review.

    Returns
    -------
    local_user: Django user object.
    """
    local_user = user
    user_model = auth.get_user_model()
    if isinstance(user, TokenUser):
        local_user = user_model.objects.get(pk=local_user.id)

    return local_user


def get_user_object(user: Any) -> Any:
    """
    Legacy function. Use "get_user" instead. This function will be removed in future versions.

    Parameters
    ----------
    user : User object to review.

    Returns
    -------
    Django user object.
    """
    return get_user(user)