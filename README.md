# Zepp Life Steps

一个基于 Python 的 Zepp Life（原小米运动）步数修改工具。

## 功能

* 使用 Zepp Life 账号密码登录
* 自动获取 `login_token`
* 自动获取 `app_token`
* 修改当天运动步数
* 支持通过 `.env` 配置账号信息
* 使用 `uv` 管理 Python 依赖

---

## 重要说明

本工具使用的是 **Zepp Life 账号**，不是小米账号。

由于 Zepp Life 的登录接口需要账号密码验证，因此：

* 不支持微信、Apple、手机系统等一键登录方式
* 必须注册一个 Zepp Life 账号，并使用账号密码登录
* 推荐使用邮箱注册 Zepp Life 账号

例如：

```
账号：your_account
密码：your_password
```

注册完成后，将该账号信息配置到 `.env` 文件中。

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
ZEEP_ACCOUNT=your_account
ZEEP_PASSWORD=your_password
ZEEP_STEPS=66666
```

参数说明：

| 变量              | 说明                    |
| --------------- | --------------------- |
| `ZEEP_ACCOUNT`  | Zepp Life 注册账号  |
| `ZEEP_PASSWORD` | Zepp Life 账号密码        |
| `ZEEP_STEPS`    | 修改后的目标步数（可选，默认 66666） |

注意：

* 请勿将 `.env` 文件提交到 GitHub
* `.env` 文件包含账号密码等敏感信息

建议保留：

`.env.example`

示例：

```env
ZEEP_ACCOUNT=your_account
ZEEP_PASSWORD=your_password
ZEEP_STEPS=66666
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

说明：

* `main.py`

  * 程序入口
  * 读取环境变量
  * 调用核心功能

* `xiaomi_steps.py`

  * 核心业务逻辑
  * Zepp Life 登录
  * Token 获取
  * 步数修改

* `.env`

  * 保存账号配置
  * 不提交到 Git

---

## 运行

推荐使用 uv：

```bash
uv run main.py
```

或者：

```bash
python main.py
```

运行成功示例：

```
账号: your_account, 目标步数: 66666
登录成功
获取Token成功，User ID=xxxxxxxx
获取app_token成功
✓ 步数修改成功
```

---

## 常见问题

### 登录失败

请检查：

* 是否使用 Zepp Life 注册账号
* 是否填写正确的账号密码
* 是否误用了小米账号登录方式
* 网络是否正常
* 是否触发接口访问频率限制

---

### 获取 Token 失败

可能原因：

* 账号登录状态异常
* Zepp Life 接口发生变化
* 网络请求失败

建议稍后重新运行。

---

### 修改失败

请确认：

* Zepp Life 账号可以正常登录
* `.env` 中账号密码正确
* 网络连接正常

---

## 开发

添加依赖：

```bash
uv add <package>
```

同步依赖：

```bash
uv sync
```

更新锁文件：

```bash
uv lock
```

---

## 免责声明

本项目仅用于学习和技术研究。

请遵守 Zepp Life 平台相关服务协议，不得将本项目用于违反平台规则或法律法规的用途。

因使用本项目产生的任何后果，由使用者自行承担。
