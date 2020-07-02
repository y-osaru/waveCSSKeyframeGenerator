import math

#keyframeの%の間隔
STEP = 1
#sinカーブの振幅
AMP = 1

def main():
  """
  CSSで振動keyframeをpxで設定したい時の値を計算するscript
  振動=sinカーブと考えた
  """
  rad = 0
  for i in range(0,101,STEP):
    if i > 0:
      # 0~2πを0~100にした時、1ステップが2π/100=π/50
      rad = rad + (math.pi * STEP / 50)
    sinY = round(AMP * math.sin(rad),4)
    print(str(i) + "% { transform: translateY("+ str(sinY) + "px); }")

if __name__ == '__main__':
	main()