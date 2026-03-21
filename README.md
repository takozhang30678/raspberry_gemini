# __raspberry_gemini_revise_3nd
致理上課
#sudo systemctl status docker
#sudo systemctl start docker
#sudo systemctl stop docker
#ctrl b, ctrl alt b, ctrl j

vscode設定

    中文版
    自動存檔
    使用雲端登入至github
    終端機預設為Git bash
    安裝jupyter notebook
    安裝github codespace

codespace設定 - 開發環境的設定

    建立devcontainer.json(要求建立python的開發環境)
    啟動開發環境(rebuilt)->可以想像成重新灌作業系統

git設定

git config --global user.name "xxxxxxxx"
git config --global user.email "xxxxx@gmail.com"
git config --global pull.rebase false

git上傳流程

    變更 -> 暫存的變更 -> 建立有名稱的提交 -> 同步
    working tree -> stage -> commit -> push

git強制同步上傳目前的所有提交(當不知如何處理時)

git push --force

git conflic(檔案衝突)

    先修改衝突檔
    重新建立commit
    同步