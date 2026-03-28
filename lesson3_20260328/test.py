"""
title: Example Filter
author: open-webui
author_url: https://github.com/open-webui
funding_url: https://github.com/open-webui
version: 0.1
"""
# 從 pydantic 匯入 BaseModel 和 Field，用於定義資料模型與欄位設定
from pydantic import BaseModel, Field
# 從 typing 匯入 Optional，用於標示可為 None 的型別
from typing import Optional


# 定義 Filter 類別，作為 Open WebUI 的過濾器插件主體
class Filter:
    # 定義系統層級的設定（Valves），繼承自 BaseModel 以支援型別驗證
    class Valves(BaseModel):
        # 過濾器的優先順序，數字越小優先級越高，預設為 0
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )
        # 系統層級允許的最大對話輪數，預設為 8
        max_turns: int = Field(
            default=8, description="Maximum allowable conversation turns for a user."
        )
        pass

    # 定義使用者層級的設定（UserValves），每位使用者可自行調整
    class UserValves(BaseModel):
        # 使用者層級允許的最大對話輪數，預設為 4
        max_turns: int = Field(
            default=4, description="Maximum allowable conversation turns for a user."
        )
        pass

    # 初始化方法，在 Filter 物件建立時自動執行
    def __init__(self):
        # 若要啟用自訂檔案處理邏輯，可取消下方註解
        # 設為 True 後，WebUI 會將檔案相關操作交由此類別的方法處理
        # self.file_handler = True

        # 建立 Valves 實例並指派給 self.valves，用於統一管理系統設定
        self.valves = self.Valves()
        pass

    # inlet 方法：請求進入 API 前的前處理器（pre-processor）
    def inlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # 印出目前模組名稱，方便除錯時確認來源
        print(f"inlet:{__name__}")
        # 印出收到的請求 body 內容
        print(f"inlet:body:{body}")
        # 印出目前使用者資訊
        print(f"inlet:user:{__user__}")

        # 判斷使用者角色是否為 "user" 或 "admin"，若是則進行對話輪數檢查
        if __user__.get("role", "admin") in ["user", "admin"]:
            # 從 body 中取得訊息列表，若不存在則回傳空列表
            messages = body.get("messages", [])

            # 取使用者設定與系統設定中較小的 max_turns 值，確保不超過任一限制
            max_turns = min(__user__["valves"].max_turns, self.valves.max_turns)
            # 若訊息數量超過最大輪數限制，則拋出例外中止請求
            if len(messages) > max_turns:
                raise Exception(
                    f"Conversation turn limit exceeded. Max turns: {max_turns}"
                )

        # 回傳（可能已修改的）請求 body，傳遞給後續的 API 處理
        return body

    # outlet 方法：API 回應後的後處理器（post-processor）
    def outlet(self, body: dict, __user__: Optional[dict] = None) -> dict:
        # 印出目前模組名稱，方便除錯時確認來源
        print(f"outlet:{__name__}")
        # 印出 API 回傳的 body 內容
        print(f"outlet:body:{body}")
        # 印出目前使用者資訊
        print(f"outlet:user:{__user__}")

        # 回傳（可能已修改的）回應 body
        return body
