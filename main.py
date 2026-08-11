import os
from dotenv import load_dotenv

from xiaomi_steps import login, get_app_token, change_steps


def main():
    load_dotenv()

    account = os.environ["XIAOMI_ACCOUNT"]
    password = os.environ["XIAOMI_PASSWORD"]
    steps = int(os.environ.get("XIAOMI_STEPS", "66666"))

    print(f"账号: {account}, 目标步数: {steps}")

    login_token, user_id = login(account, password)
    if not login_token:
        return

    app_token = get_app_token(login_token)
    if not app_token:
        return

    if change_steps(user_id, app_token, str(steps)):
        print("✓ 步数修改成功")
    else:
        print("✗ 步数修改失败")


if __name__ == "__main__":
    main()
