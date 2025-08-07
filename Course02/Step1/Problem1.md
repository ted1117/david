# 협업 시 충돌
## 단계
1. 로컬에서 파일 수정 후 커밋
2. 웹에서 파일 수정 후 커밋 및 푸시
3. 로컬에서 push -> 오류 발생

## 상황
### 원격
[커밋](https://github.com/ted1117/david/commit/899aa9661e750f00d9b3c3230af16de28e9fdf51)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <center>
      <p>메뉴판</p>
      <button name="menu1" style="width: 70pt">아메리카노</button><br />
      <button name="menu2" style="width: 70pt">카페라떼</button><br />
      <button name="menu2" style="width: 70pt">녹차</button><br />
    </center>
  </body>
</html>
```

## 해결
1. 로컬에서 hr 태그 추가 후 [커밋](https://github.com/ted1117/david/commit/b2e5c50e2808e523651576baadf7b7905bacf57d)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <center>
      <p>메뉴판</p>
      <button name="menu1" style="width: 70pt">아메리카노</button><br />
      <button name="menu2" style="width: 70pt">카페라떼</button><br />
      <hr />
      <button name="menu2" style="width: 70pt">녹차</button><br />
    </center>
  </body>
</html>
```

2. 원격에서 둥글레차 메뉴 추가 후 [커밋](https://github.com/ted1117/david/commit/6564929aaccfa3982b55daa652624b375f07154d)
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <center>
      <p>메뉴판</p>
      <button name="menu1" style="width: 70pt">아메리카노</button><br />
      <button name="menu2" style="width: 70pt">카페라떼</button><br />
      <button name="menu2" style="width: 70pt">녹차</button><br />
      <button name="menu2" style="width: 70pt">둥글레차</button>
    </center>
  </body>
</html>
```

3. 로컬에서 git push 시도
```bash
hidsquid97@yangseungjoui-MacBookAir-2 david % git push -u origin main
To https://github.com/ted1117/david.git
! [rejected] main -> main (fetch first)
error: 레퍼런스를 'https://github.com/ted1117/david.git'에 푸시하는데 실패했습니다
힌트: 리모트에 로컬에 없는 사항이 들어 있으므로 업데이트가
힌트: 거부되었습니다. 이 상황은 보통 또 다른 저장소에서 같은
힌트: 저장소로 푸시할 때 발생합니다. 푸시하기 전에
힌트: ('git pull ...' 등 명령으로) 리모트 변경 사항을 먼저
힌트: 포함해야 합니다.
힌트: 자세한 정보는 'git push --help'의 "Note about fast-forwards' 부분을
힌트: 참고하십시오.
```

3. ```git pull --no-rebase``` 후 병합 메시지 확인
```bash
hidsquid97@yangseungjoui-MacBookAir-2 david % git pull --no-rebase
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 6 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (6/6), 1.16 KiB | 397.00 KiB/s, 완료.
https://github.com/ted1117/david URL에서
899aa96..6564929 main -> origin/main
자동 병합: Course02/Step1/templates/menu.html
Merge made by the 'ort' strategy.
Course02/Step1/templates/menu.html | 1 +
1 file changed, 1 insertion(+)
```

4. git push
```bash
hidsquid97@yangseungjoui-MacBookAir-2 david % git push -u origin main
오브젝트 나열하는 중: 22, 완료.
오브젝트 개수 세는 중: 100% (22/22), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (10/10), 완료.
오브젝트 쓰는 중: 100% (12/12), 1016 bytes | 1016.00 KiB/s, 완료.
Total 12 (delta 6), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
To https://github.com/ted1117/david.git
6564929..ca898e7 main -> main
branch 'main' set up to track 'origin/main'.
```