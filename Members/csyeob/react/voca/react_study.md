src 쪽을 수정해주면 웹사이트가 바로바로 바뀜
node module 의 파일들은
package . json 내용들에 다 들어있음.
git에는 node_modules를 올리지 않음 파일들이 커서
근데 package.json만 있으면 동일한 구성환경을 구성할수있음.
public 파일에는 idex.html 에 div id = root 로 react 코드로 실행된 돔이 실행됨
대부분의 작업은 src에서 작업이됨.

package.jon에서 scripts에
start는 실행 개발모드
build는 배포로 만들어줌

index.js에서 인덱스해서 사용


---- 
<strong>Rest API</strong> <br>
C R U D <br>
<p>
create : POST 
Read : GET            json-server 서버 포트로 열어서 days/2 해보면 id가 2인 애가 뜨는데 그걸 읽는걸 GET 주소를 읽음 ?day=1 day=1에 일치한 주소를 다가져옴
Updata : PUT
Delete : DELETE
</p> 