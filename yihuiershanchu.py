def read_py_file_to_string(file_path):
    """
    读取.py文件内容并返回字符串格式
    
    参数:
        file_path (str): Python文件的路径
        
    返回:
        str: 文件内容的字符串表示
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"读取文件时出错: {str(e)}"
examples_str = read_py_file_to_string("/home/zpc/AFlow/scripts/tools.py")



print(examples_str)
