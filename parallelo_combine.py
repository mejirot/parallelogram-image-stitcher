from PIL import Image, ImageDraw
import os
import numpy as np

def parallelogram_crop(img, skew_factor=0.2):
    """画像を平行四辺形に切り抜く関数"""
    width, height = img.size
    
    # 平行四辺形の4点を計算 (左上、右上、右下、左下)
    offset = int(height * skew_factor)
    points = [
        (offset, 0),          # 左上
        (width, 0),           # 右上
        (width - offset, height),  # 右下
        (0, height)           # 左下
    ]
    
    # 透明なマスクを作成
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(points, fill=255)
    
    # 透明度を持った新しい画像を作成
    result = Image.new('RGBA', img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    
    return result, offset

def main():
    # 画像フォルダのパス
    img_folder = 'img'
    
    # フォルダ内の画像ファイルを取得
    image_files = [f for f in os.listdir(img_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort()  # 名前でソート
    
    if not image_files:
        print("画像が見つかりません")
        return
    
    # 最初の画像を読み込んで、サイズを確認（基準とする）
    first_img = Image.open(os.path.join(img_folder, image_files[0]))
    img_width, img_height = first_img.size
    
    # 平行四辺形の重なりの計算用
    overlap = 0.5  # 重なりの割合 (0.0〜1.0)
    skew_factor = 0.2  # 傾斜の強さ
    
    # 処理した画像とオフセットを保存するリスト
    processed_images = []
    offsets = []
    
    # 各画像を平行四辺形に切り抜く
    for img_file in image_files:
        img_path = os.path.join(img_folder, img_file)
        img = Image.open(img_path).convert("RGBA")
        
        # リサイズが必要ならここで行う
        if img.size != (img_width, img_height):
            img = img.resize((img_width, img_height), Image.LANCZOS)
        
        # 平行四辺形に切り抜く
        parallelogram_img, offset = parallelogram_crop(img, skew_factor)
        processed_images.append(parallelogram_img)
        offsets.append(offset)
    
    # 最終画像の幅を計算（オーバーラップを考慮）
    effective_width = int(img_width - offset * overlap)
    total_width = effective_width * len(processed_images) - int(effective_width * (1 - overlap))
    
    # 新しい画像を作成
    final_image = Image.new('RGBA', (total_width, img_height), (0, 0, 0, 0))
    
    # 画像を順番に配置
    x_offset = 0
    for idx, img in enumerate(processed_images):
        # 最初の画像以外は、オーバーラップを考慮して配置
        if idx > 0:
            x_offset = int(x_offset + effective_width * (1 - overlap))
        
        final_image.paste(img, (x_offset, 0), img)
    
    # 結果を保存
    output_path = 'parallelogram_combined.png'
    final_image.save(output_path)
    print(f"画像が正常に処理され、{output_path}として保存されました。")

if __name__ == "__main__":
    main()