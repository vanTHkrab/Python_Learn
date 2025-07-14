from PIL import Image
import os


def compress_image(input_image_path, output_image_path, quality):
    """
    บีบอัดไฟล์ JPG โดยการปรับคุณภาพ

    :param input_image_path: เส้นทางของไฟล์รูปภาพต้นฉบับ (JPG)
    :param output_image_path: เส้นทางที่จะบันทึกไฟล์รูปภาพที่บีบอัด
    :param quality: คุณภาพของรูปภาพ (0-100, ค่าที่น้อยกว่าคือการบีบอัดที่มากขึ้น)
    """
    try:
        with Image.open(input_image_path) as img:
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img.save(output_image_path, "JPEG", quality=quality, optimize=True)

        print(f"บีบอัดสำเร็จ: '{input_image_path}' -> '{output_image_path}' (Quality: {quality})")

        original_size = os.path.getsize(input_image_path)
        compressed_size = os.path.getsize(output_image_path)
        print(f"  ขนาดเดิม: {original_size / 1024:.2f} KB")
        print(f"  ขนาดใหม่: {compressed_size / 1024:.2f} KB")
        print(f"  ลดลง: {((original_size - compressed_size) / original_size) * 100:.2f}%")

    except FileNotFoundError:
        print(f"ข้อผิดพลาด: ไม่พบไฟล์ที่ '{input_image_path}'")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบีบอัด '{input_image_path}': {e}")


def compress_images_in_folder(input_folder, output_folder, quality):
    """
    บีบอัดไฟล์ JPG ทั้งหมดในโฟลเดอร์ที่ระบุ และบันทึกลงในอีกโฟลเดอร์

    :param input_folder: เส้นทางของโฟลเดอร์ที่มีรูปภาพต้นฉบับ
    :param output_folder: เส้นทางของโฟลเดอร์ที่จะบันทึกรูปภาพที่บีบอัด
    :param quality: คุณภาพของรูปภาพ (0-100)
    """
    if not os.path.exists(input_folder):
        print(f"ข้อผิดพลาด: โฟลเดอร์ต้นฉบับ '{input_folder}' ไม่พบ")
        return

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"สร้างโฟลเดอร์ปลายทาง: '{output_folder}'")

    print(f"\n--- เริ่มบีบอัดรูปภาพใน '{input_folder}' ไปยัง '{output_folder}' (Quality: {quality}) ---")
    image_count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            compress_image(input_path, output_path, quality)
            print("-" * 30)
            image_count += 1

    if image_count == 0:
        print(f"ไม่พบไฟล์รูปภาพ JPG/JPEG ในโฟลเดอร์ '{input_folder}'")
    else:
        print(f"--- การบีบอัดเสร็จสิ้น ({image_count} ไฟล์บีบอัด) ---")


if __name__ == "__main__":
    source_folder = "s1 van"
    destination_folder_low = "compressed_images_low"
    destination_folder_medium = "compressed_images_medium"
    destination_folder_high = "compressed_images_high"


    # compress_images_in_folder(source_folder, destination_folder_low, 30)
    # print("\n" + "=" * 50 + "\n")
    #
    # compress_images_in_folder(source_folder, destination_folder_medium, 70)
    # print("\n" + "=" * 50 + "\n")

    compress_images_in_folder(source_folder, destination_folder_high, 90)
    print("\n" + "=" * 50 + "\n")