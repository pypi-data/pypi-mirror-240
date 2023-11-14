from setuptools import setup, find_packages

setup(
    name="ssu_package_deploy_tutorial",             # 패키지 명
    version="1.0.0",                                # 패키지 버전
    author="Junwon Moon",                           # 작성자
    description="PyPI를 활용한 패키지 배포 과정 알아보기 (tutorial)",  # 패키지 설명
    packages=find_packages(),                       # 패키지 디렉토리 (__init__.py 파일 여부로 구분)
)