# Example Filter 說明文件

## 概述

此程式是一個 **Open WebUI Filter 插件**，用於在使用者與 AI 對話的過程中，對請求與回應進行攔截與處理。主要功能是限制使用者的對話輪數，防止過長的對話消耗過多資源。

---

## 檔案結構說明

### 頂層 Docstring（模組說明）

```python
"""
title: Example Filter
author: open-webui
...
version: 0.1
"""
```

Open WebUI 插件的標準元資料區塊，平台會讀取這些資訊顯示在插件管理介面中。

---

## 類別說明

### `Filter`

插件的主體類別，Open WebUI 會自動識別並載入此類別。

---

### `Filter.Valves`（系統設定）

繼承自 `pydantic.BaseModel`，定義**管理員層級**的全域設定。

| 欄位 | 型別 | 預設值 | 說明 |
|------|------|--------|------|
| `priority` | `int` | `0` | 過濾器優先順序，數字越小越優先執行 |
| `max_turns` | `int` | `8` | 系統允許的最大對話輪數上限 |

---

### `Filter.UserValves`（使用者設定）

繼承自 `pydantic.BaseModel`，定義**使用者層級**的個人設定，每位使用者可自行調整。

| 欄位 | 型別 | 預設值 | 說明 |
|------|------|--------|------|
| `max_turns` | `int` | `4` | 該使用者允許的最大對話輪數 |

---

### `__init__`（初始化）

建立 `Filter` 物件時自動執行，初始化 `self.valves` 為 `Valves` 的預設實例。

若需要自訂檔案處理邏輯，可取消 `self.file_handler = True` 的註解，WebUI 將把檔案操作交由此類別處理。

---

### `inlet(body, __user__)` → `dict`

**請求前處理器（Pre-processor）**

在使用者訊息送往 AI API 之前被呼叫，可用於：
- 驗證請求內容
- 修改請求 body
- 根據條件中止請求（拋出例外）

**對話輪數限制邏輯：**

1. 確認使用者角色為 `"user"` 或 `"admin"`
2. 取得 `messages` 列表長度（代表目前對話輪數）
3. 以 `min(UserValves.max_turns, Valves.max_turns)` 計算實際上限
   - 例如：使用者設定 4，系統設定 8 → 實際上限為 4
4. 若訊息數超過上限，拋出 `Exception` 中止請求

**參數：**
- `body: dict` — 完整的請求內容（包含 messages、model 等）
- `__user__: Optional[dict]` — 使用者資訊，包含 `role` 與 `valves`

**回傳：** 修改後（或原始）的 `body` dict

---

### `outlet(body, __user__)` → `dict`

**回應後處理器（Post-processor）**

在 AI API 回傳結果之後被呼叫，可用於：
- 分析或記錄回應內容
- 修改回應 body 再傳回給使用者
- 進行後續的統計或稽核

目前實作僅印出 body 與使用者資訊後直接回傳，可依需求擴充。

**參數：**
- `body: dict` — API 回傳的完整回應內容
- `__user__: Optional[dict]` — 使用者資訊

**回傳：** 修改後（或原始）的 `body` dict

---

## 運作流程

```
使用者送出訊息
      ↓
  inlet() 被呼叫
  ├─ 檢查對話輪數
  ├─ 超過上限 → 拋出例外，中止請求
  └─ 未超過 → 回傳 body，繼續送往 AI API
      ↓
  AI API 處理
      ↓
  outlet() 被呼叫
  └─ 印出回應資訊，回傳 body 給使用者
```

---

## 注意事項

- `max_turns` 的實際上限取 `UserValves` 與 `Valves` 兩者的**較小值**，確保使用者無法自行突破系統上限。
- `inlet` 中的角色判斷目前包含 `"admin"`，若需排除管理員限制可調整條件。
- `__user__` 為 `Optional[dict]`，在某些情境下可能為 `None`，使用前應注意防呆處理。
