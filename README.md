## :satisfied: SMF 코딩테스트 스터디 repo 
사용 언어: Python <br>
e-Book : this is coding test 활용 (1월 ~2월) <br>
이후 [프로그래머스](https://school.programmers.co.kr/) 활용 예정<br>

## :question:스터디 Rules 
* e-Book 공부는 매일 밤 10시 리뷰(결 사유시 Issues나 톡방에 연락)
* 1일 1커밋 개인 프로젝트, 공부 및 현 스터디 repo
* reviews 폴더에 개인 프로젝트 및 공부 review를 진행할 예정
* **할 수 있는 만큼만 하기! 무리 X**

## :wrench:진행 방법
* memebers: 멤버 폴더. 자신 개인 공부 및 개인 프로젝트 관리하는 폴더
* E-book Study: e-book 공부를 올리고 피드<br>


1. 원격저장소 로컬에 가져오기 <br>
<code> **https://github.com/SMF-GroupStudy/SMF_Algorithm-Study.git** </code> 
2. 로컬에서 개인 브랜치 생성하기<br>
local workspace에 'csyeob'라는 이름으로 브랜치 생성<br>
<code> **git branch csyeob** </code>
3. 로컬에서 브랜치를 변경 후 git add로 추가, commit, push를 진행
4. 코딩테스트 branch라면 제한을 protection이 걸려있어서 merge를 바로 못함 (review를 하기 위함).
5. push 후 원격저장소 github에서 pull request를 진행

**※코딩테스트 branch 라면?**<br>
```
reviewers에 PR리뷰를 해줄 팀원 1명이상 지정
Assignees 현재 PR 담당자 (나)를 지정
리뷰 => merge를 할지 않을지 결정하는 확인 절차이므로 1명이상의 Approve 승인을 받아야함.
```
**※개인 공부 branch 라면?**<br>
1. <code>**git checkout csyeob**</code>  - main에서 csyeob 브랜치로 전환 로컬에서 작업
2. <code>**git commit -m "message"**</code> - 작업 후 <code>**git add .**</code> 이후 커밋
3. <code>**git push origin csyeob**</code>  - 원격저장소 csyeob 브랜치에 푸시
4. <code>**git checkout main**</code>  - 브랜치 전환(main에 merge 요청하기 위함)
5. <code>**git pull**</code> - 원격저장소 main의 최신 정보를 로컬에 업데이트 시키기(최신정보가 아니면 push가 안됨)
6. <code>**git merge csyeob**</code>  - main에 csyeob 브랜치 작업 반영
7. <code>**git push origin main**</code> - 원격저장소 main에 반영
