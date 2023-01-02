## :satisfied: SMF 코딩테스트 스터디 repo 
사용 언어: Python <br>
e-Book : this is coding test 활용 (1월 ~2월) <br>
이후 [프로그래머스](https://school.programmers.co.kr/) 활용 예정<br>

## :question:스터디 Rules 
* 맡은 파트 정리 (e-Book)
* 1일 1커밋 개인 프로젝트, 공부 및 현 스터디 repo
* 매주 금 혹은 주말 review 진행 review 파일에 정리
* **할 수 있는 만큼만 하기! 무리 X**

## :wrench:진행 방법
* memebers: 멤버 폴더. 자신 개인 공부 및 개인 프로젝트 관리하는 폴더
* E-book Study: e-book 공부를 올리고 피드
원격저장소 로컬에 가져오기
 git clone https://github.com/TheCopiens/algorithm-study.git 

로컬에서 개인 브랜치 생성하기
local workspace에 'ohhako'라는 이름으로 브랜치 생성
 git branch ohhako 

로컬에서 브랜치 작업후 원격저장소에 반영하기
로컬 브랜치가 있는 폴더에서 개인작업을 마친 후 공동 저장소에 반영한다.

 git checkout ohhako  - master에서 ohhako 브랜치로 전환
workspace에서 작업
 git commit -m "message"
 git push origin ohhako  - 원격저장소 ohhako 브랜치에 반영
 git checkout master  - 브랜치 전환
 git pull  - 원격저장소 master의 최신 정보를 로컬에 업데이트 시키기
 git merge ohhako  - master에 ohhako 브랜치 작업 반영
 git push origin master  - 원격저장소 master에 반영
