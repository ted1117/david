# 강제 push
## 단계
0. 원격과 로컬 모두 app.py에 test2 함수만 존재
1. 로컬에서 test2 삭제 후 [커밋](https://github.com/ted1117/david/commit/25c97376a3a1502c59b57a2adcdc058a74adb035)
2. 로컬에서 test1 추가 후 [커밋](https://github.com/ted1117/david/commit/d0d0a1689d93d85bd661ab47363c7d69de15e0e6)
3. 원격에서 test2 추가 후 [커밋](https://github.com/ted1117/david/commit/d5740df37fd711484de250dfc19a9253214ab17b)
4. 로컬에서 강제 push

## 결말
1. 로컬에서 커밋한 이력이 원격에 덮어 씌어짐
2. 원격에서 test2를 추가한 커밋이 이력에서 없어짐
3. 강제 푸시한 이후로 app.py엔 test1 함수만 존재