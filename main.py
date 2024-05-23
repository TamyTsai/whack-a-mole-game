import pygame # 引入Pygame模組 以使用其函式
import time 
from random import randint # 用以隨機生成地鼠之座標值
import os # 統一路徑寫法

FPS = 60 # 遊戲幀數

WIDTH = 400 # 視窗寬度
HEIGHT = 400  # 視窗高度

WHITE = (255, 255, 255) # 白色

x, y = None, None # 地鼠座標 (初始設定為沒有地鼠，所以沒有地鼠座標位置)
score = 0 # 遊戲分數
game_time = 20 # 遊戲時間限制
state = 0 # 遊戲狀態:初始畫面0 遊戲中1 結束2

# 創建視窗 及 頻率鐘
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # pygame用以創建視窗的函式，函式參數為一個元組，裏頭裝視窗寬高
pygame.display.set_caption("打地鼠") # 視窗標題設定
clock = pygame.time.Clock() # 創建此頻率鐘物件 可對時間做管理與操縱

# 載入遊戲圖片
mallet = pygame.image.load(os.path.join("img", "mallet.png")) # 一般槌子
down_mallet = pygame.image.load(os.path.join("img", "down-mallet.png")) # 打下去的槌子
mole = pygame.image.load(os.path.join("img", "mole.png")) # 地鼠
bad_mole = pygame.image.load(os.path.join("img", "bad-mole.png")) # 壞地鼠
mole_mini = pygame.transform.scale(mole, (25, 19)) # 小地鼠(視窗左上圖示)
pygame.display.set_icon(mole_mini) # 設定視窗左上圖示
grass = pygame.image.load(os.path.join("img", "grass.png")) # 草地

pygame.mouse.set_visible(False) # 隱藏滑鼠座標顯示(因為要讓 鼠標與槌子 融為一體)
pygame.font.init() # 初始化文字模組

# 初始畫面
def welcome_screen():
    screen.blit(grass,(0,0)) # 在畫面(screen)畫出(blit)草的圖片(grass) 圖片左上角座標為(0,0)
    font = pygame.font.SysFont('corbel',40) # 設定字體
    text = font.render("Press ENTER to start", False, WHITE) # 將文字物件 渲染出來 #(文字內容, 字體是否反鋸齒, 文字顏色)
    screen.blit(text, ((WIDTH - text.get_width())/2, 185)) # 在畫面畫出剛剛渲染出來的文字
    mallet_position = mallet.get_rect() # 將槌子以矩形框起來(取得 槌子 的矩形範圍)
    mallet_position.center = pygame.mouse.get_pos() # 將槌子的中心點 設在 滑鼠的位置
    if pygame.mouse.get_pressed()[0]: # pygame.mouse.get_pressed()會回傳一整串布林值(代表每個滑鼠按鍵是否被按下的狀態) # 列表中第一筆[0]資料為滑鼠左鍵是否被按下 # 若滑鼠左鍵被按下
        screen.blit(down_mallet, mallet_position) # 就在畫面(screen)畫出(blit)打下去的槌子圖片(down_mallet) 定位在滑鼠所在矩形位置(mallet_position)
    else:  # 如果沒有按下滑鼠左鍵
        screen.blit(mallet, mallet_position) # 就在畫面(screen)畫出(blit)一般槌子圖片(mallet) 定位在滑鼠所在矩形位置(mallet_position)

# 遊戲進行
def play():
    global state, score, start_time # 取用 遊戲狀態、分數、遊戲開始時間 資訊
    start_time = time.time() # 設定遊戲開始時間 為 當前時間 # time.time()函式會取得 目前時間
    score = 0 # 初始分數設定為0
    state = 1 # 遊戲狀態設定為 遊戲中
    new_mole() # 產生新地鼠 函式
    whack() # 產生新地鼠瞬間先檢查是否有被打到 函式

# 結束遊戲
def end():
    global state # 取用 遊戲狀態 資訊
    state = 2 # 遊戲狀態設定為 結束

# 產生新地鼠 函式
def new_mole():
    global x, y # 取用 地鼠座標 資訊
    x = randint(0, WIDTH - mole.get_width()) # 地鼠的左邊邊界，可以位於視窗最左邊，到視窗最右邊減去一個地鼠寬度的距離
    y = randint(30, HEIGHT - mole.get_height()) # 地鼠的上方邊界，可以位於離視窗上方30px之處，到視窗最底部減去一個地鼠高度的距離

# 判斷是否在矩形區塊內 函式
def isInRect(p, rect): # (點座標, 矩形左上角座標 與 長寬) # 參數的資料型態為 元組
    x1, y1 = p # 點座標
    x2, y2, len, width = rect # 矩形左上角座標 與 長(橫向)寬(縱向)
    if(x1 < x2 or x1 > x2+len): # 如果點座標在x軸方向，不在 矩形 的範圍(矩形 左邊界:x2 右邊界:x2+len)
        return False # 就回傳 不在 矩形區塊內
    elif(y1 < y2 or y1 > y2+width): # 如果點座標在y軸方向，不在 矩形 的範圍(矩形 上邊界:y2 下邊界:y2+width)
        return False # 就回傳 不在 矩形區塊內
    else: # 如果點座標 不管在x或y軸方向 都在 矩形座標的範圍內
        return True # 就回傳 在 矩形區塊內

