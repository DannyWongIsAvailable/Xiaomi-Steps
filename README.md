# Xiaomi Steps

一个基于 Python 的小米运动（Zepp Life）步数修改工具。

## 功能

* 使用小米账号登录
* 自动获取 `login_token`
* 自动获取 `app_token`
* 修改当天运动步数
* 支持通过 `.env` 配置账号信息，不需要修改源码
* 使用 `uv` 管理依赖

---

## 环境要求

* Python 3.11+
* uv

安装 uv：

```bash
pip install uv
```

---

## 安装

克隆项目：

```bash
git clone <your-repository>
cd <your-repository>
```

安装依赖：

```bash
uv sync
```

---

## 配置

在项目根目录创建 `.env` 文件：

```env
XIAOMI_ACCOUNT=your_account
XIAOMI_PASSWORD=your_password
XIAOMI_STEPS=66666
```

参数说明：

| 变量                | 说明                    |
| ----------------- | --------------------- |
| `XIAOMI_ACCOUNT`  | 小米账号（手机号或邮箱）          |
| `XIAOMI_PASSWORD` | 小米账号密码                |
| `XIAOMI_STEPS`    | 修改后的目标步数（可选，默认 66666） |

为了避免泄露账号密码，请不要将 `.env` 提交到 Git。

建议保留一个 `.env.example`：

```env
XIAOMI_ACCOUNT=your@email.com
XIAOMI_PASSWORD=your_password
XIAOMI_STEPS=66666
```

---

## 项目结构

```
.
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
├── uv.lock
├── xiaomi_steps.py
└── .venv/
```

其中：

* `main.py`：程序入口，负责读取环境变量并执行流程。
* `xiaomi_steps.py`：核心业务逻辑，包括登录、获取 Token、修改步数等。
* `.env`：保存账号及配置（不会提交到 Git）。

---

## 运行

推荐使用 uv：

```bash
uv run main.py
```

也可以：

```bash
python main.py
```

运行成功后示例输出：

```
账号: your@email.com, 目标步数: 66666
登录成功
获取Token成功，User ID=xxxxxxxx
获取app_token成功
✓ 步数修改成功
```

---

## 常见问题

### 登录失败

请确认：

* 账号或密码是否正确
* 网络是否正常
* 是否触发了接口访问频率限制

---

### 提示获取 Token 失败

通常是账号登录状态异常或接口变更导致，可稍后重试。

---

### 修改失败

请确认：

* 账号能够正常登录 Zepp Life（小米运动）
* 当天已有运动数据
* 网络连接正常

---

## 开发

安装新增依赖：

```bash
uv add <package>
```

同步依赖：

```bash
uv sync
```

更新依赖：

```bash
uv lock
```

---

## 免责声明

本项目仅供学习与技术研究使用。

请遵守相关平台的服务协议，不得将本项目用于任何违反法律法规或平台规则的用途。因使用本项目造成的任何后果，由使用者自行承担。
