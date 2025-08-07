# 커밋 메시지 수정
## 단계
1. 기존에 작성한 test2 함수 삭제
2. **test2 데코레이터와 함수 코드 삭제** 메시지로 커밋 후 push
3. git log로 깃 로그 확인
4. 커밋 메시지 수정 **test2 데코레이터와 함수 코드를 삭제 - 기획 변경으로 테스트 코드 삭제**

## 원리
1. ```git commit --amend -m "메시지"```로 가장 마지막 커밋 삭제 후 새로운 커밋으로 덮어씀
```bash
// 기존 커밋
623962d (HEAD -> main, origin/main, origin/HEAD) test2 데코레이터와 함수 코드를 삭제

// 새로운 커밋
4ea14ca (HEAD -> main, origin/main, origin/HEAD) test2 데코레이터와 함수 코드를 삭제 - 기획 변경으로 해당 테스트 코드 삭제
```
2. ```git push```로는 원격 커밋 로그와 로컬 커밋 로그가 다르기 때문에 충돌
3. ```git push --force```로 원격 커밋을 로컬 커밋으로 덮어씀