# 產生新地鼠瞬間先檢查是否有被打到 並且在判斷有打到時 加分 函式 
def whack():
    global score  # 取用 遊戲分數 資訊
    mx, my =  pygame.mouse.get_pos() # 將滑鼠目前的x, y座標 指定給 變數 mx, my
    width, height = mole.get_size() # 將地鼠圖片的寬、高 指定給 變數 width, height
    if isInRect((mx,my),(x, y, width, height)): # 如果滑鼠 目前的x, y座標 在 地鼠矩形範圍內
    # 傳入 兩個 分別存有 點座標(滑鼠位置) 與 矩形座標及長寬(地鼠位置及大小) 的 元組 進isInRect(p, rect)函式
        score += 1 # 遊戲分數就加1分
        new_mole() # 並生成新地鼠
        # 地鼠沒有被打到 就不生成更多新地鼠

# 遊戲中畫面
def play_screen():
    screen.blit(grass, (0,0)) # 畫草地背景
    font = pygame.font.SysFont('corbel', 30) # 設定字體
    text_score = font.render('Score:' + str(score), False, WHITE) # 渲染 分數文字 # 將文字物件 渲染出來 #(文字內容, 字體是否反鋸齒, 文字顏色)
    current = game_time - (time.time() - start_time) # 現在剩餘時間 = 遊戲時間限制(20秒) - (目前時間點 - 遊戲開始的時間點) = 遊戲時間限制(20秒) - 遊戲開始後已經過時間
    if current <= 0: # 若現在剩下的時間<=0
        end() # 就結束遊戲
    text_time = font.render('Time:' + str(int(current)), False, WHITE) # 渲染 時間文字 
    if pygame.mouse.get_pressed()[0]: # pygame.mouse.get_pressed()會回傳一整串布林值(代表每個滑鼠按鍵是否被按下的狀態) # 列表中第一筆[0]資料為滑鼠左鍵是否被按下 # 若滑鼠左鍵被按下
        screen.blit(down_mallet, pygame.mouse.get_pos()) # 就在畫面(screen)畫出(blit)打下去的槌子圖片(down_mallet) 定位在滑鼠所在位置(pygame.mouse.get_pos())
    else:  # 如果沒有按下滑鼠左鍵
        screen.blit(mallet, pygame.mouse.get_pos()) # 就在畫面(screen)畫出(blit)一般槌子圖片(mallet) 定位在滑鼠所在位置(pygame.mouse.get_pos())
    screen.blit(text_score, (10,0)) # 在畫面(左上角) 畫出 渲染後 分數文字
    screen.blit(text_time, (300,0)) # 在畫面(右上角) 畫出 渲染後 現在剩餘時間 文字
    screen.blit(mole, (x, y)) # 在畫面 畫出 地鼠圖片

# 結束畫面
def end_screen():
    screen.blit(grass, (0,0)) # 畫草地背景
    font = pygame.font.Font(None, 48) # 設定 遊戲結束 字體
    game_over = font.render("GAME OVER", False, WHITE) # 渲染後 遊戲結束 文字 # 將文字物件 渲染出來 #(文字內容, 字體是否反鋸齒, 文字顏色)
    font = pygame.font.Font(None, 25) # 設定 最終分數 字體
    points = font.render("Score: " + str(score), False, WHITE) # 渲染後 最終分數 文字 
    font = pygame.font.Font(None, 22) # 設定 重新開始 字體
    restart = font.render("Press ENTER to play again", False, WHITE) # 渲染後 重新開始 文字 
    # 在畫面畫出以上 渲染後的 字
    screen.blit(game_over, ((WIDTH/2 - game_over.get_width()/2), 100))
    screen.blit(points, ((WIDTH/2 - points.get_width()/2), 200))
    screen.blit(restart, ((WIDTH/2 - restart.get_width()/2), 300))

# 遊戲迴圈
running = True
while running: # running為True時:

    # 取得輸入 更新遊戲
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 檢查 事件列表中 事件內容 是否為 使用者點擊關閉視窗鍵
            running = False # 跳出迴圈 關閉遊戲
        elif state == 0: # 如果遊戲狀態為 初始畫面 下
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: # 按下了ENTER鍵
                play() # 執行 遊戲進行 函數
        elif state == 1: # 如果遊戲狀態為 遊戲中
            if event.type == pygame.MOUSEBUTTONDOWN: # 點下滑鼠
                whack() # 執行 產生新地鼠瞬間先檢查是否有被打到 並且在判斷有打到時 加分 函式 
        elif state == 2: # 如果遊戲狀態為 結束(等待重新開始的畫面)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN: # 按下了ENTER鍵
                play() # 執行 遊戲進行 函數
    # 畫面顯示
    if state == 0:
        welcome_screen()
    elif state == 1:
        play_screen()
    elif state == 2:
        end_screen()
    
    clock.tick(FPS) # 限制畫面更新速度
    pygame.display.update() # 更新畫面，一秒鐘執行FPS次

# running = False所以跳出遊戲迴圈，關閉視窗
pygame.quit()
