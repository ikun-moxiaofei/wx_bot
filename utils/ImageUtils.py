import os
import base64
from PIL import Image
import config


def compress_png_to_size(input_path, max_size=10 * 1024 * 1024):
    """
    压缩PNG文件直到其大小小于或等于max_size指定的字节数。

    参数:
    input_path: str，PNG文件的路径。
    max_size: int，目标文件大小的最大字节数，默认为10MB。
    """
    orig_size = os.path.getsize(input_path)
    if orig_size > max_size:
        with Image.open(input_path) as img:
            # 尝试不同的质量设置，直到文件大小小于max_size
            quality = 95
            while quality >= 10 and orig_size > max_size:
                img.save(input_path, 'PNG', quality=quality)
                orig_size = os.path.getsize(input_path)
                quality -= 5
            print(f"图片压缩完成，原始大小：{orig_size}字节")
    else:
        print(f"图片大小未超过10MB，无需压缩。原始大小：{orig_size}字节")


def imageDecode(temp_path, target_path=r'temp_image', xor_value=config.xor_value):

    # 确保目标路径存在
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    print(temp_path)
    if os.path.exists(temp_path):
        print("文件路径存在")
    else:
        print("文件路径不存在")
    # 打开DAT文件进行读取
    with open(temp_path, "rb") as dat_read:
        dat_data = dat_read.read()
    # 计算解密后的数据
    decrypted_data = bytes([b ^ xor_value for b in dat_data])

    # 构建输出文件的完整路径
    out_file_path = os.path.join(target_path, os.path.basename(temp_path).replace('.dat', '.png'))

    # 打开输出文件进行写入
    with open(out_file_path, "wb") as png_write:
        png_write.write(decrypted_data)

    # 压缩图片
    compress_png_to_size(out_file_path)

    # 读取PNG文件内容并编码为Base64
    with open(out_file_path, 'rb') as f:
        image_base64 = base64.b64encode(f.read())
        with open("base64.txt", 'wb') as ff:
            ff.write(image_base64)

    # 看看image_base64类型是不是正确的“bytes”类型
    # print(type(image_base64))
    # 解码图片
    imgdata = base64.b64decode(image_base64)
    # 将图片保存为文件
    with open("temp.jpg", 'wb') as f:
        f.write(imgdata)

    return image_base64.decode()  # 返回Base64编码的字符串


# 主函数
# if __name__ == '__main__':
#     # 修改.dat文件的路径
#     # dat_file_path = r'D:\w\WeChat Files\wxid_rizc5bcmmtre12\FileStorage\Image\2024-05\b8f3ea98a17947601eab5d4bfa216615.dat'
#
#     # 修改转换成png图片后的存放路径
#     target_path = r'D:\zhuomian\youdao_bot\temp_image'
#
#     # 修改加密的异或值，例如：xor_value = 0xC3
#     xor_value = 0xC3
#
#     # 确保目标路径存在
#     if not os.path.exists(target_path):
#         os.makedirs(target_path)
#
#     # 对单个文件进行解码并获取Base64编码
#     base64_image = imageDecode(dat_file_path)
#     # print(f"Base64 encoded image: {base64_image}")
#     print("end")
