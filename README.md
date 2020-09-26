# File-to-Directory-Classifier

---

## 설명
특정 디렉토리에서 각 파일들을 대표 디렉토리에 넣어주는 스크립트. 대표 디렉토리는,

- 영문으로 시작하는 파일: 파일 이름의 첫 글자(대문자)
- 숫자로 시작하는 파일: 디렉토리 '0'
- 한글로 시작하는 파일: 첫 글자의 대표 한글 (예. '깃허브.txt'의 경우 '가' 디렉토리)

## 사용법
* 정리가 필요한 디렉토리에 본 파이썬 스크립트를 복사해서 실행
> python classifier.py

* 또는 정리가 필요한 디렉토리의 절대/상대 경로를 파라미터로 지정하여 실행
> python classifier.py ../tmp/log

