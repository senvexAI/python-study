import os

def list_files_in_directory(directory=None):
    """
    Lists all non-hidden files in the same folder as this .py file,
    unless a specific directory를 지정해주면 그 쪽을 봅니다.

    Args:
        directory (str | None):
            None일 경우 이 함수가 정의된 .py 파일의 위치를 사용.
            str을 주면 그 디렉터리를 사용.
    """
    # 1) directory 파라미터가 없으면 (__file__ 기반) 스크립트 위치로 계산
    if directory is None:
        try:
            # __file__은 이 함수를 정의한 스크립트의 경로
            directory = os.path.dirname(os.path.abspath(__file__))
        except NameError:
            # __file__이 없는 환경(인터프리터, Jupyter 등)에서는 cwd 사용
            directory = os.getcwd()

    try:
        # 2) 숨김파일(.)·_(언더스코어)로 시작하는 파일은 제외
        files = [
            f for f in os.listdir(directory)
            if not (f.startswith(".") or f.startswith("_"))
        ]
        for f in files:
            print(f)
    except Exception as e:
        print(f"An error occurred: {e}")

# 사용 예:
# - 스크립트 위치 기준으로 보고 싶으면 인자 없이
list_files_in_directory()