Python 2 2020년 1월 1일자로 공식 지원 종료

대부분 배포판(예: Ubuntu, Fedora, Debian 등)은 보안과 유지관리 문제로 Python 2를 기본에서 제거하거나 선택적으로 설치하도록 변경


- Python은 이미 실행 파일로 PATH에 등록되어 있어야 실행 가능

- 터미널에서 python 또는 python3 명령어로 실행된다면, 이미 환경 변수(PATH)에 등록되어 있다는 의미

- Python 패키지 관리자 = pip pip3
# Python과 패키지 관리자 환경 변수 등록

# 환경 변수 PATH에 등록 여부 확인 방법

7eerup@c6r3s5:~/ia-codyssey$ which python
/usr/bin/python

7eerup@c6r3s5:~/ia-codyssey$ which python3
/usr/bin/python3

# Python 실행 위치
$ python -c "import sys; print(sys.executable)"

# pip 확인
$ which pip

/usr/bin/pip

$ pip --version

pip 23.2.1 from /usr/lib/python3.12/site-packages/pip (python 3.12)



# 설치
$ pip install Flask

# 확인
$ pip show flask

