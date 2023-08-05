# -*- coding: utf-8 -*-


def isNotCurrentProfile(context):
    return context.readDataFile("collectivecontactduplicated_marker.txt") is None


def post_install(context):
    """Post install script"""
    if isNotCurrentProfile(context):
        return
