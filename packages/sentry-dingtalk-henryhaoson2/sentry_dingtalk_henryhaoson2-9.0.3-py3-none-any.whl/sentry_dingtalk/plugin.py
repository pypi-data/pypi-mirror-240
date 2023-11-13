"""
  @Project     : sentry-dingtalk
  @Time        : 2021/07/12 17:34:35
  @File        : plugin.py
  @Author      : Jedore and Henryhaoson
  @Software    : VSCode
  @Desc        :
"""

import requests
import six
from sentry import tagstore
from sentry.plugins.bases import notify
from sentry.utils import json
from sentry.utils.http import absolute_uri
from sentry.integrations import FeatureDescription, IntegrationFeatures
from sentry_plugins.base import CorePluginMixin
from django.conf import settings
import logging

logger = logging.getLogger('sentry.plugins.dingtalk')


class DingTalkPlugin(CorePluginMixin, notify.NotificationPlugin):
    title = "DingTalk"
    slug = "dingtalk"
    description = "Post notifications to Dingtalk."
    conf_key = "dingtalk"
    required_field = "webhook"
    author = "Henryhaoson"
    author_url = "https://git.17bdc.com/android-apps/sentry-dingtalk"
    version = "9.0.3"
    resource_links = [
        ("Report Issue", "https://git.17bdc.com/android-apps/sentry-dingtalk/issues"),
        ("View Source", "https://git.17bdc.com/android-apps/sentry-dingtalk"),
    ]

    feature_descriptions = [
        FeatureDescription(
            """
                Configure rule based Dingtalk notifications to automatically be posted into a
                specific channel.
                """,
            IntegrationFeatures.ALERT_RULE,
        )
    ]

    def is_configured(self, project):
        logger.info("is_configured start")
        return bool(self.get_option("webhook", project))

    def get_config(self, project, **kwargs):
        return [
            {
                "name": "webhook",
                "label": "webhook",
                "type": "url",
                "placeholder": "https://oapi.dingtalk.com/robot/send?access_token=**********",
                "required": True,
                "help": "钉钉 webhook 会@ 成员",
                "default": self.set_default(project, "webhook", "DINGTALK_WEBHOOK"),
            },
            {
                "name": "webhook_optional",
                "label": "webhook_optional",
                "type": "url",
                "placeholder": "https://oapi.dingtalk.com/robot/send?access_token=**********",
                "required": False,
                "help": "Optional - 可选 webhook， 不会 @成员",
                "default": self.set_default(
                    project, "webhook_optional", ""
                ),
            },
            {
                "name": "ats",
                "label": "@成员",
                "type": "string",
                "placeholder": "填写钉钉手机号",
                "required": False,
                "help": "Optional - 填写钉钉手机号，会 @ 对应成员",
                "default": self.set_default(
                    project, "ats", ""
                ),
            },
            {
                "name": "alter_template",
                "label": "告警模板",
                "type": "select",
                "choices": (
                    ("Server", "服务端告警模板"),
                    ("App", "app告警模板")
                ),
                "required": True,
                "help": "告警模板选择",
                "default": "Server"
            }
        ]

    def set_default(self, project, option, env_var):
        if self.get_option(option, project) != None:
            return self.get_option(option, project)
        if hasattr(settings, env_var):
            return six.text_type(getattr(settings, env_var))
        return None

    def notify(self, notification, raise_exception=False):
        logger.info("func notify start")

        try:
            event = notification.event
            group = event.group
            self._post(event, group)
        except Exception as e:
            logger.error(e, "notify exit(1)")

    def _post(self, event, group):
        logger.info("func _post start")
        project = group.project
        release = event.release

        try:
            webhook = self.get_option("webhook", project)
            webhook_optional = self.get_option("webhook_optional", project)
            ats_str = self.get_option("ats", project)
            if ats_str == None:
                ats_str = ""
            if webhook_optional == None:
                webhook_optional = "http://localhost"

            ats_array = ats_str.split(",")
            ats_ding_str = ""
            for at in ats_array:
                ats_ding_str = f"{ats_ding_str} @{at} "

            issue_link = group.get_absolute_url(params={"referrer": "dingtalk"})
            release_link_path = issue_link.split("/issues/")[0]
            release_link = f"{release_link_path}/releases/{release}?project={project.id}"

            alter_template = self.get_option("alter_template", project)
            if alter_template == "Server":
                logger.info("use Server alter_template")
                etype = event.get_event_metadata().get('type')
                environment = event.get_tag('environment')
                server_name = event.get_tag('server_name')
                project = event.get_tag('project')
                payload = f"#### type: [{etype}] \n\n"
                payload = f"{payload} #### App: {project} \n\n"
                payload = f"{payload} #### Environment: {environment} \n\n"
                payload = f"{payload} #### Server Name: [{server_name}] \n\n"
                payload = f"{payload} {event.title} \n\n"
                payload = f"{payload} {event.culprit} \n\n"
                payload = f"{payload} {issue_link} \n\n"
            else:
                logger.info("use App alter_template")
                user = event.get_minimal_user()
                user_id = None
                if user is not None:
                    user_id = user.id if hasattr(user, 'id') else None
                payload = f"## Error: [{group.title}>>]({issue_link}) \n\n"
                payload = f"{payload} #### UserId: [{user_id}](https://admin.shanbay.com/jetty/users/{user_id}) \n\n"
                payload = f"{payload} #### Project: {project.name} \n\n"
                payload = f"{payload} #### Release: [{release}]({release_link}) \n\n"
                payload = f"{payload} #### Event type: {group.get_event_type()} \n\n"
                payload = f"{payload} > Detail: {group.message} \n\n"

            headers = {
                "Content-type": "application/json",
                "Accept": "text/plain",
                "charset": "utf8"
            }

            data_optional = {
                "msgtype": "markdown",
                "markdown": {
                    "title": group.title,
                    "text": payload,
                },
            }
            # 可选 webhook，不会 @ 成员
            logger.info("webhook_optional start")
            if len(webhook_optional) != 0:
                requests.post(webhook_optional, data=json.dumps(
                    data_optional), headers=headers)

            # 必填 webhook，如果配置了 @ 成员，会执行
            payload = f"{payload} {ats_ding_str} \n\n"
            data = {
                "msgtype": "markdown",
                "markdown": {
                    "title": group.title,
                    "text": payload,
                },
                "at": {
                    "atMobiles": ats_array,
                    "isAtAll": "false"
                }
            }
            data_json = json.dumps(data)
            logger.info(data_json)
            requests.post(webhook, data=data_json, headers=headers)
        except Exception as e:
            logger.error(e, "_post fail")
        logger.info("func _post end")
