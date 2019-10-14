def get_avatar(img):
    import base64
    with open(img, 'rb') as f:
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        print(ls_f)


if __name__ =='__main__':
    get_avatar('./imgs/position_bias_history.jpg')
