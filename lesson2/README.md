UV：現代化的 Python 套件管理與虛擬環境工具
目錄

    簡介
    為什麼選擇 UV？
    安裝 UV
    基本使用
    虛擬環境管理
    套件管理
    專案管理
    進階功能
    與其他工具的比較
    最佳實踐
    常見問題
    參考資料

簡介

uv 是由 Astral 團隊（ruff 的開發者）使用 Rust 語言打造的現代化 Python 套件管理與虛擬環境工具。它旨在提供極速的套件安裝、依賴解析和專案管理功能，成為 Python 開發者的首選工具。
主要特色

    ⚡ 極速性能：比 pip 快 10-100 倍
    🔧 一體化工具：整合虛擬環境、套件管理、依賴解析
    📦 現代化專案管理：支援 pyproject.toml 標準
    🐍 Python 版本管理：自動安裝和管理 Python 版本
    🔒 依賴鎖定：確保可重現的建置環境

為什麼選擇 UV？
與 Conda 的比較

    速度：uv 在安裝和解析依賴項方面，速度顯著優於 Conda。這在大型專案或需要頻繁建立環境的場景中尤其有感。
    現代化的專案管理：uv 鼓勵使用 pyproject.toml 檔案來管理專案依賴，這是目前 Python 社群推崇的最佳實踐，有助於提高專案的可重現性和標準化。
    單一工具鏈：uv 整合了虛擬環境管理、套件安裝、依賴解析等多種功能，無需像 Conda 那樣在 conda 和 pip 之間切換。

與 pip 的比較

    依賴解析：uv 提供更智能的依賴解析，避免衝突
    虛擬環境整合：無需手動建立和管理虛擬環境
    鎖定檔案：自動生成 uv.lock 檔案確保可重現性
    Python 版本管理：自動安裝所需的 Python 版本

安裝 UV
系統需求

    Python 3.8+（UV 會自動管理 Python 版本）
    支援的作業系統：Windows、macOS、Linux

安裝方法
方法一：獨立安裝腳本（推薦）

macOS 和 Linux：

curl -LsSf https://astral.sh/uv/install.sh | sh

Windows：

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

方法二：套件管理器

macOS (Homebrew)：

brew install uv

Windows (Scoop)：

scoop install uv

Linux (Cargo)：

cargo install uv

方法三：pip 安裝

pip install uv

驗證安裝

uv --version

基本使用
快速開始

# 在已有的專案
uv init --python 3.10
uv venv
uv sync

# 建立新專案
uv init my-project
cd my-project
uv sync

# 建立虛擬環境
uv venv

# 啟用虛擬環境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows

# 安裝套件
uv add requests

# 執行 Python 腳本
uv run python script.py

虛擬環境管理
建立虛擬環境
基本建立

# 在當前目錄建立虛擬環境（預設名稱：.venv）
uv venv

# 指定 Python 版本
uv venv --python 3.11

# 指定虛擬環境名稱
uv venv --name myenv

# 指定虛擬環境路徑
uv venv --path /path/to/venv

Python 版本管理

# 列出可用的 Python 版本
uv python list

# 安裝特定 Python 版本
uv python install 3.11

# 使用特定 Python 版本建立虛擬環境
uv venv --python 3.11

啟用/停用虛擬環境
啟用虛擬環境

# macOS/Linux
source .venv/bin/activate

# Windows Command Prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

停用虛擬環境

deactivate

虛擬環境管理命令

# 列出所有虛擬環境
uv venv list

# 移除虛擬環境
uv venv remove .venv

# 同步虛擬環境（根據 pyproject.toml 更新）
uv sync

套件管理
安裝套件
使用 uv add（推薦）

# 安裝套件到專案
uv add requests

# 安裝多個套件
uv add numpy pandas matplotlib

# 安裝開發依賴
uv add pytest --dev

# 安裝特定版本
uv add "django>=4.0,<5.0"

# 安裝可選依賴
uv add "fastapi[all]"

使用 uv pip

# 在虛擬環境中安裝套件
uv pip install requests

# 從 requirements.txt 安裝
uv pip install -r requirements.txt

