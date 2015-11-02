from django.conf import settings
import requests



def invite_to_slack(team, email, token=settings.SLACK_API_KEY):
    return requests.post(
        'https://{}.slack.com/api/users.admin.invite'.format(team),
         data={"email": email, "token": token, "set_active": "true"}).json()
