import traceback

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

import config


def set_google_drive_permission_to_anyone(file_id):
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            config.CREDENTIAL_PATH, config.CREDENTIAL_SCOPES
        )
        service = build("drive", "v3", credentials=creds)

        permission_to_anyone = {"role": "reader", "type": "anyone"}
        response = (
            service.permissions()
            .create(
                body=permission_to_anyone, fileId=file_id, sendNotificationEmail=False
            )
            .execute()
        )

        print("Access Granted...")

        return response
    except:
        traceback.print_exc()


if __name__ == "__main__":
    file_id = ""
    response = set_google_drive_permission_to_anyone(file_id)
    print(response)