# 安裝開發依賴
uv pip install -e .

套件管理命令

# 列出已安裝的套件
uv pip list

# 顯示套件資訊
uv pip show requests

# 更新套件
uv pip install --upgrade requests

# 移除套件
uv remove requests

# 同步依賴（根據 pyproject.toml）
uv sync

依賴管理

# 生成 requirements.txt
uv pip freeze > requirements.txt

# 從 requirements.txt 安裝
uv pip install -r requirements.txt

# 檢查依賴衝突
uv pip check

專案管理
初始化專案

# 建立新專案
uv init my-project
cd my-project

# 或初始化現有目錄
uv init

pyproject.toml 管理

# 新增依賴到 pyproject.toml
uv add requests

# 新增開發依賴
uv add pytest --dev

# 移除依賴
uv remove requests

# 更新依賴
uv sync

專案執行

# 執行 Python 腳本
uv run python script.py

# 執行模組
uv run -m mymodule

# 執行命令
uv run pytest

# 執行腳本（在 pyproject.toml 中定義）
uv run my-script

進階功能
鎖定檔案 (uv.lock)

# 生成鎖定檔案
uv lock

# 根據鎖定檔案安裝
uv sync --locked

工作區管理

# 建立工作區
uv init --workspace

# 新增工作區成員
uv add --workspace ./subproject

腳本定義

在 pyproject.toml 中定義腳本：

[project.scripts]
my-script = "mypackage.cli:main"

環境變數管理

# 設定環境變數
uv run --env-file .env python script.py

與其他工具的比較
功能 	UV 	pip 	conda 	poetry
安裝速度 	⚡ 極快 	🐌 慢 	🐌 慢 	🐌 慢
依賴解析 	✅ 智能 	❌ 基本 	✅ 智能 	✅ 智能
虛擬環境 	✅ 整合 	❌ 需手動 	✅ 整合 	✅ 整合
Python 管理 	✅ 自動 	❌ 無 	✅ 支援 	❌ 無
鎖定檔案 	✅ uv.lock 	❌ 無 	❌ 無 	✅ poetry.lock
專案管理 	✅ 現代 	❌ 基本 	❌ 基本 	✅ 現代
最佳實踐
1. 專案結構

my-project/
├── .venv/              # 虛擬環境（由 uv 管理）
├── pyproject.toml      # 專案配置
├── uv.lock            # 依賴鎖定檔案
├── src/
│   └── mypackage/
└── tests/

2. 依賴管理

    使用 uv add 而非 uv pip install
    定期執行 uv sync 同步依賴
    將 uv.lock 加入版本控制

3. 開發流程

# 1. 建立專案
uv init my-project
cd my-project

# 2. 新增依賴
uv add requests fastapi

# 3. 開發
uv run python main.py

# 4. 測試
uv add pytest --dev
uv run pytest

# 5. 部署
uv sync --locked

常見問題
Q: 如何從 requirements.txt 遷移？

# 安裝現有依賴
uv pip install -r requirements.txt

# 轉換為 pyproject.toml
uv add $(uv pip freeze | cut -d'=' -f1)

Q: 如何處理私有套件？

在 pyproject.toml 中設定：

[[tool.uv.index]]
name = "private"
url = "https://pypi.company.com/simple/"

Q: 如何更新所有依賴？

# 更新所有依賴
uv sync --upgrade

# 更新特定依賴
uv add requests --upgrade

Q: 如何處理不同環境的依賴？

# 開發環境
uv add pytest --dev

# 生產環境
uv sync --no-dev

參考資料

    UV 官方文件
    UV GitHub 儲存庫
    pyproject.toml 規範
    Python 套件管理最佳實踐

結論

uv 憑藉其卓越的速度和現代化的專案管理理念，為 Python 開發者提供了一個取代傳統工具的絕佳選擇。透過遵循本指南，您可以輕鬆地將您現有的開發流程轉移到 uv，並享受到更高效、更流暢的 Python 開發體驗。從今天起，嘗試在您的新專案中使用 uv，感受下一代 Python 工具所帶來的變革。

