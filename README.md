# 打地鼠遊戲
![螢幕擷取畫面 2024-05-23 遊戲中](https://github.com/TamyTsai/whack-a-mole-game/assets/97825677/b198e4c0-04ef-43ab-9a54-138d97fcba6c)

## 關於打地鼠遊戲
- 挑戰在時限內打到最多的地鼠，來測試你的手眼協調吧！
- 遊戲開始後，玩家透過移動滑鼠控制鐵鎚，地鼠將在整個遊戲畫面中隨機出現，玩家看到地鼠後，須操控鐵鎚敲打地鼠(按下滑鼠左鍵可敲下鐵鎚)，遊戲時間限制 20 秒，時間結束後，遊戲根據玩家打到的地鼠數量結算成績。

<!-- ## 專案目的 -->

<!-- ## 簡介
- 本專案為一個打地鼠遊戲，玩家透過移動滑鼠來操縱鐵鎚，以鐵鎚敲擊地鼠，在時限內獲取分數
- 以Python撰寫
- 主要使用Pygame套件中的函式撰寫
- 本專案圖片素材皆為自行繪製 -->

<!-- ## 功能
- 於遊戲初始畫面按下鍵盤ENTER鍵，即開始遊戲
- 透過移動滑鼠來操縱鐵鎚，對準隨機出現的地鼠按下滑鼠左鍵，即可敲打地鼠
- 每成功敲打一隻地鼠，得1分
- 當成功敲打地鼠，就會隨機再生成下一隻地鼠
- 遊戲時限20秒
- 20秒結束時，結算分數，分數顯示於畫面，並且按下ENTER鍵可重新開始遊戲 -->

## 專案畫面與功能介紹
### 初始畫面
- 按下鍵盤ENTER鍵，即開始遊戲
  
![螢幕擷取畫面 2024-05-23 初始畫面](https://github.com/TamyTsai/whack-a-mole-game/assets/97825677/14535124-3e8b-4283-b704-41daf10063df)

<hr>

### 遊戲進行中
- 透過移動滑鼠來操縱鐵鎚，對準隨機出現的地鼠按下滑鼠左鍵，即可敲打地鼠
- 每成功敲打一隻地鼠，得1分
- 當成功敲打地鼠，就會隨機再生成下一隻地鼠
- 遊戲時限20秒
  
![螢幕擷取畫面 2024-05-23 遊戲中](https://github.com/TamyTsai/whack-a-mole-game/assets/97825677/b198e4c0-04ef-43ab-9a54-138d97fcba6c)

<hr>

### 遊戲結束
- 20秒結束時，結算分數，分數顯示於畫面，並且按下ENTER鍵可重新開始遊戲
  
![螢幕擷取畫面 2024-05-23 遊戲結束](https://github.com/TamyTsai/whack-a-mole-game/assets/97825677/89645165-57b3-4426-be7f-5bcb703c42ab)


## 安裝與執行
以下皆為於windows環境運行

<hr>

### 命令列介面執行
### 檢查是否有安裝Python，若無，則至官網下載安裝
```bash
py --version
```

### 安裝Python延伸套件

### 檢查是否有安裝pip
```bash
py -m pip --version
```

### 安裝Pygame套件
```bash
py -m pip install pygame
```

### 取得專案
```bash
git clone https://github.com/TamyTsai/whack-a-mole-game.git
```

### 移動到專案內
```bash
cd whack-a-mole-game
```

### 執行專案
```bash
python main.py
```

<hr>

### 圖形化使用者介面執行
下載專案後，雙擊專案目錄中之main.exe，即可執行程式，開啟遊戲
![exe檔](https://github.com/user-attachments/assets/392c25ca-5c01-4d28-8537-7791df553783)


## 資料夾及檔案說明
- img - 遊戲圖片放置處
- main.exe - 打包後的遊戲主程式執行檔
- main.py - 遊戲Python檔
- mole.ico - 遊戲圖示

<!-- ## 專案技術
- Python v3.12.3
  - pygame v2.5.2  -->

## 專案技術
- 程式語言：Python
- 框架：pygame
- 版本控制：Git

## 使用技術詳細說明
- 使用pygame模組以簡化製作遊戲之過程，包含簡化加入文字、圖案、聲音等元素，與進行事件處理等過程。
- 使用Python的標準函式time，以處理時間。
- 使用Python的標準函式random，以隨機產生地鼠的座標
- 使用Python的標準函式os，以統一路徑寫法

## 聯絡作者
你可以透過email與我聯絡：tamy8677@gmail.com

<i>最後更新：2024.5.23</i>
