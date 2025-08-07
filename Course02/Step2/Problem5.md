# Stash
## 단계
1. menu.html에서 메뉴판 아래에 hr 태그 추가 후 status 확인
2. ```git stash```로 임시 저장 후 status 확인 및 ```git stash list```로 stash 확인
3. menu.html에 유자차 메뉴 추가 후 커밋 및 push
4. ```git stash apply```로 stash한 커밋을 다시 불러오기
5. ```git add```로 스테이지로 올리고 커밋
6. push

## 상황
- hr 태그 -> 유자차 추가 순으로 수정
- 하지만 hr 태그 추가는 stash
- 유자차 메뉴를 추가하고 push 할 땐 hr 태그 추가는 반영되지 않음
- stash apply로 hr 태그 추가를 후반영
- 따라서 커밋 기록으로는 유자차 -> hr 순