# Zepp Life Steps

一个基于 Python 的 Zepp Life（原小米运动）步数修改工具。

> 本项目提供 **命令行版本（CLI）**，适合开发者、本地自动化任务和脚本调用。
>
> 如果你希望直接通过浏览器使用，请查看配套 Web 项目：
>
> 👉 **Xiaomi Steps Web**
>
> https://github.com/DannyWongIsAvailable/Xiaomi-Steps-web.git
>
> 在线体验：
>
> https://xiaomi-steps-web.pages.dev/

---

## 项目关系

本仓库是 Xiaomi Steps 的核心 Python 实现。

对应关系：

```text
Xiaomi-Steps
        |
        |  核心接口逻辑
        |  - Zepp Life 登录
        |  - Token 获取
        |  - 步数提交
        |
        ↓

Xiaomi-Steps-web
        |
        |  Vue 3 前端
        |  Cloudflare Pages Function
        |  浏览器在线使用
```

两个项目共享相同的 Zepp Life API 调用思路：

- 使用 Zepp Life 账号密码登录
- 自动获取 `login_token`
- 自动获取 `app_token`
- 修改当天运动步数

---

## 功能

- 使用 Zepp Life 账号密码登录
- 自动获取 `login_token`
- 自动获取 `app_token`
- 修改当天运动步数（默认随机生成 25000-50000 步）
- 支持 `.env` 配置账号信息
- 使用 `uv` 管理 Python 依赖

---

## 重要说明

本工具使用的是 **Zepp Life 账号**，不是小米账号。

由于 Zepp Life 登录接口需要账号密码验证：

- 不支持微信、Apple、手机系统等一键登录方式
- 必须注册 Zepp Life 账号并使用账号密码登录
- 推荐使用邮箱注册 Zepp Life 账号

---

## 环境要求

- Python 3.11+
- uv

安装：

```bash
pip install uv
```

---

## 安装

```bash
git clone https://github.com/DannyWongIsAvailable/Xiaomi-Steps.git
cd Xiaomi-Steps
uv sync
```

---

## 配置

创建 `.env`：

```env
ZEEP_ACCOUNT=your_account
ZEEP_PASSWORD=your_password
ZEEP_STEPS=30000
```

---

## 运行

```bash
uv run main.py
```

---

## 项目结构

```text
.
├── main.py
├── xiaomi_steps.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## 常见问题

如果希望免安装 Python 环境，推荐使用 Web 版本：

https://github.com/DannyWongIsAvailable/Xiaomi-Steps-web.git

---

## 免责声明

本项目仅用于学习和技术研究。

请遵守 Zepp Life 平台相关服务协议，不得将本项目用于违反平台规则或法律法规的用途。

因使用本项目产生的任何后果，由使用者自行承担。
